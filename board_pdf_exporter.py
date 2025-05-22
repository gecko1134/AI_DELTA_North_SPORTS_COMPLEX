
from fpdf import FPDF

def export_board_pdf(content, filename='board_summary.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Board Summary Export", ln=True)
    for line in content:
        pdf.cell(0, 10, line, ln=True)
    pdf.output(filename)
    return filename
