from dataclasses import dataclass, field

@dataclass
class Memory:
    user_id:str
    short:list[str]=field(default_factory=list)
    facts:list[str]=field(default_factory=list)
    def remember(self,message):
        self.short=(self.short+[message])[-6:]
        if message.lower().startswith("remember:"): self.facts.append(message.split(":",1)[1].strip())
    def context(self): return {"recent":self.short,"facts":self.facts}

if __name__=="__main__":
    m=Memory("demo"); m.remember("Hello"); m.remember("remember: prefers concise reports"); print(m.context())
