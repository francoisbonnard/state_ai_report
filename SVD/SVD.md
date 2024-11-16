D'accord, décomposons la matrice \( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \) en utilisant la **Décomposition en Valeurs Singulières (SVD)**. Nous allons suivre chaque étape de manière détaillée.

\[
A = U \Sigma V^T
\]

où :
- \( U \) est une matrice orthogonale \( 2 \times 2 \),
- \( \Sigma \) est une matrice diagonale \( 2 \times 2 \) contenant les valeurs singulières,
- \( V^T \) est la transposée d'une matrice orthogonale \( V \).

### Étape 1 : Calcul de \( A^T A \)

Premièrement, calculons le produit \( A^T A \).

\[
A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
\]

\[
A^T A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 \times 1 + 3 \times 3 & 1 \times 2 + 3 \times 4 \\ 2 \times 1 + 4 \times 3 & 2 \times 2 + 4 \times 4 \end{bmatrix} = \begin{bmatrix} 10 & 14 \\ 14 & 20 \end{bmatrix}
\]

### Étape 2 : Calcul des Valeurs Propres de \( A^T A \)

Les valeurs singulières de \( A \) sont les racines carrées des valeurs propres de \( A^T A \). Pour trouver ces valeurs propres, résolvons le déterminant suivant :

\[
\det(A^T A - \lambda I) = 0
\]

\[
\det\begin{bmatrix} 10 - \lambda & 14 \\ 14 & 20 - \lambda \end{bmatrix} = (10 - \lambda)(20 - \lambda) - 14^2 = \lambda^2 - 30\lambda + 4 = 0
\]

Résolvons l'équation quadratique :

\[
\lambda^2 - 30\lambda + 4 = 0
\]

\[
\lambda = \frac{30 \pm \sqrt{900 - 16}}{2} = \frac{30 \pm \sqrt{884}}{2} = \frac{30 \pm 2\sqrt{221}}{2} = 15 \pm \sqrt{221}
\]

Approximativement :

\[
\lambda_1 \approx 15 + 14.8661 = 29.8661
\]

\[
\lambda_2 \approx 15 - 14.8661 = 0.1339
\]

Les valeurs singulières sont donc :

\[
\sigma_1 = \sqrt{29.8661} \approx 5.465
\]

\[
\sigma_2 = \sqrt{0.1339} \approx 0.366
\]

### Étape 3 : Calcul des Vecteurs Propres de \( A^T A \) (Matrice \( V \))

Pour chaque valeur propre \( \lambda \), trouvons le vecteur propre correspondant.

#### 3.1. Pour \( \lambda_1 \approx 29.8661 \) :

Résolvons \( (A^T A - \lambda_1 I) \mathbf{v} = 0 \).

\[
\begin{bmatrix} 10 - 29.8661 & 14 \\ 14 & 20 - 29.8661 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} -19.8661 & 14 \\ 14 & -9.8661 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\]

Cela donne l'équation :

\[
-19.8661 v_1 + 14 v_2 = 0 \quad \Rightarrow \quad v_1 = \frac{14}{19.8661} v_2 \approx 0.705 v_2
\]

Choisissons \( v_2 = 1 \), alors :

\[
v_1 \approx 0.705
\]

Le vecteur propre non normalisé est donc :

\[
\mathbf{v}_1 \approx \begin{bmatrix} 0.705 \\ 1 \end{bmatrix}
\]

Normalisons ce vecteur :

\[
\|\mathbf{v}_1\| = \sqrt{0.705^2 + 1^2} \approx \sqrt{0.497 + 1} = \sqrt{1.497} \approx 1.223
\]

Ainsi, le vecteur propre normalisé est :

\[
\mathbf{v}_1 \approx \begin{bmatrix} \frac{0.705}{1.223} \\ \frac{1}{1.223} \end{bmatrix} \approx \begin{bmatrix} 0.577 \\ 0.817 \end{bmatrix}
\]

#### 3.2. Pour \( \lambda_2 \approx 0.1339 \) :

Résolvons \( (A^T A - \lambda_2 I) \mathbf{v} = 0 \).

\[
\begin{bmatrix} 10 - 0.1339 & 14 \\ 14 & 20 - 0.1339 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 9.8661 & 14 \\ 14 & 19.8661 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\]

