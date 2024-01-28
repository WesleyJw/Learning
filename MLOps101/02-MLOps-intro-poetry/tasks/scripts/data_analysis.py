import pandas as pd


def read_data(path):
    return pd.read_csv(path)


def data_explore(df):
    print(">>> Data head:")
    print(df.head())

    print(">>> Data describe:")
    print(df.describe())


def price_by_product(df):

    try:
        print("Price by product:")
        df["Total Vendido"] = df["Quantidade Vendida"] * \
            df["Preço Unitário"]

        result = df.groupby("Produto").agg(
            {"Quantidade Vendida": "sum",
                "Total Vendido": "sum"}
        )
        print("Total Sales by product:")
        print(result.head())
        return(result)
    except:
        print(
            "Something is wrong. please check if the df contain a <Quantidade Vendida> and <Preço Unitário> column.")


def total_sales(df):
    try:
        df = price_by_product(df)
        total = df["Total Vendido"].sum()
        print("Total Sales: ", total)
        return total
    except:
        print(
            "Something is wrong. please check your dataframe.")


if __name__ == "__main__":
    path = "Data/sales_data.csv"
    # Import dataset
    df = read_data(path)

    # Print data exploration
    data_explore(df)

    # Get Price by Product
    price_by_product(df)

    # Print total Sales
    total_sales(df)
