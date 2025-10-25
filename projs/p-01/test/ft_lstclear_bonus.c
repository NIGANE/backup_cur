/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 16:48:29 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/24 18:46:40 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*cur;
	t_list	*temp;

	if (!lst || !del)
		return ;
	cur = *lst;
	while (cur)
	{
		temp = cur;
		cur = cur->next;
		del(temp->content);
		free(temp);
	}
	*lst = NULL;
}
