from PyPDF2 import PdfFileMerger
import os
from msvcrt import getch
import datetime

# references
# https://stackoverflow.com/questions/3444645/merge-pdf-files

currDir = ".\\" # Get the current directory
pdfCou = 0
merger = PdfFileMerger()
for i, item in enumerate(os.listdir(currDir)):
    if str(item).lower().endswith(".pdf"):
        print(f"PDF found:{item}")
        pdfCou += 1
        merger.append(item)
if pdfCou:
    customDT = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
    merger.write(f"Merged__{customDT}.pdf")
    merger.close()
    print("Merging completed. Press any key to exit.")
else:
    print(print("There is no PDF file. Press any key to exit."))
getch()