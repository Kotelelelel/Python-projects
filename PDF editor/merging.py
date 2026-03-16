from pypdf import PdfWriter

def PDFmerge(pdfs, output):
    pdfWriter = PdfWriter()

    for pdf in pdfs:
        pdfWriter.append(pdf)
    
    with open(output, 'wb') as f:
        pdfWriter.write(f)

def main():
    pdfs = ['example.pdf', 'rotated_example.pdf']
    output = 'combined_example.pdf'
    PDFmerge(pdfs=pdfs, output=output)

if __name__ == '__main__':
    main()