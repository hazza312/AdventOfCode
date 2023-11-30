BEGIN {    
    split("20 60 100 140 180 220", sample_idx)
    for (i in sample_idx) sample_point[sample_idx[i]]
    
    x = 1
}

function step(n) {
    for (i = 0; i < n; i++) {    
        if (++cycle in sample_point) 
            sample_sum += x * cycle
        
        crtx = (cycle - 1) % 40
        printf (x >= crtx - 1 && x <= crtx + 1) ? "#" : "."
        if (crtx == 39) 
            print ""
    }
    
}

$1 == "addx" {
    step(2)
    x += $2
}

$1 == "noop" {
    step(1)
}

END {
    print sample_sum
}