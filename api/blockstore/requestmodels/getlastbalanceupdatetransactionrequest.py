from pybitcoin import Address
from pybitcoin import Model


class GetLastBalanceUpdateTransactionRequest(Model):
    """A GetLastBalanceUpdateTransactionRequest."""
    address: Address

