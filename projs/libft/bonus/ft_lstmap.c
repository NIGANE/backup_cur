/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 19:32:08 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/18 19:32:13 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdlib.h>

void	lst_clear(t_list **head, void (*del)(void *))
{
	t_list	*temp;

	if (!head || !del)
		return ;
	while (*head)
	{
		temp = *head;
		*head = (*head)->next;
		if (temp->content)
			del(temp->content);
		free(temp);
	}
	*head = NULL;
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*cur;
	t_list	*head;

	if (!lst || !f || !del)
		return (NULL);
	cur = malloc(sizeof(t_list));
	if (!cur)
		return (NULL);
	cur->content = f(lst->content);
	if (!cur->content)
	{
		free(cur);
		return (NULL);
	}
	cur->next = NULL;
	head = cur;
	lst = lst->next;
	while (lst)
	{
		cur->next = malloc(sizeof(t_list));
		if (!cur->next)
		{
			lst_clear(&head, del);
			return (NULL);
		}
		cur->next->content = f(lst->content);
		if (!cur->next->content)
		{
			lst_clear(&head, del);
			return (NULL);
		}
		cur->next->next = NULL;
		lst = lst->next;
		cur = cur->next;
	}
	return (head);
}
