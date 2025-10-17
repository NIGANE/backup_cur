/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 11:49:45 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 17:57:41 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>
void	*ft_memcpy(void *dest, void *src, size_t size)
{
	unsigned char	*dest_buf;
	unsigned char	*src_buf;

	dest_buf = (unsigned char *) dest;
	src_buf = (unsigned char *) src;
	while (size-- > 0)
		*dest_buf++ = *src_buf++;
	return (dest);
}

#include <stdio.h>
#include <string.h>
int main() {
	char src[] = "Hello, World!";
	char dest1[20];
	char dest2[20];

	// Using custom ft_memcpy
	ft_memcpy(dest1, src, strlen(src) + 1);
	printf("ft_memcpy result: %s\n", dest1);

	// Using standard memcpy for comparison
	memcpy(dest2, src, strlen(src) + 1);
	printf("memcpy result: %s\n", dest2);

	return 0;
}