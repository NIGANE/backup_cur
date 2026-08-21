#include "header.h"

void sleep_coder(coder_t *coder)
{
    pthread_cond_wait(&(coder->cond), &(coder->env->env_lock));
}

int lock(pthread_mutex_t *_lock)
{
    return pthread_mutex_lock(_lock);
}

int unlock(pthread_mutex_t *_lock)
{
    return pthread_mutex_unlock(_lock);
}

int grab_dongles(coder_t *coder)
{
    dongle_t *left;
    dongle_t *right;
    env_t *env;

    left = coder->left_dongle;
    right = coder->right_dongle;
    env = coder->env;
    if (env->stop_simulation)
        return 0;
    while ((timestamp(left->last_use) < env->t_cooldown || timestamp(right->last_use) < env->t_cooldown) && !env->stop_simulation)
        suspend(2);
    if (coder->left_dongle->ready_to_use && coder->right_dongle->ready_to_use && !(env->stop_simulation))
    {
        lock(&(coder->left_dongle->dongle_lock));
        lock(&env->print_lock);
        printf("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time), coder->id);
        unlock(&env->print_lock);
        lock(&(coder->right_dongle->dongle_lock));
        lock(&env->print_lock);
        printf("[%lld] [%d] has taken a dongle\n", timestamp(env->start_time), coder->id);
        unlock(&env->print_lock);
        coder->left_dongle->ready_to_use = 0;
        coder->right_dongle->ready_to_use = 0;
        return (1);
    }
    return (0);
}

void leave_dongles(coder_t *coder)
{
    coder->left_dongle->last_use = current_time_ms();
    coder->right_dongle->last_use = current_time_ms();
    coder->left_dongle->ready_to_use = 1;
    coder->right_dongle->ready_to_use = 1;
    unlock(&(coder->left_dongle->dongle_lock));
    unlock(&(coder->right_dongle->dongle_lock));
    lock(&coder->env->env_lock);
    coder->left_dongle->available = 1;
    coder->right_dongle->available = 1;
    unlock(&coder->env->env_lock);
}
