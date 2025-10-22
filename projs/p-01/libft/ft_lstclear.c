/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 14:13:32 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/18 14:13:36 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdlib.h>

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*cur;
	t_list	*temp;

	if (!lst || !del)
		return ;
	if (!*lst)
		return ;
	cur = *lst;
	while (cur->next)
	{
		temp = cur;
		cur = cur->next;
		del(temp->content);
		temp->next = NULL;
		free(temp);
	}
	*lst = NULL;
}
