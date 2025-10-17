/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 10:06:45 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 10:06:59 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isascii(int a)
{
	if (a >= 0 && a <= 127)
		return (1);
	return (0);
}

#include <ctype.h>
#include <stdio.h>
int main()
{
	int c = 0; // Example character 'A'
	if (ft_isascii(c))
		printf("%d is an ASCII character.\n", c);
	else
		printf("%d is not an ASCII character.\n", c);

	int b = 0; // Example non-ASCII character
	if (isascii(b))
		printf("%d is an ASCII character.\n", b);
	else
		printf("%d is not an ASCII character.\n", b);
	return 0;
}
