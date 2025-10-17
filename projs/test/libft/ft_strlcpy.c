/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:26:30 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 09:26:40 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	src_len;

	src_len = 0;
	while (src[src_len])
		src_len++;
	if (dstsize <= 0)
		return (src_len);
	dstsize -= 1;
	while (dstsize-- > 0)
		*dst++ = *src++;
	*dst = '\0';
	return (src_len);
}

#include <stdio.h>
#include <bsd/string.h>
int main() {
	char dest1[9];
	char dest2[9];
	const char *src = "NULL";

	size_t result1 = ft_strlcpy(dest1, src, sizeof(dest1));
	// size_t result2 = strlcpy(dest2, src, 10);

	printf("ft_strlcpy result: %zu, dest: %s\n", result1, dest1);
	// printf("strlcpy result: %zu, dest: %s\n", result2, dest2);

	return 0;
}
