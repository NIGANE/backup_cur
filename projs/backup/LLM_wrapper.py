import json
import torch
from typing import Dict, List, Any, Set
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FunctionSchema:
    """Represents a function call schema"""
    name: str
    description: str
    parameters: Dict[str, Any]
    required: List[str]


class ConstrainedDecoder:
    """Constrained decoding for Small_LLM_Model using logit masking"""
    
    def __init__(self, llm_model, prompts_file: str, schemas_file: str):
        """
        Parameters
        ----------
        llm_model : Small_LLM_Model
            Instance of your Small_LLM_Model class
        prompts_file : str
            Path to file containing prompts
        schemas_file : str
            Path to file containing function schemas
        """
        self.model = llm_model
        self.prompts = self.load_prompts(prompts_file)
        self.schemas = self.load_schemas(schemas_file)
        
        # Build token-to-id mappings for JSON constraints
        self._build_token_mappings()
        
    def _build_token_mappings(self):
        """Build mappings for common JSON tokens"""
        # Common JSON structure tokens
        json_tokens = ['{', '}', '[', ']', ':', ',', '"', 'true', 'false', 'null']
        self.json_token_ids = {}
        
        for token in json_tokens:
            encoded = self.model.encode(token)
            if encoded.numel() > 0:
                self.json_token_ids[token] = encoded[0, 0].item()
    
    def load_prompts(self, file_path: str) -> List[str]:
        """Load prompts from a JSON or text file"""
        path = Path(file_path)
        
        if path.suffix == '.json':
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict) and 'prompts' in data:
                    return data['prompts']
        else:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        
        raise ValueError(f"Could not parse prompts from {file_path}")
    
    def load_schemas(self, file_path: str) -> Dict[str, FunctionSchema]:
        """Load function schemas from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        schemas = {}
        for func_name, schema_data in data.items():
            schemas[func_name] = FunctionSchema(
                name=func_name,
                description=schema_data.get('description', ''),
                parameters=schema_data.get('parameters', {}),
                required=schema_data.get('required', [])
            )
        
        return schemas
    
    def get_schema_for_prompt(self, prompt: str) -> FunctionSchema:
        """Determine which schema to use for a given prompt"""
        prompt_lower = prompt.lower()
        
        # Try to find matching schema
        for schema_name, schema in self.schemas.items():
            keywords = schema_name.lower().split('_')
            if any(keyword in prompt_lower for keyword in keywords):
                return schema
        
        # Return first schema as default
        return list(self.schemas.values())[0]
    
    def build_system_prompt(self, schema: FunctionSchema) -> str:
        """Build a system prompt that instructs the model to output JSON"""
        param_descriptions = []
        for param_name, param_spec in schema.parameters.items():
            param_type = param_spec.get('type', 'string')
            required = '(required)' if param_name in schema.required else '(optional)'
            param_descriptions.append(f'  - {param_name}: {param_type} {required}')
        
        params_text = '\n'.join(param_descriptions)
        
        prompt = f"""You must respond with a valid JSON function call in this exact format:
{{
  "function": "{schema.name}",
  "arguments": {{
    ...
  }}
}}

Function: {schema.name}
Description: {schema.description}
Parameters:
{params_text}

