import pandas as pd
import glob
import os

data_folder = os.path.join('data')
csv_files = glob.glob(os.path.join(data_folder, '*.csv'))
print(f"CSV files found: {csv_files}\n")

df_list = [pd.read_csv(f) for f in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

#print(f"Combined dataframe found: {combined_df}\n")

combined_df = combined_df[combined_df["product"] == "pink morsel"]

combined_df['price'] = combined_df['price'].str.replace('$', '', regex=False).astype(float)
combined_df['quantity'] = combined_df['quantity'].astype(float)

combined_df['sales'] = combined_df['quantity'] * combined_df['price']
combined_df = combined_df[['sales', 'date', 'region']]
print(combined_df.head())


output_folder = os.path.join('pink_morsel_sales_data.csv')
combined_df.to_csv(output_folder, index=False)
print(f"Done! Output saved to: {output_folder}")



