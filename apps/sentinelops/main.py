from dataclasses import dataclass, field

@dataclass
class Alert:
    id:str; indicators:list[str]; evidence:list[str]=field(default_factory=list); severity:str="unknown"; verdict:str="undetermined"

def analyze(a:Alert):
    suspicious=sum(1 for e in a.evidence if "malicious" in e.lower())
    a.verdict="needs_review" if suspicious else "insufficient_evidence"
    a.severity="high" if suspicious>=2 else "medium" if suspicious else "low"
    return a

def mitigation(a:Alert):
    return ["Preserve evidence","Validate indicator with approved intelligence sources","Escalate to analyst"] if a.verdict=="needs_review" else ["Collect additional evidence"]

if __name__=="__main__":
    a=analyze(Alert("INC-DEMO",["198.51.100.10"],["source-a: malicious","source-b: malicious"])); print(a); print(mitigation(a))
