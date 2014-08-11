'''
This module supports checking for some C++ coding idioms and unsafe practices.
'''

import re
from opensc.severity import Severity

#This regex matches all strings which are (*VARIABLE).VARIABLE
DEREF_REGEX = ur"\( *\* *(.*?) *\)\..*"

def checkCStyleCast(checkFile, \
    title="C-Style cast", \
    message="C-Style casts are not reccomended.",
    severity=Severity.WARNING):
  '''This function checks for C-Style casts in C++ files'''

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.CSTYLE_CAST_EXPR:
      checkFile.addLineIssue(severity,\
                node.location.line, node.location.column,\
                title, message)

    for c in node.get_children():
      nodeSearch(c)

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkDereferenceUsage(checkFile,\
    title="Unnecessary pointer dereference")
    message=\
"Dereferencing pointers to access members is unnecessary use foo->bar instead."
    severity=Severity.WARNING):
  '''This function checks for the use of (*ptr).member and reccomends instead
     using ptr->member.'''

  for match in checkFile.performLineRegex(DEREF_REGEX):
    #Ignore the case where the variable name is this as we will handle it in
    #another function
    if match[2].group(1) != 'this':
      checkFile.addLineIssue(severity, match[0], match[1], title, message)

def checkThisUsage(checkFile,\
    title="Unnecessary use of this",\
    message="Using the this variable is not needed inside member functions",\
    severity=Severity.WARNING):
  '''This function checks for (*this).member and this->member which are
     non-idiomatic code pieces'''

  for match in checkFile.performLineRegex(DEREF_REGEX):
    #Only get cases with this as the variable
    if match[2].group(1) == 'this':
      checkFile.addLineIssue(severity, match[0], match[1], title, message)

  for match in checkFile.performLineRegex(ur"this->.*"):
    checkFile.addLineIssue(severity, match[0], match[1], title, message)
