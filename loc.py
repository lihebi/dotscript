#!/usr/bin/env python3

'''
count loc of programs
'''
import os,sys

def countLine(proj):
    print('count for project ' + proj, end='\t')
    count=0
    for root,dirs,files in os.walk(proj):
        for f in files:
            if not f.endswith('.c'): continue
            try:
                for line in open(root+'/' + f):
                    count+=1
            except UnicodeDecodeError:
                try:
                    for line in open(root+'/'+f, encoding='latin1'):
                        count+=1
                except UnicodeDecodeError:
                    print('exception for '+root+'/'+f, file=sys.stderr)
            except FileNotFoundError:
                print('FileNotFoundError for '+root+'/'+f, file=sys.stderr)
    return count

for root,dirs,files in os.walk(sys.argv[1]):
    if root != sys.argv[1]: continue
    for proj in dirs:
        count = countLine(root+'/'+proj)
        print(count)
