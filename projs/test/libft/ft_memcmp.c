/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:35:16 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 13:35:21 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*s1_buf;
	unsigned char	*s2_buf;
	size_t			i;

	i = 0;
	s1_buf = (unsigned char *)s1;
	s2_buf = (unsigned char *)s2;
	while (i < n)
	{
		if (s1_buf[i] != s2_buf[i])
			return (s1_buf[i] - s2_buf[i]);
		i++;
	}
	return (0);
}

#include <string.h>
int main(void)
{
	const char *str1 = NULL;
	const char *str2 = "Hello, World!";
	const char *str3 = "Hello, World?";
	size_t test_lengths[] = { 5, 13, 0, 7, 14 };
	int num_tests = sizeof(test_lengths) / sizeof(test_lengths[0]);
	
	for (int i = 0; i < num_tests; i++)
	{
		size_t n = test_lengths[i];
		
		int my_result_equal = ft_memcmp(str1, str2, n);
		int std_result_equal = memcmp(str1, str2, n);
		
		if (my_result_equal == std_result_equal)
			printf("ft_memcmp(\"%s\", \"%s\", %zu) == memcmp: PASS\n", str1, str2, n);
		else
			printf("ft_memcmp(\"%s\", \"%s\", %zu) != memcmp: FAIL\n", str1, str2, n);
		
		int my_result_diff = ft_memcmp(str1, str3, n);
		int std_result_diff = memcmp(str1, str3, n);
		
		if (my_result_diff == std_result_diff)
			printf("ft_memcmp(\"%s\", \"%s\", %zu) == memcmp: PASS\n", str1, str3, n);
		else
			printf("ft_memcmp(\"%s\", \"%s\", %zu) != memcmp: FAIL\n", str1, str3, n);
	}
	
	return 0;
}