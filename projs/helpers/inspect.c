#include "../header.h"
void inspect_env(t_env *env)
{
    printf("coders: %d\n",env->nb_coders);
    printf("time of compiling: %ld\n",env->t_compile);
    printf("time of debugin: %ld\n",env->t_compile);
    printf("time of refactoring: %ld\n",env->t_refactore);
    printf("time of burn_out: %ld\n",env->t_burn_out);
    printf("required compiles: %d\n", env->required_compiles);
    printf("time of cooldown: %ld\n", env->t_cooldown);
    printf("\n");
}