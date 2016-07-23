#!/usr/bin/python
#!-*-coding:utf-8-*-

def notifications(massage):
    import subprocess
    cmd = "terminal-notifier -message '%s'" % massage
    subprocess.call( cmd, shell=True  )

if __name__ == "__main__":
    import sys
    param = sys.argv
    massage = "%s スクリプト完了" % param[0]
    notifications(massage)
