from enum import Enum


class AppView(str, Enum):
    START = "START"
    OPEN = "OPEN"
    EDIT = "EDIT"
    MERGE = "MERGE"