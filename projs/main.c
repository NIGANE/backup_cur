/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/07/23 16:26:50 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "./header.h"

int in_queue(coder_t *coder);
void _log(char *s, env_t *env)
{
    if (!env)
    {
        printf("%s", s);
        return;
    }
    lock(&(env->print_lock));
    printf("%s", s);
    unlock(&(env->print_lock)); 
}
int compiles_end(env_t *env)
{
    coder_t *coder;
    int i;

    i = 0;
    coder = NULL;
    while (i < env->nb_coders)
    {
        coder = &(env->coders[i]);
        if (coder->compiles_count < coder->req_compiles)
            return (0);
        i++;
    }
    return (1);
}
int is_burn_out(env_t *env)
{
    coder_t *coder;
    int i;
    
    i = 0;
    coder = NULL;
    while (i < env->nb_coders)
    {
        coder = &(env->coders[i]);
        if (timestamp(coder->last_compile_time) >= coder->env->t_burn_out)
            return (printf("[%d] burns out\n", coder->id), 1);
        i++;
    }
    return (0);
}

int len(node_t *head)
{
    int re;
    if (!head)
        return (0);
    re = 0;
    while (head)
    {
        re++;
        head = head->next;
    }
    return (re);
}

void sleep_coder(coder_t *coder)
{
    pthread_cond_wait(&(coder->cond), &(coder->env->env_lock));
}

long long current_time_ms(void)
{
    struct timeval tv;

    gettimeofday(&tv, NULL);

    return (long long)tv.tv_sec * 1000 + tv.tv_usec / 1000;
}
int timestamp(long long start)
{
    return (current_time_ms() - start);
}

void suspend(long s)
{
    usleep(s * 1000);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

int validate_args(char **av, int st, int len)
{
    int i;

    i = st;
    while (i < 8)
    {
        if (!is_positive_number(av[i]))
            return (0);
        i++;
    }
    return (1);
}
int lock(pthread_mutex_t *_lock)
{
    return pthread_mutex_lock(_lock);
}
int unlock(pthread_mutex_t *_lock)
{
    return pthread_mutex_unlock(_lock);
}
int extract_args(int ac, char **av)
{
    env_t *env;

    if (!validate_args(av, 1, ac))
        return (printf("error validating args"), 0);
    if (!ft_atoi(av[1]) || !ft_atoi(av[2])
        || !ft_atoi(av[3])
        || !ft_atoi(av[4]) || !ft_atoi(av[5])
        || !ft_atoi(av[6]) || !ft_atoi(av[7]))
        return (0);
    if (ft_strcmp(av[8], "edf") && ft_strcmp(av[8], "fifo"))
        return (0);
    return (1);
}
void request_ticket(coder_t *coder)
{
    lock(&(coder->env->print_lock));
    printf("[%d] make request\n", coder->id);
    unlock(&(coder->env->print_lock));
    coder->env->fifo = ft_insert(coder, coder->env->fifo);
}

int my_turn(int id, env_t *env)
{
    if (!(env->fifo))
        return (0);
    return *(int *)env->fifo->data == id;
}

int whos_next(env_t *env)
{
    return (*(int *) env->fifo->data);
}

void grab_ticket(env_t *env)
{
    ft_pop(&(env->fifo));
}

int grab_dongles(coder_t *coder)
{
    return (0);
    if (coder->left_dongle->is_available && coder->right_dongle->is_available)
    {
        lock(&(coder->left_dongle->dongle_lock));
        lock(&(coder->right_dongle->dongle_lock));
        lock(&(coder->env->print_lock));
        printf("[%d] grab_dongles\n", coder->id);
        unlock(&(coder->env->print_lock));

        coder->left_dongle->is_available = 0;
        coder->right_dongle->is_available = 0;
        
        return (1);
    }
    return (0);
}

void leave_dongles(coder_t *coder)
{
    unlock(&(coder->left_dongle->dongle_lock));
    unlock(&(coder->right_dongle->dongle_lock));
    coder->left_dongle->is_available = 1;
    coder->right_dongle->is_available = 1;
}

void *monitor(void *arg)
{
    env_t *env = (env_t *) arg;
    if (!env)
        return (printf("no arg provided"), NULL);
    lock(&(env->env_lock));
    while (len(env->fifo) < env->nb_coders)
    {
        _log("monitor sleeps\n", env);
        unlock(&(env->env_lock));
        usleep(200);
        lock(&(env->env_lock));
    }
    _log("monitor start work\n", env);
    while (!(env->stop_simulation) && !compiles_end(env))
    {
        if (is_burn_out(env) || compiles_end(env))
            break;
        _log("grab_next ticket - ", env);
        _log("wake the threads\n", env);
        sleep(2);
    }
    pthread_cond_wait(&(env->monitor_cond), &(env->env_lock));
    return (env);
}

void *routine(void *arg)
{
    coder_t *coder = (coder_t *) arg;
    env_t *env = coder->env;
    if (!coder)
        return (printf("no arg provided\n"), NULL);
    while (coder->compiles_count < coder->req_compiles)
    {
        lock(&(env->env_lock));
        while (!(coder->ready) && !(env->stop_simulation))
        {
            if (env->stop_simulation)
                return (unlock(&env->env_lock), coder);
            if (!in_queue(coder))
                request_ticket(coder);
            _log("to sleep\n", env);
            sleep_coder(coder);
        }
        unlock(&(env->env_lock));
        if (!env->stop_simulation)
            return (printf("end simulation\n"), coder);
        coder->ready = 0;
        grab_dongles(coder);
        _log("do the work\n", env);
        leave_dongles(coder);       
    }
    return (coder);
}

int in_queue(coder_t *coder)
{
    node_t *cur = coder->env->fifo;
    coder_t *tmp;
    
    cur = coder->env->fifo;
    while (cur)
    {
        tmp = (coder_t *) cur->data;
        if (tmp->id == coder->id)
            return (1);
        cur = cur->next;
    }
    return (0);
}


coder_t *create_coders(env_t *env)
{
    coder_t *coders;
    int i;

    if (!env)
        return (NULL);
    coders = malloc(sizeof(coder_t) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_count = 0;
        coders[i].env = env;
        i++;
    }
    return (coders);
}

void usage_message(void)
{
    printf("Error: helpful usage error message.");
}

coder_t *init_coders(env_t *env)
{
    coder_t *coders;
    int i;
    
    coders = malloc(sizeof(coder_t) * env->nb_coders);
    if (!coders)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        coders[i].id = i + 1;
        coders[i].compiles_count = 0;
        coders[i].req_compiles = env->required_compiles;
        coders[i].left_dongle = &(env->dongles[coders[i].id]);
        coders[i].right_dongle = &(env->dongles[coders[i + 1].id % env->nb_coders]);
        coders[i].env = env;
        coders[i].ready = 0;
        coders[i].last_compile_time = 0;
        i++;
    }
    return (coders);
}

