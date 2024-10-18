
## Method

![Hugging Face Librairies](./img/image6.png)

https://huggingface.co/arcee-ai/SuperNova-Medius-GGUF

    ollama run arcee-ai/SuperNova-Medius-GGUF

https://github.com/ollama/ollama/blob/5687f1a0cfa3d2408bfcb04f4342f657f6dada58/examples/jupyter-notebook/ollama.ipynb

## GGUF

Les librairies GGUF sur Hugging Face font référence à un nouveau format de modèles, appelé GGUF (GPTQ GGML Unified Format), qui a été développé pour unifier différents formats de modèles optimisés pour une utilisation plus efficace sur du matériel limité ou des dispositifs à faible consommation (comme des ordinateurs personnels ou des serveurs sans GPU puissant). Ce format est particulièrement adapté aux modèles d'IA tels que les grands modèles de langage (LLMs) et se concentre sur l'optimisation pour une exécution plus rapide tout en réduisant les exigences en matière de mémoire.

Objectif : GGUF est conçu pour unifier et simplifier les formats existants comme GGML et GPTQ, qui sont des techniques d'optimisation populaires pour des modèles comme LLaMA. GGML (Generalized Graphical Model Language) est utilisé pour exécuter des modèles sur CPU en réduisant leur taille (en utilisant des techniques comme la quantification), tandis que GPTQ est un autre type de compression des modèles basé sur la quantification pour les rendre plus petits et plus rapides à exécuter.
