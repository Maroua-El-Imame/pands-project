# This program is part of the programming and Scripting module project in ATU.
# This project concerns the well-known Fisher’s Iris dataset
# Please refer to Readme file and Jupyter notebook for aditional information about Iris dataset research, analysis and visualization.

# 1. Download and place the Iris into the current repository:
                # https://archive.ics.uci.edu/dataset/53/iris

# 2. Current file : analysis.py
    # This program outputs a summary of each variable to a single text file
    # Saves a histogram of each variable to png files
    # Outputs a scatter plot of each pair of variables
    # Performs any other analysis we think is appropriate.

# scope : 
    # Imagine we are giving a presentation on the Iris dataset where we explain what investigating a dataset entails and how Python can be used to do it.

# Author : Maroua EL imame 

### ***Analyzing the Iris dataset using Python***
#### Import Python packages:

# packages will be updated according to the task progression.

import csv
# for dataframes 
import pandas as pd
# machine Learning Library that contains datasets.
import sklearn as skl 


#Write a program called analysis.py that:
#1. Outputs a summary of each variable to a single text file,
# Txt Files

#* Load dataset
# Load the iris dataset.
# using the file path as I already downloaded the IRIS dataset in csv format.
# the method is explained in Pandas documentation 
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None  )
#* Import dataset previously downloaded
# as we already imported pd and downloaded the dataset, I went to the folder where the file is saved, and through properties I did copy the file path.
# assigning a value 
file_path = (r'C:\Users\marou\Desktop\pands\pands-project\iris dataset\iris.data')
# read the data
df = pd.read_csv(file_path)
# show dataframe
# dataset shape shows 5 columns with 149 rows. I can see that the target column (species) of the dataset is included, while the column names are not. 
# reference : https://archive.ics.uci.edu/dataset/53/iris
df
# add meaningful columns names
# https://archive.ics.uci.edu/dataset/53/iris   ( see variables table )
column_names = ['sepal length in cm ' , 'sepal width in cm ' , 'petal lengthin cm ' , 'petal width in cm ', 'species']
iris_data = pd.read_csv(file_path, header= None, names=column_names)
# show data frame
iris_data
# access the columns names 
iris_data.columns
#* Output a summary of each Iris dataset variable to a single text file  
# group by column names allows me to access each variable of dataset 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html ( iloc documentation )
# https://www.w3schools.com/python/pandas/ref_df_iloc.asp ( use iLoc practice)

sepal_length= iris_data.iloc[:,0]
sepal_width = iris_data.iloc[:,1]
petal_length= iris_data.iloc[:,2]
petal_width =iris_data.iloc[:,3]

# save sepal length column values into a txt file
# showing the header in txt file by setting the parameter header to True, hiding the index by setting it to False
# repeat for the 4 variables

# Sepal length
sepal_length.to_csv('sepal_length.txt', header=True, index=False)
# Sepal width
sepal_width.to_csv('sepal_width.txt', header=True, index=False)
# Petal length
petal_length.to_csv('petal_length.txt', header=True, index=False)
# Petal width
petal_width.to_csv('petal_width.txt', header=True, index=False)

