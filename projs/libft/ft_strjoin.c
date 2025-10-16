/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:58:45 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 09:20:58 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strjoin(const char *s1, const char *s2)
{
	size_t	s1_size;
	size_t	s2_size;
	char	*re;
	char	*bf;

	s1_size = 0;
	s2_size = 0;
	if (!s1 || !s2)
		return (NULL);
	while (s1[s1_size])
		s1_size++;
	while (s2[s2_size])
		s2_size++;
	re = malloc(s1_size + s2_size + 1);
	if (!re)
		return (NULL);
	bf = re;
	while (*s1)
		*bf++ = *s1++;
	while (*s2)
		*bf++ = *s2++;
	*bf = '\0';
	return (re);
}
