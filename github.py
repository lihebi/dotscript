#!/usr/bin/env python3
from urllib import request
import json

import argparse
import sys

from threading import Thread
from download import Download

import loc

filename = 'repos.txt'

def query():
    url = 'https://api.github.com'
    api = '/search/repositories'
    query = 'language:C&stars:>10&per_page=100'
    # req = request.Request(url+api+"?q="+query, method="GET")
    response = request.urlopen(url+api+"?q="+query)
    # print(response.read())
    s = response.read().decode('utf8')
    j = json.loads(s)
    f = open(filename, 'w')
    for item in j['items']:
        f.write(item['clone_url'] + "\t" + str(item['stargazers_count']))
        f.write('\n')
    f.close()
    print('result saved to '+filename)


def download():
    Download(filename, 'git').download()

def analyze():
    d = loc.loc('tmp')

def printResult():
    for line in open(filename):
        url = line.split()[0]
        url = url.replace("https://github.com/",'')
        url = url.replace('.git','')
        print(url)

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', help='query github api', action='store_true')
parser.add_argument('-d', '--download', help='download repos', action='store_true')
parser.add_argument('-a', '--analyze', help='analyze repos', action='store_true')
parser.add_argument('-p', '--print', help='print', action='store_true')
args = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help()
if (args.query):
    query()
if (args.download):
    download()
if (args.analyze):
    analyze()
if (args.print):
    printResult()
