#include <stdio.h>
int main()
{
    int annee;
    printf("année?\n");
    scanf("%d", &annee);
    if ((annee % 4) == 0 && (annee % 100) != 0 && (annee % 400) != 0)
    {
        printf("année bissextile \n");
    }
    else
    {
        printf("année non-bissextile\n");
    }
    return 0;
}
