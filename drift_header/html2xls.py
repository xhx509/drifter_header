# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:05:56 2015

@author: hxu
"""

from bs4 import BeautifulSoup
import urllib
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('a test sheet')
f = urllib.urlopen("http://www.nefsc.noaa.gov/drifter/")
html = f.read()
soup = BeautifulSoup(html)
#print soup.prettify()
#print soup
 
table = soup.find("table")
  
rows = table.findAll("tr")
x = 0
for tr in rows:
    cols = tr.findAll("td")
    if not cols: 
        # when we hit an empty row, we should not print anything to the workbook
        continue
    y = 0
    for td in cols:
        texte_bu = td.text
        texte_bu = texte_bu.encode('utf-8')
        texte_bu = texte_bu.strip()
        ws.write(x, y, td.text)
        print(x, y, td.text)
        y = y + 1
    # update the row pointer AFTER a row has been printed
    # this avoids the blank row at the top of your table
    x = x + 1
 
wb.save('BlastResults.xls')
'''
import xlwt
def html_table_to_excel(table):
    """ html_table_to_excel(table): Takes an HTML table of data and formats it so that it can be inserted into an Excel Spreadsheet.
    """
    data = {}
    table = table[table.index('<tr>'):table.index('</table>')]
    rows = table.strip('\n').split('</tr>')[:-1]
    for (x, row) in enumerate(rows):
    columns = row.strip('\n').split('</td>')[:-1]
    data[x] = {}
    for (y, col) in enumerate(columns):
    data[x][y] = col.replace('<tr>', '').replace('<td>', '').strip()
    return data
'''    