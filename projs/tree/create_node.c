
#include "./tree.h"

Node* create_node(int *n)
{
    Node* new_node = malloc(sizeof(Node));
    if (!new_node)
        return (NULL);
    new_node->data = n;
    new_node->left = NULL;
    new_node->right = NULL;
    return (new_node);
}


