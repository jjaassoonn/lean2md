--BEGIN:IGNORE
def ignore_me : true := ⟨⟩
--END:IGNORE

/-MD
# Natural numbers
MD-/
inductive mynat
| Z : mynat
| S : mynat → mynat

/-MD
## math also works
$\mathbb N$
MD-/

--BEGIN:IGNORE
open mynat
--END:IGNORE
/-MD 
## Define addition on natural number
$+ : \mathbb N \to \mathbb N \to \mathbb N$
MD-/
def myadd : mynat → mynat → mynat
| Z Z := Z
| Z (S m) := S m
| (S m) Z := S m
| (S m) (S n) := S (myadd m n)
