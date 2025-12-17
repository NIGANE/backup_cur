#include "../includes/sta1.h"

void free_split_arr(char **arr)
{
    char **bf;

    bf = arr;
    while (*bf != NULL)
        free(*bf++);
    free(arr);
}