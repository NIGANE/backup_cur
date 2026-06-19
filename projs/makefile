
FILE="./maps/challenger/01_the_impossible_dream.txt"
EASY_01="./maps/easy/01_linear_path.txt"
EASY_02="./maps/easy/02_simple_fork.txt"
EASY_03="./maps/easy/03_basic_capacity.txt"
medium_01="./maps/medium/01_dead_end_trap.txt"

run:
	@uv run python3 -m src $(medium_01)

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
