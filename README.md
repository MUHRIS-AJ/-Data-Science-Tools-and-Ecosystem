import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

# Exercise 2 - Title
nb['cells'].append(nbf.v4.new_markdown_cell(
    "# Data Science Tools and Ecosystem\n"
    "This notebook summarizes some of the key tools, libraries, and languages used by data scientists.\n\n"
    "This is the final assignment for the Data Science Tools course."
))

# Exercise 3 - Introduction
intro_text = """\
## Introduction
Data Science is an interdisciplinary field that combines programming, statistics, mathematics, and domain expertise to extract meaningful insights from data.

In this notebook, we will explore:
- The most common programming languages used by data scientists.
- Widely adopted libraries that simplify data analysis and machine learning.
- Popular tools and platforms in the data science ecosystem.
- Simple arithmetic expressions to demonstrate coding in Python.

This notebook serves as a summary of the Data Science tools covered in the course.
"""
nb['cells'].append(nbf.v4.new_markdown_cell(intro_text))

# Exercise 4 - Data Science Languages
languages_text = """\
## Some of the popular languages used by Data Scientists include:
1. Python
2. R
3. SQL
4. Julia
5. Scala
"""
nb['cells'].append(nbf.v4.new_markdown_cell(languages_text))

# Exercise 5 - Data Science Libraries
libraries_text = """\
## Commonly used libraries by Data Scientists:
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow
- ggplot2
"""
nb['cells'].append(nbf.v4.new_markdown_cell(libraries_text))

# Exercise 6 - Data Science Tools Table
tools_table = """\
## Data Science Tools
| Tool / Platform | Category | Description |
|-----------------|---------|-------------|
| Jupyter Notebook | IDE / Notebook | Interactive coding and visualization environment |
| RStudio | IDE | Integrated environment for R programming |
| Apache Spark | Big Data Framework | Distributed computing for big data processing |
| TensorFlow | ML Framework | Deep learning and neural networks |
| Hadoop | Big Data Platform | Distributed storage and processing of large data sets |
| Excel | Data Analysis Tool | Widely used for quick data analysis and visualization |
| Google Colab | Cloud Notebook | Cloud-based Jupyter Notebook with free GPU access |
| Power BI / Tableau | Visualization Tool | Business Intelligence and data visualization dashboards |
"""
nb['cells'].append(nbf.v4.new_markdown_cell(tools_table))

# Exercise 7 - Arithmetic Expression Introduction
nb['cells'].append(nbf.v4.new_markdown_cell(
    "## Examples of Arithmetic Expressions\n"
    "Below are examples of simple arithmetic operations using Python:\n\n"
    "- Addition (+)\n"
    "- Subtraction (-)\n"
    "- Multiplication (*)\n"
    "- Division (/)\n"
    "- Modulus (%)\n"
    "- Exponentiation (**)"
))

# Exercise 8 - Multiply and Add Numbers
multiply_add_code = """\
# This is a simple arithmetic expression to multiply and then add integers
a = 5
b = 4
c = 3

result = (a * b) + c
print("The result of (5 * 4) + 3 is:", result)
"""
nb['cells'].append(nbf.v4.new_code_cell(multiply_add_code))

# Exercise 9 - Convert Minutes to Hours
minutes_to_hours_code = """\
# This code converts minutes into hours
minutes = 200
hours = minutes / 60
print(minutes, "minutes is equal to", hours, "hours.")
"""
nb['cells'].append(nbf.v4.new_code_cell(minutes_to_hours_code))

# Exercise 10 - Objectives
objectives_text = """\
## Objectives of this notebook:
- List data science languages
- List data science libraries
- Show tools used in data science
- Practice arithmetic operations
- Convert time from minutes to hours
"""
nb['cells'].append(nbf.v4.new_markdown_cell(objectives_text))

# Exercise 11 - Author
author_text = """\
## Author
Name: MUHRIS_A.J  
Course: Data Science Tools and Ecosystem  
Date: 2025-09-08
"""
nb['cells'].append(nbf.v4.new_markdown_cell(author_text))
