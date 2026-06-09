
run:
	@echo "Running the application..."
	@uv run python -m src --functions_definition data/input/functions_definition.json --input data/input/function_calling_tests.json --output data/output/function_calls.json

test:
	@echo "Running test..."
	uv run python -m main

install:
	@echo "Installing dependencies..."
	pip install --break-system-packages uv
	uv sync

clean:
	@echo "Cleaning up..."
	@rm -rf data/output/*
	@rm -rf */__pycache__/
	@rm -rf __pycache__
	@rm -rf */*/__pycache__/