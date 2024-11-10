Pour comprendre l'algorithme UMAP (*Uniform Manifold Approximation and Projection*), un niveau en mathématiques de niveau universitaire est utile, en particulier en ce qui concerne l'algèbre linéaire, la géométrie, et un peu de topologie. Voici les concepts mathématiques principaux pour comprendre UMAP en profondeur :

### 1. **Algèbre Linéaire**
   - **Espaces vectoriels** et **transformations linéaires** : UMAP repose sur des opérations qui manipulent des vecteurs dans un espace multidimensionnel.
   - **Décomposition en valeurs propres** : Des concepts comme la réduction de dimension via la décomposition de matrices sont fondamentaux.
   - **Matrices de distance** : Comprendre comment les distances sont calculées dans un espace de haute dimension est important.

### 2. **Géométrie et Géométrie des Manifolds**
   - UMAP est basé sur l’idée de manifolds, des structures qui ressemblent localement à des espaces euclidiens dans des espaces de dimension plus élevée. Avoir une intuition pour la géométrie des manifolds et comprendre comment les données peuvent résider dans des sous-espaces de moindre dimension est essentiel.

### 3. **Théorie de la Topologie**
   - **Simplicial Complexes** : UMAP utilise la notion de complexes simpliciaux (un concept de topologie) pour représenter des relations de voisinage dans des espaces de haute dimension.
   - **Théorie des graphes** et **connexité** : L'algorithme construit un graphe pour représenter la connectivité locale dans l’espace de données original, une approche inspirée par la topologie.
   - **Persistance de voisinage** : UMAP cherche à maintenir la "forme" des données en conservant des relations de voisinage, ce qui est lié aux concepts de continuité et de préservation des structures dans la topologie.

### 4. **Probabilités et Statistiques**
   - **Distribution de distances** : L’algorithme utilise une distribution probabiliste (la distribution uniforme, souvent) pour ajuster les distances entre les points dans le nouvel espace.
   - **Optimisation** : L'algorithme applique des méthodes d'optimisation stochastiques pour ajuster les points dans l’espace réduit, souvent inspiré par des techniques comme l’optimisation par gradient stochastique.

### 5. **Notions en Apprentissage Automatique**
   - Bien que ce ne soit pas un prérequis en mathématiques, avoir des bases en **réduction de dimension** et comprendre comment les algorithmes de projection (comme t-SNE ou PCA) fonctionnent peut aider à comprendre pourquoi et comment UMAP est conçu pour préserver la structure des données à grande échelle.

### Niveau recommandé
Un étudiant de **niveau licence ou maîtrise en mathématiques appliquées** (ou équivalent en sciences des données ou apprentissage automatique) pourrait être bien préparé pour comprendre UMAP. Avoir une certaine expérience avec des concepts de géométrie et de topologie avancées est particulièrement utile pour apprécier la profondeur mathématique de l'algorithme.

# How Umap Work

[how Umap Work](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html)