import unittest

from app.utils.FileReader import base_reader


class TestDocumentParsing(unittest.TestCase):
    """ Tests for parsed PDF files """
    def setUp(self) -> None:
        with open("/Users/prateek/Downloads/papers/BNN.pdf", "rb") as pdf_file:
            self.pdf_bytes = pdf_file.read()

    def test_sections(self):
        document = base_reader(self.pdf_bytes)
        document = list(document)
        self.assertEqual(len(document), 16)

if __name__ == "__main__":
    unittest.main()
