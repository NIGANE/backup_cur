

#include "get_line.h"
#include "../stack/sta1.h"

size_t	valid_len(char *s)
{
	size_t	len;

	len = 0;
	if (!s)
		return (0);
	while (s[len] && s[len] != '\n')
		len++;
	if (s[len] == '\n')
		len++;
	return (len);
}

int	ft_strchr(char *s, int c)
{
	int	i;

	if (!s)
	{
		return (0);
	}
	i = 0;
	while (s[i] && s[i] != c)
		i++;
	if (s[i] == c)
		return (1);
	return (0);
}

char	*extract_line(const char *s)
{
	char	*re;
	size_t	size;
	size_t	i;

	i = 0;
	if (!s)
		return (NULL);
	size = valid_len((char *)s);
	re = malloc(size + 1);
	if (!re)
		return (NULL);
	while (i < size)
	{
		re[i] = s[i];
		i++;
	}
	re[size] = '\0';
	return (re);
}

char	*ft_strjoin(char *s, char *b)
{
	char	*re;
	int		i;
	char	*temp;

	i = 0;
	if (!s && b)
		s = "";
	if (!b && s)
		b = "";
	if (!b && !s)
		return (NULL);
	re = malloc(ft_strlen(s) + ft_strlen(b) + 1);
	if (!re)
		return (NULL);
	temp = s;
	while (*temp)
		re[i++] = *temp++;
	temp = b;
	while (*temp)
		re[i++] = *temp++;
	re[i] = '\0';
	return (re);
}
