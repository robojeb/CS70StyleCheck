'''
This module provides support for generating issue reports in HTML markup
It is not designed to create an entire HTML page but can be placed as the body
to any HTML page
'''

from opensc.abstractreport import AbstractReport
from opensc.severity import Severity

class HTMLBodyReport(AbstractReport):
  SEVERITY_MAP_START = {
  Severity.ERROR:      '<span style="color:red">ERROR</span>',
  Severity.WARNING:    '<span style="color:yellow">WARNING</span>',
  Severity.SUGGESTION: '<span style="color:blue">SUGGESTION</span>',
  Severity.HINT:       '<span style="color:green">HINT</span>'
  }

  def asString(self):
    outString = ""
    for fI in self.checkFile.getFileIssues():
      print "<h3>%s: %s</h3>\n<p>%s</p>" % (TerminalReport.SEVERITY_MAP[fI[0]], fI[1], fI[2])

    for lI in self.checkFile.getLineIssues():
      print "<h3>%s (%d, %d): %s</h3>\n<p>%s<p>" % \
        (TerminalReport.SEVERITY_MAP[fI[0]], fI[1], fI[2], fI[3], fI[4])

    return outString
