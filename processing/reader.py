import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    function takes a pdf file and extracts the text from the pdf
    :param pdf_file: pdf file input
    :return: text from pdf
    """
    with open(pdf_file, "rb") as f:
        doc = fitz.open(stream=f.read(), filetype=".pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text