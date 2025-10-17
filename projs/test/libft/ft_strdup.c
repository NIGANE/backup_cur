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

#include <stdio.h>
#include <string.h>
int main(void)
{
	const char	*original = "NULL";
	char		*duplicate;

	duplicate = ft_strdup(original);
	if (duplicate)
	{
		printf("Original: %s\n", original);
		printf("Duplicate: %s\n", duplicate);
		free(duplicate);
	}
	else
	{
		printf("Memory allocation failed.\n");
	}
	return (0);
}