from pystratis.core.types import Address
from pystratis.api import Model


class GetLastBalanceUpdateTransactionRequest(Model):
    """A request model for the blockstore/getlastbalanceupdatetransaction endpoint.

    Args:
        address (Address): An address to query.
    """
    address: Address

