from fpdf import FPDF
pdf = FPDF('p', 'cm', (10, 15))
pdf.add_page()
pdf.set_font('Arial', size=16)
pdf.cell(w=10, h=5, txt='HEllo, bich', align='C', border=1)



pdf.output('test.pdf')