Respond ONLY with valid JSON. Do not include any other text."""
        
        return prompt
    
    def get_allowed_tokens_at_position(
        self, 
        partial_json: str, 
        schema: FunctionSchema
    ) -> Set[int]:
        """
        Determine which tokens are valid at the current position in JSON generation.
        Returns set of allowed token IDs.
        """
        # This is a simplified version - you can make this more sophisticated
        # by parsing the JSON state and determining valid next tokens
        
        # For now, we'll allow all tokens but you can implement proper JSON grammar
        # For a complete implementation, use a JSON parser to track state
        
        # Basic approach: if we're starting, only allow '{'
        if not partial_json.strip():
            return {self.json_token_ids.get('{', -1)}
        
        # Otherwise, allow all tokens (simplified)
        # In production, you'd implement a proper JSON state machine
        return set()  # Empty set means no masking
    
    def apply_logit_mask(
        self, 
        logits: List[float], 
        allowed_token_ids: Set[int]
    ) -> List[float]:
        """
        Apply masking to logits - set disallowed tokens to -inf
        """
        if not allowed_token_ids:  # If empty, no masking
            return logits
        
        masked_logits = []
        for token_id, logit in enumerate(logits):
            if token_id in allowed_token_ids:
                masked_logits.append(logit)
            else:
                masked_logits.append(float('-inf'))
        
        return masked_logits
    
    def sample_token(self, logits: List[float], temperature: float = 0.7) -> int:
        """Sample next token from logits with temperature"""
        logits_tensor = torch.tensor(logits, dtype=torch.float32)
        
        # Apply temperature
        logits_tensor = logits_tensor / temperature
        
        # Softmax to get probabilities
        probs = torch.softmax(logits_tensor, dim=-1)
        
        # Sample
        token_id = torch.multinomial(probs, num_samples=1).item()
        return token_id
    
    def generate_constrained(
        self, 
        prompt: str, 
        schema: FunctionSchema,
        max_tokens: int = 200,
        temperature: float = 0.7
    ) -> str:
        """
        Generate output with constrained decoding to match schema
        
        Parameters
        ----------
        prompt : str
            User prompt
        schema : FunctionSchema
            Schema to constrain output to
        max_tokens : int
            Maximum tokens to generate
        temperature : float
            Sampling temperature
            
        Returns
        -------
        str
            Generated JSON string
        """
        # Build full prompt with instructions
        system_prompt = self.build_system_prompt(schema)
        full_prompt = f"{system_prompt}\n\nUser query: {prompt}\n\nJSON response:"
        
        # Encode initial prompt
        input_ids = self.model.encode(full_prompt)[0].tolist()
        generated_text = ""
        
        for _ in range(max_tokens):
            # Get logits for next token
            logits = self.model.get_logits_from_input_ids(input_ids)
            
            # Determine allowed tokens (simplified - always allow all for now)
            # In production, implement proper JSON state tracking
            allowed_tokens = self.get_allowed_tokens_at_position(
                generated_text, schema
            )
            
            # Apply masking if we have constraints
            if allowed_tokens:
                logits = self.apply_logit_mask(logits, allowed_tokens)
            
            # Sample next token
            next_token_id = self.sample_token(logits, temperature)
            
            # Decode token
            next_token = self.model.decode([next_token_id])
            generated_text += next_token
            
            # Add to input_ids for next iteration
            input_ids.append(next_token_id)
            
            # Check for completion (closing brace)
            if generated_text.strip().endswith('}'):
                # Try to parse as JSON
                try:
                    json.loads(generated_text.strip())
                    break  # Valid JSON, we're done
                except json.JSONDecodeError:
                    continue  # Keep generating
        
        return generated_text.strip()
    
    def validate_output(self, output: str, schema: FunctionSchema) -> bool:
        """Validate generated output against schema"""
        try:
            data = json.loads(output)
            
            # Check function name
            if data.get('function') != schema.name:
                return False
            
            # Check required parameters
            args = data.get('arguments', {})
            for req_param in schema.required:
                if req_param not in args:
                    return False
            
            return True
        except json.JSONDecodeError:
            return False
    
    def process_prompt(
        self, 
        prompt: str, 
        max_tokens: int = 200,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Process a prompt end-to-end: select schema, generate, validate
        
        Returns
        -------
        dict
            Contains 'prompt', 'schema_name', 'output', 'valid', 'parsed_json'
        """
        # Select appropriate schema
        schema = self.get_schema_for_prompt(prompt)
        
        # Generate with constraints
        output = self.generate_constrained(
            prompt, schema, max_tokens, temperature
        )
        
        # Validate
        is_valid = self.validate_output(output, schema)
        
        # Try to parse
        parsed = None
        try:
            parsed = json.loads(output)
        except json.JSONDecodeError:
            pass
        
        return {
            'prompt': prompt,
            'schema_name': schema.name,
            'output': output,
            'valid': is_valid,
            'parsed_json': parsed
        }


# Example usage
if __name__ == "__main__":
    print("Constrained Decoding with Small_LLM_Model")
    print("=" * 60)
    
    # Create example files
    example_prompts = {
        "prompts": [
            "What's the weather like in Paris?",
            "Find restaurants near Times Square",
            "Calculate 15% tip on $45.50"
        ]
    }
    
    example_schemas = {
        "get_weather": {
            "description": "Get weather information for a location",
            "parameters": {
                "location": {"type": "string"},
                "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        },
        "search_restaurants": {
            "description": "Search for restaurants",
            "parameters": {
                "query": {"type": "string"},
                "location": {"type": "string"},
                "radius": {"type": "number"}
            },
            "required": ["query", "location"]
        },
        "calculate": {
            "description": "Perform calculations",
            "parameters": {
                "operation": {"type": "string"},
                "values": {"type": "array"}
            },
            "required": ["operation", "values"]
        }
    }
    
    with open('prompts.json', 'w') as f:
        json.dump(example_prompts, f, indent=2)
    
    with open('schemas.json', 'w') as f:
        json.dump(example_schemas, f, indent=2)
    
    print("\nExample files created: prompts.json, schemas.json")
    print("\nTo use:")
    print("```python")
    print("from small_llm_model import Small_LLM_Model")
    print()
    print("# Initialize your model")
    print("llm = Small_LLM_Model('Qwen/Qwen3-0.6B')")
    print()
    print("# Create constrained decoder")
    print("decoder = ConstrainedDecoder(llm, 'prompts.json', 'schemas.json')")
    print()
    print("# Process a prompt")
    print("result = decoder.process_prompt('What is the weather in Tokyo?')")
    print("print(result['output'])")
    print("```")