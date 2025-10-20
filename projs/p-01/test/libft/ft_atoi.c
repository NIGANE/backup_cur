/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:57:40 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 18:57:44 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
int	ft_atoi(char *s)
{
	int		sign;
	long	re;

	sign = 1;
	re = 0;
	if (!s)
		return (0);
	while (*s == ' ')
		s++;
	if (*s == '-' || *s == '+')
	{
		if (*s == '-')
			sign *= -1;
		s++;
	}
	while (*s >= '0' && *s <= '9')
	{
		re = re * 10 + (*s - '0');
		s++;
	}
	return (re * sign);
}
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	char *s = "345222";
	printf("ft_atoi(%s) => %d\n", s, ft_atoi(s));
	printf("atoi(%s) => %d\n", s, atoi(s));
	printf("\n\n");

	// printf("ft_atoi(NULL) => %d\n", atoi(NULL)); // non-null argument

	printf("ft_atoi("") => %d\n", ft_atoi(""));
	printf("atoi("") => %d\n", atoi(""));
	printf("\n\n");

	char *s1 = "-34522";
	printf("ft_atoi(%s) => %d\n", s1, ft_atoi(s1));
	printf("atoi(%s) => %d\n", s1, atoi(s1));
	printf("\n\n");

	char *s2 = "-2147483648";
	printf("ft_atoi(%s) => %d\n", s2, ft_atoi(s2));
	printf("atoi(%s) => %d\n", s2, atoi(s2));
}