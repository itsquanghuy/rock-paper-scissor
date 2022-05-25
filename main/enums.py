from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def get_list(cls):
        return [item for item in cls]
