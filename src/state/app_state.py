from core import PdfDocument


class AppState:
    def __init__(self):
        self.loaded_docs: list[PdfDocument] = []
        self.active_doc: PdfDocument | None = None

    def add_doc(self, doc: PdfDocument | str):
        if isinstance(doc, str):
            doc = PdfDocument(doc)

        if doc not in self.loaded_docs:
            self.loaded_docs.append(doc)
            self.active_doc = doc


    def remove_doc(self, doc: PdfDocument):
        if doc in self.loaded_docs:
            self.loaded_docs.remove(doc)

    def set_active_doc(self, doc: PdfDocument):
        self.active_doc = doc

    def get_active_doc(self) -> PdfDocument | None:
        return self.active_doc