

#include "libft.h"
#include <stdio.h>
#include <bsd/string.h>
#include <ctype.h>

void print_content(void *content)
{
    printf("%s\n", (char *)content);
}

void *dup_and_x(void *data)
{
    char *s = strdup((char *)data);
    if (!s) return NULL;
    s[0] = 'X';
    return s;
}

void del_content(void *data)
{
    free(data);
}
int main(void)
{

    // printf("ft_isalpha('a') = %d\n", ft_isalpha('a'));
    // printf("ft_isdigit('0') = %d\n", ft_isdigit('0'));
    // printf("ft_isalnum('9') = %d\n", ft_isalnum('9'));
    // printf("ft_isascii(127) = %d\n", ft_isascii(127));
    // printf("ft_isprint(' ') = %d\n", ft_isprint(' '));
    // printf("ft_toupper('a') = %c\n", ft_toupper('a'));
    // printf("ft_tolower('A') = %c\n", ft_tolower('A'));

    // char str1[20] = "Hello";
    // char str2[20] = "World";
    // printf("ft_strlen(\"%s\") = %zu\n", str1, ft_strlen(str1));
    // printf("ft_strlcpy(str1, str2, 6) = %zu, str1 = %s\n", ft_strlcpy(str1, str2, 6), str1);
    // printf("ft_strlcat(str1, \"!!!\", 20) = %zu, str1 = %s\n", ft_strlcat(str1, "!!!", 20), str1);
    // printf("ft_strchr(\"abc\", 'b') = %s\n", ft_strchr("abc", 'b'));
    // printf("ft_strrchr(\"abcab\", 'b') = %s\n", ft_strrchr("abcab", 'b'));
    // printf("ft_strncmp(\"abc\", \"abd\", 2) = %d\n", ft_strncmp("abc", "abd", 2));
    // printf("ft_strnstr(\"hello world\", \"world\", 11) = %s\n", ft_strnstr("hello world", "world", 11));
    // char *dup = ft_strdup("duplicate me");
    // printf("ft_strdup(\"duplicate me\") = %s\n", dup);
    // free(dup);
    
    // char mem[] = "123456789";
    // ft_memset(NULL, 'A', 10);
    // memset(mem, 's', 2);
    // printf("ft_memset(mem, 'A', 10) = %.*s\n", 10, mem);
    // ft_bzero(NULL);
    // bzero(NULL, 10);
    // printf("ft_bzero(mem, 10) = %.*s\n", 10, mem);
    
    
    // char src[10] = "";
    // ft_memcpy(src, mem, 7);
    // memcpy(NULL, src, 6);
    // printf("ft_memcpy(src, src, 6) = %s\n", src);
    // char dest[10] = "12345";
    // ft_memmove(mem + 1, mem, sizeof(mem));
    // printf("ft_memmove(dest, mem, 6) = %s\n", mem);
    // printf("ft_memchr(mem, '3', 6) = %s\n", (char *)ft_memchr(mem, '5', 5));
    // printf("ft_memcmp(mem, dest, 6) = %d\n", ft_memcmp(mem, dest, 6));
    
    
    // printf("ft_atoi(\"123\") = %d\n", ft_atoi("0"));
    // char *calloc_test = ft_calloc(5, sizeof(char));
    // for (int i = 0; i < 5; i++)
    // printf("%d ", calloc_test[i]);
    // printf("\n");
    // free(calloc_test);
    printf("ft_itoa(4567) = %s\n", ft_itoa(00));
    
    
    
    
    // char *substr = ft_substr(NULL, 6, 5);
    // printf("ft_substr(\"Hello World\", 6, 5) = %s\n", substr);
    // free(substr);
    
    // char *join = ft_strjoin(NULL, NULL);
    // printf("ft_strjoin(\"Hello\", \"Libft\") = %s\n", join);
    // free(join);
    
    // char *trim = ft_strtrim("agsfafbc", " ");
    // printf("ft_strtrim(\"  abc  \", \" \") = %s\n", trim);
    // free(trim);
    
    // char **split = ft_split(NULL, ' ');
    // printf("ft_split(\"a b c\", ' ') =");
    // if (split == NULL)
    //     printf(" NULL\n");
    // else
    // {
        // for (int i = 0; split[i]; i++)
        // {
            //         printf(" [%s]", split[i]);
            //         free(split[i]);
            //     }
            //     printf("\n");
            //     free(split);
        // }
        
        // ft_putchar_fd('X', 1);
        // ft_putstr_fd("", 1);
        // ft_putendl_fd(NULL, 1);
        // ft_putnbr_fd(42, 1);
        ////////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////


     printf("=== BONUS TESTS START ===\n");

    // 1. Create nodes
    // t_list *a = ft_lstnew(strdup("one"));
    // t_list *b = ft_lstnew(strdup("two"));
    // t_list *c = ft_lstnew(strdup("three"));

    // print_content(a->content);
    // print_content(b->content);
    // print_content(c->content);

    // // 2. Add front
    // ft_lstadd_front(&a, b);
    // ft_lstadd_front(&a, c);
    // printf("List after add_front:\n");
    // ft_lstiter(a, print_content);
    
    // // 3. List size
    // printf("List size: %d\n", ft_lstsize(a));
    
    // // 4. Last element
    // t_list *last = ft_lstlast(a);
    // printf("Last: %s\n", (char *)last->content);
    
    // // 5. Add back
    // ft_lstadd_back(&a, ft_lstnew(strdup("four")));
    // printf("After add_back:\n");
    // ft_lstiter(a, print_content);
    
    // // 6. Map (create new list)
    // t_list *mapped = ft_lstmap(a, dup_and_x, del_content);
    // printf("Mapped list (X start):\n");
    // ft_lstiter(mapped, print_content);
    // ft_lstiter(a, print_content);
    
    // // 7. Delete one node
    // ft_lstdelone(mapped->next->next, del_content);
    // mapped->next->next = NULL;
    // printf("After delone:\n");
    // ft_lstiter(mapped, print_content);

    // // 8. Clear both lists
    // ft_lstclear(&a, del_content);
    // ft_lstclear(&mapped, del_content);

    // printf("=== BONUS TESTS END ===\n");
    return 0;
}    
