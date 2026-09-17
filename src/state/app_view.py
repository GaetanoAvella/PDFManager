from enum import Enum


class AppView(str, Enum):
    START = "START"
    READ = "READ"
    EDIT = "EDIT"
    MERGE = "MERGE"