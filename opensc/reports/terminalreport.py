'''
This module provides support for generating issue reports for terminal based
output.
'''

from opensc.abstractreport import AbstractReport
from opensc.severity import Severity

class TerminalReport(AbstractReport):
  SEVERITY_MAP = {
    Severity.ERROR:      '\033[91m[ERROR]\033[0m',
    Severity.WARNING:    '\033[93m[WARNING]\033[0m',
    Severity.SUGGESTION: '\033[95m[SUGGESTION]\033[0m',
    Severity.HINT:       '\033[94m[HINT]\033[0m'
    }

  def asString(self):
    outString = ""
    for fI in self.checkFile.getFileIssues():
      print "%s: %s\n%s" % (TerminalReport.SEVERITY_MAP[fI[0]], fI[1], fI[2])

    for lI in self.checkFile.getLineIssues():
      print "%s (%d, %d): %s\n%s" % \
        (TerminalReport.SEVERITY_MAP[fI[0]], fI[1], fI[2], fI[3], fI[4])

    return outString
