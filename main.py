import PyPDF2

if __name__ == '__main__':
   pdfFile = open('practical_work_companies_list.pdf', 'rb')
   pdfReader = PyPDF2.PdfFileReader(pdfFile)
   output = ''
   for pages in range(pdfReader.numPages):
      page = pdfReader.getPage(pages)
      output += page.extractText()
   print(output.split("\n"))
