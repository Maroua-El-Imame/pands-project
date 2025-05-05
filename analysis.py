# Analyzing the Iris dataset using Python**

#analysis.py
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


# Import Python packages:
# packages will be updated according to the task progression.
import csv
# for dataframes 
import pandas as pd
# machine Learning Library that contains datasets.
import sklearn as skl 
# plotting library
import matplotlib.pyplot as plt
# python library for creating iterators to produce complex iterators.  
from itertools import combinations
# Data visualization library
import seaborn as sns

# Load the iris dataset.
iris_data = pd.read_csv('iris dataset/iris.data')


# refering to the documentation file 'iris.names' in this repository. see atributes, which are corresponding to a list of columns names.
column_names = ['sepal length in cm' , 'sepal width in cm' , 'petal length in cm' , 'petal width in cm', 'class']
# read the data returns the data but columns names are not included
# add meaningful columns names
iris_data = pd.read_csv('iris dataset/iris.data', names= column_names)

# access dataset variables and output a single summary txt file to each
#----------------------------------------------------------------------

# sepal length variable
sepal_length = iris_data['sepal length in cm']
# summary of sepal length 
sepal_length_summary = sepal_length.describe()
# sepal width variable
sepal_width = iris_data['sepal width in cm']
# summary of sepal width  
sepal_width_summary = sepal_width.describe()
# petal length variable
petal_length = iris_data['petal length in cm']
# summary of petal length  
petal_length_summary = petal_length.describe()
# petal width variable
petal_width = iris_data['petal width in cm']
# summary of petal width  
petal_width_summary = petal_width.describe()

#loop through the columns in order to generate txt files.
for column in iris_data.columns[:-1]: 
    summary = iris_data[column].describe()
    file_name = f"{column}_summary.txt"
    
    # save summary to individual text files
    with open(file_name, 'w') as f:
        f.write(f"Summary for {column}:\n")
        f.write(summary.to_string())

# Create then save a histogram of each variable to png files  
#-----------------------------------------------------------

# to simplify the reading and coding, assign a variable for each feature of the data set.
sepal_length    = iris_data['sepal length in cm']
sepal_width     = iris_data['sepal width in cm']
petal_length    = iris_data['petal length in cm']
petal_width     = iris_data['petal width in cm']

# plot a histogram for each variable
# 1st histogram
plt.hist(sepal_length, ec='k', color='purple', alpha=0.6)
# add x label
plt.xlabel("Sepal Length in cm")
# add y label
plt.ylabel("count")
# add title
plt.title("Sepal Length Distribution")
# save histogram in .png file 
plt.savefig("histogram of sepal length.png")

# 2nd histogram
plt.hist(sepal_width, ec='k', color='green', alpha=0.6)
# add x label
plt.xlabel("Sepal Width in cm")
# add y label
plt.ylabel("count")
# add title
plt.title("Sepal Width Distribution")
# save
plt.savefig("histogram of sepal width.png")

# 3rd histogram
plt.hist(petal_length, ec='k', color='magenta', alpha=0.6)
# add x label
plt.xlabel("Petal Length in cm")
# add y label
plt.ylabel("count")
# add title
plt.title("Petal Length Distribution")
# save
plt.savefig("histogram of petal length.png")

# 4th histogram
plt.hist(petal_width, ec='k', color='orange', alpha=0.6)
# add x label
plt.xlabel("Petal Width in cm")
# add why label
plt.ylabel("count")
# add title
plt.title("Petal Width Distribution")
# save
plt.savefig("histogram of petal width.png")


#Otput a scatter plot of each pair of variables
#---------------------------------------------
# subplots adjust parameters
plt.subplots_adjust(hspace=0.3, top=0.9)
# plot (Scatter plot of Sepal Length vs Sepal Width ) in 1st row, 1st , with color refernce to iris species
axs[0, 0].scatter(sepal_length, sepal_width, marker='.',  c=colors)
# add a grid to simplfy repering the corresponding points
axs[0, 0].grid(color='blue', linestyle='--', linewidth=0.05)
# set x and y axis labels
axs[0, 0].set_xlabel('sepal length in cm')
axs[0, 0].set_ylabel('sepal width in cm')

## I have issues when running the file both in py and ipynb, still figuring out the source of the error, although it worked beforee the previosu commit !!!

# Boxplots :
#--------------------------------------

# Seaborn library is previously imported (as sns).
iris_ds = sns.load_dataset('iris')

# create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='feature', y='measurement', hue='species', data=)
# add title
plt.title('Iris data set \n  Variables distribution by IRIS species', c='g', alpha =0.7)
# set x and y labels
plt.xlabel('variables')
plt.ylabel('measurement (cm)')
# add meaningful
plt.legend(title='IRIS species')

# Heatmaps :
#-------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Define the list of species : # ['setosa', 'versicolor', 'virginica']
species_list = iris_data['class'].unique()  


    # Step 3b: Calculate the correlation matrix for only numeric 
    corr = subset.drop('class', axis=1).corr()

    # Step 3c: Create a heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='class', vmin=-1, vmax=
    plt.title(f'Feature Correlation Heatmap: {sp.capitalize()}')
    plt.tight_layout()

    
    # Pairplots :
    # ---------------------------------------------------------------------------