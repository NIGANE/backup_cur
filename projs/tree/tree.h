#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

// typedef struct coder {
//     int val;
// } Coder;

typedef struct node {
    struct node *left;
    struct node *right;
    int *data;
} Node;

Node *create_node(int *d);
Node *insert(Node *head, int *val);