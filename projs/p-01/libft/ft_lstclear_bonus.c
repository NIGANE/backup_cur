/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 16:48:29 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/23 17:08:56 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*cur;
	t_list	*temp;

	if (!lst || !del)
		return ;
	tmp = *lst;
	while (cur)
	{
		temp = cur;
		cur = cur->next;
		del(temp->content);
		temp->next = NULL;
		free(temp);
	}
	*lst = NULL;
}
