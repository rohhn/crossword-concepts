from io import BytesIO
from PyPDF2 import PdfReader
from langchain.docstore.document import Document

def base_reader(pdf_bytes: bytes):
    """ parse byteform pdf data """
    pdf_stream = BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)
    texts = map(lambda page: page.extract_text(), reader.pages)
    texts = filter(bool, texts)
    texts = map(lambda text: Document(page_content=text), texts)
    return texts
