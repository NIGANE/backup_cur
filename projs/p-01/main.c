#include "libft/libft.h"
#include <stdio.h>
#include <bsd/string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>

static char add_one(unsigned int i, char c)
{
	(void)i;
	return (c + 1);
}

static void	*printed(void *content)
{
	printf("Node content: %s\n", (char *)content);
	return (content);
}
static void	del(void *content)
{
	free(content);
}

static void	*modify(void *content)
{
	char *str = (char *)content;
	char *new_str = ft_memset(str, 'X', 1);
	return (new_str);
}
int main(void)
{
	// printf("=== CHARACTER TESTS ===\n");
	// printf("ft_isalpha('A') = %d | expected = %d\n", ft_isalpha('A'), isalpha('A'));
	// printf("ft_isdigit('9') = %d | expected = %d\n", ft_isdigit('9'), isdigit('9'));
	// printf("ft_isalnum('@') = %d | expected = %d\n", ft_isalnum('@'), isalnum('@'));
	// printf("ft_isascii(200) = %d | expected = %d\n", ft_isascii(200), isascii(200));
	// printf("ft_isprint(31)  = %d | expected = %d\n", ft_isprint(31), isprint(31));
	// printf("ft_tolower('A') = %c | expected = %c\n", ft_tolower('A'), tolower('A'));
	// printf("ft_toupper('a') = %c | expected = %c\n", ft_toupper('a'), toupper('a'));
	// printf("\n");

	// printf("=== STRING TESTS ===\n");
	// printf("ft_strlen('Hello') = %zu \n", ft_strlen("NULL"));
	// printf("expected = %zu\n",  strlen("NULL"));
	// printf("\n\n");

	// char *strdup_test = "";
	// char *dup_std = strdup(strdup_test);
	// char *dup_ft = ft_strdup(strdup_test);
	// printf("ft_strdup('42') = '%s' | expected = %s\n", dup_ft, dup_std);
	// free(dup_ft);
	// free(dup_std);
 	// printf("\n\n");

	// printf("ft_strncmp('abc','abd',2) = %d | expected = %d\n", ft_strncmp("NULL", NULL, 0), strncmp("NULL", NULL, 0));
	// printf("\n\n");

	// printf("ft_strchr('abc','b') = %s | expected = %s\n", ft_strchr("abc", 'b'), strchr("abc", 'b'));
	// printf("\n\n");

	// printf("ft_strrchr('abcabc','b') = %s | expected = %s\n", ft_strrchr("abcabc", 'b'), strrchr("abcabc", 'b'));
	// printf("\n\n");

	// char d1[10] = "Hi";
	// char d2[10] = "Hi";
	// printf("ft_strlcpy(dest,'abcd',3) = %zu | expected = %zu\n", ft_strlcpy(d1, "abcd", 3), strlcpy(d1, "abcd", 3));
	// printf("dest after ft_strlcpy: '%s'\n", d1);
	// printf("ft_strlcat(dest,'All',10) = %zu \n", ft_strlcat(d2, "All", 10));
	// printf("ft_strlcat(dest,'All',10) = %zu \n", strlcat(d2, "All", 10));
	// printf("dest after ft_strlcat: '%s'\n", d2);
	// printf("\n\n");
	
	
	// char *joined = ft_strjoin("Hello ", "World");
	// printf("ft_strjoin('Hello ','World') = '%s' | expected = 'Hello World'\n", joined);
	// free(joined);
	// printf("\n\n");
	
	// char *sub = ft_substr(NULL, 4, 3);
	// printf("ft_substr('abcdef',4,3) = '%s' | expected = 'ef'\n", sub);
	// free(sub);
	// printf("\n\n");
	
	// char *trim = ft_strtrim("hello world ()+ negane   *(++_)", "+_)(*&^)");
	// printf("ft_strtrim('hello world ()+ negane   *(++_)', '+_)(*&^) = '%s' | expected = 'hello world ()+ negane   *(++_)' \n", trim);
	// free(trim);
	// printf("\n\n");
	
	// char *mapi = ft_strmapi("abc", add_one);
	// printf("ft_strmapi('abc',+1) = '%s' | expected = 'bcd'\n", mapi);
	// free(mapi);
	// printf("\n\n");
	
	printf("=== MEMORY TESTS ===\n");
	
	// char src[] = "Hello";
	// char dest[10];
	// ft_memcpy(dest, src, 6);
	// printf("ft_memcpy -> dest = '%s' | expected = 'Hello'\n", dest);
	// printf("ft_memcmp('abc','abd',2) = %d | expected = %d\n", ft_memcmp("abc", "abd", 2), memcmp("abc", "abd", 2));
	// printf("\n\n");
	
	// char buf[5] = {1, 2, 3, 4, 5};
	// ft_bzero(buf, 5);
	// printf("ft_bzero -> buf[0] = %d | expected = 0\n", buf[0]);
	// printf("\n\n");

	// char *p = ft_calloc(3, sizeof(char));
	// printf("ft_calloc(3,1) first byte = %d | expected = 0\n", p[0]);
	// free(p);
	// printf("\n");

	// printf("=== ITOA / ATOI TESTS ===\n");
	// char *itoa_res = ft_itoa(-2147483648);
	// printf("ft_itoa(-2147483648) = '%s' | expected = '-2147483648'\n", itoa_res);
	// free(itoa_res);
	// printf("ft_atoi('   -42abc') = %d | expected = %d\n", ft_atoi("214748364855"), atoi("214748364855"));
	// printf("\n");

	// printf("=== SPLIT TEST ===\n");
	// char **split = ft_split("hello world 42", ' ');
	// for (int i = 0; split && split[i]; i++)
	// 	printf("split[%d] = '%s'\n", i, split[i]);
	// for (int i = 0; split && split[i]; i++)
	// 	free(split[i]);
	// free(split);
	// printf("\n");

	printf("=== LINKED LIST TESTS ===\n");
	t_list *lst = NULL;
	t_list *lst1 = ft_lstnew(ft_strdup("first"));
	t_list *lst2 = ft_lstnew(ft_strdup("second"));
	ft_lstadd_front(&lst, lst2);
	ft_lstadd_front(&lst, lst1);

	// printf("ft_lstsize = %d | expected = 2\n", ft_lstsize(lst1));
	// printf("ft_lstlast = '%s' | expected = 'second'\n", (char *)ft_lstlast(lst1)->content);


	t_list *lst_new = ft_lstmap(lst, (void *)modify, del);

	ft_lstiter(lst_new, (void *)printed);
	ft_lstiter(lst1, (void *)printed);
	// ft_lstclear(&lst_new, del);
	// ft_lstclear(&lst1, del);
	printf("\n");

	// printf("=== FD TESTS (will print on terminal) ===\n");
	// ft_putstr_fd("Hello", 1);
	// ft_putchar_fd('\n', 1);
	// ft_putendl_fd("World", 1);
	// ft_putnbr_fd(42, 1);
	// ft_putchar_fd('\n', 1);

	printf("\n=== ALL TESTS DONE ===\n");
	return 0;
}