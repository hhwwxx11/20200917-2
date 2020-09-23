import collections
import re
import os
import sys
def count(words):
    collect = collections.Counter(words)
    num = 0
    for i in collect:
        num += 1
    print('total %d\n' % num)
    result = collect.most_common(10)
    # print(type(result),'result')
    for j in result:
        # print(type(j),'j')
        print('%-8s%5d' % (j[0], j[1]))
        # [('the',1),(),(),()]
def doCount(accept):
    s = '.txt'
    if s in accept:
        path = accept
    else:
        path = accept + '.txt'
    f = open(path, encoding='utf-8')
    words = re.findall(r'[a-z0-9^-]+', f.read().lower())
    count(words)

def doSomeFileCount(path):
    print(path)
    f = open(path, encoding='utf-8')
    words = re.findall(r'[a-z0-9^-]+', f.read().lower())
    count(words)
    print('----')
def doCountByPurText(inputText):
    words = re.findall(r'[a-z0-9^-]+', inputText.lower())
    count(words)

def fileFindAndCount(path1):
    files = os.listdir(path1)
    for file in files:
        if file.endswith('txt'):
            if os.path.isfile(path1+"/"+file):
               doSomeFileCount(path1+"/"+file)


def main(argv):
    if sys.argv[1] == '-s':
        if (len(sys.argv) == 3):
            doCount(sys.argv[2])
        else:
            redicertText = sys.stdin.read()
            doCountByPurText(redicertText)
    elif os.path.isdir(sys.argv[1]):
        fileFindAndCount(sys.argv[1])
    else:
        doCountByPurText(str(sys.argv[1:]))
        #doCount(sys.argv[1])

main(sys.argv[1:])