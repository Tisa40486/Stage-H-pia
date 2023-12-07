#include <stdio.h>
void swap_same_length(char* str1, char* str2, int length) {
    for(int y=0; y < length; y++){
        char tmp=str1[y] ;
        str1[y] = str2[y] ;
        str2[y] = tmp ;
    }
}
int main(){
    int x = 7;
    int y = 5;

    int* a = &x;
    int* b = &y; 

    printf("%d\n", *a);
    printf("%p\n", a);
    printf("%p\n", &x);

    int tmp = *a ;
    *a = *b ;
    *b = tmp ; 
    printf("%d\n", x);
    printf("%d\n", y);

    char s1[] = {'o', 'u', 'i', '\0'} ;
    char s2[] = {'n', 'o', 'n', '\0'} ;
    char* oui = s1;
    char* non = s2;

    printf("%s %p\n", oui, oui);
    printf("%s %p\n", non, non);

    swap_same_length(oui, non, 3);
    printf("%s %p\n", oui, oui);
    printf("%s %p\n", non, non);
    
    char* tmp2 = oui ;
    oui = non ;
    non = tmp2 ;

    printf("%s %p\n", oui, oui);
    printf("%s %p\n", non, non);

}

