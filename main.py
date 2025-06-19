import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os

def generate_invoices(folder, logo_path, output_folder="PDFs"):
    os.makedirs(output_folder, exist_ok=True)
    filepaths = glob.glob("invoices/*.xlsx")  # Return a list of paths matching in the directory    

    if not filepaths:
        raise FileNotFoundError("No Excel files found in the selected folder.")


    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        filename= Path(filepath).stem  #removes extension of the file and gives only the file name
        invoice_no, date = filename.split("-")     # Split returns a list and [0] gives first element of the list
        
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, ln=1, txt=f"Invoice no. {invoice_no}")
        
        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

        df = pd.read_excel(filepath, sheet_name="Sheet 1")  # Reads Excel file

        # Add Header to the Table
        columns = list(df.columns)
        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(20,10,100)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=60, h=8, txt=columns[1], border=1)
        pdf.cell(w=40, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

        # Add rows to table
        
        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(20,20,200)
            pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
            pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
            pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
            pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
            pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

        total_sum = df["total_price"].sum()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(20,20,200)
        pdf.cell(w=30, h=8, txt="", border=0)
        pdf.cell(w=60, h=8, txt="", border=0)
        pdf.cell(w=40, h=8, txt="", border=0)
        pdf.cell(w=30, h=8, txt="Grand Total", border=1)
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

        # Add total sum sentence
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=30, txt=f"The total price is {total_sum}", ln=1)

        # Add company name and logo
        pdf.set_font(family="Times", size=14, style="BI")
        pdf.cell(w=50, h=8, txt=f"Sunrise International Ins.",ln=1)
        pdf.image("logo.png", w=50)

        pdf.output(f"PDFs/{filename}.pdf")
    
    return len(filepaths)
    