'''
This module is designed for checking filenames and extensions. It is useful when
used as a check during an automatic commit hook check.
'''

from severity import Severity

def checkExtension(checkFile, allowedExtensions,
    title="File has unallowed extension",
    message=\
    "Files with this extension should not be committed to the repository",\
    severity=Severity.ERROR):

  if not checkFile.getExtension() in allowedExtensions:
    checkFile.addFileIssue(severity, title, message)
