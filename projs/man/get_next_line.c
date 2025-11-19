/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 15:52:49 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/19 10:45:26 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	src_len;

	src_len = 0;
	while (src[src_len])
		src_len++;
	if (dstsize <= 0)
		return (src_len);
	dstsize -= 1;
	while (*src && dstsize-- > 0)
		*dst++ = *src++;
	*dst = '\0';
	return (src_len);
}

static char	*free_some(char *s)
{
	int		size;
	char	*bf;

	if (!s)
		return (NULL);
	size = 0;
	while (s[size])
	{
		if (s[size++] == '\n')
			break ;
	}
	if ((size_t)size == ft_strlen(s))
	{
		free(s);
		return (NULL);
	}
	bf = malloc(ft_strlen(s) - size + 1);
	if (!bf)
	{
		free(s);
		return (NULL);
	}
	ft_strlcpy(bf, s + size, ft_strlen(s) - size + 1);
	free(s);
	return (bf);
}

static char	*nothing(char *s, char *bf, int size)
{
	if (size == 0)
	{
		free(bf);
		return (s);
	}
	if (size == -1)
	{
		free(bf);
		free(s);
	}
	return (NULL);
}

static char	*get_line(char *s, int fd)
{
	int		size;
	char	*bf;
	char	*tp;

	bf = (char *) malloc((size_t)(BUFFER_SIZE) + 1);
	if (!bf)
		return (NULL);
	size = 1;
	while (size >= 1 && !ft_strchr(s, '\n'))
	{
		size = read(fd, bf, BUFFER_SIZE);
		if (size == -1 || size == 0)
			return (nothing(s, bf, size));
		bf[size] = '\0';
		tp = s;
		s = ft_strjoin(s, bf);
		if (!s)
			return (nothing(tp, bf, -1));
		free(tp);
	}
	free(bf);
	return (s);
}

char	*get_next_line(int fd)
{
	static char	*temp;
	char		*re;

	if (fd < 0)
		return (NULL);
	temp = get_line(temp, fd);
	if (!temp)
		return (NULL);
	re = extract_line(temp);
	if (!re)
	{
		free(temp);
		return (NULL);
	}
	temp = free_some(temp);
	return (re);
}


#include <stdio.h>
int main(void)
{
	int fd;
	fd = open("file", O_RDONLY);
	if (fd < 0)
	{
		printf("err");
		return 1;
	}
	
	char *line = get_next_line(fd);
	
	while (line)
	{
		printf("%s", line);
		free(line);
		line = get_next_line(fd);
	}
	close(fd);
}
