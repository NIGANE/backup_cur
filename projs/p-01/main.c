#include "libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>

/* Helper macro to print test results */
#define TEST(name, expr, expected_fmt, expected_val) \
    do { \
        printf("%-15s => ", name); \
        printf("Result: " expected_fmt " | Expected: " expected_fmt "\n", (expr), (expected_val)); \
    } while (0)

/* Helper for string comparison */
#define TEST_STR(name, expr, expected) \
    do { \
        printf("%-15s => ", name); \
        char *res = (expr); \
        printf("Result: \"%s\" | Expected: \"%s\"\n", res, expected); \
        free(res); \
    } while (0)

int main(void)
{
    printf("=== BASIC CHARACTER TESTS ===\n");
    TEST("ft_isalpha", ft_isalpha('A'), "%d", isalpha('A'));
    TEST("ft_isdigit", ft_isdigit('9'), "%d", isdigit('9'));
    TEST("ft_isalnum", ft_isalnum('@'), "%d", isalnum('@'));
    TEST("ft_isascii", ft_isascii(200), "%d", isascii(200));
    TEST("ft_isprint", ft_isprint(31), "%d", isprint(31));
    TEST("ft_tolower", ft_tolower('A'), "%c", tolower('A'));
    TEST("ft_toupper", ft_toupper('a'), "%c", toupper('a'));
    puts("");

    printf("=== STRING TESTS ===\n");
    TEST("ft_strlen", ft_strlen("Hello"), "%zu", strlen("Hello"));
    TEST_STR("ft_strdup", ft_strdup("42"), "42");
    TEST("ft_strncmp", ft_strncmp("abc", "abd", 2), "%d", strncmp("abc", "abd", 2));
    TEST("ft_strchr", (size_t)(ft_strchr("abc", 'b') - "abc"), "%zu", (size_t)(strchr("abc", 'b') - "abc"));
    TEST("ft_strrchr", (size_t)(ft_strrchr("abcabc", 'b') - "abcabc"), "%zu", (size_t)(strrchr("abcabc", 'b') - "abcabc"));
    TEST("ft_strlcpy", ft_strlcpy((char[10]){0}, "abcd", 3), "%zu", 4);
    TEST("ft_strlcat", ft_strlcat((char[10]){"Hi"}, "All", 10), "%zu", strlen("Hi") + strlen("All"));
    TEST_STR("ft_strjoin", ft_strjoin("Hello ", "World"), "Hello World");
    TEST_STR("ft_substr", ft_substr("abcdef", 2, 3), "cde");
    TEST_STR("ft_strtrim", ft_strtrim("  hello  ", " "), "hello");
    TEST_STR("ft_strmapi", ft_strmapi("abc", [](unsigned int i, char c){return c + 1;}), "bcd");
    puts("");

    printf("=== MEMORY TESTS ===\n");
    char src[] = "Hello";
    char dest[10];
    ft_memcpy(dest, src, 6);
    TEST("ft_memcmp", ft_memcmp("abc", "abd", 2), "%d", memcmp("abc", "abd", 2));

    char buf[5] = {1, 2, 3, 4, 5};
    ft_bzero(buf, 5);
    TEST("ft_bzero", buf[0], "%d", 0);

    char *p = ft_calloc(3, sizeof(char));
    TEST("ft_calloc", p[0], "%d", 0);
    free(p);
    puts("");

    printf("=== ITOA / ATOI TESTS ===\n");
    TEST_STR("ft_itoa", ft_itoa(-12345), "-12345");
    TEST("ft_atoi", ft_atoi("   -42abc"), "%d", atoi("   -42abc"));
    puts("");

    printf("=== SPLIT TEST ===\n");
    char **split = ft_split("hello world 42", ' ');
    for (int i = 0; split && split[i]; i++)
        printf("split[%d] = \"%s\"\n", i, split[i]);
    puts("");

    printf("=== LINKED LIST TESTS ===\n");
    t_list *lst1 = ft_lstnew("first");
    t_list *lst2 = ft_lstnew("second");
    ft_lstadd_back(&lst1, lst2);
    printf("lstsize: %d\n", ft_lstsize(lst1));
    printf("lstlast: %s\n", (char *)ft_lstlast(lst1)->content);
    ft_lstclear(&lst1, NULL);
    puts("");

    printf("=== FILE DESCRIPTOR TESTS (prints to terminal) ===\n");
    ft_putstr_fd("Hello", 1);
    ft_putchar_fd('\n', 1);
    ft_putendl_fd("World", 1);
    ft_putnbr_fd(42, 1);
    ft_putchar_fd('\n', 1);

    puts("\n=== ALL TESTS DONE ===");
    return 0;
}
