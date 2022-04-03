import pandas as pd
import dataframe_image as dfi

def createTable(d):
    dictToPrint = {"Student":[], "Present":[]}

    for key, value in d.items():
    
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

    # return dfi.export(table, "dataframe.png")
    return table

testDict = {"Binh Le":True, "James Zhang":True, "Casey Le":False, "Nick Kang":True}
print(createTable(testDict))
