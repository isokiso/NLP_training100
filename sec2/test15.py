
# -*- coding: utf-8 -*-
import os
import sys

if(__name__ == '__main__'):
    args = sys.argv
    N = int(args[1])
    f = open('hightemp.txt')
    lines = f.readlines()
    lines_num = len(lines)
    f.close()
    for i in range(lines_num-5, lines_num):
        print(lines[i][:-1])
    

