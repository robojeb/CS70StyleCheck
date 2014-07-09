'''
This module is designed to provide helper functions for writing scripts that
test student submissions.
'''

import sys, os, subprocess, opensc


def runProcess(arguments):
  proc = subprocess.Popen(arguments, env=os.environ, stdout=subprocess.PIPE,\
                          stderr=subprocess.PIPE)
  proc.wait()
  return proc.stdout.read(), proc.stderr.read()

def runProcessAsync(arguments):
  proc = subprocess.Popen(arguments, env=os.environ)

#Checks for .o and no extension files except those in exceptions
def checkForIllegalFiles(exceptions=['Makefile']):
  #TODO:Figure out the best way to do this
  pass

def styleCheck(extensions=['cpp','hpp'], ignore=[]):
  #TODO:Make this work
  pass

def compileCheck():
  runProcess(['make', 'clean'])
  stdout, stderr = runProcess(['make'])
  runProcess(['make', 'clean'])
  return stdout, stderr
