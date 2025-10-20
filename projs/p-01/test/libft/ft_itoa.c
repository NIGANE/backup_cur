/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 16:10:53 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 16:12:28 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_nbrlen(int n)
{
	int	len;

	len = 0;
	if (n <= 0)
		len++;
	while (n)
	{
		n /= 10;
		len++;
	}
	return (len);
}

char	*reverse(char *s)
{
	size_t	len;
	size_t	i;
	char	temp;

	i = 0;
	len = 0;
	while (s[len])
		len++;
	while (i < len / 2)
	{
		temp = s[i];
		s[i] = s[len - 1 - i];
		s[len - 1 - i] = temp;
		i++;
	}
	return (s);
}

char	*to_str(int n, int sign, int len)
{
	char		*re;
	size_t		i;

	i = 0;
	re = malloc(sizeof(char) * len + 1);
	if (!re)
		return (NULL);
	if (n == 0)
	{
		re[0] = '0';
		re[1] = '\0';
		return (re);
	}
	while (n)
	{
		re[i] = n % 10 + '0';
		n = n / 10;
		i++;
	}
	if (sign < 0)
		re[i++] = '-';
	re[i] = '\0';
	return (re);
}

char	*dup_func(const char *s)
{
	char	*re;
	size_t	size;
	size_t	i;

	i = 0;
	size = 0;
	while (s[size++])
		;
	re = malloc(sizeof(char) * size);
	if (!re)
		return (NULL);
	while (size - i > 0)
	{
		re[i] = s[i];
		i++;
	}
	return (re);
}

char	*ft_itoa(int n)
{
	size_t	len;
	int		sign;

	sign = 1;
	if (n == -2147483648)
		return (dup_func("-2147483648"));
	len = ft_nbrlen(n);
	if (n <= 0)
	{
		sign = -1;
		n *= sign;
		len++;
	}
	return (reverse(to_str(n, sign, len)));
}

#include <stdio.h>
int main(void)
{
	int test_values[] = { 0, 123, -456, 2147483647, -2147483648, -1, 0, -0 };
	int num_tests = sizeof(test_values) / sizeof(test_values[0]);
	
	for (int i = 0; i < num_tests; i++)
	{
		int val = test_values[i];
		char *result = ft_itoa(val);
		printf("ft_itoa(%d) = \"%s\"\n", val, result);
		free(result);
	}
	
	return 0;
}