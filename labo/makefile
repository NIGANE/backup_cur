RUN = uv run python3 -m src

evaluate:
	$(RUN) evaluate \
	--student_search_results_path  data/output/dataset_code_public.json \
	--dataset_path data/datasets/AnsweredQuestions/dataset_code_public.json

answer_dataset:
	$(RUN) answer_dataset \
	--student_search_results_path "data/output/dataset_code_public.json" \
	--save_directory "data/output/answer_dataset_docs_public.json"


search_dataset:
	$(RUN) search_dataset \
	--dataset_path data/datasets/UnansweredQuestions/dataset_code_public.json \
	--k 3 \
	--save_directory data/output/dataset_code_public.json

search:
	$(RUN) search  "What is stored in the logits array during the qk_max calculation in vLLM's paged attention implementation?" \
	--k 3

index:
	$(RUN) index --max_chunk_size 2000

answer:
	$(RUN) answer \
	"What is the return type annotation for the _apply_matches function in vLLM's multimodal processing module?" \
	--k 3

clean:
	@rm -rf src/__pycache__

clean-all: clean
	@rm -rf data/process -rf
	@rm -rf data/output