# Installer les bibliothèques nécessaires

import torch
from transformers import GPT2Tokenizer, GPT2Model
from transformers import AutoTokenizer, AutoModel

import umap
import matplotlib.pyplot as plt
import umap.umap_ as umap

model_name = "HF"

if (model_name == "default"):
    model_name = "gpt2"  # vous pouvez choisir 'gpt2-medium', 'gpt2-large', etc.
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2Model.from_pretrained(model_name)

elif (model_name == "HF") :
    from huggingface_hub import login
    from decouple import config
    hugging_face_token = config("HUGGING_FACE_TOKEN")
    login(hugging_face_token)
    model_name = "meta-llama/Llama-3.2-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)


# Extraire les embeddings des tokens
def get_word_embeddings(word_list):
    embeddings = []
    tokens = []
    
    for word in word_list:
        # Tokeniser le mot et obtenir son embedding
        input_ids = tokenizer.encode(word, add_special_tokens=False, return_tensors="pt")
        with torch.no_grad():
            output = model(input_ids,output_hidden_states=True)
            # Obtenir l'embedding du dernier token dans la dernière couche
            embedding = output.last_hidden_state[0, -1, :].numpy()
            embeddings.append(embedding)
            tokens.append(word)
    
    return tokens, embeddings

# Exemple de mots pour lesquels obtenir des embeddings
words = ["chat", "chien", "maison", "ordinateur", "soleil", "intelligence", "humain","robot"]
tokens, embeddings = get_word_embeddings(words)


# visualisation des similarités cosinus entre les embeddings de ces mots 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
similarities = cosine_similarity(embeddings)
df_similarities = pd.DataFrame(similarities, index=words, columns=words)
print(df_similarities)

# choix de la dimension 
rep = 3

# Réduction de dimension avec UMAP pour visualisation
reducer = umap.UMAP(n_components=rep, random_state=42)

embedding_2d = reducer.fit_transform(embeddings)

if (rep ==2 ):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Visualiser les embeddings en 2D
    plt.figure(figsize=(10, 7))
    for i, (x, y) in enumerate(embedding_2d):
        plt.scatter(x, y, marker='o', color='b')
        plt.text(x + 0.01, y + 0.01, tokens[i], fontsize=12)

    plt.title("Visualisation de l'espace d'embedding avec UMAP")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
elif (rep==3):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Ajout des points et des labels
    for i, (x, y, z) in enumerate(embedding_2d):
        ax.scatter(x, y, z, marker='o', color='b')
        ax.text(x + 0.01, y + 0.01, z + 0.01, tokens[i], fontsize=10)

    ax.set_title("Visualisation de l'espace d'embedding en 3D avec UMAP")
    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    ax.set_zlabel("Dimension 3")

plt.show()
