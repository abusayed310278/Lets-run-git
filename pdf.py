import PyPDF2

f=open("demo.pdf","rb")

pdf_reader=PyPDF2.PdfFileReader(f)

pdf_reader.numPages
