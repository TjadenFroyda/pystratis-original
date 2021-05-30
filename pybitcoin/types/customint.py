from __future__ import annotations
from functools import total_ordering
from typing import Callable, Union


# noinspection PyPep8Naming
@total_ordering
class customint:
    """Represents a custom int."""
    _num_bits: int = None
    _minvalue: int = None
    _maxvalue: int = None

    def __init__(self, value, num_bits=None, minvalue=None, maxvalue=None):
        self.update(num_bits=num_bits, minvalue=minvalue, maxvalue=maxvalue)
        self.value = value

    @classmethod
    def update(cls, num_bits, minvalue, maxvalue):
        cls._num_bits = num_bits
        cls._minvalue = minvalue
        cls._maxvalue = maxvalue

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = self.validate_value(value)

    @classmethod
    def __get_validators__(cls) -> Callable:
        yield cls.validate_class

    # noinspection PyTypeChecker
    def __hex__(self) -> str:
        conversion = self.value & (2 ** self._num_bits - 1)
        fixed_width = self._num_bits // 4
        padchar = '0' if self.value > 0 else 'f'
        format_spec = f'{padchar}>{fixed_width}x'
        return format(conversion, format_spec)

    def to_hex(self) -> str:
        return self.__hex__()

    @classmethod
    def hex_to_int(cls, v: str) -> int:
        sign_mask = 1 << (len(v.replace('0x', '')) * 4 - 1)
        value_mask = sign_mask - 1
        value_int = int(v, 16)
        new_value = -(value_int & sign_mask) | (value_int & value_mask)
        return new_value

    @classmethod
    def validate_class(cls, value) -> customint:
        value = cls._check_hex_string_and_convert(value=value, num_bits=cls._num_bits)
        _check_value_out_of_range(value=value, minvalue=cls._minvalue, maxvalue=cls._maxvalue)
        return cls(value)

    def validate_value(self, value) -> int:
        value = self._check_hex_string_and_convert(value=value, num_bits=self._num_bits)
        _check_value_out_of_range(value=value, minvalue=self._minvalue, maxvalue=self._maxvalue)
        return value

    @classmethod
    def _check_hex_string_and_convert(cls, value: Union[str, int], num_bits: int) -> int:
        if isinstance(value, str):
            if len(value) != num_bits // 4:
                raise ValueError(f'Invalid hex string length. Should be {num_bits // 4}')
            value = cls.hex_to_int(value)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f'Invalid input. Accepts int or {num_bits // 4} length hex str.')
        return value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):
        return self.to_hex()

    def __eq__(self, other):
        if isinstance(other, customint):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return False

    def __lt__(self, other):
        if isinstance(other, customint):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return False

    def __gt__(self, other):
        if isinstance(other, customint):
            return self.value > other.value
        if isinstance(other, int):
            return self.value > other
        return False

    # noinspection PyTypeChecker
    def __len__(self) -> int:
        return len(self.value)


def _is_lt_minvalue(minvalue: int, value: int) -> bool:
    return value < minvalue


def _is_gt_maxvalue(maxvalue: int, value: int) -> bool:
    return value > maxvalue


def _check_value_out_of_range(value: int, minvalue: int, maxvalue: int) -> None:
    if _is_lt_minvalue(minvalue=minvalue, value=value):
        raise ValueError(f'Underflow error: value less than {minvalue}.')
    if _is_gt_maxvalue(maxvalue=maxvalue, value=value):
        raise ValueError(f'Overflow error: value greater than {maxvalue}.')
