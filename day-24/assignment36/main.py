#pdf generation
from fpdf import FPDF

pdf = FPDF(orientation="P",unit="mm", format='A4')

pdf.add_page();

pdf.set_font(family="Times",style="B", size=12)
pdf.cell(w=8,h=12,txt="Test", align="L")

pdf.output("generated_pdf.pdf")