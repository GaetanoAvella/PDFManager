from io import BytesIO
import os
import base64
import pypdf as pp
import pypdfium2 as pdfium


class PdfDocument():
    def __init__(self, pdf_path:str):
        self.pdf_path: str = pdf_path
        self.pdf_name: str = os.path.basename(pdf_path)
        self.__reader = pp.PdfReader(pdf_path)
        self.pdf_pages: int = self.__reader.get_num_pages()
        self.pages_list: list[PdfDocument.PdfPage] = []
        self.__setup_pages_list()

    class PdfPage():
        def __init__(self, page_object: pp.PageObject, pdf_source_path: str):
            self.page_content: pp.PageObject = page_object
            self.page_position = self.page_content.page_number
            self.__pdf_source_path = pdf_source_path
            self.__image_cache: str = ""

        def render_page_as_image_base64(self, scale: float) -> str:
            if not self.__image_cache == "":
                return self.__image_cache

            pdfium_doc = pdfium.PdfDocument(self.__pdf_source_path)
            try:
                pdfium_page = pdfium_doc.get_page(self.page_position)
                bitmap = pdfium_page.render(scale=scale)
                pil_image = bitmap.to_pil()

                buffer = BytesIO()
                pil_image.save(buffer, format="PNG")
                self.__image_cache = base64.b64encode(buffer.getvalue()).decode("ascii")

                pdfium_page.close()
            finally:
                pdfium_doc.close()

            return self.__image_cache


    def __setup_pages_list(self):
        for page in self.__reader.pages:
            self.pages_list.append(PdfDocument.PdfPage(page, self.pdf_path))

    def get_page(self, page_number: int) -> PdfPage:
        return self.pages_list[page_number]

    def remove_page(self, page_index: int) -> PdfPage:
        return self.pages_list.pop(page_index)

    def insert_page(self, insert_index: int, page: PdfPage):
        self.pages_list.insert(insert_index, page)

    def get_pages(self) -> list[PdfPage]:
        return self.pages_list

    def get_total_pages(self) -> int:
        return self.pdf_pages

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, PdfDocument):
            return self.pdf_path == value.pdf_path
        return False

    def __str__(self) -> str:
        return f"[{self.pdf_path}, {self.pdf_name}, {self.pdf_pages}]"