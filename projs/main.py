from llm_sdk import Small_LLM_Model as Model
import torch
prompt = "213 "

model = Model()
encode = model.encode(prompt)[0].tolist()
print(encode)
# logits = model.get_logits_from_input_ids(encode)
# next_token = torch.argmax(torch.tensor(logits))
# decode = model.decode(next_token)
# print(decode)
