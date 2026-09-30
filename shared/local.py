from shared.contracts import Document

class EchoModel:
    def generate(self, instruction: str, content: str) -> str:
        return f"[demo] {instruction}: {content[:300]}"

class KeywordRetriever:
    def __init__(self, documents: list[Document]): self.documents=documents
    def search(self, query: str, limit: int=4):
        terms=set(query.lower().split())
        ranked=sorted(self.documents,key=lambda d: len(terms & set(d.content.lower().split())),reverse=True)
        return ranked[:limit]
