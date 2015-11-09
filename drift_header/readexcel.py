# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:24:52 2015

@author: hxu
"""
import xlrd
#open_file(path):
book = xlrd.open_workbook('BlastResults.xls')  


from xlrd import open_workbook

class Arm(object):
    def __init__(self, Institution, Deployer, Date_Deployed, Dropsite, units, Science,Status,Type_Unit,Fate):
        self.id = id
        self.Institution = Institution
        self.Deployer = Deployer
        self.Date_Deployed = Date_Deployed
        self.Dropsite = Dropsite
        self.units = units
        self.Science = Science
        self.Status = Status
        self.Type_Unit = Type_Unit
        self.Fate=Fate
    def __str__(self):
        return("Arm object:\n"
               "  Arm_id = {0}\n"
               "  Institution = {1}\n"
               "  Deployer = {2}\n"
               "  Date_Deployed = {3}\n"
               "  Dropsite = {4} \n"
               "  nits = {5}"
               "  Science = {6}"
               "  Status = {7}"
               "  Type_Unit = {8}"
               "  Fate = {9}"
               
               .format(self.id,self.Institution,self.Deployer,self.Date_Deployed,self.Dropsite,self.units,self.Science,self.Status,self.Type_Unit,self.Fate))

wb = open_workbook('BlastResults.xls')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            if col==2:
                value=(sheet.cell(row,col).value).split(',')
                values.append(value)
            else:    
                value  = (sheet.cell(row,col).value)
                
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
                
            
        item = Arm(*values)
        items.append(item)



for item in items:
    #print item
    #print("Accessing one single value (eg. DSPName): {0}".format(item.Status))
    print item.Date_Deployed