dongle_t *init_dongles(env_t *env)
{
    int i;
    dongle_t *dongles;

    dongles = malloc(sizeof(dongle_t) * env->nb_coders);
    if (!dongles)
        return (NULL);
    i = 0;
    while (i < env->nb_coders)
    {
        dongles[i].id = i + 1;
        dongles[i].env = env;
        dongles[i].is_available = 1;
        i++;
    }
    return (dongles);
}

void init_threads(env_t *env)
{
    int i;

    i = 0;
    while (i < env->nb_coders)
    {
        pthread_create(&(env->coders[i].thread_id), NULL, routine, &(env->coders[i]));
        i++;
    }
    pthread_create(&(env->monitor_id), NULL, monitor, env);

}

void init_mutexes(env_t *env)
{
    int i;

    i = 0;
    pthread_mutex_init(&(env->env_lock), NULL);
    pthread_mutex_init(&(env->print_lock), NULL);
    pthread_cond_init(&(env->monitor_cond), NULL);
    while (i < env->nb_coders)
    {
        pthread_mutex_init(&(env->dongles[i].dongle_lock), NULL);
        pthread_cond_init(&(env->coders[i].cond), NULL);
        i++;
    }
}


env_t *init_env(char **av)
{
    env_t *env;

    env = malloc(sizeof(env_t));
    if (!env)
        return (NULL);
    env->nb_coders = ft_atoi(av[1]);
    env->t_burn_out = ft_atoi(av[2]);
    env->t_compile = ft_atoi(av[3]);
    env->t_debug = ft_atoi(av[4]);
    env->t_refactore = ft_atoi(av[5]);
    env->required_compiles = ft_atoi(av[6]);
    env->t_cooldown = ft_atoi(av[7]);
    env->dongles = init_dongles(env);
    env->start_simulation = 0;
    env->stop_simulation = 0;
    env->fifo = NULL;
    if (!env->dongles)
        return (free(env), NULL);
    env->coders = init_coders(env);
    if (!env->coders)
        return (free(env), NULL);
    init_mutexes(env);
    init_threads(env);
    
    return (env);
}

int main(int ac, char **av) {
    env_t *env;
    int i;

    if (ac < 8 || ac > 9 )
        return (usage_message(), 1);
    printf("parsing && vlidating\n");
    if (!extract_args(ac, av))
        return (printf("Error"), 1);
    env = init_env(av);
    
    
    i = 0;
    // while (i < env->nb_coders)
    // {
    //     pthread_join((env->coders[i].thread_id), NULL);
    //     i++;   
    // }
    // printf("end_compilations: %d\n",compiles_end(env));
    pthread_join(env->monitor_id, NULL);
}
