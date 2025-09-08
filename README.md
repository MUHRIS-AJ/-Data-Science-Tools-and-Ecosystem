import nbformat as nbf

# Create a new notebook object
nb = nbf.v4.new_notebook()

# A list to hold all the cells
cells = []

# Exercise 2 - Title (Markdown)
cells.append(nbf.v4.new_markdown_cell("# Data Science Tools and Ecosystem"))

# Exercise 3 - Introduction (Markdown)
intro_text = """
## Introduction
Data Science is an interdisciplinary field that combines programming, statistics, mathematics, and domain expertise to extract meaningful insights from data. 

In this notebook, we will explore:
- The most common programming languages used by data scientists.
- Widely adopted libraries that simplify data analysis and machine learning.
- Popular tools and platforms in the data science ecosystem.
- Simple arithmetic expressions to demonstrate coding in Python.

This notebook serves as a summary of the Data Science tools covered in the course.
"""
cells.append(nbf.v4.new_markdown_cell(intro_text))

# Exercise 4 - List of Data Science Languages (Markdown)
languages_text = """
## Some of the popular languages used by Data Scientists include:

1. Python
2. R
3. SQL
4. Julia
5. Scala
"""
cells.append(nbf.v4.new_markdown_cell(languages_text))

# Exercise 5 - List of Data Science Libraries (Markdown)
libraries_text = """
## Commonly used libraries by Data Scientists:

1. Pandas
2. NumPy
3. Matplotlib
4. Scikit-learn
5. TensorFlow
6. ggplot2
"""
cells.append(nbf.v4.new_markdown_cell(libraries_text))

# Exercise 6 - Table of Data Science Tools (Markdown)
table_text = """
## Data Science Tools

| Tool / Platform | Category | Description |
|-----------------|----------|-------------|
| **Jupyter Notebook** | IDE / Notebook | Interactive coding and visualization environment |
| **RStudio** | IDE | Integrated environment for R programming |
| **Apache Spark** | Big Data Framework | Distributed computing for big data processing |
| **TensorFlow** | ML Framework | Deep learning and neural networks |
| **Hadoop** | Big Data Platform | Distributed storage and processing of large data sets |
| **Excel** | Data Analysis Tool | Widely used for quick data analysis and visualization |
| **Google Colab** | Cloud Notebook | Cloud-based Jupyter Notebook with free GPU access |
| **Power BI / Tableau** | Visualization Tool | Business Intelligence and data visualization dashboards |
"""
cells.append(nbf.v4.new_markdown_cell(table_text))

# Exercise 7 - Intro to arithmetic expressions (Markdown)
arithmetic_intro_text = """
### Examples of Arithmetic Expressions
Below are examples of simple arithmetic operations using Python:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
"""
cells.append(nbf.v4.new_markdown_cell(arithmetic_intro_text))

# Exercise 8 - Multiply and Add Numbers (Code Cell)
multiply_add_code = """
# This is a simple arithmetic expression to multiply and then add integers
a = 5
b = 4
c = 3

result = (a * b) + c
print("The result of (5 * 4) + 3 is:", result)
"""
cells.append(nbf.v4.new_code_cell(multiply_add_code))

# Exercise 9 - Convert Minutes to Hours (Code Cell)
minutes_to_hours_code = """
# This code converts minutes into hours
minutes = 200

# 1 hour = 60 minutes
hours = minutes / 60

print(minutes, "minutes is equal to", hours, "hours.")
"""
cells.append(nbf.v4.new_code_cell(minutes_to_hours_code))

# Exercise 10 - Objectives (Markdown)
objectives_text = """
## Objectives of this notebook:
- List data science languages
- List data science libraries
- Show tools used in data science
- Practice arithmetic operations
- Convert time from minutes to hours
"""
cells.append(nbf.v4.new_markdown_cell(objectives_text))

# Exercise 11 - Author's Name (Markdown)
author_text = """
## Author
**Name:** MUHRIS_A.J
**Course:** Data Science Tools and Ecosystem
**Date:** 2025-09-08
"""
cells.append(nbf.v4.new_markdown_cell(author_text))

# Add the compiled list of cells to the notebook object
nb['cells'] = cells

# Save the notebook to a file
filename = "Data_Science_Tools_Assignment.ipynb"
with open(filename, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook '{filename}' created successfully!")
