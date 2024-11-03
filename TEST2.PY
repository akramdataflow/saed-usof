from test import PDFGenerator
import pandas as pd


reviewer_data = pd.read_csv('saved_data.csv')



pdf_generator = PDFGenerator(config_path=r'C:\Users\rf\Desktop\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdf_generator.generate_pdf('reviewer_data.pdf', reviewer_data, open_pdf=True)