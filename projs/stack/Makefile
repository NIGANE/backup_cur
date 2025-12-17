
CC=cc
CFLAGS = -Wall -Wextra -Werror
SRCS=*.c

all :
	@$(CC) ${CFLAGS} ${SRCS} -o exec.out
	./exec.out

gdb :
	@$(CC)  ${SRCS} -o exec.out -g
	gdb ./exec.out

nfl :
	@cc  ${SRCS} -o exec.out
	./exec.out

clean :
	rm -f exec.out
	clear
