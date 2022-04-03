import pandas as pd
import dataframe_image as dfi
from pathlib import Path
from datetime import datetime

class Attendance:

    def __init__(self, studentDict):
        self.studentDict = studentDict

    def createTable(self):
        dictToPrint = {"Student":[], "Present":[]}

        for key, value in self.studentDict.items():

            def getKey(val):
                if val == value:
                    return key

            dictToPrint["Student"].append(getKey(value))

            if value:
                dictToPrint["Present"].append("X")
            elif not value:
                dictToPrint["Present"].append("")

        table = pd.DataFrame(dictToPrint)
        pd.set_option('display.colheader_justify', 'right')
        table.style.set_properties(**{'text-align':'right'})

        return table

    def createTablePNG(self):
        utc_time = datetime.utcnow()
        tablePNG = dfi.export(self.createTable(), f'class_roster{str(utc_time)[0:10]}.png')
        return tablePNG

    def tableCSV(self):
        utc_time = datetime.utcnow()
        df = self.createTable()
        filepath = Path(f'classroster{str(utc_time)[0:10]}.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        csvFile = df.to_csv(filepath)

        return csvFile

# testing Attendance class
    # testDict = {"Binh Le":True, "James Zhang":True, "Casey Le":False, "Nick Kang":True}
    # tables = Attendance(testDict)
    # print(tables.createTable())
    # tables.createTablePNG()
    # tables.tableCSV()
