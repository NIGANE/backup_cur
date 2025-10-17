/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:49:13 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 09:32:11 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <ctype.h>
int	ft_isalpha(int a)
{
	if ((a >= 65 && a <= 90) || (a >= 97 && a <= 122))
		return (1);
	return (0);
}

int main()
{
	char test1 = 'A';
	char test2 = 'z';
	char test3 = '1';
	char test4 = '%';

	printf("ft_isalpha('%c') = %d\n", test1, ft_isalpha(test1)); // Expected: 1
	printf("ft_isalpha('%c') = %d\n", test1, isalpha(test1)); // Expected: 1
	printf("\n");

	printf("ft_isalpha('%c') = %d\n", test2, ft_isalpha(test2)); // Expected: 1
	printf("ft_isalpha('%c') = %d\n", test2, isalpha(test2)); // Expected: 1
	printf("\n");

	printf("ft_isalpha('%c') = %d\n", test3, ft_isalpha(test3)); // Expected: 0
	printf("ft_isalpha('%c') = %d\n", test3, isalpha(test3)); // Expected: 0
	printf("\n");

	printf("ft_isalpha('%c') = %d\n", test4, ft_isalpha(test4)); // Expected: 0
	printf("ft_isalpha('%c') = %d\n", test4, isalpha(test4)); // Expected: 0
	printf("\n");

	return 0;
}
