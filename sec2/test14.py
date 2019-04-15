
# -*- coding: utf-8 -*-
import os
import sys

if(__name__ == '__main__'):
    args = sys.argv
    N = int(args[1])
    f = open('hightemp.txt')
    for i in range(N):
        print(f.readline()[:-1]) #純粋にreadline()だと最後に改行コードが含まれるから消す

