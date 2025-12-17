#include <stdlib.h>


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
void swap(t_stack_node **top);
void rotate(t_stack *stack);
void rev_rotate(t_stack *stack);
void print_stack(t_stack *stack);
t_stack *extract_stack(t_stack *st, int cn, char **av);
int ft_atoi(char *str);
