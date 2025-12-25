/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sta1.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:45:31 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/25 21:54:01 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# ifndef STA1_H
#define STA1_H
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

#define CHUNK_SIZE 

typedef struct s_stack_node
{
    int data;
    int index;
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
int find_smallest(t_stack *stack);
int find_largest(t_stack *stack);
int check(t_stack *stack);
t_stack_node *find(int data, t_stack *stack);
void sort_arr(int *arr, int size);
void to_arr(t_stack *a, int *arr);
t_stack *indexing(t_stack *a);
void movetop_a(t_stack *st, int index);
void movebottom_a(t_stack *st, int index);
void movetop_b(t_stack *st, int index);
void movebottom_b(t_stack *st, int index);
void move_in_a(t_stack *st, int a, int b);
void sort_to_b(t_stack *a, t_stack *b ,int chunk_num);
void chunking(t_stack *a, t_stack *b, int low, int size);

void sort(t_stack *a, t_stack *b);
void sort_3(t_stack *a);
void sort_4(t_stack *a, t_stack *b);
void sort_5(t_stack *a, t_stack *b);
void sort_6_100(t_stack *a, t_stack *b);

t_stack *extract_stack(t_stack *st, int cn, char **av);
long ft_atoi(char *str);
char	**ft_split(char const *s, char c);
void free_split_arr(char **arr);
int ft_putstr(char *s);
size_t ft_strlen(char *s);

#endif