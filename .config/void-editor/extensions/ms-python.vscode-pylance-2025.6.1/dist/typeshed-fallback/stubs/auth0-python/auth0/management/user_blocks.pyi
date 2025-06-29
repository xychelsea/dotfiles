from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class UserBlocks:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def get_by_identifier(self, identifier: str) -> dict[str, Incomplete]: ...
    async def get_by_identifier_async(self, identifier: str) -> dict[str, Incomplete]: ...
    def unblock_by_identifier(self, identifier: dict[str, Incomplete]): ...
    async def unblock_by_identifier_async(self, identifier: dict[str, Incomplete]): ...
    def get(self, id: str) -> dict[str, Incomplete]: ...
    async def get_async(self, id: str) -> dict[str, Incomplete]: ...
    def unblock(self, id: str): ...
    async def unblock_async(self, id: str): ...
