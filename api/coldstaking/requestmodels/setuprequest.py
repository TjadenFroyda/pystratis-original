from typing import Optional
from pydantic import Field, SecretStr, conint
from pybitcoin import Address, Model
from pybitcoin.types import Money


class SetupRequest(Model):
    """A SetupRequest."""
    wallet_password: SecretStr = Field(alias='walletPassword')
    cold_wallet_address: Address = Field(alias='coldWalletAddress')
    hot_wallet_address: Address = Field(alias='hotWalletAddress')
    wallet_name: str = Field(alias='walletName')
    wallet_account: str = Field(alias='walletAccount')
    amount: Money
    fees: Money
    subtract_fee_from_amount: Optional[bool] = Field(default=True, alias='subtractFeeFromAmount')
    split_count: Optional[conint(ge=0)] = Field(default=None, alias='splitCount')
    segwit_change_address: Optional[bool] = Field(default=False, alias='segwitChangeAddress')
