LIB_N = ${LIB_NAME}
LIB_L = ${LIB_LOCA}
CC = cc -Wall -Wextra -Werror
LIB_I = ${LIB_INCLUDES}
all:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out
	./exec.out

lbsd:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -lbsd -o exec.out
	./exec.out
