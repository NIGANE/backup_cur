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
#define min(a, b) (a < b ? a : b)

//  Max heap
int * sort_max_heap(int *list, int len);
int is_max_sorted(int *list, int len);
t_heap *insert_max_heap(t_heap *heap, int data);
t_heap *pop_max_heap(t_heap *heap);

//  Min Heap
int * sort_min_heap(int *list, int len);
int is_min_sorted(int *list, int len);

t_heap *insert_min_heap(t_heap *heap, int data);
t_heap *pop_min_heap(t_heap *heap);

//  helpers
t_heap *create_heap(int data);
void swap(int *a, int *b);
void free_heap(t_heap **heap);
int indexof(int *list, int len, int ele);
void print_arr(int *list, int len);
void inspect_heap(t_heap *hp);