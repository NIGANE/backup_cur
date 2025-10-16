#include <stdlib.h>
#include <stdio.h>
int     count_mumb(const char *s, char c)
{
    int     count;

    count = 0;
    while (*s)
    {
        while (*s && *s == c)
            s++;
        if (*s == '\0')
            break ;
        if (*s != c)
        {
            while (*s && *s != c)
                s++;
            count++;
        }
    }
    return (count);
}

void    free_arr(char **ar, size_t i)
{
    while (i-- > 0)
        free(ar[i]);
    free(ar);
}

char    *ft_strdup(const char *s, char c)
{
    size_t  t;
    size_t  len;
    char    *re;

    len = 0;
    while (s[len] && s[len] != c)
        len++;
    re = malloc(sizeof(char) * (len + 1));
    if (!re)
        return (NULL);
    t = 0;
    while (len-- > 0)
        re[t++] = *s++;
    re[t] = '\0';
    return (re);
}

char    **ft_split(char const *s, char c)
{
    int     n_mumb;
    char    **re;
    size_t  i;

    i = 0;
    if (!s)
        return (NULL);
    n_mumb = count_mumb(s, c);
    re = malloc(sizeof(char *) * n_mumb);
    if (!re)
        return (NULL);
    while (*s)
    {
        while (*s && *s == c)
            s++;
        if (*s && *s != c)
        {
            re[i] = ft_strdup(s, c);
            if (!re[i])
            {
                free_arr(re, i);
                return (NULL);
            }
            while (*s && *s != c)
                s++;
            i++;
        }
        if (*s == '\0')
            break ;
    }
    return (re);
}