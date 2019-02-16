# Stubs for ssh2.knownhost (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

import ssh2.exceptions
LIBSSH2_KNOWNHOST_KEYENC_BASE64: int
LIBSSH2_KNOWNHOST_KEYENC_MASK: int
LIBSSH2_KNOWNHOST_KEYENC_RAW: int
LIBSSH2_KNOWNHOST_KEY_MASK: int
LIBSSH2_KNOWNHOST_KEY_RSA1: int
LIBSSH2_KNOWNHOST_KEY_SHIFT: int
LIBSSH2_KNOWNHOST_KEY_SSHDSS: int
LIBSSH2_KNOWNHOST_KEY_SSHRSA: int
LIBSSH2_KNOWNHOST_KEY_UNKNOWN: int
LIBSSH2_KNOWNHOST_TYPE_CUSTOM: int
LIBSSH2_KNOWNHOST_TYPE_MASK: int
LIBSSH2_KNOWNHOST_TYPE_PLAIN: int
LIBSSH2_KNOWNHOST_TYPE_SHA1: int
b64decode: Any

class KnownHost:
    @classmethod
    def __init__(*args, **kwargs) -> None: ...
    def add(self, byteshost, bytessalt, byteskey, inttypemask) -> Any: ...
    def addc(self, byteshost, byteskey, inttypemask, bytessalt, bytescomment) -> Any: ...
    def check(self, byteshost, byteskey, inttypemask) -> Any: ...
    def checkp(self, byteshost, intport, byteskey, inttypemask) -> Any: ...
    def delete(self, KnownHostEntryentry) -> Any: ...
    def get(self, KnownHostEntryprev) -> Any: ...
    def readfile(self, filename, intf_type) -> Any: ...
    def readline(self, bytesline, intf_type) -> Any: ...
    def writefile(self, filename, intf_type) -> Any: ...
    def writeline(self, KnownHostEntryentry, intf_type, size_tbuf_len) -> Any: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...

class KnownHostAddError(ssh2.exceptions.KnownHostError): ...

class KnownHostCheckError(ssh2.exceptions.KnownHostError): ...

class KnownHostCheckFailure(ssh2.exceptions.KnownHostCheckError): ...

class KnownHostCheckMisMatchError(ssh2.exceptions.KnownHostCheckError): ...

class KnownHostCheckNotFoundError(ssh2.exceptions.KnownHostCheckError): ...

class KnownHostDeleteError(ssh2.exceptions.KnownHostError): ...

class KnownHostEntry:
    key: Any = ...
    magic: Any = ...
    name: Any = ...
    typemask: Any = ...
    @classmethod
    def __init__(*args, **kwargs) -> None: ...
    def _dealloc__(self) -> Any: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...

class KnownHostError(ssh2.exceptions.SSH2Error): ...

class KnownHostGetError(ssh2.exceptions.KnownHostError): ...

class KnownHostReadFileError(ssh2.exceptions.KnownHostError): ...

class KnownHostReadLineError(ssh2.exceptions.KnownHostError): ...

class KnownHostWriteFileError(ssh2.exceptions.KnownHostError): ...

class KnownHostWriteLineError(ssh2.exceptions.KnownHostError): ...
