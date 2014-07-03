'''
This module provides the CheckFile object. This object is the encapsulation
for files that are being checked by the various check functions.
'''
import re, os

class CheckFile(object):
  def __init__(self, fileName):
    #
    #These are datamembers for maintaining the encapsulation of the file
    #

    #The name of the file we have loaded
    self.fileName = fileName
    #An array with each line of the file as an element
    self.lineArray = None

    #The whole file as one string
    self.fileContents = None

    #The parsed AST of the file
    self.AST = None

    #
    #These datamembers are for tracking the errors and other problems
    #

    self.lineIssue = []
    self.fileIssue = []

  def getLines(self):
    '''Returns an array containing each line as a string. It will lazily load
       the file as needed.'''
    if self.lineArray is None:
      with open(self.fileName, 'r') as file:
        for line in file:
          self.lineArray.append(line)
    return self.lineArray

  def getContents(self):
    '''Returns a string of the entire contents of the file. It will lazily load
       the file as needed.'''
    if self.fileContents is None:
      with open(self.fileName, 'r') as file:
        self.fileContents = file.read()
    return self.fileContents


  def performLineRegex(self, regex):
    '''Performs a regex operation on each line of file and returns a tuple
       (line, col, matchobject) for every match'''

    compiledRegex = re.compile(regex)

    matches = []
    for lineNum, line in enumerate(self.getLines()):
      match = compiledRegex.search(line)
      if not match is None:
        #If we have a match return the tuple
        #NOTE: We add one to lineNum because enumerat 0 indexes but most text
        #editors 1 index their lines. This also matches line numbers from
        #libclang's parser
        matches.append((lineNum+1, col, match))

    #return all the matches we found
    return matches

  def getlibclangAST(self):
    '''Returns the libclang AST. Lazily generates the tree as needed'''
    if self.AST is None:
      #TODO: Parse the tree
      pass
    return self.clangAST

  def addLineIssue(self, line, col, severity, title, message):
    self.lineIssues.append((line, col, severity, title, message))

  def addFileIssue(self, severity, title, message):
    self.fileIssues.append((severity, title, message))
