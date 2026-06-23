
FILE="./maps/challenger/01_the_impossible_dream.txt"
EASY_01="./maps/easy/01_linear_path.txt"
EASY_02="./maps/easy/02_simple_fork.txt"
EASY_03="./maps/easy/03_basic_capacity.txt"
medium_01="./maps/medium/01_dead_end_trap.txt"
medium_02="./maps/medium/02_circular_loop.txt"
medium_03="./maps/medium/03_priority_puzzle.txt"
hard_01="./maps/hard/01_maze_nightmare.txt"
hard_02="./maps/hard/02_capacity_hell.txt"
hard_03="./maps/hard/03_ultimate_challenge.txt"
run:
	@uv run python3 -m src $(medium_02)

test:
	@uv run python3 -m main $(FILE)

clean:
	@echo "Cleaning up..."
	@rm -rf data/output/*
	@rm -rf */__pycache__/
	@rm -rf __pycache__
	@rm -rf */*/__pycache__/

clean-all: clean
	@rm -rf .venv
