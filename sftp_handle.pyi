# Stubs for ssh2.sftp_handle (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from typing import overload

class SFTPAttributes:
    atime: Any = ...
    filesize: Any = ...
    flags: Any = ...
    gid: Any = ...
    mtime: Any = ...
    permissions: Any = ...
    uid: Any = ...
    @classmethod
    def __init__(*args, **kwargs) -> None: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...

class SFTPHandle:
    @classmethod
    def __init__(*args, **kwargs) -> None: ...
    def _readdir(self, size_tbuffer_maxlen) -> Any: ...
    def _readdir_ex(self, size_tlongentry_maxlen, size_tbuffer_maxlen) -> Any: ...
    def close(self) -> Any: ...
    def fsetstat(self, SFTPAttributesattrs) -> Any: ...
    def fstat(self) -> Any: ...
    def fstat_ex(self, SFTPAttributesattrs, intsetstat) -> Any: ...
    def fstatvfs(self) -> Any: ...
    def fsync(self) -> Any: ...
    def read(self, size_tbuffer_maxlen) -> Any: ...
    @overload
    def readdir(self, size_tbuffer_maxlen) -> Any: ...
    @overload
    def readdir() -> Any: ...
    def readdir_ex(self, size_tlongentry_maxlen, size_tbuffer_maxlen) -> Any: ...
    def rewind(self) -> Any: ...
    def seek(self, size_toffset) -> Any: ...
    def seek64(self, libssh2_uint64_toffset) -> Any: ...
    def tell(self) -> Any: ...
    def tell64(self) -> Any: ...
    def write(self, bytesbuf) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, *args) -> Any: ...
    def __iter__() -> Any: ...
    def __next__() -> Any: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...

class SFTPStatVFS:
    f_bavail: Any = ...
    f_bfree: Any = ...
    f_blocks: Any = ...
    f_bsize: Any = ...
    f_favail: Any = ...
    f_ffree: Any = ...
    f_files: Any = ...
    f_flag: Any = ...
    f_frsize: Any = ...
    f_fsid: Any = ...
    f_namemax: Any = ...
    @classmethod
    def __init__(*args, **kwargs) -> None: ...
    def __reduce__() -> Any: ...
    def __setstate__(state) -> Any: ...
