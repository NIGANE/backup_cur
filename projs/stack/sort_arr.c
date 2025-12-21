#include "../includes/sta1.h"


void swap_arr(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}

void sort_arr(int *arr, int size)
{
    int i;
    int j;

    i = 0;
    while (i < size - 1)
    {
        j = 0;
        while (j < size - 1 - i)
        {
            if (arr[j] > arr[j + 1])
                swap_arr(arr + j, arr + j + 1);
            j++;
        }
        i++;
    }
}