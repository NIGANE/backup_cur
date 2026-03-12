#include "tree.h"

void inOrder(Node *root)
{
    if (root == NULL)
        return;
    inOrder(root->left);
    printf("=> %d ", root->data);
    inOrder(root->right);
}

void postOrder(Node* root)
{
    if(root == NULL)
        return;
    postOrder(root->left);
    postOrder(root->right);
    printf("=> %d ", root->data); 
}

void preOrder(Node* root)
{
    if(root == NULL)
        return;
    printf("=> %d ", root->data);
    preOrder(root->left);
    preOrder(root->right);
}

int max(int a, int b)
{
    if (a == b)
        return (a);
    return ((a > b) * a + (a < b) + b);
}

int get_height(Node *n)
{
    if (n == NULL)
        return (0);
    return (max(get_height(n->left), get_height(n->right)) + 1);
}

int is_balanced(Node *n)
{
    int left_h;
    int right_h;

    if (!n)
        return (0);
    left_h = get_height(n->left);
    right_h = get_height(n->right);
    if (right_h > left_h + 1 || left_h > right_h + 1)
        return (0);
    return (1);
}