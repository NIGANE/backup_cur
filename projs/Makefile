CC = cc -Wall -Wextra -Werror
OUT = tt
SRC = main.c ./heap/*.c ./helpers/*.c ./simulation.c

ARGS = 5 400 10 10 10 4 2 2 2 2


arg:run
	@./$(OUT) $(ARGS)

test:
	@cc test.c
	@./a.out

run:
	@$(CC) $(SRC) -o $(OUT)
cc:
	@cc $(SRC) -o $(OUT)

gdb:
	@$(CC) $(SRC) -o $(OUT) -g
	@gdb --args ./$(OUT) $(ARGS)
clean:
	@rm -rf ./$(OUT)
	@rm -rf ./a.out

tes:
	./$(OUT)
