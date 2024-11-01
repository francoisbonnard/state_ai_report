from transformers import AutoModelForCausalLM, AutoTokenizer
 

model_name = "meta-llama/Llama-3.2-1B"
# model_name ="mistralai/Mistral-7B-Instruct-v0.2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.to("cuda")
 
# Exemple d'encodage des données d'entrée
input_text = "donne moi une approximation de pi"
tokens = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

generated_ids = model.generate(tokens, max_new_tokens=1000, do_sample=True)

# decode with mistral tokenizer
result = tokenizer.decode(generated_ids[0].tolist())
print(result)
