from pystratis.api import Model
from pydantic import Field


class MiningStats(Model):
    """A pydantic model for mining stats."""
    miner_hits: int = Field(alias='minerHits')
    """The number of miner hits in the last round."""
    last_block_produced_height: int = Field(alias='lastBlockProducedHeight')
    """The height where last block was produced by miner."""
