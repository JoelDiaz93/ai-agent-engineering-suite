from dataclasses import dataclass

@dataclass
class State:
    value:int
    route:str=""
    result:str=""

def route(s:State): s.route="even" if s.value%2==0 else "odd"; return s
def execute(s:State): s.result=f"{s.value} is {s.route}"; return s

if __name__=="__main__": print(execute(route(State(7))))
