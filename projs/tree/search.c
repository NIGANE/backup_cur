#include "tree.h"

int dfs(Node *node, int data)
{
    int founded;

    if (!node)
        return (0);
    if (node->data == data)
    {
        printf("found: %d\n", node->data);    
        return (1);
    }
    founded = 0;
    if (node->left)
        founded = dfs(node->left, data);
    if (founded == 1)
        return (founded);
    if (node->right)
        founded = dfs(node->right, data);
    return (founded);
}

// int bfs(Node *node, int data)
// {
//     int founded;

//     if (!node)
//         return (0);
//     if (node->left && node->left->data == data)
//     {
//         printf("founded: %d\n", node->left->data);
//         founded = 1;
//     }
//     if (founded = 1)
//         return founded;
//     if (node->right && node->right->data == data)
//     {
//         printf("founded: %d\n", node->right->data);
//         fonded = 1
//     }
//     if (node->left)
// }

int bfs(Node *node)
{
    Node* process_queu[100];
    size_t reader_num = 0;
    size_t add_num = 0;
    Node *cur;

    process_queu[add_num++] = node;
    while(add_num > reader_num){
        if (process_queu[reader_num]->data == data)
        {
            printf("founded: %d\n", process_queu[reader_num]->data == data);
            return (1);
        }
        if(curr->left != NULL){
            process_queu[add_num++] = curr->left;
        }
        if(curr->right != NULL){
            process_queu[add_num++] = curr->right;
        }
    }
    return (0);
}