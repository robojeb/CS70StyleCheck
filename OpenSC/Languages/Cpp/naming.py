'''
This module adds support for verifying C++ variable, class, and function
names.
'''

import re
from Severity import Severity

def checkLocalVariables(checkFile, regex, \
    title="Invalid local variable name", \
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
          node.location.line, node.location.column, \
          title, message)

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkMemberVariables(checkFile, regex, \
    title="Invalid member variable name", \
    message="Cunsult your style guidelines for correct member variable names"):
  '''This function takes a regular expression which defines a correct member
     variable name and adds an issue for each instance of a member variable that
     does not conform to this regular expression'''

  memberVariableRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.CLASS_DECL:
      classSearch(node)
    else:
      for c in node.get_children():
        nodeSearch(c)

  def classSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.FIELD_DECL:
      if memberVariableRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
          node.location.line, node.location.column, \
          title, message)

    for c in node.get_children():
      classSearch(c)

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkStaticVariables(checkFile, regex, \
    title="Invalid static variable name", \
    message="Cunsult your style guidelines for correct static variable names"):
  '''This function takes a regular expression which defines a correct static
     variable name and adds an issue for each instance of a static variable that
     does not conform to this regular expression. (This function does not
     currently differentiate between constant and non-constant static variables
     )'''

  staticVariableRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.CLASS_DECL:
      classSearch(node)
    else:
      for c in node.get_children():
        nodeSearch(c)

  def classSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.VAR_DECL:
      if memberVariableRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
          node.location.line, node.location.column, \
          title, message)

    for c in node.get_children():
      classSearch(c)

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkGlobalVariables(checkFile, regex, \
    title="Invalid global variable name", \
    message="Cunsult your style guidelines for correct global variable names"):
  '''This function takes a regular expression which defines a correct global
     variable name and adds an issue for each instance of a global variable that
     does not conform to this regular expression. (By putting an empty regex and
     changing the message it is possible to disallow global variables)'''

  globalVariableRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return
    if node.kind == clang.cindex.CursorKind.VAR_DECL:
      if globalVariableRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
        node.location.line, node.location.column, \
        title, message)
    elif node.kind == clang.cindex.CursorKind.CLASS_DECL or\
        node.kind == clang.cindex.CursorKind.FUNCTION_DECL or\
        node.kind == clang.cindex.CursorKind.CXX_METHOD:
      return

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkClassNames(checkFile, regex, \
    title="Invalid class name", \
    message="Cunsult your style guidelines for correct class names"):
  '''This function takes a regular expression which defines a correct class
     name and adds an issue for each instance of a class that
     does not conform to this regular expression.'''

  classNameRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return

    if node.kind == clang.cindex.CursorKind.CLASS_DECL:
      if classNameRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
        node.location.line, node.location.column, \
        title, message)

    for c in node.get_children():
      nodeSearch(c)

  nodeSearch(checkFile.getlibclangAST().cursor)

def checkFunctionNames(checkFile, regex, \
    title="Invalid function name", \
    message="Cunsult your style guidelines for correct function names"):
  '''This function takes a regular expression which defines a correct function
     name and adds an issue for each instance of a function that
     does not conform to this regular expression.'''

  functionNameRegex = re.compile(regex)

  def nodeSearch(node):
    if node.location.file != None and \
        str(node.location.file) != checkFile.getBaseName():
      return

    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL or \
        node.kind == clang.cindex.CursorKind.CXX_METHOD:
      if functionNameRegex.match(node.spelling) is None:
        checkFile.addLineIssue(Severity.ERROR, \
        node.location.line, node.location.column, \
        title, message)

    for c in node.get_children():
      nodeSearch(c)

  nodeSearch(checkFile.getlibclangAST().cursor)
