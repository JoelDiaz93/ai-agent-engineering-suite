import json
from pathlib import Path

class ConversationMemory:
    def __init__(self,path="memory.json"): self.path=Path(path); self.items=self._load()
    def _load(self):
        return json.loads(self.path.read_text()) if self.path.exists() else []
    def add(self,role,content): self.items.append({"role":role,"content":content}); self.path.write_text(json.dumps(self.items,indent=2))
    def window(self,n=6): return self.items[-n:]

if __name__=="__main__":
    m=ConversationMemory(); m.add("user","Hello memory"); print(m.window())
