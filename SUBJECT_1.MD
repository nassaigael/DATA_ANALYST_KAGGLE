# 📦 Projets Data Analyst Junior — Amazon Dataset

**Dataset :** `amazon.csv` — 1 465 produits Amazon India avec prix, remises, notes et avis clients.

**Colonnes disponibles :** `product_id`, `product_name`, `category`, `discounted_price`, `actual_price`, `discount_percentage`, `rating`, `rating_count`, `about_product`, `user_id`, `user_name`, `review_id`, `review_title`, `review_content`, `img_link`, `product_link`

---

## 🌳 Arborescence du projet

```
amazon-data-analyst/
│
├── data/
│   └── amazon.csv
│
├── outputs/
│   ├── dashboard_categories.csv
│   └── rapport_qualite.txt
│
├── common/
│   └── utils.ipynb            ← Notebook commun : toutes les fonctions réutilisables
│
├── niveau_1_debutant/
│   ├── ex1_1_exploration.ipynb
│   ├── ex1_2_nettoyage.ipynb
│   ├── ex1_3_stats_base.ipynb
│   ├── ex1_4_filtrage.ipynb
│   └── ex1_5_tri.ipynb
│
├── niveau_2_intermediaire/
│   ├── ex2_1_categories.ipynb
│   ├── ex2_2_analyse_categories.ipynb
│   ├── ex2_3_remise_vs_note.ipynb
│   ├── ex2_4_top_par_categorie.ipynb
│   ├── ex2_5_anomalies_prix.ipynb
│   └── ex2_6_visualisation_prix.ipynb
│
├── niveau_3_avance/
│   ├── ex3_1_score_popularite.ipynb
│   ├── ex3_2_analyse_avis.ipynb
│   ├── ex3_3_dashboard.ipynb
│   ├── ex3_4_qualite_donnees.ipynb
│   └── ex3_5_mini_projet.ipynb
│
└── requirements.txt
```

> 💡 `common/utils.ipynb` centralise les fonctions de nettoyage, de calcul de score, etc. Comme un notebook ne s'importe pas nativement comme un module Python, on utilise le package `ipynb` (ou on exécute le notebook via `%run`) pour réutiliser ses fonctions dans les autres notebooks. Chaque fonction écrite dans un niveau doit être **exportée** (recopiée dans la cellule de `utils.ipynb`) si elle est réutilisée plus tard.

---

## 🧩 Notebook commun : `common/utils.ipynb`

Pour éviter de réécrire le même code de nettoyage ou de calcul dans chaque notebook, on centralise les fonctions réutilisables dans `common/utils.ipynb`. **Chaque fois qu'un exercice te demande d'écrire une fonction destinée à être réutilisée plus tard, ajoute-la dans ce notebook et exporte-la.**

**Contenu de `common/utils.ipynb` (une fonction par cellule) :**

```python
# Cellule 1
import pandas as pd
import numpy as np
```

```python
# Cellule 2
def charger_dataset(path: str) -> pd.DataFrame:
    """Charge le CSV Amazon depuis le chemin donné."""
    return pd.read_csv(path)
```

```python
# Cellule 3
def nettoyer_colonnes_numeriques(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie discounted_price, actual_price, discount_percentage, rating_count
    (retire ₹, %, ,) et les convertit en float.
    Utilisée dès le Projet 1.2, puis importée par tous les niveaux suivants.
    """
    df = df.copy()
    df["discounted_price"] = (
        df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
    )
    df["actual_price"] = (
        df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)
    )
    df["discount_percentage"] = (
        df["discount_percentage"].str.replace("%", "").astype(float)
    )
    df["rating_count"] = (
        df["rating_count"].str.replace(",", "").astype(float)
    )
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df
```

```python
# Cellule 4
def extraire_main_category(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute la colonne main_category à partir de category (premier niveau avant '|')."""
    df = df.copy()
    df["main_category"] = df["category"].str.split("|").str[0]
    return df
```

```python
# Cellule 5
def calculer_popularity_score(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute popularity_score = rating * log10(rating_count + 1)."""
    df = df.copy()
    df["popularity_score"] = df["rating"] * np.log10(df["rating_count"] + 1)
    return df
```

```python
# Cellule 6
def calculer_discount_range(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute discount_range : tranche de remise (0-25%, 25-50%, 50-75%, 75-100%)."""
    df = df.copy()
    bins = [0, 25, 50, 75, 100]
    labels = ["0-25%", "25-50%", "50-75%", "75-100%"]
    df["discount_range"] = pd.cut(df["discount_percentage"], bins=bins, labels=labels)
    return df
```

**Comment réutiliser ce notebook depuis un autre notebook :**

