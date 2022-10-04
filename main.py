import PyPDF2, csv

if __name__ == '__main__':
   pdfFile = open('practical_work_companies_list_black.pdf', 'rb')
   pdfReader = PyPDF2.PdfFileReader(pdfFile)
   output = ''
   for pages in range(pdfReader.numPages):
      page = pdfReader.getPage(pages)
      output += page.extractText()
   sorted = output.split("\n")
   sorted = sorted[1:-1]
   fields = ["Company Name", "Website", "Address", "City", "Country", "Type of Work", "Specialization"]
   rows = []
   data = []
   for i in range(len(sorted)):
      data.append(sorted[i])
      if (i + 1) % 7 == 0:
         print(data)
         rows.append(data)
         data = []

   print(rows[0])
   print(rows[-1])
