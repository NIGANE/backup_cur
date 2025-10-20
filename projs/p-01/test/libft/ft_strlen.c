/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 10:34:16 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 10:34:34 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *s)
{
	int	len;

	len = 0;
	while (*s++)
		len++;
	return (len);
}

#include <stdio.h>
int main(void)
{
	char str[] = "Hello, World!";
	int length = ft_strlen(str);
	printf("Length of the string \"%s\" is: %d\n", str, length);
	return 0;
}