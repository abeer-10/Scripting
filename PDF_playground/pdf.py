import PyPDF2 as pdf
import sys

# with open('dummy.pdf', 'rb') as file:
#     reader = pdf.PdfFileReader(file)
#     print(reader.numPages)

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    # merger = pdf.PdfFileMerger()
    for pdfs in pdf_list:
        print(pdfs)
    #     merger.append(pdfs)
    # merger.write('Super.pdf')

pdf_combiner(inputs)