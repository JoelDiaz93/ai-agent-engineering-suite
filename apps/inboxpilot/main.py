from dataclasses import dataclass

@dataclass
class Message:
    sender:str; subject:str; body:str; thread_id:str

def classify(m):
    text=(m.subject+" "+m.body).lower()
    return "urgent" if any(x in text for x in ("urgent","incidente","production")) else "normal"

def draft(m):
    return {"thread_id":m.thread_id,"to":m.sender,"subject":"Re: "+m.subject,"body":"Thanks for your message. I am reviewing the request and will follow up shortly.","requires_approval":True}

if __name__=="__main__":
    m=Message("demo@example.com","Production incident","Please review","thread-demo")
    print(classify(m),draft(m))
