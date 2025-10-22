/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 18:56:46 by amerkht           #+#    #+#             */
/*   Updated: 2025/07/22 12:22:54 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

size_t	ne_strlen(const char *str)
{
	size_t	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	sr_len;
	size_t	ds_len;
	size_t	i;

	i = 0;
	sr_len = ne_strlen(src);
	if (!dest && size == 0)
		return (sr_len);
	ds_len = ne_strlen(dest);
	if (size != 0)
	{
		while (src[i] != '\0' && i + ds_len < size - 1)
		{
			dest[ds_len + i] = src[i];
			i++;
		}
		dest[ds_len + i] = '\0';
	}
	if (ds_len < size)
		return (sr_len + ds_len);
	else
		return (size + sr_len);
}
#include <stdio.h>
#include <bsd/string.h>

int main(void)
{
	char		*dest = NULL;
	char		*src = "World!";
	size_t		size = 0;
	// printf("ft_strlcat: %zu\n", ft_strlcat(dest, src, size));
	printf("strlcat: %zu\n", strlcat(dest, src, size));
	printf("Resulting dest: '%s'\n", dest);
	return (0);
}
