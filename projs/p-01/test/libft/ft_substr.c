/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 19:08:56 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 19:21:54 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
// #include "./libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*re;
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	re = malloc(sizeof(char) * len);
	if (!re)
		return (NULL);
	while (s[i])
	{
		if (i == start)
		{
			while (s[i] && len-- > 0)
				re[j++] = s[i++];
			return (re);
		}
		i++;
	}
	return (malloc(0));
}

#include <stdio.h>

int	main(void)
{
	char			*str;
	unsigned int	start;
	size_t			len;
	char			*substr;

	str = "Hello, World!";
	start = 9;
	len = 5;
	substr = ft_substr(str, start, len);
	if (substr)
	{
		printf("Substring: %.*s\n", (int)len, substr);
		free(substr);
	}
	else
	{
		printf("Memory allocation failed\n");
	}
	return (0);
}
