# ifndef STA1_H
#define STA1_H
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>


typedef struct s_stack_node
{
    int data;
    struct s_stack_node *next;

} t_stack_node;


typedef struct stack
{
    t_stack_node *top;
    int size;
} t_stack;


t_stack *stack_init();
void free_stack(t_stack *stack);
t_stack_node *create_stack(int data);
t_stack *push(t_stack *stack, int data);
t_stack_node *pop(t_stack *stack);
void stack_rev(t_stack_node **top);
int in_stack(int a, t_stack *st);
void swap(t_stack_node **top);
void rotate(t_stack *stack);
void rev_rotate(t_stack *stack);
void print_stack(t_stack *stack);

void sort(t_stack *a, t_stack *b);

t_stack *extract_stack(t_stack *st, int cn, char **av);
long ft_atoi(char *str);
char	**ft_split(char const *s, char c);
void free_split_arr(char **arr);
int ft_putstr(char *s);
size_t ft_strlen(char *s);

#endif