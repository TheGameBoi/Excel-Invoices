import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path



filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    print(df)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()


    filename = Path(filepath).stem
    invoice = filename.split('-')[0]

    filename = Path(filepath).stem
    date = filename.split('-')[1]

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=8, txt=f"Invoice Number: {invoice}", ln=1)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=8, txt=f"Date: {date}")

    pdf.output(f"PDF/{filename}.pdf")
