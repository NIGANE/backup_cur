/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: negane <negane@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 15:12:20 by amerkht           #+#    #+#             */
/*   Updated: 2026/08/19 19:38:20 by negane           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "./header.h"



int ft_resources(coder_t *coder)
{
    if (coder->left_dongle->available && coder->right_dongle->available)
    {
        coder->left_dongle->available = 0;
        coder->right_dongle->available = 0;
        return (1);
    }
    return (0);
}

int odd(int a)
{
    return (a % 2);
}

// coder_t *create_coders(env_t *env)
// {
//     coder_t *coders;
//     int i;

//     if (!env)
//         return (NULL);
//     coders = malloc(sizeof(coder_t) * env->nb_coders);
//     if (!coders)
//         return (NULL);
//     i = 0;
//     while (i < env->nb_coders)
//     {
//         coders[i].id = i + 1;
//         coders[i].compiles_count = 0;
//         coders[i].env = env;
//         i++;
//     }
//     return (coders);
// }



int main(int ac, char **av) {
    env_t *env;
    int i;

    if (ac < 8 || ac > 9 )
        return (usage_message(), 0);
    if (!extract_args(ac, av))
        return (usage_message(), 0);
    env = init_env(av);
    pthread_join(env->monitor_id, NULL);
    if (!env->stop_simulation)
        printf("compiles: %ld/%ld\n", env->total_compiles, env->target_compiles);
    free_threads_mutexes(env);
    clean_env(env);
    printf("all good\n");
}
