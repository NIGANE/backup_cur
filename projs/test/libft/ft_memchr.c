/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:34:00 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 13:34:12 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*bf;
	size_t			i;

	i = 0;
	bf = (unsigned char *)s;
	while (bf[i] && i < n)
	{
		if (bf[i] == (unsigned char)c)
			return (&bf[i]);
		i++;
	}
	return (NULL);
}

#include <stdio.h>
#include <string.h>
int main(void)
{
	const char *test_str = NULL;
	int test_chars[] = { 'H', 'W', '!', 'x', '\0' };
	size_t test_lengths[] = { 5, 13, 0, 7, 14 };
	int num_tests = sizeof(test_chars) / sizeof(test_chars[0]);
	
	for (int i = 0; i < num_tests; i++)
	{
		int c = test_chars[i];
		size_t n = test_lengths[i];
		
		void *my_result = ft_memchr(test_str, c, n);
		// void *std_result = memchr(test_str, c, n);
		
		// if (my_result == std_result)
		// 	printf("ft_memchr(\"%s\", '%c', %zu) == memchr: PASS\n", test_str, c, n);
		// else
		// 	printf("ft_memchr(\"%s\", '%c', %zu) != memchr: FAIL\n", test_str, c, n);
	}
	
	return 0;
}