#-------------------------------------------------------------------------------
# Name:        Principal
# Purpose:     Leer un archivo pdf y guiardarlo en formato csv.
#
# Author:      caarlos
#
# Created:     22-01-2022
# Copyright:   (c) caarlos 2022
# Licence:     <Mozilla Public License 2.0>
#-------------------------------------------------------------------------------
import pdfplumber



i = 0
archivo=open("path_to_file.txt","w")

while(i <= 6):
    with pdfplumber.open("path_toFile.pdf") as pdf_file:
        pdf_page = pdf_file.pages[i]
        archivo.write(pdf_page.extract_text())
        archivo.write("\n")
    i+=1
archivo.close()
print("Terminado")

