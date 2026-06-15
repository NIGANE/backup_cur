
all:
	@echo "Running the application..."
	@uv run python -m src --functions_definition data/input/functions_definition.json --input data/input/function_calling_tests.json --output data/output/function_calls.json --model Qwen/Qwen3-0.6B


install:
	@echo "Installing dependencies..."
	uv sync

debug:
	uv run python -m pdb src/main.py

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	@echo "Cleaning up..."
	@rm -rf data/output/*
	@rm -rf */__pycache__/
	@rm -rf __pycache__
	@rm -rf */*/__pycache__/

clean-all: clean
	@rm -rf .venv