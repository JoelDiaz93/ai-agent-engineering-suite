from dataclasses import dataclass

@dataclass
class MeetingResult:
    participants:list[str]; topics:list[str]; actions:list[str]; summary:str

def process(notes:str)->MeetingResult:
    lines=[x.strip(" -") for x in notes.splitlines() if x.strip()]
    participants=sorted({x.split(":",1)[0] for x in lines if ":" in x})
    actions=[x for x in lines if any(k in x.lower() for k in ("will ","debe ","se encargará","action:"))]
    topics=lines[:3]
    return MeetingResult(participants,topics,actions,f"Meeting with {len(participants)} participants and {len(actions)} actions.")

if __name__=="__main__":
    demo="Ana: revisar API\nCarlos: debe preparar pruebas\nAna: arquitectura del servicio"
    print(process(demo))
