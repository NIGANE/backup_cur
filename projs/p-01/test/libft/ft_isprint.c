/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 10:20:33 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 10:29:47 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
int	ft_isprint(int a)
{
	if (a >= 32 && a <= 126)
		return (1);
	return (0);
}

#include <stdio.h>
#include <ctype.h>
int main(void)
{
	int test_values[] = { ' ', 'A', 'z', '~', 31, 127, -1, 1000 };
	int num_tests = sizeof(test_values) / sizeof(test_values[0]);
	
	for (int i = 0; i < num_tests; i++)
	{
		int val = test_values[i];
		int my_result = ft_isprint(val);
		int std_result = isprint(val) ? 1 : 0;
		
		if (my_result == std_result)
			printf("ft_isprint(%d) == isprint(%d): PASS\n", val, val);
		else
			printf("ft_isprint(%d) != isprint(%d): FAIL\n", val, val);
	}
	
	return 0;
}