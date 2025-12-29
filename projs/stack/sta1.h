/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sta1.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 21:45:31 by amerkht           #+#    #+#             */
/*   Updated: 2025/12/29 22:43:49 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STA1_H
# define STA1_H
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_stack_node
{
	int					data;
	int					cp;
	struct s_stack_node	*target_node;
	struct s_stack_node	*next;
	int					index;
}						t_stack_node;
typedef struct s_stack
{
	t_stack_node		*top;
	int					size;
}						t_stack;
void					movebottom_b(t_stack *st, int index);
void					movetop_b(t_stack *st, int index);
void					movebottom_a(t_stack *st, int index);
void					movetop_a(t_stack *st, int index);
void					print_stack(t_stack *st);
void					update_target_node(t_stack *a, t_stack *b);
t_stack					*stack_init(void);
void					free_stack(t_stack *stack);
t_stack_node			*create_stack(int data);
t_stack					*push(t_stack *stack, int data);
t_stack_node			*pop(t_stack *stack);
void					stack_rev(t_stack_node **top);
int						in_stack(int a, t_stack *st);
void					swap(t_stack_node **top);
void					rotate(t_stack *stack);
void					rev_rotate(t_stack *stack);
void					print_stack(t_stack *stack);
int						find_smallest(t_stack *stack);
int						find_largest(t_stack *stack);
int						check(t_stack *stack);
t_stack_node			*find(int data, t_stack *stack);
void					sort_arr(int *arr, int size);
void					to_arr(t_stack *a, int *arr);
t_stack					*indexing(t_stack *a);
void					movetop_a(t_stack *st, int index);
void					movebottom_a(t_stack *st, int index);
void					movetop_b(t_stack *st, int index);
void					movebottom_b(t_stack *st, int index);
void					move_in_a(t_stack *st, t_stack *st2, int a, int b);
void					sort_to_b(t_stack *a, t_stack *b, int chunk_num);
void					chunking(t_stack *a, t_stack *b, int low, int size);
t_stack_node			*find_chepest(t_stack *a, t_stack *b);
void					update_target_node(t_stack *a, t_stack *b);
int						get_target_cost(t_stack_node *node, t_stack *st);
int						get_cost(t_stack_node *node, t_stack *st);
t_stack_node			*get_min_target(t_stack *st);
void					move_chepest(t_stack *a, t_stack *b,
							t_stack_node *target);
void					set_current_pos(t_stack *a, t_stack *b);
void					sort(t_stack *a, t_stack *b);
void					sort_3(t_stack *a);
void					sort_4(t_stack *a, t_stack *b);
void					sort_5(t_stack *a, t_stack *b);
void					sort_6_100(t_stack *a, t_stack *b);
t_stack					*extract_stack(t_stack *st, int cn, char **av);
long					ft_atoi(char *str);
char					**ft_split(char const *s, char c);
void					free_split_arr(char **arr);
int						ft_putstr(char *s);
size_t					ft_strlen(char *s);
int						abs(int n);
#endif