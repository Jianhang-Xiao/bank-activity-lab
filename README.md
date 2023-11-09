# README

Credit to the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) for this template. To complete this project, delete all template text (save for the headers) and fill in your own information.

Begin reading `instructions.md` to get started.

## Project Intro/Objective
The purpose of this project is to analyze stock data. This pipeline is used by the machine learning team to restructure of data, which will subsequetnly be interated with daily news headline data to measure how reliable predicts stock price. 


### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling


### Technologies
* Python
* Pandas, jupyter


## Project Description

This project uses a CSV file representing daily closing stock prices and calculates summary statistics. The input to these methods is the stock data loaded from the file, and the general actions involve iterating through the rows, converting relevant values to floats, and performing statistical calculations. The output for each method is a list of calculated values (averages, medians, and standard deviations) for each row in the stock data. The challenge I had at the beginning was reading the instructions file to understand exactly what I needed to do. Then, I understood I needed to run the code in the “StockMetrics” file that also imported coding from the “StockData.” “StockMetrics” is inheriting from “StockData.” List comprehension is also hard to write for the code: new_row=[float(val) for val in row[1:] if val !="" and val !=" "] The purpose of this line is to create a new list (“new_row”) containing the floating point that is non-empty and non-space values in the sub list “row” staring from the second element. It is a “for” loop used in the context of a list comprehension. The new list is called "new_row", which uses a list comprehension to interate through each element in the "row" list. The loop continues to the next row and reperated for each row until finish. 

