# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/11 15:34
# software: PyCharm


import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution:
    def findWords(self, board: list(list()), words: list) -> list:
        ret = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, '', ret)
        return ret

    def dfs(self, board, node, i, j, path, ret):
        if node.isWord:
            ret.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        b = board[i][j]
        node = node.children.get(b)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, node, i + 1, j, path + b, ret)
        self.dfs(board, node, i - 1, j, path + b, ret)
        self.dfs(board, node, i, j - 1, path + b, ret)
        self.dfs(board, node, i, j + 1, path + b, ret)
        board[i][j] = b


so = Solution()
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
print(so.findWords(board, words))
