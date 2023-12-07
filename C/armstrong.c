#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

void digit_in_number(char* number){
    int size= strlen(number);
    printf("%d\n",size);
    int value=0;
    char digit[2];
    digit[1] = 0;

    for(int y=0; y < size; y++){
        digit[0] = number[y];
        int d = atoi(digit);
        value = value + pow(d, size);
    }
    //printf("%d\n",value );
    if (value == atoi(number)){
        printf("nombre armstrong\n");
    }
    else{
        printf("nombre non armstrong\n");
    }
}


int main()
{
    digit_in_number("9");
    digit_in_number("10");
    digit_in_number("153");
    digit_in_number("154");

}
