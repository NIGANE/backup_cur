/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:48:21 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 10:48:31 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
int	ft_toupper(int c)
{
	if (c >= 90 && c <= 122)
		c = c - ('a' - 'A');
	return (c);
}

#include <stdio.h>

int main()
{
	char lower = 'b';
	char upper = 'B';
	char non_alpha = '1';

	printf("Original: %c, To Upper: %c\n", lower, ft_toupper(lower));
	printf("Original: %c, To Upper: %c\n", upper, ft_toupper(upper));
	printf("Original: %c, To Upper: %c\n", non_alpha, ft_toupper(non_alpha));

	return 0;
}