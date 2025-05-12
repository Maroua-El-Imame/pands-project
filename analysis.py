# Project - Programming and Scripting module 
# Analyzing the Iris dataset using Python

# current file : analysis.py
# This program is part of the programming and Scripting module project in ATU.
# This project concerns the well-known Fisher’s Iris dataset
# Please refer to Readme file and Jupyter notebook for aditional information about Iris dataset research, analysis and visualization

# This program :
# Outputs a summary of each variable of Iris data  set to a single text file
# Saves a histogram of each variable to png files
# Outputs a scatter plot of each pair of variables
# Performs additional analysis and saves the output into png files. 

# Author : Maroua EL imame 


# Import Python packages:
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
iris_data = pd.read_csv('iris.data')

# refering to the documentation file 'iris.names' in this repository. see atributes, which are corresponding to a list of columns n
column_names = ['sepal length in cm' , 'sepal width in cm' , 'petal length in cm' , 'petal width in cm', 'class']
# add meaningful columns names
iris_data = pd.read_csv('iris.data', names= column_names)

# access dataset variables and output a single summary txt file to each iris variable

# summary of sepal length 
sepal_length = iris_data['sepal length in cm']
sepal_length_summary = sepal_length.describe()

# summary of sepal width  
sepal_width = iris_data['sepal width in cm']
sepal_width_summary = sepal_width.describe()

# summary of petal length  
petal_length = iris_data['petal length in cm']
petal_length_summary = petal_length.describe()

# summary of petal width  
petal_width = iris_data['petal width in cm']
petal_width_summary = petal_width.describe()

# save files
# I skip the class. I applied the negative indexing method.
for column in iris_data.columns[:-1]:  
    # summary of each column
    summary = iris_data[column].describe()
    # create a file for each column, add the file name and format
    # f-string formatting will generate a filename based on each column
    file_name = f"summary of {column}.txt"
    # open each file created previosuly, and overwrite the summary 
    with open(file_name, "w") as f:
        f.write(summary.to_string())

# Create then save a histogram of each variable to png files  

# to simplify the reading and coding, assign a variable for each feature of the data set
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
plt.clf()

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
plt.clf()

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
plt.clf()

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
plt.clf()

# Output a scatter plot of each pair of variables  

# the input list used to find the combinations.
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# imported in cell 1 itertools package to apply the combination method into python.
# itertools helps to create and work with repeated or unique patterns from a given list.

# generate all possible combinations(length = 2) generates pairs where the order doesn't matter.
#for i in combinations(columns, 2):
    #print(i)

# create a color dictionary
# assigning colors to species, each specie is coloured differently so it is visually identifiable. 
species_colors = {
    'Iris-setosa': '#00A36C',
    'Iris-versicolor': '#EE4B2B',
    'Iris-virginica': 'blue'
}

# access the class column , then appply the mapping function which in this case is mapping the species names to colors.
colors = iris_data['class'].map(species_colors)

# create a  grid of 2 rows 3 columns each (6 plots)
fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# cutomizing different parameters of the function 
fig.suptitle('scatter plot of every pair of variables \n  Iris Dataset', size=16, c='g', alpha = 0.7)

# 1st plot (Scatter plot of Sepal Length vs Sepal Width ) in 1st row, 1st column , with color refernce to iris species
axs[0, 0].scatter(sepal_length, sepal_width, marker='.',  c=colors)
# add a grid for easier reference of point
axs[0, 0].grid(color='blue', linestyle='--', linewidth=0.05)
# set x and y axis labels
axs[0, 0].set_xlabel('sepal length in cm')
axs[0, 0].set_ylabel('sepal width in cm')

# 2nd plot (Scatter plot of Sepal Length vs Petal Length) in 1st row
axs[0, 1].scatter(sepal_length, petal_length, marker='.',  c=colors)
axs[0, 1].grid(color='blue', linestyle='--', linewidth=0.05)
axs[0, 1].set_xlabel('sepal length in cm')
axs[0, 1].set_ylabel('petal length in cm')

# 3rd plot (Scatter plot of Sepal Length vs Petal Width) in 1st row,
axs[0, 2].scatter(sepal_length, petal_width, marker='.',  c=colors)
axs[0, 2].grid(color='blue', linestyle='--', linewidth=0.05)
axs[0, 2].set_xlabel('sepal length in cm')
axs[0, 2].set_ylabel('petal width in cm')

