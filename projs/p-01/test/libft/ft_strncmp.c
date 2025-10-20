/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:51:50 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 11:51:56 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	while (n > 0 && *s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
		n--;
	}
	if (n == 0)
		return (0);
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

#include <stdio.h>
#include <string.h>
int main(void)
{
	const char *str1 = "";
	const char *str2 = "";
	size_t n = 5;

	int result_ft = ft_strncmp(str1, str2, n);
	int result_std = strncmp(str1, str2, n);

	printf("ft_strncmp result: %d\n", result_ft);
	printf("strncmp result: %d\n", result_std);

	return 0;
}