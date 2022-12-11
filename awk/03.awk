@load "ordchr"

function add(A, s, p) {
    delete visited
    for (i=1; i<=length(s); i++) {
        ch = substr(s, i, 1)
        if (!(ch in visited)) {
            A[ch]++
            visited[ch]
        }
    }
}

function priority(A, n) {
    for (c in A) if (A[c] == n) break
    minus = (c < "a") ? ord("A") - 27 : ord("a") - 1
    return ord(c) - minus
}

{
    # common character in split line
    n = length($0)
    add(A, substr($0, 1, n/2))
    add(A, substr($0, 1+n/2, n/2))
    split_sum += priority(A, 2)
    delete A
    
    # common character across 3 whole lines
    add(B, $0)
}

NR % 3 == 0 {
    by3_sum += priority(B, 3)
    delete B
}

END {
    print split_sum
    print by3_sum
}