from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO


def get_pdf_dimensions(pdf_path):
    reader = PdfReader(pdf_path)
    
    for i, page in enumerate(reader.pages):
        media_box = page.mediabox
        width = media_box.width
        height = media_box.height
        print(f"Page {i + 1}: Width = {width} pt, Height = {height} pt")




def create_overlay(text, x, y):
    packet = BytesIO()
    # Create a new PDF with ReportLab
    can = canvas.Canvas(packet)
    can.drawString(x, y, text)
    can.save()
    packet.seek(0)
    return packet

def merge_pdfs(original_pdf_path, output_pdf_path, overlay):
    # Read the original PDF
    reader = PdfReader(original_pdf_path)
    writer = PdfWriter()

    # Read the overlay PDF
    overlay_pdf = PdfReader(overlay)

    # Go through all pages and add the overlay
    for i in range(len(reader.pages)):
        original_page = reader.pages[i]
        overlay_page = overlay_pdf.pages[0]

        # Merge the overlay with the original page
        original_page.merge_page(overlay_page)
        writer.add_page(original_page)

    # Write the output PDF
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

# Usage
original_pdf_path = "cards.pdf"
output_pdf_path = "output.pdf"


get_pdf_dimensions(original_pdf_path)

# Coordinates where you want to place the text (in points)
x, y = (612*.12), (792*.12)

# Create overlay PDF
overlay = create_overlay("Hello, World!", x, y)

# Merge overlay with original PDF
merge_pdfs(original_pdf_path, output_pdf_path, overlay)
