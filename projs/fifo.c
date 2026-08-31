/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fifo.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:00:40 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/31 18:24:55 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "header.h"

t_node	*ft_create(void *data)
{
	t_node	*node;

	node = malloc(sizeof(t_node));
	if (!node)
		return (NULL);
	node->data = data;
	node->id = 0;
	node->next = NULL;
	return (node);
}

t_node	*ft_insert(void *data, t_node *fifo)
{
	t_node	*node;
	t_node	*cur;

	if (!data)
		return (fifo);
	if (!fifo)
		return (ft_create(data));
	node = ft_create(data);
	if (!node)
		return (ft_free(fifo), NULL);
	cur = fifo;
	while (cur->next)
		cur = cur->next;
	cur->next = node;
	return (fifo);
}

t_node	*ft_pop(t_node **fifo)
{
	t_node	*re;

	if (!fifo || !*fifo)
		return (NULL);
	re = *fifo;
	*fifo = (*fifo)->next;
	return (re);
}

void	ft_free(t_node *fifo)
{
	t_node	*tmp;

	if (!fifo)
		return ;
	while (fifo)
	{
		tmp = fifo;
		fifo = fifo->next;
		free(tmp);
	}
}

int	ft_len(t_node *head)
{
	int	i;

	if (!head)
		return (0);
	i = 0;
	while (head)
	{
		i++;
		head = head->next;
	}
	return (i);
}
