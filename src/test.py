#!/usr/bin/env python3
# This is a test program for the PDF library.
# It will open a PDF file and save copy as a new PDF file.
from pikepdf._qpdf import Pdf as PDF


def main():
  src = input("Enter the target: ")

  with PDF.open(src) as pdf:
    pdf.save("out.pdf")


if __name__ == '__main__':
  main()
