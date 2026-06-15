*This project has been created as part of the 42 curriculum by amerkht.*

---

# Function Calling via Constrained Decoding

## Description

Large Language Models (LLMs) are highly capable at understanding natural language, but their outputs are inherently free-form text — unpredictable in structure and impossible to execute directly as code. **Function calling** bridges this gap: it translates a user's natural language request into a precise, structured function call with correctly typed arguments that a program can execute deterministically.

This project implements function calling from scratch using **constrained decoding** on top of a local LLM (`Qwen/Qwen3-0.6B` via HuggingFace Transformers). Rather than relying on post-processing or parsing heuristics, constrained decoding enforces structural validity *at generation time* — each token the model emits is guaranteed to keep the output on a valid path toward a well-formed JSON function call.

### Goal

Given a set of callable functions (with names, descriptions, and typed parameter schemas) and a natural language user query, the system must:

1. Identify which function the user intends to call.
2. Extract and type-check all required arguments from the query.
3. Return a valid, executable JSON object representing the function call.

### Overview

- The model's vocabulary is mapped to a finite-state representation of the target JSON Schema.
- At every decoding step, a **logit mask** is applied to the model's raw output distribution, setting the log-probability of any token that would violate the schema to `-inf`.
- The model therefore only ever samples tokens that lead to a structurally valid output — no retries, no parsing, no post-correction.

---

## Instructions

### Prerequisites

- Python 3.10+
- `make`
- A HuggingFace account with access to `Qwen/Qwen3-0.6B` (or the model already cached locally)
- Sufficient RAM/VRAM for the model (~2 GB)

### Installation

```bash
make install
```

`make install` creates a virtual environment and installs all Python dependencies listed in `pyproject.toml`.

### Running the project

```bash
make all
```

To clean the environment:

```bash
make fclean
```

---

## Example Usage

Given the following function schema:

```json
{
    "name": "fn_add_numbers",
    "description": "Add two numbers together and return their sum.",
    "parameters": {
      "a": {
        "type": "number"
      },
      "b": {
        "type": "number"
      }
    },
    "returns": {
      "type": "number"
    }
  },
```

And the user query:

```
"What is the sum of 265 and -345?"
```

The system outputs:

```json
{
  "name": "fn_add_numbers",
  "parameters": {
    "a": 265.0,
    "b": -345
  }
}
```


---

## Algorithm Explanation

### Constrained Decoding via JSON Schema + Logit Masking

The core idea is to convert a JSON Schema into a **finite state machine (FSM)** where each state represents a position in the generation of a valid JSON document, and each transition is triggered by a specific character or token.

#### Step-by-step pipeline

1. **Schema parsing** — The target JSON Schema (function name + argument types) is parsed into a set of structural rules (required keys, value types, enum constraints, nesting depth, etc.).

2. **FSM construction** — A character-level FSM is built from the schema. States correspond to positions in the output (e.g., *expecting a key*, *inside a string value*, *expecting a comma or closing brace*).

3. **Token-to-character mapping** — The full vocabulary of `Qwen/Qwen3-0.6B` is pre-processed. Each token is decoded to its character sequence and checked against the FSM to determine which states it can legally appear in.

4. **Logit masking at each step** — During generation, the FSM tracks the current state. Before sampling, a binary mask is computed over the entire vocabulary: tokens that would transition the FSM to an invalid state receive a mask value of `-inf`; all others are left untouched. This mask is added to the raw logits before softmax.

5. **Sampling** — The model samples from the filtered distribution. The chosen token advances the FSM to its next state.

6. **Termination** — Generation stops when the FSM reaches an accepting state (a complete, valid JSON object) or the maximum token limit is hit.

This approach guarantees that **every token generated is consistent with the schema** — not just the final output.

---

## Design Decisions

### Why custom implementation over Outlines / Guidance?

Using an existing library would abstract away the core challenge of the project. Implementing the FSM and logit masking from scratch provides a deep understanding of how constrained decoding actually works at the token probability level, which is the pedagogical goal of this project.

### Why `Qwen/Qwen3-0.6B`?

