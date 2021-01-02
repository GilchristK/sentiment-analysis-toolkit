#Author: Katuta Kaunda
#Date: 20-oct-2020
#Description: social media sentiment visualiser
import sys,getopt
import os
import pandas as pd
import plotly
import plotly.express as plt
import time
from sentiment_analyser import *

##generates a bar chart visualization using plotly
def generateVisualization(df):
    print(df.groupby(by=['sentiment']).describe())
    df1 = df.groupby(["sentiment"]).count().reset_index()
    fig = plt.bar(df1,y=df.groupby(["sentiment"]).size(),x="sentiment",color='sentiment',title='AFINN sentiment Analysis') 
    saveReport(fig)

##Saves the generated visualizationas an html file
def saveReport(fig):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    
    # html file
    plotly.offline.plot(fig, filename='reports\sentiment_results-'+timestr+'.html')

def main():
    
    df = read_excel(r'data_store\reviews_pseudoanonymised.xlsx')
    df2 = analyse_sentiments(df)
    generateVisualization(df2)

if __name__ == '__main__':
    main()
