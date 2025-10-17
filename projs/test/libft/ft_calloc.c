/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:57:54 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/15 18:57:57 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stddef.h>
#include <stdlib.h>

void	*ft_calloc(size_t nmumb, size_t size)
{
	unsigned char	*re;
	size_t			byt;
	unsigned char	*buf;

	if (nmumb <= 0 || size <= 0)
		return (malloc(0));
	byt = nmumb * size;
	re = malloc(byt);
	if (!re)
		return (NULL);
	buf = re;
	while (byt-- > 0)
		*buf++ = 0;
	return (re);
}

#include <stdio.h>

int main()
{
	size_t nmemb = 5;
	size_t size = sizeof(int);
	int *arr = (int *)ft_calloc(nmemb, size);
	if (arr == NULL)
	{
		printf("Memory allocation failed\n");
		return 1;
	}
	for (size_t i = 0; i < nmemb; i++)
	{
		printf("arr[%zu] = %d\n", i, arr[i]);
	}
	free(arr);
	return 0;
}
