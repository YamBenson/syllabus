# importing required modules 
import PyPDF2
import sys
    
# creating a pdf file object 
pdfFileObj = open('PH141Syllabus_Fall2022.pdf', 'rb')

if len(sys.argv) == 2:
    pdfFileObj = open(sys.argv[1], 'rb')
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
# print(pdfReader.numPages) 
if len(sys.argv) == 2:
    file1=open(sys.argv[1][0:len(sys.argv[1])-3] + "txt","a")
else:
    file1=open(r"PH141Syllabus_Fall2022.txt","a")
    
for i in range(pdfReader.numPages):
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
        
    # extracting text from page 
    print(pageObj.extractText()) 
    file1.writelines(pageObj.extractText())
    
# closing the pdf file object 
pdfFileObj.close() 