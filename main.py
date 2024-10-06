from pdf2text import pdf2text
from structure_text import structure_text
from text2speech import text2speech
path = 'sample.pdf'
text = pdf2text(path)

lecture = structure_text(text)
CHUNK_SIZE = 1024
response = text2speech(lecture)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
