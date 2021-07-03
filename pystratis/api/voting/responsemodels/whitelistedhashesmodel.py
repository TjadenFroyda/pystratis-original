from typing import Optional
from pystratis.api import Model
from pystratis.core.types import uint256


class WhitelistedHashesModel(Model):
    """A WhitelistedHashesModel."""
    hash: Optional[uint256]
