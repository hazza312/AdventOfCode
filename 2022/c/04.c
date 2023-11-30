#include <stdio.h>
#include <stdlib.h>

#define MAX(a,b)                        ((a > b) ? a : b)
#define MIN(a,b)                        ((a < b) ? a : b)
#define WITHIN(inl, inh, outl, outh)    (inl >= outl && inh <= outh)

int main() {
    int lo1, hi1, lo2, hi2;
    int score1 = 0, score2 = 0;
    
    while (scanf("%d-%d,%d-%d\n", &lo1, &hi1, &lo2, &hi2) > 0) {            
        score1 += WITHIN(lo1, hi1, lo2, hi2) || WITHIN(lo2, hi2, lo1, hi1);
        score2 += MAX(lo1, lo2) <= MIN(hi1, hi2);             
    }
    
    printf("%d\n%d\n", score1, score2);
}
