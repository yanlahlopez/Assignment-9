from fileinput import filename
import json
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

with open('resume.json') as resume:
    data = json.load(resume)


pdf.ln(5)
pdf.set_font("times", 'B', 16)
pdf.cell(200, 6, data['Name'], ln=1)
pdf.set_font("times", '', 11)
pdf.cell(0, 5, data['ContactNo'], ln=1)
pdf.cell(0, 5, data['Email'], ln=1)
pdf.cell(0, 5, data['Address'], ln=1)


pdf.set_font("times", 'B', 14)
pdf.cell(100, 15, "Educational Background", ln=1)


pdf.set_font("times", 'B', 12)
pdf.cell(0, 6.5, "Tertiary:", ln=1)
pdf.set_font("times", '', 11)
pdf.cell(0, 6, data['College'], ln=1)
pdf.cell(0, 6, data['Address1'], ln=1)
pdf.cell(0, 6, data['Year1'], ln=1)
pdf.set_font("times", 'B', 12)
pdf.cell(0, 6.5, "Senior High School:", ln=1)
pdf.set_font("times", '', 11)
pdf.cell(0, 6, data['SeniorHigh'], ln=1)
pdf.cell(0, 6, data['Address2'], ln=1)
pdf.cell(0, 6, data['Year2'], ln=1)
pdf.set_font("times", 'B', 12)
pdf.cell(0, 6.5, "Secondary:", ln=1)
pdf.set_font("times", '', 11)
pdf.cell(0, 6, data['Secondary'], ln=1)
pdf.cell(0, 6, data['Address3'], ln=1)
pdf.cell(0, 6, data['Year3'], ln=1)
        

pdf.set_font("times", 'B', 14)
pdf.cell(100, 15, "Skills", ln=1)


pdf.set_font("times", '', 11)
pdf.cell(0, 5, data['Skill1'], ln=1)
pdf.cell(0, 5, data['Skill2'], ln=1)
pdf.cell(0, 5, data['Skill3'], ln=1)
pdf.cell(0, 5, data['Skill4'], ln=1)
pdf.cell(0, 5, data['Skill5'], ln=1)
pdf.cell(0, 5, data['Skill6'], ln=1)


pdf.set_font("times", 'B', 14)
pdf.cell(100, 15, "Character Reference", ln=1)


pdf.set_font("times", '', 11)
pdf.cell(0, 5, data['CharacterReference1'], ln=1)
pdf.cell(0, 5, data['CharacterReference2'], ln=1)
pdf.cell(0, 5, data['CharacterReference3'], ln=1)
pdf.cell(0, 5, data['CharacterReference4'], ln=1)
pdf.cell(0, 5, data['CharacterReference5'], ln=1)


pdf.set_line_width(0.5)
pdf.line(x1=12, y1=39, x2=205, y2=39)
pdf.line(x1=12, y1=127, x2=205, y2=127)
pdf.line(x1=12, y1=173, x2=205, y2=173)

pdf.output("LOPEZ_Y-ANLAHSOPHIAA.pdf")