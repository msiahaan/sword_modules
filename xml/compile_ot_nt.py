import sys

ntBookList = (
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
    
otBookList = (
    'kejadian.xml',
    'keluaran.xml',
    'imamat.xml',
    'bilangan.xml',
    'ulangan.xml',
    'yosua.xml',
    'hakim.xml',
    'rut.xml',
    '1samuel.xml',
    '2samuel.xml',
    '1raja.xml',
    '2raja.xml',
    '1tawarikh.xml',
    '2tawarikh.xml',
    'ezra.xml',
    'nehemia.xml',
    'ester.xml',
    'ayub.xml',
    'mazmur.xml',
    'amsal.xml',
    'pengkhotbah.xml',
    'kidung.xml',
    'yesaya.xml',
    'yeremia.xml',
    'ratapan.xml',
    'yehezkiel.xml',
    'daniel.xml',
    'hosea.xml',
    'yoel.xml',
    'amos.xml',
    'obaja.xml',
    'yunus.xml',
    'mikha.xml',
    'nahum.xml',
    'habakuk.xml',
    'zefanya.xml',
    'hagai.xml',
    'zakharia.xml',
    'maleakhi.xml',
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
  <scope>Gen-Rev</scope>
  <refSystem>Alkitab.TB</refSystem>
</work>
<work osisWork="bible">
  <type type="OSIS">Bible</type>
  <refSystem>Alkitab.TB</refSystem>
</work>
</header>''')

def compileOT(outputfile):
    for file in otBookList:
        for line in open(file, 'r').readlines():
            outputfile.write(line)

def compileNT(outputfile):
    for file in ntBookList:
        for line in open(file, 'r').readlines():
            outputfile.write(line)
            
def printFooter(outputfile):
    outputfile.write('''\n</osisText>
</osis>''')
    
def run():
    outputfile = open('indTB.xml','w')
    printHeader(outputfile)
    compileOT(outputfile)
    compileNT(outputfile)
    printFooter(outputfile)
    outputfile.close()
    
if __name__== '__main__':
    run()