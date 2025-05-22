
from fpdf import FPDF

def generate_board_packet(data, filename='board_packet.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Board Packet Summary", ln=True)
    for section in data:
        pdf.cell(0, 10, section, ln=True)
    pdf.output(filename)
    return filename
