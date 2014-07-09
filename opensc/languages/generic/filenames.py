'''
This module is designed for checking filenames and extensions. It is useful when
used as a check during an automatic commit hook check.
'''

import re
from severity import Severity

def checkExtension(checkFile, allowedExtensions,
    title="File has unallowed extension",
    message=\
    "Files with this extension should not be committed to the repository",\
    severity=Severity.ERROR):
  '''This function checks that the extension to the file is in the allowed list
     of extensions.'''

  if not checkFile.getExtension() in allowedExtensions:
    checkFile.addFileIssue(severity, title, message)

def checkFilename(checkfile, regex,\
    title="Filename violation",\
    message="Check your styleguide for file naming conventions",\
    severity=Severity.WARNING):
  '''This function checks that the filename is valid according to a regular
     expression provided by the script writer.'''

  nameRegex = re.compile(regex)

  if nameRegex.match(checkFile.getRawName()) is None:
    checkFile.addFileIssue(severity, title, message)
