/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:06:45 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 19:06:53 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	size_t	i;

	if (!s)
		return ;
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
}

#include <stdio.h>
void	print_char(unsigned int index, char *c)
{
	printf("Index: %u, Char: %c\n", index, *c);
}
int main(void)
{
	char	*str = NULL;
	
	printf("Original string: %s\n", str);
	ft_striteri(str, print_char);
	return (0);
}