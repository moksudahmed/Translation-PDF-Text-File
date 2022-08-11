# importing required modules
import PyPDF2
  
# creating a pdf file object
pdfFileObj = open('d:\\Development\\Python\\download.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# printing number of pages in pdf file
print(pdfReader.numPages)
  
# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())
  
#opt=open(r"d:\Development\Python\data.txt","a")
#opt.writelines(pageObj.extractText())

lines = ['Readme', 'How to write text files in Python']
with open('d:\Development\Python\data.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# closing the pdf file object
pdfFileObj.close()
