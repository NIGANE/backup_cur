/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:56:59 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 18:57:02 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*re;
	size_t	size;
	size_t	i;

	i = 0;
	size = 0;
	while (s[size++])
		;
	re = malloc(sizeof(char) * size);
	if (!re)
		return (NULL);
	while (size - i > 0)
	{
		re[i] = s[i];
		i++;
	}
	return (re);
}
