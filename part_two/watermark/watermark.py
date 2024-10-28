import PyPDF2
import sys

argv = sys.argv

watermark = PyPDF2.PdfFileReader(open(argv[1], "rb"))
template = PyPDF2.PdfFileReader(open(argv[2], "rb"))
output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)


with open("watermarked_output.pdf", "wb") as op:
    output.write(op)