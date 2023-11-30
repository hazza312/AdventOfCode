⍝ Day 6 APL attempt, input from file

lines ← ⊃⎕NGET'input6.txt' 1
markerstart←{¯1+⍺+⊃⍒≢¨⍺∪/⍵}

+/4 markerstart ¨ lines
+/14 markerstart ¨ lines