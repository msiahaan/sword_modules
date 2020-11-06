import sys

bookList = (
    'matius.xml',
    'markus.xml',
    'lukas.xml',
    'yohanes.xml',
    'kisah.xml',
    'roma.xml',
    '1korintus.xml',
    '2korintus.xml',
    'galatia.xml',
    'efesus.xml',
    'filipi.xml',
    'kolose.xml',
    '1tesalonika.xml',
    '2tesalonika.xml',
    '1timotius.xml',
    '2timotius.xml',
    'titus.xml',
    'filemon.xml',
    'ibrani.xml',
    'yakobus.xml',
    '1petrus.xml',
    '2petrus.xml',
    '1yohanes.xml',
    '2yohanes.xml',
    '3yohanes.xml',
    'yudas.xml',
    'wahyu.xml',
    )

def printHeader(outputfile):
    outputfile.write('''<?xml version="1.0" encoding="UTF-8"?><osis xmlns="http://www.bibletechnologies.net/2003/OSIS/namespace" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.bibletechnologies.net/2003/OSIS/namespace http://www.bibletechnologies.net/osisCore.2.1.1.xsd">
<osisText osisIDWork="IndTB" osisRefWork="bible" xml:lang="ind">
<header>
<work osisWork="IndTB">
  <title>Alkitab Terjemahan Baru</title>
  <type type="OSIS">Bible</type>
  <identifier type="OSIS">Alkitab.TB</identifier>
  <rights type="x-copyright">Copyright 1974 Lembaga Alkitab Indonesia</rights>
  <scope>Matt-Rev</scope>
  <refSystem>Alkitab.TB</refSystem>
</work>
<work osisWork="bible">
  <type type="OSIS">Bible</type>
  <refSystem>Alkitab.TB</refSystem>
</work>
</header>''')

def compileBook(outputfile):
    for file in bookList:
        for line in open(file, 'r').readlines():
            outputfile.write(line)
            
def printFooter(outputfile):
    outputfile.write('''\n</osisText>
</osis>''')
    
def run():
    outputfile = open('indTB-nt.xml','w')
    printHeader(outputfile)
    compileBook(outputfile)
    printFooter(outputfile)
    outputfile.close()
    
if __name__== '__main__':
    run()