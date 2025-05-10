#   <font color=#AA98A9	>**PROJECT - **Analyzing the Iris dataset using Python****</font>  
### *Programming and Scripting*
<br /> 

Lecturer: Andrew Beatty   
Programming and Scripting S1-2025  
Higher Diploma in Science in Computing in Data Analytics  
Atlantic Technological University - ATU Galway   
  
Submission deadline : 12/05/2025   
  
Author : Maroua EL imame  

  
## 🔹Problem Statement    
Analyzing the Iris dataset using Python.  
This project concerns the well-known Fisher’s Iris data set.  
This is one of the earliest datasets used in the literature on classification methods and widely used in statistics and machine learning.  

## 🔹Task List  

Based on the project instructions, I enumerate the task list as follows :  
This list will be periodically updated upon the progression or completion of each step.


- [x]   Research the dataset online and write a summary about it in README. file.
- [x]   Download the data set and add it to your repository.
- [x]   Write a program called analysis.py
- [x]   analysis.py > outputs a summary of each variable to a single text file
- [x]   analysis.py > saves a histogram of each variable to png files
- [x]   analysis.py > outputs a scatter plot of each pair of variables
- [x]   Perform any other analysis you think is appropriate.
- [x]   in extra: a Jupyter notebook containing all necessary comments.**•***"This notebook is intended to contain only self-written content, as well as code from external sources to include with proper referencing where appropriate*.

## 🔹 Task Breakdown

This section breaks this project into smaller manageable steps.  
It outlines the project in terms of initiation, research, analysis and visualization of the **Iris dataset using Python** .  

This project follows the five key phases of the project lifecycle: Initiation, Planning, Execution, and Closing.  
This approach mirrors the methodology outlined in the Project Management Body of Knowledge (PMBOK® Guide), a globally recognized framework for project management practices.  



### 🔸Initiation phase :
---

This project aims to illustrate the practicality of using Python for data analysis.  
The topic of this project is : **Analyzing the Iris dataset using Python**. 

### 🔸Planning phase :
---

In this 2nd phase I list the steps to follow in order to achieve the project results.  

In order to successfully run and understand the results of this project, it is essential to identify the instruments to set up the appropriate environment.   

| Python on Windows     |
|----------|

[Download cmder](https://cmder.app/)  
[Download notepad++](https://notepad-plus-plus.org/)  
[Download anaconda (python)](https://www.anaconda.com/download)   
[Download vs code](https://code.visualstudio.com/Download)  

-Open VS Code and select "File > New File",  
-Save the file as .py format (e.g., my_script.py).  
-Write a Python script in the file.  
-With Python file open in VS Code, launch the terminal (see vscode menu)  
-Navigate through the terminal until reaching the same directory where Python file is 
located.  
-Possible to use Cmder for running Python code (CAT). Same as in Vs code, navigate to the 
directory where the Python file is saved using the cd command.  
-Cmder is primarily used for command-line operations, while Visual Studio Code is typically where most coding and debugging takes place.  
 
### 🔸Execution & Implementation phase :
---
### <font color=#5D3FD>****1.Research****</font>  

Why IRIS dataset ?  
The Iris data set is often used in data analysis because it’s small, simple, well-organized which makes it an easy dataset to work with.  
It’s great for learning how to explore data, identify patterns, and practice analysis and visualization.  

### <font color=#5D3FD>**2.Execution plan**</font>  

See Task list  

### <font color=#5D3FD>**3.Programming**</font>  

| **3.1**  Files     |
|----------|  


🔹file with *py format*   
  <small>Regular python file that can be executed in a single run. </small>  
    
🔹file with *ipynb format*  
   <small>Interactive PYthon NoteBook.       
  *'This notebook files can serve as a complete computational record of a session, interleaving executable code with explanatory text, mathematics, and rich representations of resulting objects.'*  
 *Jupyter Team*, *[The Jupyter Notebook, Introduction](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#:~:text=by%20MathJax.-,Notebook%20documents)*.</small>      


| **3.2**  Methods used for collecting/generating  data    |
|----------|  

Download [**Iris data set**](https://archive.ics.uci.edu/dataset/53/iris)  
the process of retrieving the data from an online source.  
The file was downloaded to ensure the data is locally available and ready for analysis.   

| **3.*3*  Methods for processing the data    |
|----------|  
Program dev progress :

🔹Part 1 :

-Import PYthon packages/libraries for data processing.
-In this repository, read the 'iris.data' file in csv format through the identified file path  
-View the dataframe  
-Dataset variables are separated into columns  
-Add columns names since the dataframe doesnt include any  
-Group the dataset by columns which corresponds to Iris data set features (variables)  
-Customise txt files names   
-Create txt files  
-Save a summary of each variable to a single txt file   
-Plot a histogram for each data set variable   
-Save a histogram of each variable to png files    
-Output a Scatterplot of each pair of variables from Iris data set 

overview :  
In this part 1, I introduced a few Python libraries during the process to demonstrate how Python can be a powerful and accessible tool for processing, analyzing and visualizing data.   
I demonstrated how to create and save text files directly to the repository, how to plot histograms and save them as separate '.png' files, then create a figure of each pair of variable within the Iris data set.  



🔹Part 2:

In this section, I will show how I can take this further within the notebook itself, by :    
-Exploring additional python libraries.  
-using Seaborn, Create 1 boxplot figure combining the 3 iris species with all their 4 features.  


 ### <font color=#5D3FD>**4.Data visualization**</font> 
See generated files in the current repository  

---

**Txt file of each variable summary  from Iris data set**:

summary of sepal length in cm  
summary of sepal width in cm  
summary of petal length in cm  
summary of petal width in cm  

**Histogram of each variable from Iris dataset**:  

Histogram of sepal length  
Histogram of sepal width in cm  
Histogram of petal length in cm  
Histogram of petal width in cm   

See cell output in the corresponding notebook  

---

**Scatter plots**:   

a figure of 6 plots where each scatter plot matches a pair of Iris dataset variables.  

sepal_length--sepal_width   
sepal_length--petal_length   
sepal_length--petal_width   
sepal_width --petal_length   
sepal_width --petal_width   
petal_length--petal_width   

**Pie plot** :  

1 pei chart

**Boxplots** :  

a figure of 1 boxplot, showing variables distribution by IRIS species 

**Heatmaps** :

3 species heatmaps showing correlation between iris variable

**Pair plot** :

scatter plots & KDE

### 🔸Closing phase  

---
* Summary of findings  


* Conclusion and Reflections  

This project provided a practical introduction to using Python for data analysis. The Iris dataset served as an excellent example, allowing me to apply Python methods for data reading, preprocessing, and visualization.  

Iris data set exploration brought into perspective how much insight can be gained from a small dataset, which demonstrates the practicality of using Python in data analysis and visualization.  

One of the main lessons I learned during this project was the importance of consistent referencing and accurate documentation.  
Adding explanations and comments alongside my code in notebook was useful to keep track of my code progress, to continiously understand the code, the ability to reproduce the code and most of all, it helped in filtering the best resources of documentation.  

This project is only a starting point for exploring data analysis and visualization. There's certainly much more to learn, but I am confident and encouraged to develop additional coding and alaysis skills. 

The IRIS data set, was indeed a story waiting to be told with the right tools and mindset.

dataset, no matter how small, carries a story waiting to be 

 More importantly, this whole process of data exploration and visualization reminded me that every dataset holds a story waiting to be told. And, who doesn’t like a story with a captivating plot?
 


<br /> 
<br /> 
<br /> 
<br /> 
<br /> 


