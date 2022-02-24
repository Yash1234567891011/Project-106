import csv
import numpy as np
def getdata(path):
    coffee_in_ml=[]
    sleep_in_hours=[]
    with open (path) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x":coffee_in_ml,"y":sleep_in_hours}
def findcorrelaton(data):
    c=np.corrcoef(data["x"],data["y"])
    print("Correlation:",c[0,1])  
def main():
    path="./data2.csv"
    datasource=getdata(path)
    findcorrelaton(datasource)
main()                  