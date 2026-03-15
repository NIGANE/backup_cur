#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

// typedef struct coder {
//     int val;
// } Coder;

typedef struct s_heap {
    int* data;
    int len;
} t_heap;

#define P(i) ((i - 1) / 2)
#define L(i) (i == 0 ? i + 1 : (2 * (i + 1)))
#define R(i) (i == 0 ? i + 2 : (2 * (i + 2)))
#define max(a, b) (a > b ? a : b)

//  heap
int * sort_max_heap(int *list, int len);
int is_max_sorted(int *list, int len);
t_heap *create_max_heap(int data);
t_heap *insert_max_heap(t_heap *heap, int data);
t_heap *pop_max_heap(t_heap *heap);

//  helpers
void swap(int *a, int *b);
void free_heap(t_heap **heap);
int indexof(int *list, int len, int ele);