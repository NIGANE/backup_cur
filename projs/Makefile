CC = cc -Wall -Wextra -Werror
OUT = tt
SRC = main.c ./heap/*.c ./helpers/*.c

ARGS = 4 400 10 10 10 4 2 2 2 2

arg:run
	@./$(OUT) $(ARGS)


run:
	@$(CC) $(SRC) -o $(OUT)
cc:
	@cc $(SRC) -o $(OUT)

gdb:
	@$(CC) $(SRC) -o $(OUT) -g
	@gdb --args ./$(OUT) $(ARGS)
clean:
	@rm -rf $(OUT)

tes:
	./$(OUT)
