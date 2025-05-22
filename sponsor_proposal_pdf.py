
from fpdf import FPDF

def create_sponsor_proposal(sponsor_name, roi, benefits, filename='proposal.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Proposal for {sponsor_name}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Estimated ROI: {roi}", ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, "Key Benefits:", ln=True)
    for b in benefits:
        pdf.cell(0, 10, f"- {b}", ln=True)
    pdf.output(filename)
    return filename
