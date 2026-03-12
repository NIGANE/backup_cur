#include "tree.h"

Node *insert(Node *head, int val)
{
    if (!head)
        return (create_node(val));

    if ((head->data) < val)
        head->right = insert(head->right, val);
    else if ((head->data) > val)
        head->left = insert(head->left, val);
    return (head);
}