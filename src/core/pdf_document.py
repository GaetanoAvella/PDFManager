import os

import pypdf as pp


class PdfDocument():
    def __init__(self, pdf_path:str):
        self.pdf_path: str = pdf_path
        self.pdf_name: str = os.path.basename(pdf_path)
        self.__reader = pp.PdfReader(pdf_path)
        self.pdf_pages: int = self.__reader.get_num_pages()
        self.pages_list: list[PdfDocument.PdfPage] = []
        self.__get_pages_list()

    class PdfPage():
        def __init__(self, page_object: pp.PageObject):
            self.page_content: pp.PageObject = page_object
            self.page_position = self.page_content.page_number

    def __get_pages_list(self):
        for page in self.__reader.pages:
            self.pages_list.append(PdfDocument.PdfPage(page))

    def get_page(self, page_number: int) -> PdfPage:
        return self.pages_list[page_number]

    def remove_page(self, page_index: int) -> PdfPage:
        return self.pages_list.pop(page_index)

    def insert_page(self, insert_index: int, page: PdfPage):
        self.pages_list.insert(insert_index, page)