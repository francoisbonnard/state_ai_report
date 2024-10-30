# Installer les bibliothèques nécessaires

import torch
from transformers import GPT2Tokenizer, GPT2Model
from transformers import AutoTokenizer, AutoModelForCausalLM

import umap
import matplotlib.pyplot as plt
import umap.umap_ as umap

model_name = "gpt2"

if (model_name == "gpt2"):
    model_name = "gpt2"  # vous pouvez choisir 'gpt2-medium', 'gpt2-large', etc.
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2Model.from_pretrained(model_name)

else :
    from huggingface_hub import login
    from decouple import config
    hugging_face_token = config("HUGGING_FACE_TOKEN")
    login("hugging_face_token")
    model_name = "meta-llama/Llama-3.2-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

# Extraire les embeddings des tokens
def get_word_embeddings(word_list):
    embeddings = []
    tokens = []
    
    for word in word_list:
        # Tokeniser le mot et obtenir son embedding
        input_ids = tokenizer.encode(word, add_special_tokens=False, return_tensors="pt")
        with torch.no_grad():
            output = model(input_ids)
            # Obtenir l'embedding du dernier token dans la dernière couche
            embedding = output.last_hidden_state[0, -1, :].numpy()
            embeddings.append(embedding)
            tokens.append(word)
    
    return tokens, embeddings

# Exemple de mots pour lesquels obtenir des embeddings
words = ["chat", "chien", "maison", "ordinateur", "soleil", "intelligence", "humain", "machine"]
tokens, embeddings = get_word_embeddings(words)

# Réduction de dimension avec UMAP pour visualisation
reducer = umap.UMAP(n_components=2, random_state=42)

embedding_2d = reducer.fit_transform(embeddings)

# Visualiser les embeddings en 2D
plt.figure(figsize=(10, 7))
for i, (x, y) in enumerate(embedding_2d):
    plt.scatter(x, y, marker='o', color='b')
    plt.text(x + 0.01, y + 0.01, tokens[i], fontsize=12)

plt.title("Visualisation de l'espace d'embedding avec UMAP")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()
