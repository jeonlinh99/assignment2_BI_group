import pandas as pd

new_sales_record = pd.read_csv('Sales-Records.csv')
# Remove rows that have null Unit Price, Unit cost, Units Sold, Total Cost
new_sales_record.dropna(subset=["Unit Price", "Unit Cost", "Total Cost","Units Sold"], inplace= True)
# Remove rows that have special characters(!@#$%^&*) in columns: Item Type
speChars = ["!",'@','#','$','%','^','&','*']
for char in speChars:
    new_sales_record['Item Type'] = new_sales_record['Item Type'].str.replace(char, '',regex= True)
# Replace wrong data to default: negative value in column Total Profit to 0:
for x in new_sales_record.index:
    if new_sales_record.loc[x, "Total Profit"] < 0:
        new_sales_record.loc[x, "Total Profit"] = 0
print(new_sales_record)
# save new_sales_record to a new file "New_sales_record.csv":
new_sales_record.to_csv('New_sales_record.csv', index=False)