Cela donne l'équation :

\[
9.8661 v_1 + 14 v_2 = 0 \quad \Rightarrow \quad v_1 = -\frac{14}{9.8661} v_2 \approx -1.419 v_2
\]

Choisissons \( v_2 = 1 \), alors :

\[
v_1 \approx -1.419
\]

Le vecteur propre non normalisé est donc :

\[
\mathbf{v}_2 \approx \begin{bmatrix} -1.419 \\ 1 \end{bmatrix}
\]

Normalisons ce vecteur :

\[
\|\mathbf{v}_2\| = \sqrt{(-1.419)^2 + 1^2} \approx \sqrt{2.014 + 1} = \sqrt{3.014} \approx 1.737
\]

Ainsi, le vecteur propre normalisé est :

\[
\mathbf{v}_2 \approx \begin{bmatrix} \frac{-1.419}{1.737} \\ \frac{1}{1.737} \end{bmatrix} \approx \begin{bmatrix} -0.817 \\ 0.577 \end{bmatrix}
\]

#### 3.3. Formation de la Matrice \( V \)

Les vecteurs propres normalisés forment les colonnes de \( V \) :

\[
V = \begin{bmatrix} 0.577 & -0.817 \\ 0.817 & 0.577 \end{bmatrix}
\]

### Étape 4 : Calcul de la Matrice \( \Sigma \)

La matrice \( \Sigma \) est une matrice diagonale contenant les valeurs singulières \( \sigma_1 \) et \( \sigma_2 \) :

\[
\Sigma = \begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix} = \begin{bmatrix} 5.465 & 0 \\ 0 & 0.366 \end{bmatrix}
\]

### Étape 5 : Calcul de la Matrice \( U \)

Pour trouver \( U \), nous utilisons la relation :

\[
U = A V \Sigma^{-1}
\]

Calculons \( \Sigma^{-1} \) :

\[
\Sigma^{-1} = \begin{bmatrix} \frac{1}{5.465} & 0 \\ 0 & \frac{1}{0.366} \end{bmatrix} \approx \begin{bmatrix} 0.183 & 0 \\ 0 & 2.732 \end{bmatrix}
\]

Ensuite, calculons \( A V \) :

\[
A V = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0.577 & -0.817 \\ 0.817 & 0.577 \end{bmatrix} = \begin{bmatrix} 1 \times 0.577 + 2 \times 0.817 & 1 \times (-0.817) + 2 \times 0.577 \\ 3 \times 0.577 + 4 \times 0.817 & 3 \times (-0.817) + 4 \times 0.577 \end{bmatrix}
\]

Calculons les éléments :

\[
A V = \begin{bmatrix} 0.577 + 1.634 & -0.817 + 1.154 \\ 1.731 + 3.268 & -2.451 + 2.308 \end{bmatrix} = \begin{bmatrix} 2.211 & 0.337 \\ 5.0 & -0.143 \end{bmatrix}
\]

Maintenant, multiplions \( A V \) par \( \Sigma^{-1} \) :

\[
U = A V \Sigma^{-1} = \begin{bmatrix} 2.211 & 0.337 \\ 5.0 & -0.143 \end{bmatrix} \begin{bmatrix} 0.183 & 0 \\ 0 & 2.732 \end{bmatrix} = \begin{bmatrix} 2.211 \times 0.183 + 0.337 \times 0 & 2.211 \times 0 + 0.337 \times 2.732 \\ 5.0 \times 0.183 + (-0.143) \times 0 & 5.0 \times 0 + (-0.143) \times 2.732 \end{bmatrix}
\]

Calculons les éléments :

\[
U = \begin{bmatrix} 0.404 & 0.920 \\ 0.915 & -0.390 \end{bmatrix}
\]

Cependant, nous devons nous assurer que les colonnes de \( U \) sont orthonormées. Vérifions la normalisation :

\[
\|\mathbf{u}_1\| = \sqrt{0.404^2 + 0.915^2} \approx \sqrt{0.163 + 0.837} = \sqrt{1} = 1
\]

\[
\|\mathbf{u}_2\| = \sqrt{0.920^2 + (-0.390)^2} \approx \sqrt{0.846 + 0.152} = \sqrt{0.998} \approx 1
\]

