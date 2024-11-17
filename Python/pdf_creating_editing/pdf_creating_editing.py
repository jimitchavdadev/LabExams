import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger
from datetime import datetime

def load_orders(file_path):
    """Load order data from a CSV file."""
    return pd.read_csv(file_path)

def generate_invoice(order):
    """Generate a PDF invoice for a given order."""
    order_id = order['Order ID']
    customer_name = order['Customer Name']
    product_name = order['Product Name']
    quantity = order['Quantity']
    unit_price = order['Unit Price']
    total_amount = quantity * unit_price

    # Create a PDF invoice
    pdf_file = f"invoice_{order_id}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, f"Invoice Number: {order_id}")
    c.drawString(100, 730, f"Date of Purchase: {datetime.now().strftime('%Y-%m-%d')}")
    c.drawString(100, 710, f"Customer Name: {customer_name}")
    c.drawString(100, 690, f"Product Name: {product_name}")
    c.drawString(100, 670, f"Quantity: {quantity}")
    c.drawString(100, 650, f"Unit Price: ${unit_price:.2f}")
    c.drawString(100, 630, f"Total Amount: ${total_amount:.2f}")
    c.save()

    return pdf_file

def merge_pdfs(pdf_files, output_file):
    """Merge multiple PDF files into a single PDF file."""
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

def main():
    # Step 1: Load order data
    orders = load_orders('orders.csv')

    # Step 2: Generate PDF invoices
    pdf_files = []
    for _, order in orders.iterrows():
        pdf_file = generate_invoice(order)
        pdf_files.append(pdf_file)

    # Step 3: Merge PDF invoices into a single file
    merge_pdfs(pdf_files, 'invoices_merged.pdf')

    print("Invoices have been generated and merged into 'invoices_merged.pdf'.")

if __name__ == "__main__":
    main()