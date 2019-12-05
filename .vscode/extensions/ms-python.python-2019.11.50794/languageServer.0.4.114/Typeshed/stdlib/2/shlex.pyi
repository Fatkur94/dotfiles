from typing import Optional, List, Any, IO

def split(s: Optional[str], comments: bool = ..., posix: bool = ...) -> List[str]: ...

class shlex:
    def __init__(self, instream: IO[Any] = ..., infile: IO[Any] = ..., posix: bool = ...) -> None: ...
    def get_token(self) -> Optional[str]: ...
    def push_token(self, _str: str) -> None: ...
    def read_token(self) -> str: ...
    def sourcehook(self, filename: str) -> None: ...
    def push_source(self, stream: IO[Any], filename: str = ...) -> None: ...
    def pop_source(self) -> IO[Any]: ...
    def error_leader(self, file: str = ..., line: int = ...) -> str: ...

    commenters = ...  # type: str
    wordchars = ...  # type: str
    whitespace = ...  # type: str
    escape = ...  # type: str
    quotes = ...  # type: str
    escapedquotes = ...  # type: str
    whitespace_split = ...  # type: bool
    infile = ...  # type: IO[Any]
    source = ...  # type: Optional[str]
    debug = ...  # type: int
    lineno = ...  # type: int
    token = ...  # type: Any
    eof = ...  # type: Optional[str]
