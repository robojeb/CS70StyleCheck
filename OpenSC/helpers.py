import os

LIB_CLANG_PATH = '/usr/lib/llvm-3.3/lib/libclang.so'

def getExtension(fileName):
  basename = os.path.basename(fileName)
  return os.path.splitext(basename)[1]

def getBasename(fileName):
  return os.basename(fileName)
