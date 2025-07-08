import nbformat as nbf

nb = nbf.v4.new_notebook()

# Markdown and code cells content
cells = [
    # Exercise 2 - Title (Markdown)
    nbf.v4.new_markdown_cell("# Data Science Tools and Ecosystem"),

    # Exercise 3 - Introduction (Markdown)
    nbf.v4.new_markdown_cell(
        "In this notebook, I will summarize some of the key tools, libraries, and languages used by data scientists. "
        "This is the final assignment for the Data Science Tools course."
    ),

    # Exercise 4 - List of Data Science Languages (Markdown)
    nbf.v4.new_markdown_cell(
        "## Some of the popular languages used by Data Scientists include:\n\n"
        "1. Python  \n"
        "2. R  \n"
        "3. SQL  \n"
        "4. Julia  \n"
        "5. Scala  "
    ),

    # Exercise 5 - List of Data Science Libraries (Markdown)
    nbf.v4.new_markdown_cell(
        "## Commonly used libraries by Data Scientists:\n\n"
        "1. Pandas  \n"
        "2. NumPy  \n"
        "3. Matplotlib  \n"
        "4. Scikit-learn  \n"
        "5. TensorFlow  \n"
        "6. ggplot2  "
    ),

    # Exercise 6 - Table of Data Science Tools (Markdown)
    nbf.v4.new_markdown_cell(
        "## Examples of Data Science Tools\n\n"
        "| Tool            | Type               | Usage                      |\n"
        "|-----------------|--------------------|----------------------------|\n"
        "| RStudio         | IDE                | R language development     |\n"
        "| Apache Spark    | Big Data Platform  | Large-scale data processing|\n"
        "| TensorFlow      | ML Library         | Deep learning models       |"
    ),

    # Exercise 7 - Intro to arithmetic expressions (Markdown)
    nbf.v4.new_markdown_cell("### Below are examples of simple arithmetic operations using Python:"),

    # Exercise 8 - Multiply and add numbers (Code)
    nbf.v4.new_code_cell("# This is a simple arithmetic expression to multiply and then add integers\n(5 * 4) + 3"),

    # Exercise 9 - Convert minutes to hours (Code)
    nbf.v4.new_code_cell(
        "# This will convert 200 minutes to hours\n"
        "minutes = 200\n"
        "hours = minutes / 60\n"
        "hours"
    ),

    # Exercise 10 - List Objectives (Markdown)
    nbf.v4.new_markdown_cell(
        "## Objectives of this notebook:\n"
        "- List data science languages  \n"
        "- List data science libraries  \n"
        "- Show tools used in data science  \n"
        "- Practice arithmetic operations  \n"
        "- Convert time from minutes to hours"
    ),

    # Exercise 11 - Author name (Markdown)
    nbf.v4.new_markdown_cell("**Author:** MUHRIS_A.J")
]

# Add cells to notebook
nb['cells'] = cells

# Save notebook to a file
filename = "Data_Science_Tools_Assignment.ipynb"
with open(filename, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook '{filename}' created successfully!")

