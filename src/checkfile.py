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

  #
  # Getters for things about the file itself
  #

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

  def getlibclangAST(self):
    '''Returns the libclang AST. Lazily generates the tree as needed'''
    if self.AST is None:
      #TODO: Parse the tree
      pass
    return self.clangAST

  def getName(self):
    '''Returns the basename of the file with extension'''
    return os.path.basename(self.fileName)

  def getRawName(self):
    '''Returns the basename of the file without its extension'''
    return os.path.splitext(self.getName())[0]

  def getExtension(self):
    '''Returns the file extension. This trims the '.' from the extension'''
    return os.path.splitext(self.getName())[1][1:]

  #
  # Functions for manipulating issues with the file
  #

  def addLineIssue(self, line, col, severity, title, message):
    '''Adds an issue at a specific line in the file'''
    self.lineIssues.append((line, col, severity, title, message))

  def addFileIssue(self, severity, title, message):
    '''Adds a general issue. This is for issues which don't generally have line
       numbers. (Like missing include guards)'''
    self.fileIssues.append((severity, title, message))

  def getLineIssues(self):
    '''Sorts the line issues by line number and column and returns the list'''
    self.lineIssues.sort()
    return self.lineIssues

  def getFileIssues(self):
    '''Returns the list of file issues in the order they were added'''
    return self.fileIssues

  #
  # Helper functions for performing actions on the file
  #

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
