# This program is part of the programming and Scripting module project in ATU.
# This project concerns the well-known Fisher’s Iris dataset
# Please refer to Readme file and Jupyter notebook for aditional information about Iris dataset research, analysis and visualization.

# analysins.py : ***Analyzing the Iris dataset using Python***  
    # This program outputs a summary of each variable of Iris data  set to a single text file
    # Saves a histogram of each variable to png files
    # Outputs a scatter plot of each pair of variables
    # Performs any other analysis we think is appropriate.

# scope : 
    # Imagine we are giving a presentation on the Iris dataset where we explain what investigating a dataset entails and how Python can be used to do it.

# Author : Maroua EL imame 

# packages will be updated according to the task progression

# Import Python packages:

# for dataframes 
import pandas as pd
# machine Learning Library that contains datasets.
import sklearn as skl 
# plotting library
import matplotlib.pyplot as plt

# Load the iris dataset.
# using the file path as I already downloaded the IRIS dataset in csv format.
# assigning a value to the function

file_path = (r'C:\Users\marou\Desktop\pands\pands-project\iris dataset\iris.data')
iris_data = pd.read_csv(file_path)

# show the original data frame ; add a section title 
print( '     ', end='\n')
title1 = "Original data frame"
print(title1,end='\n\n')
print(iris_data)

# read the data returns the data but columns names are not included
# add meaningful columns names
column_names = ['sepal length in cm' , 'sepal width in cm' , 'petal length in cm' , 'petal width in cm', 'species']
iris_data = pd.read_csv(file_path, header= None, names=column_names)
# show data frame
title2 = "Data frame with header"
print( '     ', end='\n')
print(title2,end='\n\n')
print(iris_data)


# access dataset variables and output a single summary txt file to each
# sepal length variable
sepal_length = iris_data['sepal length in cm']

# summary of sepal length 
sepal_length_summary = sepal_length.describe()
#show
title3 = "Sepal length summary "
print( '     ', end='\n')
print(title3,end='\n\n')
print(sepal_length_summary)

sepal_width = iris_data['sepal width in cm']

# summary of sepal width  
sepal_width_summary = sepal_width.describe()
#show
title3 = "Sepal width summary "
print( '     ', end='\n')
print(title3,end='\n\n')
print(sepal_width_summary)

# summary of petal length  
petal_length = iris_data['petal length in cm']
petal_length_summary = petal_length.describe()
#show
title3 = "Petal length summary "
print( '     ', end='\n')
print(title3,end='\n\n')
print(petal_length_summary)

# summary of petal width  
petal_width = iris_data['petal width in cm']
petal_width_summary = petal_width.describe()
#show
title3 = "Petal width summary "
print( '     ', end='\n')
print(title3,end='\n\n')
print(petal_width_summary)

for column in iris_data.columns[:-1]:  # Skip 'Class'
    summary = iris_data[column].describe()
    file_name = f"{column}_summary.txt"
    
    # Step 3: Save summary to individual text file
    with open(file_name, 'w') as f:
        f.write(f"Summary for {column}:\n")
        f.write(summary.to_string())


print("      ", end='\n')
print("!Note: a summary of each variable of Iris data set was saved into a single text file, see repository files")

# in the analysis.ipynb I already created variables histgrams under one figure to save them in one ong file.
# However i should revise the code, in order to add a statement that will save each unique histogram into an individual file

for column in iris_data.columns[:-1]: 
    # Create a new figure for each plot
    plt.figure()  
    iris_data(column).hist() 

    # I will need to learn more how to call the column name in the histogram plot
    # 