import PyPDF2

if __name__ == '__main__':
   pdfFile = open('practical_work_companies_list.pdf', 'rb')
   pdfReader = PyPDF2.PdfFileReader(pdfFile)
   print(pdfReader.numPages)
   page = pdfReader.getPage(0)
   print(page.extractText())
