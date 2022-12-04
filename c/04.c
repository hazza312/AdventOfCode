#include <stdio.h>
#include <stdlib.h>

int main() {
    int lo1, hi1, lo2, hi2;
    int score1 = 0, score2 = 0;
    
    while (scanf("%d-%d,%d-%d\n", &lo1, &hi1, &lo2, &hi2) > 0) {        
        score1 += (lo1 >= lo2 && hi1 <= hi2) || (lo2 >= lo1 && hi2 <= hi1);
        score2 += (lo1 >= lo2 && lo1 <= hi2) || (lo2 >= lo1 && lo2 <= hi1);             
    }
    
    printf("%d\n%d\n", score1, score2);
}
