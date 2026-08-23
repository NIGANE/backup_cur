#include "header.h"

void	request_ticket(coder_t *coder)
{
	if (!coder || coder->env->stop_simulation)
		return ;
	if (coder->env->heap)
	{
		coder->env->heap = edf_heap_push(coder->env->heap, coder);
		return ;
	}
	coder->env->fifo = ft_insert(coder, coder->env->fifo);
}

coder_t	*whos_next(env_t *env)
{
	if ((env->heap) && env->heap->size > 0)
		return (env->heap->array[0]->data);
	if (!(env->fifo))
		return (NULL);
	return ((coder_t *)(env->fifo->data));
}

void	grab_ticket(env_t *env)
{
	edf_node_t	*node;

	if (env->heap && env->heap->size > 0)
	{
		node = edf_heap_pop(env->heap);
		edf_node_free(node);
		return ;
	}
	ft_pop(&(env->fifo));
}

int	in_queue(coder_t *coder)
{
	node_t	*cur;
	coder_t	*tmp;

	if (coder->env->heap)
		return (in_heap(coder));
	cur = coder->env->fifo;
	while (cur)
	{
		tmp = (coder_t *)cur->data;
		if (tmp->id == coder->id)
			return (1);
		cur = cur->next;
	}
	return (0);
}

int	lunch_up(env_t *env)
{
	int	i;

	i = 0;
	while (i < env->nb_coders)
	{
		if (odd(i))
		{
			if (pthread_create(&(env->coders[i].thread_id), NULL, routine,
					&(env->coders[i])) != 0)
				return (0);
		}
		i++;
	}
	suspend(5);
	i = 0;
	while (i < env->nb_coders)
	{
		if (!odd(i))
		{
			if (pthread_create(&(env->coders[i].thread_id), NULL, routine,
					&(env->coders[i])) != 0)
				return (0);
		}
		i++;
	}
	return (1);
}
