/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:52:15 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/18 10:42:31 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	lit_size;
	size_t	i;

	i = 0;
	lit_size = 0;
	while (little[lit_size])
		lit_size++;
	if (!little || lit_size == 0)
		return ((char *)big);
	while (*big && len-- > 0)
	{
		if (*big == *little)
		{
			while (little[i] && *(big + i) == little[i] && len >= i)
				i++;
			if (little[i] == '\0')
				return ((char *)big);
			i = 0;
		}
		big++;
	}
	return (NULL);
}
