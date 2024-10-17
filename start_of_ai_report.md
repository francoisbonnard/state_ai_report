# Introduction

## 10 AI chip company Cerebras has filed to IPO

# Research

## 12 Gpt-4o

For example, GPT-4o outperforms Claude 3.5 Sonnet on MMLU, but apparently underperforms it on MMLU-Pro - a benchmark designed to be more challenging.

MMLU (Massive Multitask Language Understanding) est un benchmark conçu pour évaluer les modèles de langage sur leur capacité à comprendre et à raisonner à travers une grande variété de sujets académiques et professionnels. 

Il couvre plus de 57 sujets différents, allant de l’histoire à la physique, en passant par la médecine et les mathématiques. Les tâches sont conçues pour tester des compétences variées, comme la compréhension des concepts, la résolution de problèmes, et le raisonnement complexe. Les questions dans ce benchmark sont souvent de niveau universitaire ou professionnel.

## 13 Chain of thougt COT

o1 reasons through complex prompts step-by-step	
in a chain-of-thought (COT) style, employing RL to sharpen the COT and the strategies it uses	
    
AIME 2024 (competition math), with a	
whopping score of 83.83 versus 13.4.	
    
1M input tokens of	
o1-preview costs $15, while 1M output tokens will set you back $60. This	
makes it 3-4x more expensive than GPT-4o.	
    
