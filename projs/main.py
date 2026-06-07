from llm_sdk import Small_LLM_Model as Model
import torch


prompt = "b"
model = Model()
encode = model.encode("-")[0].tolist()
print(encode)
print(model.decode(encode))

# logits = model.get_logits_from_input_ids(encode)
# next_token = torch.argmax(torch.tensor(logits))
# decode = model.decode(next_token)
# print(decode)
