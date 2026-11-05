RUN = uv run python3 -m src
K = --k 0
query = "What is the return type annotation for the \
		_apply_matches function in vLLM's multimodal \
		processing module?"
chunk_size = --max_chunk_size 2000

evaluate:
	$(RUN) evaluate \
	--student_search_results_path  data/output/dataset_code_public.json \
	--dataset_path data/datasets/AnsweredQuestions/dataset_code_public.json

answer_dataset:
	$(RUN) answer_dataset \
	--student_search_results_path "data/output/dataset_code_public.json" \
	--save_directory "data/output/answer_dataset_code_public.json"


search_dataset:
	$(RUN) search_dataset \
	--dataset_path data/datasets/UnansweredQuestions/dataset_code_public.json \
	$(K) \
	--save_directory data/output/dataset_code_public.json --vector --hybrid

search:
	$(RUN) search \
	$(query) \
	$(K)

index:
	$(RUN) index $(chunk_size)

answer:
	$(RUN) answer \
	$(query) \
	$(K)

clean:
	@rm -rf src/__pycache__

clean-all: clean
	@rm -rf data/process -rf
	@rm -rf data/output