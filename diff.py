from timeit import main
import PyPDF2
import difflib
import sys


def pdfToText(pdf, txt):
    pdffileobj = open(pdf, "rb")

    # create reader variable that will read the pdffileobj
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)

    # This will store the number of pages of this pdf file
    x = pdfreader.numPages

    # create a variable that will select the selected number of pages
    pageobj = pdfreader.getPage(0)

    # (x+1) because python indentation starts with 0.
    # create text variable which will store all text datafrom pdf file
    text = pageobj.extractText()

    file = open(txt, "w+")
    file.write(text)


def compare_txt(_text_A, _text_B):
    with open(_text_A) as file_1:
        file_1_text = file_1.readlines()

    with open(_text_B) as file_2:
        file_2_text = file_2.readlines()

    # Find and print the diff:
    for line in difflib.unified_diff(file_1_text, file_2_text, fromfile="file1.txt", tofile="file2.txt", lineterm=""):
        print(line)


if __name__ == "__main__":
    # List of pdfs
    pdf = []
    # total arguments
    n = len(sys.argv)
    for i in range(1, n):
        pdf_file = sys.argv[i]
        pdf.append(pdf_file)

    # List of text file names. Just some dummy files GOOD FOR NOTHING
    txt = ["txt1.txt", "txt2.txt"]

    for i in range(2):
        pdfToText(pdf[i], txt[i])

    compare_txt(txt[0], txt[1])
