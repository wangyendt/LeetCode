# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/27 17:52
# software: PyCharm


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def recursive(node, word, i):
            if i == len(word):
                if not node.isEnd:
                    return False  # word is not in trie
                node.isEnd = False  # delete word via changing isEnd be False
                return len(node.children) == 0  # return whether it has no children
            if word[i] not in node.children:  # word is not in trie
                return False
            need_delete = recursive(node.children[word[i]], word, i + 1)
            if need_delete:
                node.children.pop(word[i])
                return len(node.children) == 0
            return False  # current node still has other chars, don't need to delete it

        recursive(self.root, word, 0)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)