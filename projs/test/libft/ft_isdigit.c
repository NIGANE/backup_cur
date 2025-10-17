/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 09:39:37 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 09:43:56 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_isdigit(int a)
{
	if (a >= 48 && a <= 57)
		return (1);
	return (0);
}

#include <ctype.h>

int main(void)
{
	int test_values[] = { '0', '5', '9', 'a', 'Z', ' ', 47, 58, -1, 1000 };
	int num_tests = sizeof(test_values) / sizeof(test_values[0]);
	
	for (int i = 0; i < num_tests; i++)
	{
		int val = test_values[i];
		int my_result = ft_isdigit(val);
		int std_result = isdigit(val) ? 1 : 0;
		
		if (my_result == std_result)
			printf("ft_isdigit(%d) == isdigit(%d): PASS\n", val, val);
		else
			printf("ft_isdigit(%d) != isdigit(%d): FAIL\n", val, val);
	}
	
	return 0;
}