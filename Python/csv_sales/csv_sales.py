import os
import pandas as pd

def read_sales_data(directory):
    """Read all sales data CSV files from the specified directory and its subdirectories."""
    sales_data = []
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return pd.DataFrame()  # Return an empty DataFrame if the directory doesn't exist

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv') and 'product_names' not in file:  # Exclude product_names.csv
                file_path = os.path.join(root, file)
                try:
                    sales_data.append(pd.read_csv(file_path))
                except Exception as e:
                    print(f"Error reading '{file_path}': {e}")
    return pd.concat(sales_data, ignore_index=True) if sales_data else pd.DataFrame()

def main():
    # Step 1: Read the sales data
    sales_directory = 'sales_data'  # Specify the directory containing sales data
    sales_df = read_sales_data(sales_directory)

    if sales_df.empty:
        print("No sales data available to process.")
        return

    # Step 2: Calculate total sales for each product
    try:
        total_sales = sales_df.groupby('Product ID')['Quantity sold'].sum().reset_index()
        total_sales.rename(columns={'Quantity sold': 'Total Quantity Sold'}, inplace=True)
    except KeyError as e:
        print(f"Error: Missing expected column in sales data - {e}")
        return

    # Step 3: Load product names
    try:
        product_names_df = pd.read_csv(os.path.join(sales_directory, 'product_names.csv'))
    except FileNotFoundError:
        print(f"Error: 'product_names.csv' not found in '{sales_directory}'.")
        return
    except Exception as e:
        print(f"Error reading 'product_names.csv': {e}")
        return

    # Merge total sales with product names
    try:
        sales_summary = pd.merge(total_sales, product_names_df, on='Product ID')
    except Exception as e:
        print(f"Error merging sales data with product names: {e}")
        return

    # Step 4: Calculate average quantity sold per month
    try:
        months_count = sales_df['Date'].nunique() / sales_df['Store ID'].nunique()  # Unique months per store
        sales_summary['Average Quantity Sold per Month'] = sales_summary['Total Quantity Sold'] / months_count
    except ZeroDivisionError:
        print("Error: Division by zero when calculating average quantity sold per month.")
        return
    except KeyError as e:
        print(f"Error: Missing expected column in sales summary - {e}")
        return

    # Step 5: Determine the top 5 best-selling products
    top_5_products = sales_summary.nlargest(5, 'Total Quantity Sold')

    # Step 6: Write the summary to a new CSV file
    output_file = 'sales_summary.csv'
    try:
        top_5_products[['Product ID', 'Product Name', 'Total Quantity Sold', 'Average Quantity Sold per Month']].to_csv(output_file, index=False)
        print(f"Sales summary has been written to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")

if __name__ == "__main__":
    main()