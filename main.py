from pdf2text import pdf2text
from structure_text import structure_text
path = 'sample.pdf'
text = pdf2text(path)

lecture = structure_text(text)


print(lecture)