Un notebook ne s'importe pas avec `import` comme un fichier `.py`. Deux options pour réutiliser `utils.ipynb` :

**Option A — `%run` (la plus simple, recommandée pour ce projet) :**
Place cette ligne dans la **première cellule** de chaque exercice. Elle exécute tout `utils.ipynb` et rend ses fonctions disponibles directement dans le notebook courant.

```python
# Première cellule de chaque notebook d'exercice
%run ../common/utils.ipynb
```

**Option B — package `ipynb` (si tu veux un import plus explicite) :**

```bash
pip install ipynb
```

```python
from ipynb.fs.full.utils import charger_dataset, nettoyer_colonnes_numeriques
```

> ⚠️ Pour `%run`, le chemin est relatif à l'emplacement du notebook : depuis `niveau_2_intermediaire/`, on remonte d'un niveau (`../common/utils.ipynb`).

**Exemple concret — première cellule de `ex2_1_categories.ipynb` :**

```python
# Cellule 1 : on charge toutes les fonctions communes
%run ../common/utils.ipynb
```

```python
# Cellule 2 : on les utilise directement
df = charger_dataset("../data/amazon.csv")
df = nettoyer_colonnes_numeriques(df)
df = extraire_main_category(df)
df.head()
```

```python
# Cellule 3 : à toi de jouer pour la suite de l'exercice !
```

---

## 🟢 Niveau 1 — Débutant : Chargement & Exploration

### Projet 1.1 — Première exploration
**Fichier :** `niveau_1_debutant/ex1_1_exploration.ipynb`

Charge le fichier `amazon.csv` avec pandas et réponds aux questions suivantes :

- Combien y a-t-il de lignes et de colonnes ?
- Quels sont les noms des colonnes et leurs types (`dtypes`) ?
- Y a-t-il des valeurs manquantes ? Dans quelles colonnes ?
- Affiche les 5 premières lignes du dataset.

**Structure du notebook (cellules) :**

```python
# Cellule 1 — import
import pandas as pd
```

```python
# Cellule 2 — chargement
df = pd.read_csv("../data/amazon.csv")
df.head()
```

```python
# Cellule 3 — à toi de jouer ! (shape, dtypes, valeurs manquantes...)
```

**📥 Import :** aucun (premier fichier, pandas direct)
**📤 Export vers `common/utils.ipynb` :** fonction `charger_dataset(path)` — à créer ici et recopier dans `utils.ipynb` une fois validée, pour que tous les notebooks suivants l'utilisent via `%run` au lieu de refaire `pd.read_csv()`.

### Projet 1.2 — Nettoyage des colonnes numériques
**Fichier :** `niveau_1_debutant/ex1_2_nettoyage.ipynb`

Les colonnes `discounted_price`, `actual_price`, `discount_percentage` et `rating_count` sont stockées comme des chaînes de caractères avec des symboles (₹, %, ,).

- Retire les symboles et convertis ces colonnes en `float`
- Vérifie les types après conversion avec `.dtypes`
- Affiche un `.describe()` sur les colonnes nettoyées

> **Aide :** Utilise `.str.replace()` et `.astype(float)`

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset`
**📤 Export vers `common/utils.ipynb` :** fonction `nettoyer_colonnes_numeriques(df)` — c'est LA fonction la plus réutilisée de tout le projet, elle sera importée par presque tous les exercices suivants.

### Projet 1.3 — Statistiques de base
**Fichier :** `niveau_1_debutant/ex1_3_stats_base.ipynb`

Après nettoyage des colonnes, réponds aux questions suivantes :

- Quel est le prix moyen après réduction ?
- Quel est le pourcentage de réduction moyen ?
- Quelle est la note (`rating`) moyenne de tous les produits ?
- Quel est le produit le moins cher ? Le plus cher ?

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (exercice de lecture/diagnostic, pas de nouvelle fonction réutilisable)

### Projet 1.4 — Filtrage simple
**Fichier :** `niveau_1_debutant/ex1_4_filtrage.ipynb`

Filtre le dataset pour obtenir :

- Tous les produits avec une note `rating >= 4.5`
- Tous les produits avec une réduction supérieure à 70%
- Les produits dont le prix après réduction est inférieur à ₹200

Affiche le nombre de résultats pour chaque filtre.

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (filtres ponctuels, pas de fonction générique à ce stade)

### Projet 1.5 — Tri et sélection
**Fichier :** `niveau_1_debutant/ex1_5_tri.ipynb`

- Trie les produits du mieux noté au moins bien noté
- Trie les produits du plus de réduction au moins
- Affiche uniquement les colonnes `product_name`, `rating`, `discounted_price`, `discount_percentage` pour les 10 produits les moins chers

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun

---

## 🟡 Niveau 2 — Intermédiaire : Analyse & Groupement

### Projet 2.1 — Extraction de la catégorie principale
**Fichier :** `niveau_2_intermediaire/ex2_1_categories.ipynb`

La colonne `category` contient des hiérarchies séparées par `|`
Exemple : `Computers&Accessories|Accessories&Peripherals|Cables`

- Crée une nouvelle colonne `main_category` avec uniquement le premier niveau
- Combien de catégories principales distinctes y a-t-il ?
- Affiche le top 10 des catégories par nombre de produits (avec un graphique à barres)

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.ipynb` :** fonction `extraire_main_category(df)` — réutilisée dans tous les exercices suivants qui groupent par catégorie (2.2, 2.4, 3.3, 3.5).

