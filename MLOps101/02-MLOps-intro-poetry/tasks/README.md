## Task 001: Home work - Data Manipulation with Pandas

Create a Python script named data_analysis.py that performs the following tasks:

**Answare**. I created the script in the scripts directory.

1. Using the Pandas library, read the CSV file from `Data/sales_data.csv` containing sales data.

2. Perform a simple data analysis by calculating and printing:

- The total sales (Quantity Sold * Unit Price) for each product.
- The total sales for the company.

3. Use the if __name__ == '__main__': structure to ensure that the code is executed only when the script is called directly, not when it is imported as a module.

4. Create a Makefile or Justfile with a rule named analysis that runs the data_analysis.py script.

5. Document the code appropriately, including explanatory comments.

Upon completion, execute the script in the terminal using the Makefile/Justfile and verify if the results are correct.

Additionally, test the script importation in a Python environment, ensuring that the analyses are not automatically executed when importing the module.

### Data Analysis

- Data describe:
  
Statistics  | Quantidade Vendida | Preço Unitário
------------|--------------------|---------------
count       |           6.000000 |       6.000000
mean        |           9.500000 |      16.083333
std         |           3.619392 |       3.810074
min         |           5.000000 |      12.000000
25%         |           7.250000 |      12.937500
50%         |           9.000000 |      15.750000
75%         |          11.500000 |      19.312500
max         |          15.000000 |      20.500000

The average sales are R\$ *16.08*, and product prices differ slightly. The standard deviation of prices is R\$ *3.81*.

Product A is the best-selling product and represents the highest amount raised by the company.

Produto   | Quantidade Vendida | Total Vendido  
----------|--------------------|---------------                                   
Produto A |                 25 |         512.5
Produto B |                 12 |         189.0
Produto C |                 20 |         240.0

The company's total sales are R\$ 941.5.

- Configuring a justfile:
  
```
shell: 
    poetry shell
execute: 
    poetry run python scripts/data_analysis.py
```

The `data_analysis.py` script answers all questions and task challenges.