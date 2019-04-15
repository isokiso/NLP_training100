
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
    sec = lines_num/N
    if lines_num % N != 0:
        sec+=1
    
    for i in range(N):
        f = open('test16_'+str(i)+'.txt','w')
        for j in range(sec):
            if N*i+j < lines_num:
                f.write(lines[N*i+j])
        f.close()
    

