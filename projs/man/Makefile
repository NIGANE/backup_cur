CC = cc 
CFLAGS = -Wall -Wextra -Werror
SRC = get_next_line.c get_next_line_utils.c main.c
all:
	@${CC} ${CFLAGS} ${SRC} -o exec.out
	./exec.out

gdb:
	@$(CC) ${CFLAGS} ${SRC} -o exec.out -g
	gdb ./exec.out

nfl:
	@${CC} ${SRC} -o exec.out
	./exec.out
	
clean:
	rm -f exec.out