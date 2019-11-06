# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/11/4 20:24
# software: PyCharm

import os
import shutil

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn import metrics
from torch.autograd import Variable


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            shutil.rmtree(path_file)


if __name__ == '__main__':
    use_tensorboard = False
    if use_tensorboard:
        from tensorboardX import SummaryWriter
    plt.rcParams['font.size'] = 16
    plt.rcParams['font.family'] = 'FangSong'
    plt.rcParams['axes.unicode_minus'] = False
    np.random.seed(2019)
    torch.manual_seed(2019)
    if os.path.exists('runs'):
        del_file('runs')
    data = pd.read_csv('case2_training.csv')
    data_final_test = pd.read_csv('case2_testing.csv')
    print(data.head(2))
    data = np.array(data)[:, 1:]
    data_final_test = np.array(data_final_test)[:, 1:]
    factor = np.array([10, 365, 7, 1, 4, 5, 1, 1000])
    x = data[:, :-1]
    y = data[:, -1]
    x = np.apply_along_axis(
        lambda t: t / factor, 1, x
    )
    data_final_test = np.apply_along_axis(
        lambda t: t / factor, 1, data_final_test
    )
    # z = list(zip(x, y))
    # np.random.shuffle(z)
    # x, y = zip(*z)
    x, y = np.array(x), np.array(y)
    print(x.max(), x.min(), y.max(), y.min())
    y = np.eye(2)[(y).astype(np.int)].squeeze()
    gap = int(0.7 * x.shape[0])
    x_train, x_test = x[:gap], x[gap:]
    y_train, y_test = y[:gap], y[gap:]
    print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
    X_train = Variable(torch.FloatTensor(x_train))
    X_test = Variable(torch.FloatTensor(x_test))
    y_train = Variable(torch.FloatTensor(y_train))
    y_test = Variable(torch.FloatTensor(y_test))
    data_final_test = Variable(torch.FloatTensor(data_final_test))
    dnn = nn.Sequential(
        nn.Linear(8, 20),
        nn.BatchNorm1d(20),
        nn.ReLU(),
        nn.Linear(20, 20),
        nn.BatchNorm1d(20),
        nn.ReLU(),
        nn.Linear(20, 2),
        nn.Softmax()
    )
    if os.path.exists('runs'):
        try:
            del_file('runs')
        except:
            pass
    if use_tensorboard:
        writer = SummaryWriter()
    # writer.add_graph(dnn.cpu(), (torch.rand(10, 6)))
    epochs = 200
    lr = 0.01
    loss_func = nn.BCELoss()
    optimizer = torch.optim.Adam(dnn.parameters(), lr)
    for ep in range(epochs):
        dnn.train()
        y_train_pred = dnn(X_train)
        loss = loss_func(y_train_pred, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        dnn.eval()
        y_eval_train_pred = dnn(X_train)
        y_eval_test_pred = dnn(X_test)
        train_loss = loss_func(y_eval_train_pred, y_train)
        test_loss = loss_func(y_eval_test_pred, y_test)
        train_acc = (y_train.cpu().numpy().argmax(axis=1) == y_eval_train_pred.cpu().detach().numpy().argmax(
            axis=1)).mean()
        test_acc = (y_test.cpu().numpy().argmax(axis=1) == y_eval_test_pred.cpu().detach().numpy().argmax(
            axis=1)).mean()
        log = 'epoch: %d, train loss: %.6f, test loss: %.6f, train acc: %.6f, test acc: %.6f' % \
              (ep, train_loss.item(), test_loss.item(), train_acc, test_acc)
        print(log)
        if use_tensorboard:
            writer.add_text('training log', log, ep)
            writer.add_scalars('data/loss', {'train loss': train_loss.data, 'test loss': test_loss.data}, ep)
            writer.add_scalars('data/accuracy', {'train accuracy': train_acc, 'test accuracy': test_acc}, ep)
            for name, param in dnn.named_parameters():
                writer.add_histogram(name, param.clone().data.cpu().numpy(), ep)
    y_final_test = dnn(data_final_test).detach().numpy().argmax(1)
    y_true = y_test.numpy().argmax(1)
    y_score = dnn(X_test).detach().numpy()[:, 1].squeeze()
    print(y_score)
    y_pred = dnn(X_test).detach().numpy().argmax(1)
    label = ['not accepted', 'accepted']
    print('precision:', metrics.precision_score(y_true, y_pred))
    print('recall:', metrics.recall_score(y_true, y_pred))
    print('f1 score:', metrics.f1_score(y_true, y_pred))
    print('confusion matrix: ', metrics.confusion_matrix(y_true, y_pred))
    print(metrics.classification_report(y_true, y_pred, target_names=label))

    cm = metrics.confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots()
    ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')
    plt.xlabel('predicted label')
    plt.ylabel('true label')
    plt.show()
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)  ###计算真正率和假正率
    roc_auc = metrics.auc(fpr, tpr)  ###计算auc的值
    print(f'auc={roc_auc}')
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)
    plt.title('Receiver operating characteristic Curve')
    plt.legend(loc="lower right")
    plt.show()

    if use_tensorboard:
        writer.add_embedding(torch.FloatTensor(X_train.cpu()), metadata=torch.FloatTensor(y_train.cpu()))
        writer.close()
        os.startfile('logdir.bat')