### Projet 2.2 — Analyse par catégorie
**Fichier :** `niveau_2_intermediaire/ex2_2_analyse_categories.ipynb`

Pour chaque catégorie principale, calcule :

- Le nombre de produits
- Le prix moyen après réduction
- Le discount moyen
- La note moyenne

Affiche le résultat sous forme de tableau trié par nombre de produits décroissant.

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun (le `.groupby()` reste local à cet exercice)

### Projet 2.3 — Relation remise / note
**Fichier :** `niveau_2_intermediaire/ex2_3_remise_vs_note.ipynb`

- Crée une colonne `discount_range` qui classe les produits par tranche de remise : `0-25%`, `25-50%`, `50-75%`, `75-100%`
- Calcule la note moyenne par tranche
- Visualise avec un graphique à barres
- Réponds : Les produits très remisés sont-ils moins bien notés ?

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.ipynb` :** fonction `calculer_discount_range(df)` — réutilisable si un autre exercice (ex: 3.5) souhaite croiser remise/note par tranche.

### Projet 2.4 — Produits les mieux notés par catégorie
**Fichier :** `niveau_2_intermediaire/ex2_4_top_par_categorie.ipynb`

Pour chaque catégorie principale, trouve le produit le mieux noté.

Affiche un tableau avec :

- La catégorie
- Le nom du produit
- La note
- Le prix remisé

> **Aide :** Utilise `.groupby()` + `.idxmax()`

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun

### Projet 2.5 — Détection d'anomalies de prix
**Fichier :** `niveau_2_intermediaire/ex2_5_anomalies_prix.ipynb`

- Après nettoyage, identifie les produits où `discounted_price > actual_price` (anomalie)
- Identifie les produits où `discount_percentage` ne correspond pas au calcul réel :
  `((actual_price - discounted_price) / actual_price) * 100`
- Combine les deux : affiche tous les produits suspects

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (logique de détection spécifique à cet exercice)

### Projet 2.6 — Visualisation des prix
**Fichier :** `niveau_2_intermediaire/ex2_6_visualisation_prix.ipynb`

Crée les visualisations suivantes avec matplotlib ou seaborn :

- Histogramme de la distribution des prix après réduction
- Boxplot des prix par top 5 catégories principales
- Scatter plot : `discount_percentage` en X, `rating` en Y (coloré par catégorie principale)

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun

---

## 🔴 Niveau 3 — Avancé : Scoring, Texte & Synthèse

### Projet 3.1 — Score de popularité
**Fichier :** `niveau_3_avance/ex3_1_score_popularite.ipynb`

Crée un score de popularité qui combine la note ET le volume d'avis :

```
score = rating × log10(rating_count + 1)
```

- Ajoute cette colonne `popularity_score` au dataframe
- Affiche le top 20 des produits selon ce score
- Compare avec le classement par `rating` seul — est-ce très différent ?

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.ipynb` :** fonction `calculer_popularity_score(df)` — réutilisée dans 3.3 (dashboard) et 3.5 (mini-projet final).

### Projet 3.2 — Analyse des mots-clés dans les avis
**Fichier :** `niveau_3_avance/ex3_2_analyse_avis.ipynb`

Utilise la colonne `review_title` pour une analyse textuelle simple :

- Sépare les produits en deux groupes : bons (`rating >= 4`) et mauvais (`rating < 3`)
- Pour chaque groupe, compte les 20 mots les plus fréquents dans les titres d'avis (retire les stopwords courants : "good", "product", "the", "a", "is"...)
- Affiche les résultats sous forme de tableau ou de nuage de mots (wordcloud)

```python
from collections import Counter
# ou
from wordcloud import WordCloud
```

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (sauf si tu veux créer `compter_mots_frequents(textes, stopwords)` réutilisable, optionnel)

