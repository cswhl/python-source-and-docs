#!/usr/bin/env python
# coding: utf-8

import subprocess

def test(size):
    print('start')
    cmd = 'dd if=/dev/urandom bs=1 count=%d 2>/dev/null' % size
    p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    # p.communicate()
    p.wait()
    print('end')

test(64*1024 + 1)
