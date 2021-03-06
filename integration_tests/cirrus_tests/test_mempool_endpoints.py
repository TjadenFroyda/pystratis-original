import pytest
import time
from pystratis.core.types import Money, uint256
from pystratis.nodes import CirrusMinerNode


@pytest.mark.integration_test
@pytest.mark.cirrus_integration_test
def test_raw_mempool(cirrusminer_node: CirrusMinerNode,
                     cirrusminer_syncing_node: CirrusMinerNode,
                     send_a_transaction,
                     wait_and_clear_mempool,
                     get_node_address_with_balance,
                     get_node_unused_address):
    assert wait_and_clear_mempool()
    mining_address = get_node_address_with_balance(cirrusminer_node)
    receiving_address = get_node_unused_address(cirrusminer_syncing_node)
    assert send_a_transaction(
        node=cirrusminer_node, sending_address=mining_address, min_confirmations=2,
        receiving_address=receiving_address, amount_to_send=Money(1)
    )
    time.sleep(1)
    response = cirrusminer_node.mempool.get_raw_mempool()
    for item in response:
        assert isinstance(item, uint256)
