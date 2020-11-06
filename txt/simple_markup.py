#simple_markup.py
import sys, re
from util import lines

#Variables, need to be changed every run
bookID = "Mal"
title = "MALEAKHI"

#Pattern for re
chapterPattern = r'\*(.+?)\*'
versePattern = r'^(\d{1,3}):(\d{1,3})\b(.*)$'

def run():
    print '''<div type="book" osisID="%s" canonical="true">
<title type="main">%s</title>''' % (bookID, title)

    for line in lines(sys.stdin):
        line = re.sub(chapterPattern, r'<chapter osisID="%s." chapterTitle="\1">\n<title type="chapter">\1</title>' % bookID, line)
        line = re.sub(versePattern, r'<verse osisID="%s.\1.\2">\3</verse>' % bookID, line)
        line = re.sub(r'\*\*', r'</chapter>', line)
        print line.strip()
    print '</div>'
    
if __name__== '__main__':
    run()
