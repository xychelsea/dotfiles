from typing import Any, ClassVar

import passlib.utils.handlers as uh

class HexDigestHash(uh.StaticHandler):
    checksum_chars: ClassVar[str]
    supported: ClassVar[bool]

def create_hex_hash(digest, module="passlib.handlers.digests", django_name=None, required: bool = True): ...

hex_md4: Any
hex_md5: Any
hex_sha1: Any
hex_sha256: Any
hex_sha512: Any

class htdigest(uh.MinimalHandler):
    name: ClassVar[str]
    default_encoding: ClassVar[str]
    setting_kwds: ClassVar[tuple[str, ...]]
    context_kwds: ClassVar[tuple[str, ...]]
    @classmethod
    def hash(cls, secret, user, realm, encoding=None): ...  # type: ignore[override]
    @classmethod
    def verify(cls, secret, hash, user, realm, encoding: str = "utf-8"): ...  # type: ignore[override]
    @classmethod
    def identify(cls, hash): ...
    @classmethod
    def genconfig(cls): ...
    @classmethod
    def genhash(cls, secret, config, user, realm, encoding=None): ...  # type: ignore[override]

__all__ = ["create_hex_hash", "hex_md4", "hex_md5", "hex_sha1", "hex_sha256", "hex_sha512"]
