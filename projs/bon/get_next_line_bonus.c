#include "../man/get_next_line.h"


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

	bf = malloc(BUFFER_SIZE + 1);
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

char	*get_next_line_bonus(int fd)
{
	static char	**temp;
	char		*re;

	if (fd < 0 || (fd >= 1 && fd <= 2))
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
