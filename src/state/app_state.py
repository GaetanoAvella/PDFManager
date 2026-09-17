from core import PdfDocument
from .app_view import AppView


class AppState:
    def __init__(self):
        self.__loaded_docs: list[PdfDocument] = []
        self.__active_doc: PdfDocument | None = None
        self.__active_doc_zoom: float = 1.5
        self.__active_view: AppView = AppView.START

    def add_doc(self, doc: PdfDocument | str):
        if isinstance(doc, str):
            doc = PdfDocument(doc)

        if doc not in self.__loaded_docs:
            self.__loaded_docs.append(doc)
            self.set_active_doc(doc)


    def remove_doc(self, doc: PdfDocument):
        if doc in self.__loaded_docs:
            self.__loaded_docs.remove(doc)

    def set_active_doc(self, doc: PdfDocument):
        if doc not in self.__loaded_docs:
            self.add_doc(doc)
        self.__active_doc = doc

    def get_active_doc(self) -> PdfDocument | None:
        return self.__active_doc

    def get_active_doc_zoom(self) -> float:
        return self.__active_doc_zoom

    def set_active_doc_zoom(self, zoom_level: float):
        self.__active_doc_zoom = zoom_level

    def get_active_view(self) -> AppView:
        return self.__active_view

    def set_active_view(self, view: AppView):
        self.__active_view = view
