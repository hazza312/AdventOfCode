#include <stdio.h>
#include <stdlib.h>

int get_score1(int opponent, int me) {
    if (me == opponent) {
        return me + 4;
    }
    
    return me + 1 + (opponent == (me + 2) % 3) * 6;
}

int get_score2(int opponent, int me) {
    switch(me) {
        case 'X':   return 1 + (opponent + 2) % 3;
        case 'Y':   return 4 + opponent;
        default:    return 7 + (opponent + 1) % 3;        
    }
}

int main() {
    int score1 = 0, score2 = 0;
    char opponent, me;
    
    while (scanf("%c %c\n", &opponent, &me) > 0) {        
        score1 += get_score1(opponent - 'A', me - 'X');
        score2 += get_score2(opponent - 'A', me);              
    }
    
    printf("%d\n%d\n", score1, score2);
}