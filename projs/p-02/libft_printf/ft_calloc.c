/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 18:57:54 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/28 16:44:16 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdint.h>
#include <stdlib.h>

void	*ft_calloc(size_t nmumb, size_t size)
{
	unsigned char	*re;
	size_t			byt;
	unsigned char	*buf;

	if (nmumb <= 0 || size <= 0)
		return (malloc(0));
	if (nmumb != 0 && SIZE_MAX / nmumb < size)
		return (NULL);
	byt = nmumb * size;
	re = malloc(byt);
	if (!re)
		return (NULL);
	buf = re;
	while (byt-- > 0)
		*buf++ = 0;
	return (re);
}
