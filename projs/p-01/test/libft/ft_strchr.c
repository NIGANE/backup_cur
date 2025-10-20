/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:06:17 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 11:06:19 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

char	*ft_strchr(const char *s, int c)
{
	int	i;

	i = 0;
	if (!s)
		return (NULL);
	while (s[i] && s[i] != c)
		i++;
	if (s[i] == c)
		return ((char *)(s + i));
	return (NULL);
}

#include <stdio.h>
#include <string.h>
int main(void)
{
	const char	*str = "Hello, World!";
	char		*result;

	result = ft_strchr(str, 'W');
	if (result)
		printf("Character found: %s\n", result);
	else
		printf("Character not found.\n");

	result = ft_strchr(str, 'z');
	if (result)
		printf("Character found: %s\n", result);
	else
		printf("Character not found.\n");

	result = ft_strchr(str, '\0');
	if (result)
		printf("Null terminator found: %s\n", result);
	else
		printf("Null terminator not found.\n");
	result = ft_strchr(NULL, '\0'); // Testing : non-null string

	return (0);
}
