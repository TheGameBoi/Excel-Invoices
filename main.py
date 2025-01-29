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
    filename = Path(filepath).stem + '.pdf'
    invoice = filename.split('-')[0]
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=8, txt=f"Invoice Number {invoice}")
    pdf.output(f"PDF/{filename}")
