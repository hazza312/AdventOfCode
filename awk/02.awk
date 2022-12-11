@load "ordchr"

function part1_score(opponent, me) {
    if (opponent == me) 
        return 3 + me + 1
    
    return 6 * ((me + 2) % 3 == opponent) + me + 1
}

function part2_score(opponent, me) {
    if (me == 0) 
        return ((opponent + 2) % 3) + 1
    if (me == 1) 
        return 3 + opponent + 1

    return 6 + ((opponent + 1) % 3) + 1
}

{
    opponent = ord($1) - ord("A")
    me = ord($2) - ord("X")

    part1_total += part1_score(opponent, me)
    part2_total += part2_score(opponent, me)
}

END {
    print part1_total
    print part2_total
}