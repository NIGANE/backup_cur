
#include "get_next_line.h"
/// ---------------- utils
static size_t	ft_strlen(char *s)
{
	size_t	len;

    if (!s)
    {
        return (0);
    }
	len = 0;
	while (*s++)
		len++;
	return (len);
}

static int ft_strchr(char *s, int c)
{
    int	i;
    
    if (!s)
    {
        return (1);
    }
	i = 0;
	while (s[i] && s[i] != c)
    i++;
	if (s[i] == c)
        return (1);
	return (0);
}

static char	*ft_strdup(const char *s)
{
	char	*re;
	size_t	size;
	size_t	i;

	i = 0;
	size = 0;
	if (!s)
		return (NULL);
	while (s[size] && s[size] != '\n')
		size++;

	re = malloc(size + 2);
	if (!re)
		return (NULL);
	while (i < size)
	{
		re[i] = s[i];
		i++;
	}
    re[size] = '\n';
    re[size + 1] = '\0';
	return (re);
}

static char *ft_strjoin(char *s, char *b)
{
    char *re;
    int    i;

    i = 0;
    if (!s && b)
        return (ft_strdup(b));
    if (!b && s)
        return (ft_strdup(s));
    if (!b && !s)
        return (NULL);
    re = malloc(sizeof(ft_strlen(s) + ft_strlen(b) + 1));
    if (!re)
        return (NULL);
    while (*s)
        re[i++] = *s++;
    while (*b)
        re[i++] = *b++;
    re[i] = '\0';
    free(s);
    return (re);
}

char *free_some(char *s)
{
    int size;
    char *bf;
    char *tp;

    if (!s)
        return (NULL);
    size = 0;
    while (s[size])
    {
		size++;
        if (s[size] == '\n')
            break;
    }
    bf = malloc(size - ft_strlen(s) + 1);
    tp = bf;
    while (s[size])
        *tp++ = s[size++];
    *tp = '\0';
    free(s);
    return (bf);
}
/// ---------------- utils


static char *get_line(char *s, int fd)
{
    int size;
    char *bf;

    bf = malloc(BUFFER_SIZE + 1);
    if (!bf)
        return (NULL);
    size = 1;
    while (size >= 1 && !ft_strchr(s, '\n'))
    {
        size = read(fd, bf, BUFFER_SIZE);
        bf[size] = '\0';
        s = ft_strjoin(s, bf);
        if (!s)
            return (NULL);
    }
    free(bf);
    return (bf);
}

char    *get_next_line(int fd)
{
    static char *temp;
    char *re;

    if (fd <= 2)
        return (NULL);
    
    temp = get_line(temp, fd);
    if (!temp)
        return (NULL);
    re = ft_strdup(temp);
    if (!re)
    {
        free(temp);
        return (NULL);
    }
    temp = free_some(temp);
    printf("remaining: %s\n", temp);
    return (re);
}

int main(void)
{
    int fd = open("file_test", O_WRONLY);
    if (fd == -1)
    {
        printf("err while opning file from main func.");
        return 0;
    }
    
    char *s = get_next_line(fd);

    printf("line: %s", s);
}