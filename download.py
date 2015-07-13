#!/usr/bin/env python3

'''
download a list of repo.
The Repo.txt file format:
    http://github.com/... xxx xxx
    http://svn.com/... xxx xxx
It will extract the first component as the url.
Whether --git should be provided
'''

from threading import Thread
from subprocess import call, DEVNULL
class Download:
    def __init__(self, filename, t):
        self.filename = filename
        if t == 'git':
            self.prefix = t + ' clone '
        else:
            print('only support git')
            exit(1)
    def getId(self, url):
        return url.replace('https://github.com/','').replace('.git','').replace('/','-')
    def download(self):
        f = open(self.filename, 'r')
        for line in f:
            url = line.split()[0]
            name = self.getId(url)
            command = self.prefix+url+' tmp/' + name
            DownloadThread(command).start()
        f.close()


class DownloadThread(Thread):
    def __init__(self, command):
        Thread.__init__(self)
        self.command = command
    def run(self):
        print('[running]\t' + self.command)
        if call(self.command, stderr=DEVNULL, stdout=DEVNULL, shell=True) != 0:
            print('[fail]\t' + self.command)
        else:
            print('[success]\t' + self.command)
