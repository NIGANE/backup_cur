#include "libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>

static char add_one(unsigned int i, char c)
{
	(void)i;
	return (c + 1);
}

int main(void)
{
	printf("=== CHARACTER TESTS ===\n");
	printf("ft_isalpha('A') = %d | expected = %d\n", ft_isalpha('A'), isalpha('A'));
	printf("ft_isdigit('9') = %d | expected = %d\n", ft_isdigit('9'), isdigit('9'));
	printf("ft_isalnum('@') = %d | expected = %d\n", ft_isalnum('@'), isalnum('@'));
	printf("ft_isascii(200) = %d | expected = %d\n", ft_isascii(200), isascii(200));
	printf("ft_isprint(31)  = %d | expected = %d\n", ft_isprint(31), isprint(31));
	printf("ft_tolower('A') = %c | expected = %c\n", ft_tolower('A'), tolower('A'));
	printf("ft_toupper('a') = %c | expected = %c\n", ft_toupper('a'), toupper('a'));
	printf("\n");

	printf("=== STRING TESTS ===\n");
	printf("ft_strlen('Hello') = %zu | expected = %zu\n", ft_strlen("Hello"), strlen("Hello"));

	char *dup = ft_strdup("42");
	printf("ft_strdup('42') = '%s' | expected = '42'\n", dup);
	free(dup);

	printf("ft_strncmp('abc','abd',2) = %d | expected = %d\n", ft_strncmp("abc", "abd", 2), strncmp("abc", "abd", 2));

	printf("ft_strchr('abc','b') = %ld | expected = %ld\n",
		ft_strchr("abc", 'b') - "abc", strchr("abc", 'b') - "abc");

	printf("ft_strrchr('abcabc','b') = %ld | expected = %ld\n",
		ft_strrchr("abcabc", 'b') - "abcabc", strrchr("abcabc", 'b') - "abcabc");

	char d1[10] = "Hi";
	char d2[10] = "Hi";
	printf("ft_strlcpy(dest,'abcd',3) = %zu | expected = 4\n", ft_strlcpy(d1, "abcd", 3));
	printf("ft_strlcat(dest,'All',10) = %zu | expected = %zu\n", ft_strlcat(d2, "All", 10), strlen("Hi") + strlen("All"));

	char *joined = ft_strjoin("Hello ", "World");
	printf("ft_strjoin('Hello ','World') = '%s' | expected = 'Hello World'\n", joined);
	free(joined);

	char *sub = ft_substr("abcdef", 2, 3);
	printf("ft_substr('abcdef',2,3) = '%s' | expected = 'cde'\n", sub);
	free(sub);

	char *trim = ft_strtrim("  hello  ", " ");
	printf("ft_strtrim('  hello  ',' ') = '%s' | expected = 'hello'\n", trim);
	free(trim);

	char *mapi = ft_strmapi("abc", add_one);
	printf("ft_strmapi('abc',+1) = '%s' | expected = 'bcd'\n", mapi);
	free(mapi);
	printf("\n");

	printf("=== MEMORY TESTS ===\n");
	char src[] = "Hello";
	char dest[10];
	ft_memcpy(dest, src, 6);
	printf("ft_memcpy -> dest = '%s' | expected = 'Hello'\n", dest);
	printf("ft_memcmp('abc','abd',2) = %d | expected = %d\n", ft_memcmp("abc", "abd", 2), memcmp("abc", "abd", 2));

	char buf[5] = {1, 2, 3, 4, 5};
	ft_bzero(buf, 5);
	printf("ft_bzero -> buf[0] = %d | expected = 0\n", buf[0]);

	char *p = ft_calloc(3, sizeof(char));
	printf("ft_calloc(3,1) first byte = %d | expected = 0\n", p[0]);
	free(p);
	printf("\n");

	printf("=== ITOA / ATOI TESTS ===\n");
	char *itoa_res = ft_itoa(-12345);
	printf("ft_itoa(-12345) = '%s' | expected = '-12345'\n", itoa_res);
	free(itoa_res);
	printf("ft_atoi('   -42abc') = %d | expected = %d\n", ft_atoi("   -42abc"), atoi("   -42abc"));
	printf("\n");

	printf("=== SPLIT TEST ===\n");
	char **split = ft_split("hello world 42", ' ');
	for (int i = 0; split && split[i]; i++)
		printf("split[%d] = '%s'\n", i, split[i]);
	for (int i = 0; split && split[i]; i++)
		free(split[i]);
	free(split);
	printf("\n");

	printf("=== LINKED LIST TESTS ===\n");
	t_list *lst1 = ft_lstnew("first");
	t_list *lst2 = ft_lstnew("second");
	ft_lstadd_back(&lst1, lst2);
	printf("ft_lstsize = %d | expected = 2\n", ft_lstsize(lst1));
	printf("ft_lstlast = '%s' | expected = 'second'\n", (char *)ft_lstlast(lst1)->content);
	ft_lstclear(&lst1, NULL);
	printf("\n");

	printf("=== FD TESTS (will print on terminal) ===\n");
	ft_putstr_fd("Hello", 1);
	ft_putchar_fd('\n', 1);
	ft_putendl_fd("World", 1);
	ft_putnbr_fd(42, 1);
	ft_putchar_fd('\n', 1);

	printf("\n=== ALL TESTS DONE ===\n");
	return 0;
}