from shared.contracts import Document
from shared.local import KeywordRetriever, EchoModel

docs=[Document("Password reset requires identity verification.","support.md"),Document("MFA is mandatory for administrators.","security.md")]
retriever=KeywordRetriever(docs); model=EchoModel()
q="How do I reset password?"
hits=retriever.search(q,2)
context="\n".join(f"[{d.source}] {d.content}" for d in hits)
print(model.generate("Answer only from context",context+"\nQuestion: "+q))
