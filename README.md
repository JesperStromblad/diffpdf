# diffpdf

A basic pdf compare program.

## Steps for running the program

### Requirements

- Python3.7.x

### Install dependencies

`pip3 install -r requirements.txt`

### Running the program

`python3 diff.py <file1>.pdf <file2>.pdf`

### Test with the following command

`python3 diff.py d1.pdf d2.pdf`

### Output

Changes are indicated with a + sign.

```
--- file1.txt
+++ file2.txt
@@ -1,15 +1,15 @@
-pdfcompare

+Pdf2compare

 ==========



 Compare text of two PDF files, write a resulting PDF with highlighted changes.

 Potential text portions that were moved around are recognized and analyzed

-for similarity with a second level diff.

+for s2imilarity with a second level diff.



 Dependencies:



 * pyPdf

 * reportlab.pdfgen

-* reportlab.lib.colors

+* reportla 2b.lib.colors

 * pygame.font

 * poppler -utils for pdftohtml
```
