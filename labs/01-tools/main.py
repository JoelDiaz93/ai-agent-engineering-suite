from dataclasses import dataclass

@dataclass
class Tool:
    name: str
    fn: callable
    def invoke(self, value): return self.fn(value)

def lookup_user(user_id: str):
    demo={"UX341234":{"name":"Demo User","tier":"pro"}}
    return demo.get(user_id,{"error":"not_found"})

if __name__=="__main__":
    tool=Tool("user_lookup",lookup_user)
    print(tool.invoke("UX341234"))
