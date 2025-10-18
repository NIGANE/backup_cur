/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:28:23 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 11:29:19 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

char	*ft_strrchr(const char *s, int c)
{
	int	i;

	i = 0;
	if (!s)
		return (NULL);
	while (s[i++])
		;
	while (i >= 0)
	{
		if (s[i] == c)
			return ((char *)&s[i]);
		i--;
	}
	if (c == '\0')
		return ((char *)&s[i]);
	return (NULL);
}

#include <stdio.h>
int main()
{
	const char *str = NULL;
	char ch = 'h';
	char *result = ft_strrchr(str, ch);
	if (result)
		printf("Last occurrence of '%c': %s\n", ch, result);
	else
		printf("Character '%c' not found.\n", ch);
	return 0;
}
