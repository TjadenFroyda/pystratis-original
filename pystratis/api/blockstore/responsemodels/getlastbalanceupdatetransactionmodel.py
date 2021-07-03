from typing import Optional
from pydantic import Field, conint
from pystratis.api import Model
from pystratis.api.global_responsemodels import TransactionModel


class GetLastBalanceUpdateTransactionModel(Model):
    """A GetLastBalanceUpdateTransactionModel."""
    transaction: Optional[TransactionModel]
    block_height: Optional[conint(ge=0)] = Field(alias='blockHeight')
