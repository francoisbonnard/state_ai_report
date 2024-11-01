# Hugging Face

## Hugging Face Librairies

[Hugging Face Librairies](./img/image6.png)



Frameworks d'apprentissage profond :

PyTorch, TensorFlow, JAX : Ce sont des frameworks majeurs utilisés pour construire et entraîner des modèles de machine learning.
Bibliothèques spécifiques à certaines tâches d'IA :

Transformers, sentence-transformers : Utilisées pour les modèles de traitement du langage naturel (NLP), notamment les architectures transformer.
Diffusers, stable-baselines3 : Liées aux modèles de génération (images, texte) et à l'apprentissage par renforcement.
timm (Torch Image Models), sample-factory : Outils pour les modèles d'images et l'apprentissage par renforcement.
Flair : Une bibliothèque pour le NLP (traitement du langage naturel).
Outils de manipulation de données et d'entraînement :

PEFT (parameter-efficient fine-tuning) : Pour affiner les modèles avec un usage efficace de la mémoire.
Safetensors : Format pour stocker des tensors de manière plus sécurisée et rapide.
TensorBoard : Visualisation des performances des modèles pendant l'entraînement.
ONNX : Format d'échange de modèles entre différents frameworks.
Outils pour des modèles spécialisés ou des accélérateurs matériels :

OpenVINO, GGUF, TensorBoard, ONNX : Pour faciliter l'export et l'exécution de modèles sur des infrastructures spécifiques (matériels dédiés).
Graphcore, Habana : Optimisés pour des architectures spécifiques de matériel d'IA.
Bibliothèques pour des tâches spécifiques :

spacy, flair, AllenNLP, Stanza : Pour le NLP (traitement de la langue naturelle).
fastText : Modèles de classification de texte rapides.
Asteroid, pyannote.audio : Pour le traitement du son/audio.
Outils pour l'entraînement distribué et optimisation :

ml-agents : Apprentissage par renforcement pour les agents dans des environnements virtuels.
fairseq, PaddlePaddle, fastai : Des bibliothèques pour former des modèles à grande échelle ou en parallèle.
Bibliothèques pour des frameworks multi-tâches ou des projets spécifiques :

Scikit-learn, Keras : Généralement utilisées pour les modèles plus traditionnels de machine learning ou deep learning.
SpeechBrain : Pour la reconnaissance vocale et d'autres tâches liées au son.

## Transformer path

PATH : %USERPROFILE%\.cache\huggingface\hub


## Transformer info 

    print(model.config)

| **LlamaConfig**                           | **MistralConfig**                        |
|-------------------------------------------|------------------------------------------|
| `_attn_implementation_autoset`: true      | `_attn_implementation_autoset`: true     |
| `_name_or_path`: "meta-llama/Llama-3.2-1B"| `_name_or_path`: "mistralai/Mistral-7B-Instruct-v0.2" |
| `architectures`: ["LlamaForCausalLM"]     | `architectures`: ["MistralForCausalLM"]  |
| `attention_bias`: false                   |                                          |
| `attention_dropout`: 0.0                  | `attention_dropout`: 0.0                 |
| `bos_token_id`: 128000                    | `bos_token_id`: 1                        |
| `eos_token_id`: 128001                    | `eos_token_id`: 2                        |
| `head_dim`: 64                            | `head_dim`: 128                          |
| `hidden_act`: "silu"                      | `hidden_act`: "silu"                     |
| `hidden_size`: 2048                       | `hidden_size`: 4096                      |
| `initializer_range`: 0.02                 | `initializer_range`: 0.02                |
| `intermediate_size`: 8192                 | `intermediate_size`: 14336               |
| `max_position_embeddings`: 131072         | `max_position_embeddings`: 32768         |
| `mlp_bias`: false                         |                                          |
| `model_type`: "llama"                     | `model_type`: "mistral"                  |
| `num_attention_heads`: 32                 | `num_attention_heads`: 32                |
| `num_hidden_layers`: 16                   | `num_hidden_layers`: 32                  |
| `num_key_value_heads`: 8                  | `num_key_value_heads`: 8                 |
| `pretraining_tp`: 1                       |                                          |
| `rms_norm_eps`: 1e-05                     | `rms_norm_eps`: 1e-05                    |
| `rope_scaling`:                           |                                          |
| &nbsp;&nbsp; `factor`: 32.0               |                                          |
| &nbsp;&nbsp; `high_freq_factor`: 4.0      |                                          |
| &nbsp;&nbsp; `low_freq_factor`: 1.0       |                                          |
| &nbsp;&nbsp; `original_max_position_embeddings`: 8192 |                   |
| &nbsp;&nbsp; `rope_type`: "llama3"        |                                          |
| `rope_theta`: 500000.0                    | `rope_theta`: 1000000.0                  |
| `tie_word_embeddings`: true               | `tie_word_embeddings`: false             |
| `torch_dtype`: "bfloat16"                 | `torch_dtype`: "bfloat16"                |
| `transformers_version`: "4.46.1"          | `transformers_version`: "4.46.1"         |
| `use_cache`: true                         | `use_cache`: true                        |
| `vocab_size`: 128256                      | `vocab_size`: 32000                      |


    print(model)

