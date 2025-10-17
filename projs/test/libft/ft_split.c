/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 14:00:32 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/16 14:00:36 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	count_mumb(const char *s, char c)
{
	int	count;

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

char	**free_arr(char **ar, size_t i)
{
	while (i-- > 0)
		free(ar[i]);
	free(ar);
	ar = NULL;
	return (ar);
}

char	*ft_strdup(const char *s, char c)
{
	size_t	t;
	size_t	len;
	char	*re;

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

char	**ft_split(char const *s, char c)
{
	char	**re;
	size_t	i;

	i = 0;
	if (!s)
		return (NULL);
	re = malloc(sizeof(char *) * (count_mumb(s, c) + 1));
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
				return (free_arr(re, i));
			while (*s && *s != c)
				s++;
			i++;
		}
	}
	re[i] = NULL;
	return (re);
}

#include <stdio.h>
int main(void)
{
	char	**res;
	size_t	i;

	res = ft_split("Hello,,World,,This,is,a,test", ',');
	if (!res)
		return (1);
	i = 0;
	while (res[i])
	{
		printf("res[%zu]: %s\n", i, res[i]);
		free(res[i]);
		i++;
	}
	free(res);

	printf("-----\n");
	res = ft_split("This is a test", ',');
	if (!res)
		return (1);
	i = 0;
	while (res[i])
	{
		printf("res[%zu]: %s\n", i, res[i]);
		free(res[i]);
		i++;
	}
	free(res);

	printf("-----\n");
	res = ft_split("", ',');
	if (!res)
		return (1);
	i = 0;
	while (res[i])
	{
		printf("res[%zu]: %s\n", i, res[i]);
		free(res[i]);
		i++;
	}
	free(res);


	printf("-----\n");
	res = ft_split(NULL, ',');
	if (!res)
		return (1);
	i = 0;
	while (res[i])
	{
		printf("res[%zu]: %s\n", i, res[i]);
		free(res[i]);
		i++;
	}
	free(res);
	return (0);
}