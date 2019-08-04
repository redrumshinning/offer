# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, node):
        # write code here
        for num in range(len(self.stack_out)):
            self.stack_in.append(self.stack_out.pop())
        self.stack_in.append(node)

    def pop(self):
        # return xx
        for num in range(len(self.stack_in)):
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()