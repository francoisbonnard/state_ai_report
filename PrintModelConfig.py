from transformers import AutoModel, AutoTokenizer

# model_name = "meta-llama/Llama-3.2-1B"
model_name = "mistralai/Mistral-7B-Instruct-v0.2"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print(model.config)  # Affiche la configuration du modèle
print(model)  # Affiche la structure complète du modèle
