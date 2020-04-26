#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:07:30 2018

@author: Bonnie
"""
#Create two different graphs with data excerpted from your project in assignment #2.
#At least one graph should include at least two records' of data (e.g. a line chart with 
#two or more lines) with appropriate legends.
#The two graphs should use different formats (e.g. a line chart and pie chart).
#At least one python script should request a range of values (e.g. a range of years) 
#or selected values from the user and validate the user's response before creating the graph.


#data set from Kaggle: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps#, cleaned in Assignment 2 and assigned to applestore_out.csv

import pylab
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

    
    
#graph 1: pie chart of division of app genres
#graph 2: ask for genre, graph (line graph)

def graph_pie_genres():

    f = 'applestore_out.csv'
        
    try: 
        source = open(f,'r')
    except:
        print("File not found or could not be opened.")
    else:
        print("Data file opened, processing begins.")
        
        newlist = []
        
        for line in source:
            data = line.split(",")
            
            newlist.append(data[-2])
            
            new_no_title = newlist[1:len(newlist)]


        fig, ax = plt.subplots(figsize=(15, 12), subplot_kw=dict(aspect="equal"))
        
        graph_data = Counter(new_no_title)
        
        data = [float(v) for v in graph_data.values()]
        genres = [str(k) for k in graph_data]
        
        
        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%\n({:d} apps)".format(pct, absolute)
        
        
        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))
        
        ax.legend(wedges, genres,
                  title="Genres",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.setp(autotexts, size=8, weight="bold")
        
        ax.set_title("Genres of Apps")
        
        plt.show()

#    
#    labels = ['Book','Business','Catalogs','Education','Entertainment','Finance','Food & Drink',
#              'Games','Health & Fitness','Lifestyle','Medical','Music','Navigation','News',
#              'Photo & Video', 'Productivity','Reference','Shopping','Social Networking','Sports',
#              'Travel','Utilities','Weather']


graph_pie_genres()

    
#scatterplot of <= 20 apps plotting avg user ratings in all versions vs. 
#avg user ratings in current version

def scatter_plot():
            
        f = 'applestore_out.csv'
    
        try: 
            source = open(f,'r')
        except:
            print("File not found or could not be opened.")
        else:
            print("Data file opened, processing begins.")
            
            newlist_avgratings = []
            newlist_avgratings_current = []
            
            for line in source:
                new_data = line.split(",")
                
                newlist_avgratings.append(new_data[5])
                
                newlist_avgratings_current.append(new_data[6])
                
        apps_printed = input("How many apps do you want to see? (max. 20) ")
        
        if apps_printed.isalpha():
                print("Sorry. That is not a numerical value. ")
        if apps_printed > "20":
                print("Sorry. You've asked for the data of more than 20 apps.")

        else:
            rng = np.random.RandomState(0)
            x = newlist_avgratings[1:int(apps_printed)]
            y = newlist_avgratings_current[1:int(apps_printed)]
            colors = rng.rand(int(apps_printed)-1)
            sizes = 1000 * rng.rand(int(apps_printed)-1)

            plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
                        cmap='viridis')
            plt.colorbar();  # show color scale
            
            pylab.xlabel("Average Ratings Across All Versions")
            pylab.ylabel("Average Ratings For Current Version")
            
                    

scatter_plot()