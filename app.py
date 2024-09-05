from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas

def create_multiline_pdf(file_name, lines, x, font_name="Helvetica", font_size=12):
    # Set up the canvas with landscape orientation
    c = canvas.Canvas(file_name, pagesize=landscape(letter))
    width, height = landscape(letter)
    
    # Set the font name and size
    c.setFont(font_name, font_size)
    
    # Apply rotation
    c.translate(height,0)  # Move the origin to the center of the page
    c.rotate(90)  # Rotate the canvas by 90 degrees clockwise
    #c.translate(-height / 2, -width / 2)  # Move the origin back to the top-left corner of the rotated page
    
     # Set the starting position for the text
    x_offset = width*x # Offset to the left
    y_position = height-height*.09  # Starting position from the top of the page

    # Set the space between lines and blocks
    line_spacing = font_size + 2  # Space between lines within the same block
    block_spacing = font_size + 105 # Space between different blocks (name/address pairs)
    # Draw each block of lines
    for i in range(0, len(lines), 4):
        if i < len(lines):
            c.drawString(x_offset, y_position, lines[i])
        if i+1 < len(lines):
            y_position -= line_spacing
            c.drawString(x_offset, y_position, lines[i+1])
        if i+2 < len(lines):
            y_position -= line_spacing
            c.drawString(x_offset, y_position, lines[i+2])  
        if i+3 < len(lines):
            y_position -= line_spacing
            c.drawString(x_offset, y_position, lines[i+3])
        
        # Move down to the next block
        y_position -= block_spacing
    c.showPage()
    c.save()

# Define the lines with names, addresses, and city/state/zip
lines = [
"John Doe", "1234 Elm Street", "Springfield, IL 62704","",
"Jane Smith", "5678 Oak Avenue", "Metropolis, IL 62960","",
    "Alice Johnson", "9101 Maple Lane", "Gotham, NY 10001",""
]

# Create the content PDF with rotated text
create_multiline_pdf("content_pdf.pdf", lines,.035, font_size=9)



import PyPDF2

def merge_pdfs(background_pdf, content_pdf, output_pdf):
    # Read the background PDF
    background = PyPDF2.PdfReader(background_pdf)
    background_page = background.pages[0]

    # Read the content PDF
    content = PyPDF2.PdfReader(content_pdf)
    content_page = content.pages[0].rotate(90)

    # Rotate the content page by 90 degrees clockwise
    #content_page.rotate(90)

    # Merge the rotated content on top of the background
    background_page.merge_page(content_page)

    # Write the output
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(background_page)
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Merge the PDFs with rotation
merge_pdfs("Card_Scan.pdf", "content_pdf.pdf", "merged_pdf.pdf")

lines = [
    "","", "", "Springfield, IL 62704",
    "","", "", "Metropolis, IL 62960",
    "","", "", "Gotham, NY 10001"
]

create_multiline_pdf("content_pdf.pdf", lines,.50, font_size=9)

merge_pdfs("merged_pdf.pdf", "content_pdf.pdf", "merged_pdf.pdf")

