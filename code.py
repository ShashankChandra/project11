import numpy as np
import csv
import plotly.express as px

def plotFigure(data_path):
  with open(data_path) as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
    fig.show()

def getData(data_path):
  days = []
  marks = []
  with open(data_path) as f:
    data = csv.DictReader(f)
    for row in data:
      days.append(float(row["Marks In Percentage"]))
      marks.append(float(row["Days Present"]))
    
  return {"x" : days, "y": marks}

def defineCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"]) 
  print(correlation[0,1])

data_path = "data.csv"
data_source = getData(data_path)
defineCorrelation(data_source)
plotFigure(data_path)