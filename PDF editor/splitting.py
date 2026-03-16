# importing the required modules
from pypdf import PdfReader, PdfWriter

def PDFsplit(pdf, splits):
    # creating pdf reader object
    reader = PdfReader(pdf)

    # starting index of first slice
    start = 0

    # starting index of last slice
    end = splits[0]


    for i in range(len(splits)+1):
        # creating pdf writer object for (i+1)th split
        writer = PdfWriter()

        # output pdf file name
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'

        # adding pages to pdf writer object
        for page in range(start,end):
            writer.add_page(reader.pages[page])

            # writing split pdf pages to pdf file
            with open(outputpdf, "wb") as f:
                writer.write(f)

            # interchanging page split start position for next split
            start = end
            try:
                # setting split end position for next split
                end = splits[i+1]
            except IndexError:
                # setting split end position for last split
                end = len(reader.pages)


def main():
    # pdf file to split
    pdf = 'example.pdf'

    # split page positions
    splits = [2,4]

    # calling PDFsplit function to split pdf
    PDFsplit(pdf, splits)

if __name__ == "__main__":
    # calling the main function
    main()