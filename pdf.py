from ptext.pdf.document import Document
from ptext.pdf.page.page import Page
from ptext.pdf.pdf import PDF
from ptext.pdf.canvas.layout.paragraph import Paragraph
from ptext.pdf.canvas.layout.page_layout import SingleColumnLayout
from ptext.io.read.types import Decimal


# Create an empty Document
document = Document()

# Create an empty page
page = Page()

# Add the Page to the Document
document.append_page(page)

# Write the Document to a file
with open("output.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, document)

# Setting a layout manager on the Page
layout = SingleColumnLayout(page)

# Adding a Paragraph to the Page
layout.add(Paragraph("Hello World", font_size=Decimal(20), font="Helvetica"))

document.append_page(page)

with open("output.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, document)