!NF {
    if (this_sum > top1) {
        top3 = top2
        top2 = top1
        top1 = this_sum
    } else if (this_sum > top2) {
        top3 = top2
        top2 = this_sum
    } else if (this_sum > top3) {
        top3 = this_sum
    }       
    
    this_sum = 0
}

{
    this_sum += $1
}

END {
    print top1
    print top1 + top2 + top3
}