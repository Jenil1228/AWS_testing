from fpdf import FPDF
''' 
pdf = FPDF(orientation='P', unit='mm', format='A4')
#pdf = FPDF(orientation='P', unit='mm', format='A5')
pdf.add_page()
pdf.set_font("Arial", size=20)
pdf.cell(200, 10, txt="Welcome to PythonGuides", ln=1, align="L")
pdf.output("E:\\OneKnotOne\\whatsapp\\test.pdf") 
''' 
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# open the text file in read mode
f = open("/home/ubuntu/AWS_testing/myfile.txt", "r")
 
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
  
# save the pdf with name .pdf
pdf.output("/home/ubuntu/AWS_testing/txtpy.pdf") 


''' 
# create a cell
pdf.cell(200, 10, txt = "PDF python",
         ln = 1, align = 'C')
 
# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')
 
# save the pdf with name .pdf
pdf.output("E:\\OneKnotOne\\whatsapp\\PDFPY.pdf")
'''
