/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:56:38 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 10:56:42 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
int	ft_tolower(int c)
{
	if (c >= 65 && c <= 90)
		c = c + ('a' - 'A');
	return (c);
}

#include <stdio.h>
int main(void)
{
	char c = 'A';
	printf("%c\n", ft_tolower(c)); // Output: a
	c = 'z';
	printf("%c\n", ft_tolower(c)); // Output: z
	c = '1';
	printf("%c\n", ft_tolower(c)); // Output: 1
	return 0;
}