## Python projects

- https://github.com/blurg/sauron-engine 

All others are dead :()

- https://github.com/nemonik/Intellect (Dead - 2017)
- https://github.com/jruizgit/rules (dead)
- https://github.com/cmaclell/py_rete (dead)
- https://github.com/nilp0inter/experta (dead)
- https://github.com/GNaive/naive-rete (dead)

## Other technologies

- [[CLIPS]]
- https://www.evrete.org/ (Java)

## Mockup API In Python

See: https://www.evrete.org/guides/run/prime-numbers/

```python
from dataclasses import dataclass  
  
  
def main():  
    service = KnowledgeService()  
    knowledge = service.new_knowledge(  
        "PYTHON-CLASS",  
        RuleSet  
    )  
  
    # Init subject and its known properties  
    fritz = Subject(croaks=True, eats_flies=True)  
  
    # Insert Fritz and fire all rules  
    knowledge.new_stateless_session().insert_and_fire(fritz)  
  
    # Fritz should have been identified as a green frog  
    print("Is Fritz a frog?\t", fritz.is_frog)  
    print("Is Fritz green? \t", fritz.is_green)  
  
    service.shutdown()  
  
  
@dataclass  
class Subject:  
    croaks: bool = False  
    eats_flies: bool = False  
    is_frog: bool = False  
    is_green: bool = False  
  
  
class RuleSet:  
    @staticmethod  
    def rule1(ctx, s):  
        if s.is_frog and not s.is_green:  
            s.is_green = True  
            ctx.update(s)  
  
    @staticmethod  
    def rule2(ctx, s):  
        if s.croaks and s.eats_flies and not s.is_frog:  
            s.is_frog = True  
            ctx.update(s)  
  
  
# Alt  
  
@rule  
@where({"$s.is_frog", "!$s.is_green"})  
def rule1(ctx, s):  
    s.is_green = True  
    ctx.update(s)  
  
  
@rule  
@where({"$s.croaks", "$s.eats_flies", "!$s.is_frog"})  
def rule2(ctx, s):  
    s.is_frog = True  
    ctx.update(s)  


# 
# Framework
#
class KnowledgeService:  
    def new_knowledge(self, name, rule_set_class):  
        return Knowledge(rule_set_class)  
  
    def shutdown(self):  
        pass  
  
  
class Knowledge:  
    def __init__(self, rule_set_class):  
        self.rule_set_class = rule_set_class  
  
    def new_stateless_session(self):  
        return StatelessSession(self.rule_set_class)  
  
  
class StatelessSession:  
    def __init__(self, rule_set_class):  
        self.rules = [rule_set_class.rule1, rule_set_class.rule2]  
  
    def insert_and_fire(self, subject):  
        ctx = RhsContext()  
        for rule in self.rules:  
            rule(ctx, subject)  
  
  
class RhsContext:  
    def update(self, subject):  
        pass  
  
  
if __name__ == "__main__":  
    main()
```
