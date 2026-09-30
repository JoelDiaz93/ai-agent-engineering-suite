from dataclasses import dataclass, field
from typing import Protocol

class TextModel(Protocol):
    def generate(self, instruction: str, content: str) -> str: ...

@dataclass
class Document:
    content: str
    source: str
    metadata: dict = field(default_factory=dict)

class Retriever(Protocol):
    def search(self, query: str, limit: int = 4) -> list[Document]: ...
