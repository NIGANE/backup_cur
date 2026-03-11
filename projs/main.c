/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/03/11 02:06:01 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./tree/tree.h"


int main()
{
    int data[5] = {1, 2, 3, 4, 5};
    Node *head;

    head = insert(head, data);
    printf("head: %d\n", *(head->data));
    if (head->left)
        printf("left %d\n", *(head->left->data));
}