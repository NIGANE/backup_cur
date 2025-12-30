CC = cc
CFLAGS = -Wall -Wextra -Werror
RM = rm -f
NAME = push_swap
BONUS_NAME = checker

PS_SRCS = array_operations.c check.c extract_stack.c find_various.c \
	ft_atoi.c ft_putstr.c ft_split.c ft_strlen.c ps_main.c \
	moving_node.c operations_2.c operations_1.c opirations.c \
	push.c rev_rotate.c rotate.c sort_1_5.c sort_6_max.c \
	sort.c sort_to_b.c stack_op1.c stack_op2.c swap.c \
	add_turk.c move_chepest.c abs.c indexing.c

PS_BONUS_SRCS = checker_main.c get_line_utils.c stack_op1.c stack_op2.c \
	ft_atoi.c ft_putstr.c ft_split.c get_line.c check.c \
	array_operations.c operations_2_checker.c operations_1_checker.c \
	opirations_checker.c extract_stack.c ft_strlen.c rotate.c \
	rev_rotate.c push.c swap.c

PS_OBJS = $(PS_SRCS:.c=.o)
PS_BONUS_OBJS = $(PS_BONUS_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(PS_OBJS)
	$(CC) $(CFLAGS) $(PS_OBJS) -o $(NAME)

bonus: $(BONUS_NAME)

$(BONUS_NAME): $(PS_BONUS_OBJS)
	$(CC) $(CFLAGS) $(PS_BONUS_OBJS) -o $(BONUS_NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(PS_OBJS) $(PS_BONUS_OBJS)

fclean: clean
	$(RM) $(NAME) $(BONUS_NAME)

re: fclean all

.PHONY: all clean fclean re bonus