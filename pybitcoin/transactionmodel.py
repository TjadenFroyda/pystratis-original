from typing import Optional, List
from pydantic import BaseModel, conint
from .vin import VIn
from .vout import VOut
from pybitcoin.types import uint256, hexstr


class TransactionModel(BaseModel):
    """A TransactionModel."""
    hex: Optional[hexstr]
    txid: uint256
    hash: uint256
    version: conint(ge=0)
    size: conint(ge=0)
    vsize: conint(ge=0)
    weight: Optional[conint(ge=0)]
    locktime: conint(ge=0)
    vin: Optional[List[VIn]]
    vout: Optional[List[VOut]]
    blockhash: Optional[uint256]
    confirmations: Optional[int]
    time: Optional[conint(ge=0)]
    blocktime: Optional[conint(ge=0)]

    class Config:
        allow_population_by_field_name = True

    def json(self, *args, **kwargs) -> str:
        return super(TransactionModel, self).json(exclude_none=True, by_alias=True)
