/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 15:37:49 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 17:56:53 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;

	d = dest;
	s = src;
	if (d < s)
	{
		while (n--)
			*d++ = *s++;
	}
	else
	{
		d += n;
		s += n;
		while (n-- > 0)
			*(--d) = *(--s);
	}
	return (dest);
}

#include <stdio.h>
#include <string.h>
int main() 
{
	char str1[20] = "";
	char str2[20] = "";

	// Overlapping regions: dest starts within src
	ft_memmove(str1 + 7, str1, 6);
	printf("ft_memmove result: %s\n", str1);

	// strcpy(str2, "abcdefg");
	// Reset str2 for standard memmove test
	memmove(str2 + 7, str2, 6);
	printf("memmove result: %s\n", str2);

	return 0;
}