from pypdf import PdfReader, PdfWriter

def PDFrotate(origFileName, newFileName, rotation):
    reader = PdfReader(origFileName)
    writer = PdfWriter()

    for page in range(len(reader.pages)):
        pageObj = reader.pages[page]
        pageObj.rotate(rotation)
        writer.add_page(pageObj)
    
    with open(newFileName, 'wb') as newFile:
        writer.write(newFile)

def main():
    origFileName = 'example.pdf'
    newFileName = 'rotated_example.pdf'
    rotation = 270
    PDFrotate(origFileName, newFileName, rotation)

if __name__ == "__main__":
    main()