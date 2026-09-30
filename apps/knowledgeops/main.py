from shared.contracts import Document
from shared.local import KeywordRetriever

class KnowledgeOps:
    def __init__(self,docs): self.retriever=KeywordRetriever(docs)
    def query(self,q):
        hits=self.retriever.search(q,3)
        return {"question":q,"evidence":[{"source":d.source,"content":d.content} for d in hits]}

if __name__=="__main__":
    app=KnowledgeOps([Document("Contracts expire on the date defined in each agreement.","contract-demo.md")])
    print(app.query("When does the contract expire?"))
