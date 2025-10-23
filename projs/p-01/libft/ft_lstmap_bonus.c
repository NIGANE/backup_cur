/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 16:50:10 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/22 16:50:13 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdlib.h>

t_list	*lst_clear(t_list **head, void (*del)(void *))
{
	t_list	*temp;

	if (!head || !del)
		return (NULL);
	while (*head)
	{
		temp = *head;
		*head = (*head)->next;
		if (temp->content)
			del(temp->content);
		free(temp);
	}
	*head = NULL;
	return (*head);
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*cur;
	t_list	*head;
	t_list	*new;

	if (!lst || !f || !del)
		return (NULL);
	cur = NULL;
	head = NULL;
	while (lst)
	{
		new = malloc(sizeof(t_list));
		if (!new)
			return (lst_clear(&head, del));
		if (head == NULL)
			head = new;
		else
			cur->next = new;
		new->content = f(lst->content);
		if (!new->content)
			return (lst_clear(&head, del));
		new->next = NULL;
		cur = new;
		lst = lst->next;
	}
	return (head);
}
