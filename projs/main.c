/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/13 01:40:13 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./tree/tree.h"
void print_nodes(Node *node)
{
    printf("   P(%d)\n", (node->data));
    if (node->left)
        printf("L(%d)/\\", (node->left->data));
    if (node->right)
        printf("R(%d)", (node->right->data));
    printf("\n");
}

int main()
{
    int data[] = {4, 2, 8, 1, 3, 9};
    Node *head = NULL;

    int i = 0;
    while (i < 6)
    {
        head = insert(head, data[i]);
        i++;
    }
    printf("is balanced: %d\n", is_balanced(head));
    bfs(head, 3);

}