'''
This module adds support for checks about style issues within header files
'''


import re
from Severity import Severity

INCLUDE_GUARD_REGEX = re.compile(ur"#ifndef *([A-Z_]+).*\n#define *([A-Z_]+)")

def checkUsing(checkFile, \
    title="Using directive detected", \
    message="Using directives are not reccommended in header files",
    severity=Severity.WARNING):
  '''This function checks for using directives. It assumes that it is being run
     on a header file and adds an issue for each using directive.'''

  #A regular expression for finding using directives
  usingRegex = ur"using namespace .*;"

  for match in checkFile.performLineRegex(usingRegex):
    checkFile.addLineIssue(severity, match[0], match[1], title, message)

def checkIncludeGuardExistance(checkFile, \
    title="No include guards detected", \
    message="Header files should contain include guards",
    severity=Severity.ERROR):
  '''This function checks that there is an include guard in a header file'''
  #TODO: Make this function actually check for correctly matched #endifs

  #Find the first match for this regex
  match = INCLUDE_GUARD_REGEX.search(checkFile.getContents())

  #If there is no match we must not have an include guard
  if match is None:
    checkFile.addFileIssue(severity, title, message)

def checkIncludeGuardValidity(checkFile, \
    title="Misformed include guard", \
    message="Include guards variable names have to match",
    severity=Severity.ERROR):
  '''This function checks that there is an include guard in a header file'''


  #Find the first match for this regex
  match = INCLUDE_GUARD_REGEX.search(checkFile.getContents())

  #If there is no match we must not have an include guard
  if not match is None:
    if match.group(1) != match.group(2):
      checkFile.addFileIssue(severity, title, message)

def checkIncludeGuardNaming(checkFile, \
    title="Invalid include guard naming", \
    message="Include guards should contain the name of the file they are in",
    severity=Severity.WARNING):
  '''This function checks that the include guards contain the name of the file
     that they are in. If the include guards don't exist this does nothing'''


  #Find the first match for this regex
  match = INCLUDE_GUARD_REGEX.search(checkFile.getContents())

  #If there is no match we must not have an include guard
  if not match is None:
    nameRegex = re.compile(checkFile.getRawName().upper())
    #Seach in the matching group 1 (which is the include guard name)
    nameMatch = nameRegex.search(match.group(1))
    if nameMatch == None:
      checkFile.addFileIssue(severity, title, message)
