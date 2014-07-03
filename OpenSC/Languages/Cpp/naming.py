'''
This module adds support for verifying C++ variable, class, and function
names.
'''

import re
from Severity import Severity

def checkLocalNames(checkFile, regex, \
    title="Invalid Local Variable Name", \
    message="Consult your style guidelines for correct local variable names"):
  '''This function takes a regular expression which defines a correct local
     variable name and adds an issue for each instance of a local variable that
     does not conform to this regular expression'''

  localVariableRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL or\
       node.kind == clang.cindex.CursorKind.CXX_METHOD:
      functionSearch(node)
    else:
      for c in node.get_children():
        nodeSearch(node)

  def functionSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.VAR_DECL:
      if localVariableRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
          node.location.line, node.location.column,\
          title, message)

  nodeSearch(checkFile.getlibclangAST().cursor)
  