### Projet 3.3 — Tableau de bord synthétique
**Fichier :** `niveau_3_avance/ex3_3_dashboard.ipynb`

Construis un tableau de bord complet par catégorie principale avec les métriques suivantes :

| Catégorie | Nb produits | Prix moyen | Remise moyenne | Note moyenne | Score popularité moyen |
|---|---|---|---|---|---|

- Exporte ce tableau en fichier CSV (`dashboard_categories.csv`)
- Identifie la catégorie avec le meilleur rapport qualité/prix (note haute + prix bas)
- Identifie la catégorie la plus compétitive (remise la plus forte)

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category, calculer_popularity_score`
**📤 Export :** le CSV `dashboard_categories.csv` est exporté dans `outputs/` (pas une fonction du notebook commun, mais un fichier de données pour le rapport final 3.4 et le mini-projet 3.5).

### Projet 3.4 — Rapport de qualité des données
**Fichier :** `niveau_3_avance/ex3_4_qualite_donnees.ipynb`

En tant que data analyst, tu dois produire un rapport de qualité du dataset :

- Taux de valeurs manquantes par colonne
- Taux de doublons (`product_id` en double ?)
- Vérification de cohérence : les prix sont-ils tous positifs ?
- Distribution des notes : y a-t-il des valeurs aberrantes ?

Génère un fichier `rapport_qualite.txt` avec un résumé de tes observations.

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** le fichier `rapport_qualite.txt` est exporté dans `outputs/` (livrable texte, pas une fonction)

### Projet 3.5 — Mini-projet final
**Fichier :** `niveau_3_avance/ex3_5_mini_projet.ipynb`

**Objectif :** Répondre à la question business suivante :

> « Quels types de produits offrent le meilleur équilibre entre attractivité (forte remise), qualité (bonne note) et popularité (nombreux avis) ? »

Construis une analyse complète :

1. Nettoie et prépare les données (reprends tes fonctions des Projets précédents)
2. Calcule un score global combinant remise, note et popularité (définis ta propre formule et justifie-la)
3. Visualise les top 10 produits selon ce score avec leurs infos clés
4. Rédige une conclusion en commentaires dans ton code (3-5 lignes) avec ta recommandation

**📥 Import :** `%run ../common/utils.ipynb` (en première cellule) — fonctions utilisées : `charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category, calculer_popularity_score, calculer_discount_range`
**📤 Export :** ce fichier consomme TOUT le module commun construit depuis le Projet 1.2 — c'est l'aboutissement du projet, aucune nouvelle fonction n'est nécessaire à exporter.

---

## 📁 Récapitulatif des fichiers

| Fichier | Niveau | Thème |
|---|---|---|
| `ex1_1_exploration.ipynb` | 🟢 | Chargement et première vue |
| `ex1_2_nettoyage.ipynb` | 🟢 | Nettoyage des types |
| `ex1_3_stats_base.ipynb` | 🟢 | Statistiques descriptives |
| `ex1_4_filtrage.ipynb` | 🟢 | Filtrage conditionnel |
| `ex1_5_tri.ipynb` | 🟢 | Tri et sélection |
| `ex2_1_categories.ipynb` | 🟡 | Extraction de catégories |
| `ex2_2_analyse_categories.ipynb` | 🟡 | Groupement et agrégation |
| `ex2_3_remise_vs_note.ipynb` | 🟡 | Analyse croisée |
| `ex2_4_top_par_categorie.ipynb` | 🟡 | GroupBy avancé |
| `ex2_5_anomalies_prix.ipynb` | 🟡 | Détection d'anomalies |
| `ex2_6_visualisation_prix.ipynb` | 🟡 | Visualisation |
| `ex3_1_score_popularite.ipynb` | 🔴 | Feature engineering |
| `ex3_2_analyse_avis.ipynb` | 🔴 | Analyse textuelle |
| `ex3_3_dashboard.ipynb` | 🔴 | Synthèse & export |
| `ex3_4_qualite_donnees.ipynb` | 🔴 | Qualité des données |
| `ex3_5_mini_projet.ipynb` | 🔴 | Projet intégré |

---

## 🛠️ Librairies recommandées

```bash
pip install pandas matplotlib seaborn wordcloud jupyterlab notebook ipynb
```

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np
```

**Pour lancer l'environnement de travail :**

```bash
jupyter lab
# ou
jupyter notebook
```

> 💡 Conseil de data analyst : garde une cellule Markdown au-dessus de chaque section pour documenter ta démarche (titre, question posée, observation). C'est ce qui distingue un notebook d'analyse propre d'une suite de cellules de code.

---

**Bonne analyse !** Commence par le niveau 1 et avance progressivement. Chaque Projet s'appuie sur le précédent. 🚀