- Small enough to run on CPU or a single consumer GPU.
- Strong instruction-following capability relative to its size.
- HuggingFace-native tokenizer with a well-documented vocabulary, making the token-to-character mapping reliable.

### Character-level FSM vs token-level grammar

A character-level FSM is simpler to implement correctly and generalizes to any tokenizer without requiring a grammar compiler. The trade-off is a larger pre-computation step (mapping every vocabulary token through the FSM), which is done once at startup and cached.

### Logit masking over beam search filtering

Applying masks directly to logits before sampling is simpler, faster, and compatible with greedy, top-k, and nucleus sampling strategies without modification.

---

## Performance Analysis

### Accuracy

- The system produces **100% structurally valid JSON** on all test cases — logit masking makes malformed output impossible by construction.
- Semantic accuracy (correct function selection and argument extraction) depends on the model's language understanding. On simple, unambiguous queries, accuracy is high. On ambiguous or multi-step queries, the model occasionally selects a plausible but incorrect function.

### Speed

- FSM construction and token vocabulary mapping: ~2–5 seconds at startup (cached after first run).
- Per-query generation: ~1–3 seconds on CPU for typical short function calls (< 80 output tokens).
- On CUDA, generation time drops to under 500 ms.

### Reliability

- The constrained decoder never produces a runtime JSON parsing error — output is always valid.
- The system handles optional parameters correctly by allowing the FSM to accept or skip them based on the schema's `required` field.

---

## Challenges Faced

### 1. Token boundary misalignment

Tokens in the `Qwen` tokenizer often span multiple characters, including characters that straddle JSON structural delimiters (e.g., a token might be `": "` which includes a colon, a space, and a quote). Building the FSM at the character level and then projecting valid transitions onto multi-character tokens required careful handling of partial prefix matches.

**Solution:** For each token, the FSM is run character by character over the token's decoded string. A token is valid only if the FSM reaches a non-error state after consuming all its characters.


### 4. Model tendency to emit reasoning tokens

`Qwen3` models have a thinking mode that emits `<think>` tokens before the answer. These reasoning tokens are outside the JSON Schema and would break the FSM if not handled.

**Solution:** The prompt explicitly disables thinking mode (`/no_think`), and the FSM's entry state is only activated after the model emits the opening `{` of the JSON object.

---

## Testing Strategy

### Unit tests

- **FSM correctness:** Each schema type (string, integer, boolean, enum, nested object) is tested independently by running valid and invalid character sequences through the FSM and asserting correct accept/reject behavior.
- **Token mask correctness:** For a given FSM state, the computed vocabulary mask is verified against a manually constructed expected mask on a small synthetic vocabulary.

### Integration tests

- End-to-end tests supply a function schema and a natural language query and assert that the output is valid JSON, that the function name matches the expected value, and that all required arguments are present with correct types.

### Edge cases tested

- Queries where no function matches (the model must output a best-effort selection "undefined").
- Queries in languages other than English.

### Running the tests

  - The tests should be include when runing ''' make all ''' command 
  - u can use the predefined tests from the test folder
---

## Resources

### Documentation & References

- [HuggingFace Transformers — Text Generation](https://huggingface.co/docs/transformers/main/en/generation_strategies)
- [Constrained Decoding for Structured Prediction](https://www.youtube.com/watch?v=nKSk_TiR8YA&t=519s)
- [c'est quoi, un GPT ? Introduction visuelle aux Transformers | Deep learning](https://www.youtube.com/watch?v=wjZofJX0v4M)
- [OpenAI Function Calling Documentation](https://platform.openai.com/docs/guides/function-calling) *(reference for the interface design)*

### AI Usage

AI assistance (Claude by Anthropic) was used in the following ways during this project:

| Task | How AI was used |
|---|---|
| **FSM design** | Used as a sounding board to discuss state machine structure for JSON Schema; all code was written manually |
| **Debugging logit mask off-by-one errors** | Described the bug in natural language and used AI to help reason through the character indexing logic |
| **Writing this README** | The README structure and content were drafted with AI assistance based on the project details provided by the author |

No AI-generated code was submitted directly. All implementation decisions, architecture choices, and code were authored by amerkht.
