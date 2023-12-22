#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define LEN_X 5
// largeur
#define LEN_Y 5
// hauteur
#define NUM_BOMB 10
// nombre bomb
const char hidden_cell = 'O';
const char bomb_cell = '*';
const char flag_cell = 'F';

void print_bool(bool tableau[LEN_X][LEN_Y])
// bool grid, true = Mine
{
    for (int i = 0; i < LEN_X; i += 1)
    {
        for (int j = 0; j < LEN_Y; j += 1)
        {
            if (tableau[i][j])
            {
                printf("X\t");
            }
            else
            {
                printf("O\t");
            }
        }
        printf("\n");
    }
}
void fill_char(char tableau[LEN_X][LEN_Y])
{
    for (int x = 0; x < LEN_X; x += 1)
    {
        for (int y = 0; y < LEN_Y; y += 1)
        {
            tableau[x][y] = hidden_cell;
        }
    }
}

void print_char(char tableau[LEN_X][LEN_Y])
// print grid players
{
    for (int i = 0; i < LEN_X; i += 1)
    {
        for (int j = 0; j < LEN_Y; j += 1)
        {
            printf("%c\t", tableau[i][j]);
        }
        printf("\n");
    }
}
bool verification(int x, int y)
{
    bool result= true;
    if (x < 0 || x >= LEN_X)
    {
        printf("position (x) inconnue, veuillez choisir un nombre entre 0 et %d\n", (LEN_X - 1));
        result = false;
    }
    if (y < 0 || y >= LEN_Y)
    {
        printf("position (y) inconnue, veuillez choisir un nombre entre 0 et %d\n", (LEN_Y - 1));
        result = false;
    }
    return result;
}
void bomb_position(bool bomb[LEN_X][LEN_Y])
// generate bomb in grid
{
    int x = rand() % LEN_X;
    int y = rand() % LEN_Y;
    while (bomb[x][y] == 1)
    {
        x = rand() % LEN_X;
        y = rand() % LEN_Y;
    }
    bomb[x][y] = true;
}

void position(int *x, int *y)
{
    bool verif = false;
    while (!verif)
    {
        printf("vertical (x) ? \n");
        scanf("%d", x);
        printf("horizontal (y) ?\n");
        scanf("%d", y);
        verif = verification(*x, *y);
    }

    printf("que voulez-vous faire sur les positions  %d : %d\n", *x, *y);
    printf("\n");
    printf("1/put Flag");
    printf("\n");
    printf("2/reveal case");
    printf("\n");
    printf("3/remove Flag");
    printf("\n");
}

void reveal(bool bomb[LEN_X][LEN_Y], char revetement[LEN_X][LEN_Y], int x, int y)
{
    if (revetement[x][y] != hidden_cell)
    {
        return;
    }
    int i;
    int j;
    int compteur = 0;
    int nx;
    int ny;
    for (i = -1; i < 2; i += 1)
    {
        for (j = -1; j < 2; j += 1)
        {
            nx = x + i;
            ny = y + j;
            if (nx < 0 || nx >= LEN_X)
            {
                continue;
            }
            if (ny < 0 || ny >= LEN_Y)
            {
                continue;
            }
            if (bomb[nx][ny])
            {
                compteur += 1;
            }
        }
    }
    revetement[x][y] = compteur + 48;
    if (compteur == 0)
    {
        for (i = -1; i < 2; i += 1)
        {
            for (j = -1; j < 2; j += 1)
            {
                nx = x + i;
                ny = y + j;
                if (nx < 0 || nx >= LEN_X)
                {
                    continue;
                }
                if (ny < 0 || ny >= LEN_Y)
                {
                    continue;
                }
                reveal(bomb, revetement, nx, ny);
            }
        }
    }
}

bool showcase(bool bomb[LEN_X][LEN_Y], char revetement[LEN_X][LEN_Y], int x, int y)
{
    if (bomb[x][y])
    {
        revetement[x][y] = bomb_cell;
        return true;
    }
    else
    {
        reveal(bomb, revetement, x, y);
        return false;
    }
}

bool condition_victory(char revetement[LEN_X][LEN_Y])
{
    int compteur = 0;
    for (int i = 0; i < LEN_X; i += 1)
    {
        for (int j = 0; j < LEN_Y; j += 1)
        {
            if (revetement[i][j] == flag_cell)
            {
                compteur += 1;
            }
            if (revetement[i][j] == hidden_cell)
            {
                compteur += 1;
            }
        }
    }
    if (compteur == NUM_BOMB)
    {
        return true;
    }
    return false;
}

void gamechoice(bool bomb[LEN_X][LEN_Y], char revetement[LEN_X][LEN_Y])
// gameplay/locate
{
    int x;
    int y;
    int action;
    bool defeat = false;
    bool win = false;
    while (!defeat && !win)
    {
        print_char(revetement);
        position(&x, &y);
        scanf("%d", &action);
        if (action == 1)
        {
            // Flag
            revetement[x][y] = flag_cell;
        }
        else if (action == 2)
        {
            defeat = showcase(bomb, revetement, x, y);
        }
        else if (action == 3 && revetement[x][y] != hidden_cell)
        {
            // remove flag
            if (revetement[x][y] == flag_cell)
            {
                revetement[x][y] = hidden_cell;
            }
            else
            {
                continue;
            }
        }
        win = condition_victory(revetement);
       
    }
    if (win)
    {
        printf("Gagné !");
        printf("\n");
    }
    else
    {
        printf("Perdu !");
        printf("\n");
    }
}

int main()
{
    srand(time(NULL));
    bool layer_1[LEN_X][LEN_Y];
    char layer_2[LEN_X][LEN_Y];
    for (int i = 0; i < NUM_BOMB; i++)
    {
        bomb_position(layer_1);
    }
    fill_char(layer_2);
    gamechoice(layer_1, layer_2);
}
