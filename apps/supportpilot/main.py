from dataclasses import dataclass
from shared.contracts import Document
from shared.local import KeywordRetriever

@dataclass
class Ticket:
    id:str; question:str; category:str="general"; confidence:float=0; status:str="new"; answer:str|None=None

class SupportPilot:
    def __init__(self,docs): self.r=KeywordRetriever(docs)
    def handle(self,t:Ticket):
        hits=self.r.search(t.question,3); t.confidence=min(1.0,len(hits)*0.25) if hits else 0
        if t.confidence < .6: t.status="human_review"; return t
        t.answer=hits[0].content; t.status="resolved_by_knowledge"; return t

if __name__=="__main__":
    s=SupportPilot([Document("Reset password from Settings > Security.","faq.md") for _ in range(3)])
    print(s.handle(Ticket("TK-DEMO","reset password")))
