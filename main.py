import PyPDF2 as p2

pdfFileName = "translation.pdf"
pdfFile = open(pdfFileName, 'rb')
pdfread = p2.PdfFileReader(pdfFile)
number_of_pages = pdfread.getNumPages()

with open('covid.txt', 'w', encoding="utf-8") as f:
	for page_number in range(number_of_pages):
		print(f'Sheet{page_number}')
		pageinfo = pdfread.getPage(page_number)
		lines = pageinfo.extractText().split('\n')
		
		for line in lines:
			f.write(line)
			f.write('\n')