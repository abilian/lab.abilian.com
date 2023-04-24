
Here are three packages that can create and format text (aka "ASCII") tables in Python:

1. [**tabulate**](https://pypi.org/project/tabulate/): tabulate is a library for formatting and printing tables in Python. It can create tables from a variety of data sources, including lists, tuples, and dictionaries.
2. [**PrettyTable**](https://pypi.org/project/prettytable/): a simple library to create ASCII tables in Python. It can create tables from a variety of data sources, including lists, dictionaries, and CSV files.
3. [**Texttable**](https://pypi.org/project/texttable/): a library for creating ASCII tables in Python. It supports a wide range of formatting options, including alignment, padding, and border styles.


Additionally:

- [**rich**] is another Python library that can be used to print pretty tables in Python, along with many other types of rich output, such as syntax highlighting, progress bars, and more. Its API is similar to PrettyTable.
- [**Pandas**](https://pandas.pydata.org/) can be used to create and manipulate tables. It provides a lot of options for formatting and printing tables, including HTML and LaTeX output. But it is a large piece of software and shouldn't be imported just for its table-printing abilities.
- [**Tablib**](https://pypi.org/project/tablib/) is a Python library for working with tabular data, such as spreadsheets or CSV files. It provides a flexible data container called `Dataset` that can be used to store and manipulate tabular data in memory, as well as a variety of tools for importing, exporting, and transforming data between different formats and sources.


## Tabulate usage

To use the tabulate library in Python, you first need to install it using pip:

```
pip install tabulate
```

Once you have installed the library, you can use it in your Python code by importing it as follows:

```python
from tabulate import tabulate
```

Then, you can pass your data as a list of lists or a list of tuples to the `tabulate()` function along with the table headers. For example:

```python
data = [
    ["John", 28, "Male"],
    ["Alice", 32, "Female"],
    ["Bob", 45, "Male"]
]

headers = ["Name", "Age", "Gender"]

print(tabulate(data, headers=headers))
```

This will output the following table:

```
Name    Age  Gender
------  ---  -------
John     28  Male
Alice    32  Female
Bob      45  Male
```

You can also customize the formatting of the table by setting various parameters of the `tabulate()` function, such as the alignment of columns, the table border style, and the table format (e.g., "plain", "simple", "grid", "pipe", "orgtbl", "jira", "presto", "fancy_grid", "github", "mediawiki", "moinmoin", "latex", "latex_booktabs", "tsv", etc.). For more information, you can refer to the official documentation of the library.


## PrettyTable usage

To use the PrettyTable library in Python, you first need to install it using pip:

```
pip install prettytable
```

Once you have installed the library, you can use it in your Python code by importing it as follows:

```python
from prettytable import PrettyTable
```

Then, you can create a new instance of the `PrettyTable` class and add data to it using the `add_row()` method. For example:

```python
# create a new table
table = PrettyTable()

# add columns to the table
table.field_names = ["Name", "Age", "Gender"]

# add rows to the table
table.add_row(["John", 28, "Male"])
table.add_row(["Alice", 32, "Female"])
table.add_row(["Bob", 45, "Male"])

# print the table
print(table)
```

This will output the following table:

```
+-------+-----+--------+
|  Name | Age | Gender |
+-------+-----+--------+
|  John |  28 |  Male  |
| Alice |  32 | Female |
|  Bob  |  45 |  Male  |
+-------+-----+--------+
```

You can customize the formatting of the table by setting various properties of the `PrettyTable` object, such as the alignment of columns, the border style, and the header style. For more information, you can refer to the official documentation of the library.


## Texttable usage

To use the Texttable library in Python, you first need to install it using pip:

```
pip install texttable
```

Once you have installed the library, you can use it in your Python code by importing it as follows:

```python
from texttable import Texttable
```

Then, you can create a new instance of the `Texttable` class and add data to it using the `add_row()` method. For example:

```python
# create a new table
table = Texttable()

# set the table header
table.header(["Name", "Age", "Gender"])

# add rows to the table
table.add_row(["John", 28, "Male"])
table.add_row(["Alice", 32, "Female"])
table.add_row(["Bob", 45, "Male"])

# print the table
print(table.draw())
```

This will output the following table:

```
+-------+-----+--------+
|  Name | Age | Gender |
+=======+=====+========+
|  John |  28 |  Male  |
+-------+-----+--------+
| Alice |  32 | Female |
+-------+-----+--------+
|  Bob  |  45 |  Male  |
+-------+-----+--------+
```

You can customize the formatting of the table by setting various properties of the `Texttable` object, such as the alignment of columns, the border style, and the header style. For more information, you can refer to the official documentation of the library.