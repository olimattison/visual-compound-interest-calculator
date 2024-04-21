# Compound Interest Calculator

This Python-based application provides a simple graphical user interface (GUI) to calculate
compound interest over time, displaying both numerical data and a graphical representation of the growth.

## Features

- Input principal amount, annual interest rate, time in years, and compounds per year.
- Calculate the future value of an investment based on the compound interest formula.
- Visualize the growth of the investment over time through an interactive graph.

## Prerequisites

Before you run the application, ensure you have Python installed on your system. Python 3.6 or higher is recommended. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, the application requires the following Python libraries:
- `customtkinter`
- `matplotlib`
- `numpy`

These will be installed in the next step

## Installation

1. Download / clone repository:
```bash
git clone https://github.com/olimattison/visual-compound-interest-calculator.git
```

2. Download prerequisites:
```bash
pip install -r requirements.txt 
```


## Usage
To run the application, execute main.py from a command line

example usage:
 ```py C:\path\to\main.py```

Upon running the application, you will see a GUI window. Enter the following information:

- **Pincipal ($):** The initial amount of money invested or borrowed.
- **Annual Rate (%):** The interest rate per year as a percentage.
- **Time (years):** The total number of years the money is invested or borrowed for.
- **Compounds per Year:** How often the interest is compounded per year.

After filling out the fields, click the "Calculate" button to see the future value of the investment and a graph
 depicting the growth over time. Move your mouse over the graph to see details about specific points in time


## License
This project is open-source and available under the MIT License. For more details, see
the LICENSE file in the project repository.

## Contributions
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## Support
For support, open an issue on the GitHub project page.
