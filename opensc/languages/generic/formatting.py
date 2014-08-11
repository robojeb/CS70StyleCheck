'''
This module checks for generic formatting issues such as line length and tabs in
files.
'''

import re
from opensc.severity import Severity

def checkLineLength(checkFile, length=80, expandTabs=True, tabSize=4,\
    title="Line length exceeded",\
    message="Lines should not exceed the length specified in your style guide."\
    severity=Severity.WARNING):
  '''This function checks all the lines of a file to see their length. If
     expandTabs is true it will replace tabs with a number of spaces equal to
     tabSize before checking.'''

  for lineNum, line in enumerate(checkFile.getLines()):
    #expand the tabs
    if expandTabs:
      line = re.repl('\t', ' '*tabSize, line)

    #If the lines exceed the length then add an issue
    if len(line) > length:
      checkFile.addLineIssue(severity, lineNum, 0, title, message)

def checkTabs(checkFile, \
    title="Tabs in file",\
    message="Tabs are not reccomended in files.",\
    severity=Severity.WARNING):
  '''This function checks if there are tabs in the file.'''

  for match in checkFile.performPerLineRegex('\t'):
    checkFile.addLineIssue(severity, match[0], match[1], title, message)