| **LlamaModel**                                                                 | **MistralModel**                                                                 |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `(embed_tokens): Embedding(128256, 2048)`                                     | `(embed_tokens): Embedding(32000, 4096)`                                         |
| `(layers): ModuleList(`                                                       | `(layers): ModuleList(`                                                          |
| &nbsp;&nbsp; `(0-15): 16 x LlamaDecoderLayer(`                                 | &nbsp;&nbsp; `(0-31): 32 x MistralDecoderLayer(`                                 |
| &nbsp;&nbsp;&nbsp;&nbsp; `(self_attn): LlamaSdpaAttention(`                    | &nbsp;&nbsp;&nbsp;&nbsp; `(self_attn): MistralSdpaAttention(`                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(q_proj): Linear(2048, 2048, bias=False)`| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(q_proj): Linear(4096, 4096, bias=False)`  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(k_proj): Linear(2048, 512, bias=False)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(k_proj): Linear(4096, 1024, bias=False)`  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(v_proj): Linear(2048, 512, bias=False)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(v_proj): Linear(4096, 1024, bias=False)`  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(o_proj): Linear(2048, 2048, bias=False)`| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(o_proj): Linear(4096, 4096, bias=False)`  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(rotary_emb): LlamaRotaryEmbedding()`    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `(rotary_emb): MistralRotaryEmbedding()`    |
| &nbsp;&nbsp; `)`                                                              | &nbsp;&nbsp; `)`                                                                 |
| &nbsp;&nbsp; `(mlp): LlamaMLP(`                                               | &nbsp;&nbsp; `(mlp): MistralMLP(`                                               |
| &nbsp;&nbsp;&nbsp;&nbsp; `(gate_proj): Linear(2048, 8192, bias=False)`         | &nbsp;&nbsp;&nbsp;&nbsp; `(gate_proj): Linear(4096, 14336, bias=False)`          |
| &nbsp;&nbsp;&nbsp;&nbsp; `(up_proj): Linear(2048, 8192, bias=False)`           | &nbsp;&nbsp;&nbsp;&nbsp; `(up_proj): Linear(4096, 14336, bias=False)`            |
| &nbsp;&nbsp;&nbsp;&nbsp; `(down_proj): Linear(8192, 2048, bias=False)`         | &nbsp;&nbsp;&nbsp;&nbsp; `(down_proj): Linear(14336, 4096, bias=False)`          |
| &nbsp;&nbsp;&nbsp;&nbsp; `(act_fn): SiLU()`                                    | &nbsp;&nbsp;&nbsp;&nbsp; `(act_fn): SiLU()`                                      |
| &nbsp;&nbsp; `)`                                                              | &nbsp;&nbsp; `)`                                                                 |
| &nbsp;&nbsp; `(input_layernorm): LlamaRMSNorm((2048,), eps=1e-05)`             | &nbsp;&nbsp; `(input_layernorm): MistralRMSNorm((4096,), eps=1e-05)`             |
| &nbsp;&nbsp; `(post_attention_layernorm): LlamaRMSNorm((2048,), eps=1e-05)`    | &nbsp;&nbsp; `(post_attention_layernorm): MistralRMSNorm((4096,), eps=1e-05)`    |
| `)`                                                                           | `)`                                                                              |
| `(norm): LlamaRMSNorm((2048,), eps=1e-05)`                                    | `(norm): MistralRMSNorm((4096,), eps=1e-05)`                                     |
| `(rotary_emb): LlamaRotaryEmbedding()`                                        |                                                                                  |



