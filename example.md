# Natural numbers
```lean
inductive mynat
| Z : mynat
| S : mynat → mynat
```
## math also works
$\mathbb N$
## Define addition on natural number
$+ : \mathbb N \to \mathbb N \to \mathbb N$
```lean
def myadd : mynat → mynat → mynat
| Z Z := Z
| Z (S m) := S m
| (S m) Z := S m
| (S m) (S n) := S (myadd m n)
```
