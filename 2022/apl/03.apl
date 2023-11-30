⍝ Day 3 APL attempt, input from file

lines ← ⊃⎕NGET'input3.txt' 1
linesplit ← {⍵⊆⍨1+(2÷⍨⍴⍵)<⍳⍴⍵}¨ lines
linesby3 ← {⍵⊆⍨⌈3÷⍨⍳⍴⍵} lines
do ← +/{c-96 38⊃⍨1+96>c←⎕UCS⊃⊃∩/⍵}¨

do linesplit
do linesby3
