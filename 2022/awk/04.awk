function within(inl, inh, outl, outh) {
    return inl >= outl && inh <= outh
}

function overlaps(lo1, hi1, lo2, hi2) {
    return (lo1 > lo2 ? lo1 : lo2) <= (hi1 < hi2 ? hi1 : hi2)
}

match($0, /([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)/, A) {
    part1 += within(A[1], A[2], A[3], A[4]) || within(A[3], A[4], A[1], A[2])
    part2 += overlaps(A[1], A[2], A[3], A[4])
}

END {
    print part1
    print part2
}