Ainsi, les colonnes de \( U \) sont déjà normalisées.

#### 5.1. Vérification de l'Orthogonalité

Vérifions que les colonnes de \( U \) sont orthogonales :

\[
\mathbf{u}_1 \cdot \mathbf{u}_2 = 0.404 \times 0.920 + 0.915 \times (-0.390) \approx 0.372 - 0.357 = 0.015 \approx 0
\]

Une petite erreur numérique due aux approximations, mais \( U \) est essentiellement orthogonal.

#### 5.2. Formation de la Matrice \( U \)

\[
U = \begin{bmatrix} 0.404 & 0.920 \\ 0.915 & -0.390 \end{bmatrix}
\]

### Étape 6 : Formation de la Matrice \( V^T \)

Nous avons déjà calculé \( V \). Pour obtenir \( V^T \), transposons simplement \( V \) :

\[
V^T = \begin{bmatrix} 0.577 & 0.817 \\ -0.817 & 0.577 \end{bmatrix}
\]

### Étape 7 : Vérification Finale

Vérifions que \( A = U \Sigma V^T \) :

\[
U \Sigma V^T = \begin{bmatrix} 0.404 & 0.920 \\ 0.915 & -0.390 \end{bmatrix} \begin{bmatrix} 5.465 & 0 \\ 0 & 0.366 \end{bmatrix} \begin{bmatrix} 0.577 & 0.817 \\ -0.817 & 0.577 \end{bmatrix}
\]

Calculons \( U \Sigma \) :

\[
U \Sigma = \begin{bmatrix} 0.404 \times 5.465 + 0.920 \times 0 & 0.404 \times 0 + 0.920 \times 0.366 \\ 0.915 \times 5.465 + (-0.390) \times 0 & 0.915 \times 0 + (-0.390) \times 0.366 \end{bmatrix} = \begin{bmatrix} 2.205 & 0.336 \\ 5.0 & -0.143 \end{bmatrix}
\]

Ensuite, multiplions par \( V^T \) :

\[
U \Sigma V^T = \begin{bmatrix} 2.205 & 0.336 \\ 5.0 & -0.143 \end{bmatrix} \begin{bmatrix} 0.577 & 0.817 \\ -0.817 & 0.577 \end{bmatrix} = \begin{bmatrix} 2.205 \times 0.577 + 0.336 \times (-0.817) & 2.205 \times 0.817 + 0.336 \times 0.577 \\ 5.0 \times 0.577 + (-0.143) \times (-0.817) & 5.0 \times 0.817 + (-0.143) \times 0.577 \end{bmatrix}
\]

Calculons les éléments :

\[
U \Sigma V^T \approx \begin{bmatrix} 1.274 - 0.274 & 1.801 + 0.194 \\ 2.885 + 0.117 & 4.085 - 0.083 \end{bmatrix} = \begin{bmatrix} 1.0 & 1.995 \\ 3.002 & 4.002 \end{bmatrix} \approx \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = A
\]

La légère différence est due aux arrondis lors des calculs intermédiaires.

### Résultat Final

La décomposition en valeurs singulières de la matrice \( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \) est :

\[
A = U \Sigma V^T = \begin{bmatrix} 0.404 & 0.920 \\ 0.915 & -0.390 \end{bmatrix} \begin{bmatrix} 5.465 & 0 \\ 0 & 0.366 \end{bmatrix} \begin{bmatrix} 0.577 & 0.817 \\ -0.817 & 0.577 \end{bmatrix}
\]

**Résumé des Matrices :**

- **Matrice \( U \) :**

\[
U \approx \begin{bmatrix} 0.404 & 0.920 \\ 0.915 & -0.390 \end{bmatrix}
\]

- **Matrice \( \Sigma \) :**

\[
\Sigma \approx \begin{bmatrix} 5.465 & 0 \\ 0 & 0.366 \end{bmatrix}
\]

- **Matrice \( V \) :**

\[
V \approx \begin{bmatrix} 0.577 & -0.817 \\ 0.817 & 0.577 \end{bmatrix}
\]

Ainsi, nous avons réussi à décomposer la matrice \( A \) en ses composantes \( U \), \( \Sigma \), et \( V^T \) selon la méthode de SVD.