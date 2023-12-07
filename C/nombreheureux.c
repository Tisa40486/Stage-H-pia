#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


 int digit_in_number(char* number){
    int size= strlen(number);
    // printf("%d\n",size);
    int somme =0;
    char digit[2];
    digit[1] = 0;

    for(int y=0; y < size; y++){
        digit[0] = number[y];
        int d = atoi(digit);
        somme = somme + pow(d, 2);
    }
return somme;
}

bool nombres_heureux(char* number){
    char temp[1000];

    int previous = atoi(number);
    while (previous != 1){
        sprintf(temp, "%d", previous);
        previous=digit_in_number(temp);
        
        if (previous==4||previous==16||previous==20||previous==37||previous==42||previous==58||previous==89||previous==145){
            return false;
        }

    }

}


int main(){
    printf("%d",nombres_heureux("16"));
}