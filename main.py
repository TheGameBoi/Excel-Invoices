import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path



filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()


    filename = Path(filepath).stem
    invoice = filename.split('-')[0]

    filename = Path(filepath).stem
    date = filename.split('-')[1]

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=8, txt=f"Invoice Number: {invoice}", ln=1)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=0, h=8, txt=f"Date: {date}", ln=1)


    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    columns = df.columns
    columns = [item.replace('_', ' ').title() for item in columns]
    pdf.set_font('Times', 'B', 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


    pdf.output(f"PDF/{filename}.pdf")
