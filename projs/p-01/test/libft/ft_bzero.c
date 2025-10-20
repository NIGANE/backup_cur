/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 11:26:59 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/14 11:27:06 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void	ft_bzero(void *data, size_t size)
{
	unsigned char	*buf;

	buf = (unsigned char *) data;
	while (*buf && size-- > 0)
		*buf++ = '\0';
}


void print_memory(const void *ptr, size_t size)
{
    const unsigned char *p = ptr;
    for (size_t i = 0; i < size; i++)
        printf("%02x ", p[i]);
    printf("\n");
}

int main(void)
{
	char s[] = "hello world";
	char s_[] = "hello world";
	bzero(s+2, 3);
	ft_bzero(s_+2, 3);
	print_memory(s, sizeof(s));
	print_memory(s_, sizeof(s));
	
	printf("\n\n");


	char s1[] = "";
	char s_1[] = "";
	bzero(s1+2, 3);
	ft_bzero(s_1+2, 3);
	print_memory(s1, sizeof(s1));
	print_memory(s_1, sizeof(s_1));

	printf("\n\n");

	char s2[] = "NULL";
	char s_2[] = "NULL";
	bzero(s2+2, 10);
	ft_bzero(s_2+2, 10);
	print_memory(s2, sizeof(s2));
	print_memory(s_2, sizeof(s_2));


}
