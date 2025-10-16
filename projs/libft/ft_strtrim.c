/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 10:17:04 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 10:20:15 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	in_string(char c, const char *s)
{
	while (*s)
	{
		if (*s == c)
			return (1);
		s++;
	}
	return (0);
}

int	valid_s(const char *s, const char *set, int fl_len)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (s[i] && in_string(s[i], set))
		i++;
	while (fl_len > 0 && s[fl_len - 1] && in_string(s[fl_len - 1], set))
		fl_len--;
	if (fl_len - i < 0)
		return (0);
	return (fl_len - i);
}

char	*empty_string(void)
{
	char	*re;

	re = malloc(1);
	if (!re)
		return (NULL);
	re[0] = '\0';
	return (re);
}

char	*ft_strtrim(const char *s, const char *set)
{
	int		size;
	int		full_len;
	char	*re;
	char	*bf;

	if (!s || !set)
		return (NULL);
	full_len = 0;
	while (s[full_len])
		full_len++;
	if (full_len == 0)
		return (empty_string());
	size = valid_s(s, set, full_len);
	re = malloc(size + 1);
	if (!re)
		return (NULL);
	while (*s && in_string(*s, set))
		s++;
	bf = re;
	while (*s && size-- > 0)
		*bf++ = *s++;
	*bf = '\0';
	return (re);
}
