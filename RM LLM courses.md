[Start here](https://github.com/mlabonne/llm-course)

Autoregressive : they generate the next tokens based on the sequence of tokens already generated

Attention mechanism : establishing word connections and ensures the text is coherent and contextually appropriate

## Recurrent Neural Networks (RNNs) and the vanishing gradient problem

1. **Difficulté avec les séquences longues** : Les RNNs tendent à "oublier" les informations anciennes au profit des informations récentes dans la séquence. Cela signifie que, plus la séquence est longue, plus le réseau a du mal à se souvenir des éléments en début de séquence.

2. **Cause principale : le problème de gradient évanescent** : Ce phénomène se produit lors de l'entraînement du réseau. Pendant le processus de rétropropagation, qui permet d'ajuster les poids du réseau pour minimiser l'erreur, les gradients (les valeurs qui déterminent la correction à appliquer) deviennent de plus en plus petits à mesure qu'ils sont propagés à travers chaque étape temporelle de la séquence.

3. **Effet du gradient évanescent** : Lorsque les gradients deviennent très faibles, les mises à jour des poids deviennent négligeables pour les premières parties de la séquence. Cela empêche le réseau de "retenir" efficacement des informations des premiers éléments de la séquence et limite sa capacité à capturer des dépendances à long terme.

C'est pourquoi des architectures comme les LSTM (Long Short-Term Memory) ou GRU (Gated Recurrent Unit) ont été introduites pour pallier cette limitation, en ajoutant des mécanismes permettant de mieux conserver des informations sur des périodes plus longues.

Transformer-based models addressed these challenges and
emerged as the preferred architecture for natural language
processing tasks. This architecture introduced in the
influential paper [Attention Is All You Need](https://arxiv.org/pdf/1706.03762)

## Decoder only 

Les modèles comme LLaMA utilisent une architecture de type "decoder-only" (uniquement décodeur), mais cela ne signifie pas qu'ils ne peuvent pas encoder une phrase. Voici comment ils fonctionnent pour traiter une entrée :

1. **Encodage des tokens** : Tout d'abord, l'entrée (la phrase) est divisée en unités appelées tokens, qui sont des sous-mots ou mots entiers, selon la méthode de tokenisation. Chaque token est ensuite converti en vecteur numérique par une étape d'embedding (représentation vectorielle). Cela transforme le texte d'entrée en une séquence de vecteurs numériques que le modèle peut traiter.

2. **Auto-régression** : Dans une architecture "decoder-only", l'attention est auto-régressive, ce qui signifie que chaque token est traité en fonction des tokens précédents, et non des suivants. Cette attention masque les futurs tokens pour que chaque token "ne regarde" que ce qui le précède, imitant un processus de génération étape par étape.

3. **Empilement des couches de transformeur** : Le modèle est constitué de plusieurs couches de transformeur, qui traitent cette séquence de vecteurs. Chaque couche applique une attention multi-tête et des transformations linéaires pour produire des représentations de plus en plus complexes de la séquence d’entrée. Bien que le modèle soit un décodeur, ces couches d'attention permettent de capturer et de "coder" le contexte de la phrase d'entrée.

4. **Représentation finale** : Une fois que tous les tokens de la phrase ont été traités, chaque token dans la séquence contient une représentation encodée du contexte global (dans la mesure où il s’agit des tokens précédents). Pour des tâches de génération, le modèle utilise la dernière représentation pour prédire le token suivant. Pour d’autres types de tâches (comme la classification de séquence), le modèle peut utiliser la représentation d’un token spécial (par exemple, celui qui marque le début de la séquence) pour résumer l’ensemble de la phrase.

En résumé, même s'il s'agit d'un modèle de type "decoder-only", le modèle peut encore "encoder" une phrase grâce aux mécanismes d’attention et aux représentations vectorielles des tokens, mais il le fait de manière auto-régressive. Il utilise le contexte des tokens précédents pour créer une représentation riche de l'entrée.

## Tokenization

The tokenization process is model-dependent

Advanced techniques, like the Byte-Pair encoding

Le Byte-Pair Encoding (BPE) est une technique de tokenisation sous-mot (subword tokenization). Dans le contexte du traitement du langage naturel, BPE est utilisé pour diviser les mots en unités plus petites (souvent appelées "sous-mots" ou "subwords"), ce qui aide le modèle à traiter des mots rares, des mots inconnus et des variations morphologiques.

Voici comment fonctionne BPE en tant que technique de tokenisation sous-mot :

1. **Décomposition en caractères** : Au début, chaque mot est représenté comme une séquence de caractères individuels, ce qui permet de créer un vocabulaire minimal.

2. **Fusion des paires de caractères** : Ensuite, la méthode identifie les paires de caractères qui apparaissent le plus fréquemment dans le texte d’entraînement et les fusionne en nouvelles unités. Ce processus est répété de manière itérative pour former des sous-mots de plus en plus longs.

3. **Formation d'un vocabulaire de sous-mots** : Ce processus de fusion continue jusqu'à ce que le vocabulaire atteigne une taille définie, contenant des unités qui sont souvent plus petites que des mots mais plus grandes que des caractères individuels. Le vocabulaire final contient donc des sous-mots, des racines communes et des affixes (préfixes, suffixes), permettant une représentation flexible.

4. **Avantages de la tokenisation sous-mot** : La tokenisation sous-mot comme BPE permet au modèle de traiter de manière efficace les mots rares ou nouveaux, car il peut les diviser en sous-mots existants dans le vocabulaire. Par exemple, le modèle peut traiter "running" comme "run" et "ning" si "running" ne figure pas dans le vocabulaire. Cela aide à réduire la taille du vocabulaire et à augmenter la généralisation.

BPE est largement utilisé dans les modèles de langage modernes, notamment dans les modèles de type transformeur, car il offre un bon équilibre entre la gestion des mots rares et la réduction de la taille du vocabulaire.

## NExt step : Embedding

## Training / Fine-Tuning 

https://commoncrawl.org/

After pre-training, the model typically undergoes fine-tuning
for a specific task. This stage requires further training on a
smaller dataset for a task (e.g., text translation) or a
specialized domain (e.g., biomedical, finance, etc.)

## Context size 

4o :  4,096 tokens
OpenAI's GPT-4-turbo-32k (with a 32,768-token context) 
OpenAI o1-preview model features a context window of 128,000 tokens