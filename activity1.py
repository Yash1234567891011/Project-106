import csv
import numpy as np
def getdata(path):
    marks_in_percentage=[]
    days_present=[]
    with open (path) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_present}
def findcorrelaton(data):
    c=np.corrcoef(data["x"],data["y"])
    print("Correlation:",c[0,1])  
def main():
    path="./data1.csv"
    datasource=getdata(path)
    findcorrelaton(datasource)
main()                  