CC = cc
CFLAGS = -Wall -Wextra -Werror
RM = rm -f

NAME = push_swap

PS_SRCS = array_operations.c \
	check.c \
	extract_stack.c \
	find_various.c \
	ft_atoi.c \
	ft_putstr.c \
	ft_split.c \
	ft_strlen.c \
	ps_main.c \
	moving_node.c \
	operations_1.c \
	opirations.c \
	push.c \
	rev_rotate.c \
	rotate.c \
	sort_1_5.c \
	sort_6_100.c \
	sort.c \
	sort_to_b.c \
	stack_op1.c \
	stack_op2.c \
	swap.c

PS_OBJS = $(PS_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(PS_OBJS)
	$(CC) $(CFLAGS) $(PS_OBJS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(PS_OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONEY: ${NAME} all clean fclean re
.SECONDARRY: ${PS_OBJS}