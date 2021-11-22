from enum import Enum
from typing import List

from errors import ErrorUnknownVariant


def string_to_enums(input_str: str, enum_type: Enum) -> List[Enum]:
    """
    Parse the comma separated sequence of values in input
    as a list of Enums
    """
    if input_str is not None:
        try:
            enum_list = [
                enum_type(val.strip()) for val in input_str.strip().lower().split(",")
            ]
        except ValueError as err:
            raise ErrorUnknownVariant(str(err))
    else:
        enum_list = []
    return enum_list
