/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 16:34:41 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/17 19:14:14 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include "libft.h"

char	*ft_strdup_to(const char *s)
{
	char	*re;
	char	*bf;
	size_t	len;

	len = 0;
	if (!s)
		return (NULL);
	while (s[len])
		len++;
	re = malloc(sizeof(char) * (len + 1));
	if (!re)
		return (NULL);
	bf = re;
	while (*s)
		*bf++ = *s++;
	return (re);
}

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*re;
	size_t	size;
	size_t	i;

	size = 0;
	i = 0;
	if (!s || !f)
		return (NULL);
	while (s[size])
		size++;
	re = ft_strdup_to(s);
	if (!re)
		return (NULL);
	while (re[i])
	{
		re[i] = f(i, re[i]);
		i++;
	}
	return (re);
}
