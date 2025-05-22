
from fpdf import FPDF

def create_pitchbook(data, filename='sponsor_pitchbook.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for section in data:
        pdf.cell(0, 10, section, ln=True)
    pdf.output(filename)
    return filename
