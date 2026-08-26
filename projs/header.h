/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   header.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/23 11:00:48 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/26 10:56:59 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>

typedef struct s_dongle		t_dongle;
typedef struct s_env		t_env;
typedef struct s_coder		t_coder;
typedef struct s_edf_node	t_edf_node;
typedef struct s_heap_edf	t_edf_heap;
typedef struct s_node		t_node;

typedef struct s_dongle
{
	int						id;
	int						available;
	int						ready_to_use;
	pthread_mutex_t			dongle_lock;
	long					last_use;
	t_env					*env;
}							t_dongle;

typedef struct s_env
{
	long					req;
	int						nb_coders;
	long					t_compile;
	long					t_debug;
	long					t_refactore;
	long long				t_burn_out;
	int						required_compiles;
	long					t_cooldown;
	int						running;
	int						start_simulation;
	long					start_time;
	int						stop_simulation;
	long					total_compiles;
	long					target_compiles;
	pthread_t				monitor_id;
	pthread_cond_t			monitor_cond;
	t_node					*fifo;
	t_edf_heap				*heap;
	t_coder					*coders;
	t_dongle				*dongles;
	pthread_mutex_t			env_lock;
	pthread_mutex_t			print_lock;
}							t_env;

typedef struct s_coder
{
	int						id;
	pthread_t				thread_id;
	int						compiles_count;
	int						req_compiles;
	long long				last_compile_time;
	int						ready;
	t_dongle				*left_dongle;
	t_dongle				*right_dongle;
	pthread_cond_t			cond;
	t_env					*env;
}							t_coder;

typedef struct s_edf_node
{
	long					id;
	t_coder					*data;
	long long				deadline;
}							t_edf_node;

typedef struct s_heap_edf
{
	t_edf_node				**array;
	int						size;
	int						capacity;
}							t_edf_heap;

typedef struct s_node
{
	int						id;
	void					*data;
	struct s_node			*next;
}							t_node;

//  fifo.c
void						ft_free(t_node *fifo);
t_node						*ft_create(void *data);
t_node						*ft_insert(void *data, t_node *fifo);
t_node						*ft_pop(t_node **fifo);
int							ft_len(t_node *head);

//  heap.c
t_edf_heap					*edf_heap_init(int capacity);
t_edf_node					*edf_node_create(t_coder *coder);
t_edf_heap					*edf_heap_push(t_edf_heap *heap, t_coder *coder);
t_edf_node					*edf_heap_pop(t_edf_heap *heap);

//  heap2.c
void						swap(t_edf_node *a, t_edf_node *b);
int							check_priority(t_edf_node *a, t_edf_node *b);
void						heapify(t_edf_heap *h, int i);

//  helpers.c.c
int							fifo_full(t_env *env);
int							heap_full(t_env *heap);
int							int_statics(char **av, t_env *env);

//  clean.c
void						clean_env(t_env *env);
void						free_threads_mutexes(t_env *env);
int							compiles_end(t_env *env);
void						edf_heap_free(t_edf_heap *heap);
void						edf_node_free(t_edf_node *node);

//  schedular_management.c
void						request_ticket(t_coder *coder);
t_coder						*whos_next(t_env *env);
void						grab_ticket(t_env *env);
int							in_queue(t_coder *coder);
int							lunch_up(t_env *env);

//  simulation.c
void						*monitor(void *arg);
void						monitor_body(t_env *env);
void						*routine(void *arg);
void						routine_body(t_coder *coder);

//  burn_out_protocol.c
void						check_burn_out(t_env *env);
void						burned_out(t_coder *coder, long long flag);
t_env						*wake_all(t_env *env);

//  time.c
void						sleep_coder(t_coder *coder);
long long					current_time_ms(void);
long long					timestamp(long long start);
void						suspend(long s);

//  coder_actions.c
void						compile(t_coder *coder);
void						debug(t_coder *coder);
void						refactor(t_coder *coder);
int							in_heap(t_coder *coder);
void						_log(char *s, long long time, t_coder *coder);

//  resources_management.c
int							lock(pthread_mutex_t *_lock);
int							unlock(pthread_mutex_t *_lock);
int							grab_dongles(t_coder *coder);
void						cooldown(t_env *env, t_dongle *left,
								t_dongle *right);
void						leave_dongles(t_coder *coder);

//  parsing.c
int							extract_args(int ac, char **av);
int							is_number(char *s);
void						usage_message(const char *s);

//  init.c
t_env						*init_env(char **av);
t_dongle					*init_dongles(t_env *env);
t_coder						*init_coders(t_env *env);
int							init_threads(t_env *env);
int							init_mutexes(t_env *env);

//  main.c
int							ft_resources(t_coder *coder);
int							odd(int a);
int							main(int ac, char **av);