[viral video of a PhD student reacting with astonishment](https://www.youtube.com/watch?v=M9YOO7N5jF8)

## 15 Llama 3

Llama 3.1 405B, their largest to-date, is able to hold its own against GPT-4o and Claude 3.5 Sonnet across reasoning, math, multilingual, and	
long-context tasks	
    
decoder-only transformer architecture	
    
GPT-4 : Environ 1,7 trillion de paramètres (estimation) et probablement autour de 10 à 15 trillions de tokens utilisés pour l'entraînement.
LLaMA 2 : Paramètres de 7B à 70B, entraînés sur 2 trillions de tokens.

Meta showcased open AI hardware designs, including the Catalina rack and the expanded Grand Teton platform, at the OCP Global Summit. Training the Llama 3.1 405B model required 16,000 NVIDIA H100 GPUs, highlighting Meta's scaling infrastructure. Open AI hardware systems are required to continue advancing AI capabilities.

Meta used an incredible 15T tokens to train the Llama 3 family	
    
Llama 3.1 405B was trained over 16,000 H100 GPUs, the first	Llama model trained at this scale.	
    
Meta followed up with Llama 3.2 in September, which	incorporated 11B and 90B VLMs (Llama’s multimodal debut).	

## 16 Meaning of Open Source

## 17 Dataset contamination

## 19 LMSYS Chatbot

The LMSYS Chatbot Arena Leaderboard has emerged as the community’s favorite method of formalizing evaluation by “vibes”. But as model performance improves, it’s beginning to produce counterintuitive results

## 20 Are neuro-symbolic systems making a comeback?

With AlphaGeometry, a symbolic deduction engine comes to the rescue
A Google DeepMind/NYU team generated millions of synthetic theorems and proofs using symbolic engines, using them to train a language model from scratch.

## 21 shrink models with minimal impact on performance

NVIDIA researchers took a more radical approach by pruning layers, neurons, attention heads, and embeddings, and then using knowledge distillation for efficient retraining.

## 22 distilled models become more fashionable

Andrej Karpathy and others have argued, current large model sizes could be a reflection of inefficient training.

To support these efforts, the community has started to produce open-source distillation tools, like arcee.ai’s DistillKit, which supports both Logit-based and Hidden states-based distillation

## 23 Models built for mobile compete with their larger peers

## 24 Quantization

## 25 REFT

Parameter-efficient fine-tuning (e.g. via LoRA) is nothing new, but Stanford researchers believe a more targeted approach offers greater efficiency and adaptation.

Inspired by model interpretability research, ReFT (Representation Fine-tuning) doesn’t alter the model’s weights. Instead, it manipulates the model’s internal representations at inference time to steer its behavior.


## 26 Hybrid models begin to gain traction

## 27 And could we distill transformers into hybrid models? It’s…complicated

MOHAWK is a new method for distilling knowledge from a large, pre-trained transformer model (teacher) to a smaller, subquadratic model (student) like a state-space model (SSM).

## 28 Reign of the transformers

## 29 Synthetic data starts gaining more widespread adoption…

Le concept de synthetic data (données synthétiques) dans ce contexte fait référence à des données générées artificiellement plutôt que collectées directement dans le monde réel. Ces données sont créées par des modèles d’intelligence artificielle ou par des algorithmes pour entraîner ou affiner d'autres modèles de machine learning. Les données synthétiques peuvent être utilisées pour simuler des scénarios ou des exemples qui pourraient manquer dans les données réelles, tout en offrant un contrôle plus précis sur la qualité et la diversité des données


## 30 Model Collapse

## 31 Web data is decanted openly at scale - proving quality is key

FineWeb, the dataset


## 32 Retrieval and embeddings hit the center stage

![alt text](./img/image.png)

## 33 Context proves a crucial driver of performance

Traditional RAG solutions usually involve creating text snippets 256 tokens at a time with sliding windows (128	overlapping the prior chunk). This makes retrieval more efficient, but significantly less accurat	

Anthropic solved this using ‘contextual embeddings’, where a prompt instructs the model to generate text explaining the context of each chunk in the document

# industry

## 86 NVIDIA becomes the world’s most powerful company

## 87 Blackwell family of GPUs

The new Blackwell B200 GPU and GB200 Superchip promise significant performance gain over the Hopper
architecture of H100 fame. NVIDIA claims it can reduce cost and energy consumption 25x over an H100

Jensen Huang has argued that every government needs to build its own LLM to preserve its national heritage

## Nvidia Amd Intel

A100 : Il offre des performances impressionnantes pour les tâches de calcul intensif. Par exemple, il propose jusqu'à 312 téraflops de performance en FP16 (virgule flottante 16 bits), très utile pour l'apprentissage profond.
H100 : Les performances sont largement supérieures, avec jusqu’à 1 pétaflop de performance en FP8 (un nouveau format introduit dans Hopper pour l'IA), ce qui représente une amélioration significative pour les modèles d’IA de grande tail

## 92 H100 

![alt text](./img/image3.png)

[Nvidia CEO hand-delivers world's fastest AI system to OpenAI, again — first DGX H200 given to Sam Altman and Greg Brockman](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-ceo-hand-delivers-worlds-fastest-ai-system-to-openai-again-first-dgx-h200-given-to-sam-altman-and-greg-brockman)

1x DGX GH200
Contains 256x GH200s (“Grace Hoppers”)
Each GH200 contains 1x H100 and 1x Grace CPU



## 105 But where’s the revenue…?

![alt text](./img/image4.png)

## 107 Meta Pivot

![alt text](./img/image5.png)

## 111 Chat agents as interactive developer sidekicks…

## 117 Github reigns supreme, but an ecosystem of AI coding companies is growing

By far the most widely-used AI-powered developer tool, Copilot adoption is growing 180% year-over-year and its annual revenue run rate is now $2B (double its 2022 figure). Copilot (40% of Github revenue) alone is now a bigger business than Github was when Microsoft acquired it. However, it’s just one of a number of coding companies, some of which are raising blockbuster rounds.

## 118 ML tools for AI struggle (again)

## 119 Are AI agents going commercial?

## 120 AI-powered search begins to make a dent, amid teething problems

## 145 Hot or not: smart glasses?

## 152 Attention is all you need… to build raise billions for sell your AI start-up

Noam Shazeer of Character.ai sold his team back to Google for $2.5B, while Adept was acqui-hired into Amazon and Inflection into Microsoft for $650M. These deals all involved hiring founders and star employees while paying enough money to investors as a technology licensing fee to get the deals through.

Adept's $429m execuhire to Amazon

Inflection's $650m execuhire to Microsoft

Character.ai's $2.5b execuhire to Google today

Co-auteur d’une recherche fondamentale qui a donné le coup d’envoi du boom de l’intelligence artificielle, Noam Shazeer avait quitté Google en 2021 pour créer sa propre entreprise après que le géant de Mountain View eut refusé de lancer un chatbot qu’il avait mis au point. Lorsque la start-up, Character.AI, a commencé à échouer, son ancien employeur est intervenu.

# 153 Politics

# 174 Safety

# 204 Predictions