# 1st plot (Scatter plot of Sepal Width vs Petal Length) in 2nd row 
axs[1, 0].scatter(sepal_width, petal_length, marker='.',  c=colors)
axs[1, 0].grid(color='blue', linestyle='--', linewidth=0.05)
axs[1, 0].set_xlabel('Sepal Width  in cm')
axs[1, 0].set_ylabel('Petal Length in cm')

# 2nd plot (Scatter plot of Sepal Width vs Petal Width ) in 2nd row 
axs[1, 1].scatter(sepal_width, petal_width, marker='.',  c=colors)
axs[1, 1].grid(color='blue', linestyle='--', linewidth=0.05)
axs[1, 1].set_xlabel('Sepal Width in cm')
axs[1, 1].set_ylabel('Petal Width in cm')

# 3rd plot (Scatter plot of Petal Length vs Petal Width) in 2nd row,
axs[1, 2].scatter(petal_length, petal_width, marker='.',  c=colors)
axs[1, 2].grid(color='blue', linestyle='--', linewidth=0.05)
axs[1, 2].set_xlabel('Petal Length')
axs[1, 2].set_ylabel('Petal Width')

# save fig 
plt.savefig("scatter plots of each pair of Iris variables")

# Create a pie chart of Iris species samples count 

# load the Iris dataset , Seaborn.
iris = sns.load_dataset('iris')

# count the number of instances for each species
species_counts = iris['species'].value_counts()

# create a figure
plt.figure(figsize=(8, 7))
# plot 
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('rocket'))
# add title
plt.title('Distribution of Iris Species')

# save fig
plt.savefig("pie plot of iris species count")

# Create boxplots  

# Seaborn library is previously imported (as sns).
# load dataset
iris_ds = sns.load_dataset('iris')

# melt the dataframe to long format, meaning, I need to convert the columns to rows.
iris_melted = pd.melt(iris_ds, id_vars='species', var_name='feature', value_name='measurement')

# plot the boxplot
plt.figure(figsize=(10, 6))

# each color in the box refers to an iris species. The color-coded boxes represent the interquartile range (middle data or 50%), while the lines (whiskers) show overall spread. The horizontal line inside each box is the median.
# Q1 (25th percentile) is the line, shown at the bottom edge of the box, Q3 (75th percentile) is the line shown at the top edge of the box
sns.boxplot(x='feature', y='measurement', hue='species', data=iris_melted)

# draw vertical lines to separate iris data set variables visually. 
for x in [0.5,1.5,2.5]: 
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)

# add title
plt.title('Iris data set \n  Variables distribution by IRIS species', c='g', alpha =0.7)
# set x and y labels
plt.xlabel('variables')
plt.ylabel('measurement (cm)')
# add meaningful legend
plt.legend(title='IRIS species')

# save
plt.savefig("box plots of Iris species variables")

# create Heatmaps

# identify the list of species ['setosa', 'versicolor', 'virginica']
species_list = iris_data['class'].unique() 

# loop through each species
for sp in species_list:
    # filter the dataset to only save rows of the actual species
    subset = iris_data[iris_data['class'] == sp]
    # calculate the correlation matrix
    # reference : The code was initially proposed by microsoft Copilot (AI) (generated on Bing browser search bar ), I had this idea of generating unique heatmaps of each iris species, but was unable to find approximate code through my usual sources
    # prompt used : "simplified Python code to create individual correlation heatmaps for each of the three Iris species.", the code then was updated using 'class'(column name) instead of 'species'
    corr = subset.drop('class', axis=1).corr()

    # plot heatmap  
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f'Iris dataset \n Correlation Heatmap for {sp.capitalize()}')
    plt.tight_layout()

    # save plots
    filename = f'heatmap correlation of {sp.lower()}.png'
    plt.savefig(filename, dpi=300)

    # close plot to avoid overlap
    plt.close()

# create pairplot
# load Iris dataset using seaborn.load_dataset() method, which allows users to quickly load sample datasets provided by Seaborn. 
# seaborn library is previously imported (as sns).
iris_data = sns.load_dataset('iris')

# visualize using pairplot
sns.pairplot(iris_data, hue='species', palette=['#8A2BE2', '#0343df', '#FFD700'])

# save
plt.savefig("pairplot of pairwise relationships of Iris variables")

# code ends here

