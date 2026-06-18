import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Remove $ sign and convert to number
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Calculate sales
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

final_df.to_csv("formatted_sales_data.csv", index=False)

print("formatted_sales_data.csv created successfully!")
