import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")  # Return a list of paths matching in the directory

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")  # Reads Excel file
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename= Path(filepath).stem  #removes extension of the file and gives only the file name
    invoice_no, date = filename.split("-")     # Split returns a list and [0] gives first element of the list
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, ln=1, txt=f"Invoice no. {invoice_no}")
    
    pdf.cell(w=50, h=8, txt=f"Date: {date}")
    pdf.output(f"PDFs/{filename}.pdf")
    