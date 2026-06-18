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
│   ├── __init__.py
│   └── utils.py              ← Module commun : toutes les fonctions réutilisables
│
├── niveau_1_debutant/
│   ├── __init__.py
│   ├── ex1_1_exploration.py
│   ├── ex1_2_nettoyage.py
│   ├── ex1_3_stats_base.py
│   ├── ex1_4_filtrage.py
│   └── ex1_5_tri.py
│
├── niveau_2_intermediaire/
│   ├── __init__.py
│   ├── ex2_1_categories.py
│   ├── ex2_2_analyse_categories.py
│   ├── ex2_3_remise_vs_note.py
│   ├── ex2_4_top_par_categorie.py
│   ├── ex2_5_anomalies_prix.py
│   └── ex2_6_visualisation_prix.py
│
├── niveau_3_avance/
│   ├── __init__.py
│   ├── ex3_1_score_popularite.py
│   ├── ex3_2_analyse_avis.py
│   ├── ex3_3_dashboard.py
│   ├── ex3_4_qualite_donnees.py
│   └── ex3_5_mini_projet.py
│
├── requirements.txt
└── README.md
```

> 💡 `common/utils.py` centralise les fonctions de nettoyage, de calcul de score, etc., afin que chaque exercice les **importe** au lieu de les réécrire. Chaque fonction écrite dans un niveau doit être **exportée** (ajoutée à `utils.py`) si elle est réutilisée plus tard.

---

## 🧩 Module commun : `common/utils.py`

Pour éviter de réécrire le même code de nettoyage ou de calcul dans chaque fichier, on centralise les fonctions réutilisables dans `common/utils.py`. **Chaque fois qu'un exercice te demande d'écrire une fonction destinée à être réutilisée plus tard, ajoute-la dans ce fichier et exporte-la.**

```python
# common_utils/utils.py

import pandas as pd
import numpy as np


def charger_dataset(path: str) -> pd.DataFrame:
    """Charge le CSV Amazon depuis le chemin donné."""
    return pd.read_csv(path)


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


def extraire_main_category(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute la colonne main_category à partir de category (premier niveau avant '|')."""
    df = df.copy()
    df["main_category"] = df["category"].str.split("|").str[0]
    return df


def calculer_popularity_score(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute popularity_score = rating * log10(rating_count + 1)."""
    df = df.copy()
    df["popularity_score"] = df["rating"] * np.log10(df["rating_count"] + 1)
    return df


def calculer_discount_range(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute discount_range : tranche de remise (0-25%, 25-50%, 50-75%, 75-100%)."""
    df = df.copy()
    bins = [0, 25, 50, 75, 100]
    labels = ["0-25%", "25-50%", "50-75%", "75-100%"]
    df["discount_range"] = pd.cut(df["discount_percentage"], bins=bins, labels=labels)
    return df
```

**Comment l'importer depuis un exercice :**

```python
# Exemple : niveau_2_intermediaire/ex2_1_categories.py

import sys
import os

# Permet d'importer common_utils/ depuis n'importe quel sous-dossier du projet
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from common_utils.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category

df = charger_dataset("data/amazon.csv")
df = nettoyer_colonnes_numeriques(df)
df = extraire_main_category(df)

# À toi de jouer pour la suite de l'exercice !
```

> ⚠️ Pense à créer un fichier `__init__.py` vide dans `common/` et dans chaque dossier de niveau pour que Python les reconnaisse comme des packages.

---

## 🟢 Niveau 1 — Débutant : Chargement & Exploration

### Projet 1.1 — Première exploration
**Fichier :** `niveau_1_debutant/ex1_1_exploration.py`

Charge le fichier `amazon.csv` avec pandas et réponds aux questions suivantes :

- Combien y a-t-il de lignes et de colonnes ?
- Quels sont les noms des colonnes et leurs types (`dtypes`) ?
- Y a-t-il des valeurs manquantes ? Dans quelles colonnes ?
- Affiche les 5 premières lignes du dataset.

```python
import pandas as pd

df = pd.read_csv("amazon.csv")
# À toi de jouer !
```

**📥 Import :** aucun (premier fichier, pandas direct)
**📤 Export vers `common/utils.py` :** fonction `charger_dataset(path)` — à créer ici et déplacer dans `utils.py` une fois validée, pour que tous les fichiers suivants l'importent au lieu de refaire `pd.read_csv()`.

### Projet 1.2 — Nettoyage des colonnes numériques
**Fichier :** `niveau_1_debutant/ex1_2_nettoyage.py`

Les colonnes `discounted_price`, `actual_price`, `discount_percentage` et `rating_count` sont stockées comme des chaînes de caractères avec des symboles (₹, %, ,).

- Retire les symboles et convertis ces colonnes en `float`
- Vérifie les types après conversion avec `.dtypes`
- Affiche un `.describe()` sur les colonnes nettoyées

> **Aide :** Utilise `.str.replace()` et `.astype(float)`

**📥 Import :** `from common.utils import charger_dataset`
**📤 Export vers `common/utils.py` :** fonction `nettoyer_colonnes_numeriques(df)` — c'est LA fonction la plus réutilisée de tout le projet, elle sera importée par presque tous les exercices suivants.

### Projet 1.3 — Statistiques de base
**Fichier :** `niveau_1_debutant/ex1_3_stats_base.py`

Après nettoyage des colonnes, réponds aux questions suivantes :

- Quel est le prix moyen après réduction ?
- Quel est le pourcentage de réduction moyen ?
- Quelle est la note (`rating`) moyenne de tous les produits ?
- Quel est le produit le moins cher ? Le plus cher ?

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (exercice de lecture/diagnostic, pas de nouvelle fonction réutilisable)

### Projet 1.4 — Filtrage simple
**Fichier :** `niveau_1_debutant/ex1_4_filtrage.py`

Filtre le dataset pour obtenir :

- Tous les produits avec une note `rating >= 4.5`
- Tous les produits avec une réduction supérieure à 70%
- Les produits dont le prix après réduction est inférieur à ₹200

Affiche le nombre de résultats pour chaque filtre.

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (filtres ponctuels, pas de fonction générique à ce stade)

### Projet 1.5 — Tri et sélection
**Fichier :** `niveau_1_debutant/ex1_5_tri.py`

- Trie les produits du mieux noté au moins bien noté
- Trie les produits du plus de réduction au moins
- Affiche uniquement les colonnes `product_name`, `rating`, `discounted_price`, `discount_percentage` pour les 10 produits les moins chers

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun

---

## 🟡 Niveau 2 — Intermédiaire : Analyse & Groupement

### Projet 2.1 — Extraction de la catégorie principale
**Fichier :** `niveau_2_intermediaire/ex2_1_categories.py`

La colonne `category` contient des hiérarchies séparées par `|`
Exemple : `Computers&Accessories|Accessories&Peripherals|Cables`

- Crée une nouvelle colonne `main_category` avec uniquement le premier niveau
- Combien de catégories principales distinctes y a-t-il ?
- Affiche le top 10 des catégories par nombre de produits (avec un graphique à barres)

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.py` :** fonction `extraire_main_category(df)` — réutilisée dans tous les exercices suivants qui groupent par catégorie (2.2, 2.4, 3.3, 3.5).

### Projet 2.2 — Analyse par catégorie
**Fichier :** `niveau_2_intermediaire/ex2_2_analyse_categories.py`

Pour chaque catégorie principale, calcule :

- Le nombre de produits
- Le prix moyen après réduction
- Le discount moyen
- La note moyenne

Affiche le résultat sous forme de tableau trié par nombre de produits décroissant.

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun (le `.groupby()` reste local à cet exercice)

### Projet 2.3 — Relation remise / note
**Fichier :** `niveau_2_intermediaire/ex2_3_remise_vs_note.py`

- Crée une colonne `discount_range` qui classe les produits par tranche de remise : `0-25%`, `25-50%`, `50-75%`, `75-100%`
- Calcule la note moyenne par tranche
- Visualise avec un graphique à barres
- Réponds : Les produits très remisés sont-ils moins bien notés ?

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.py` :** fonction `calculer_discount_range(df)` — réutilisable si un autre exercice (ex: 3.5) souhaite croiser remise/note par tranche.

### Projet 2.4 — Produits les mieux notés par catégorie
**Fichier :** `niveau_2_intermediaire/ex2_4_top_par_categorie.py`

Pour chaque catégorie principale, trouve le produit le mieux noté.

Affiche un tableau avec :

- La catégorie
- Le nom du produit
- La note
- Le prix remisé

> **Aide :** Utilise `.groupby()` + `.idxmax()`

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun

### Projet 2.5 — Détection d'anomalies de prix
**Fichier :** `niveau_2_intermediaire/ex2_5_anomalies_prix.py`

- Après nettoyage, identifie les produits où `discounted_price > actual_price` (anomalie)
- Identifie les produits où `discount_percentage` ne correspond pas au calcul réel :
  `((actual_price - discounted_price) / actual_price) * 100`
- Combine les deux : affiche tous les produits suspects

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (logique de détection spécifique à cet exercice)

### Projet 2.6 — Visualisation des prix
**Fichier :** `niveau_2_intermediaire/ex2_6_visualisation_prix.py`

Crée les visualisations suivantes avec matplotlib ou seaborn :

- Histogramme de la distribution des prix après réduction
- Boxplot des prix par top 5 catégories principales
- Scatter plot : `discount_percentage` en X, `rating` en Y (coloré par catégorie principale)

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category`
**📤 Export :** aucun

---

## 🔴 Niveau 3 — Avancé : Scoring, Texte & Synthèse

### Projet 3.1 — Score de popularité
**Fichier :** `niveau_3_avance/ex3_1_score_popularite.py`

Crée un score de popularité qui combine la note ET le volume d'avis :

```
score = rating × log10(rating_count + 1)
```

- Ajoute cette colonne `popularity_score` au dataframe
- Affiche le top 20 des produits selon ce score
- Compare avec le classement par `rating` seul — est-ce très différent ?

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export vers `common/utils.py` :** fonction `calculer_popularity_score(df)` — réutilisée dans 3.3 (dashboard) et 3.5 (mini-projet final).

### Projet 3.2 — Analyse des mots-clés dans les avis
**Fichier :** `niveau_3_avance/ex3_2_analyse_avis.py`

Utilise la colonne `review_title` pour une analyse textuelle simple :

- Sépare les produits en deux groupes : bons (`rating >= 4`) et mauvais (`rating < 3`)
- Pour chaque groupe, compte les 20 mots les plus fréquents dans les titres d'avis (retire les stopwords courants : "good", "product", "the", "a", "is"...)
- Affiche les résultats sous forme de tableau ou de nuage de mots (wordcloud)

```python
from collections import Counter
# ou
from wordcloud import WordCloud
```

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** aucun (sauf si tu veux créer `compter_mots_frequents(textes, stopwords)` réutilisable, optionnel)

### Projet 3.3 — Tableau de bord synthétique
**Fichier :** `niveau_3_avance/ex3_3_dashboard.py`

Construis un tableau de bord complet par catégorie principale avec les métriques suivantes :

| Catégorie | Nb produits | Prix moyen | Remise moyenne | Note moyenne | Score popularité moyen |
|---|---|---|---|---|---|

- Exporte ce tableau en fichier CSV (`dashboard_categories.csv`)
- Identifie la catégorie avec le meilleur rapport qualité/prix (note haute + prix bas)
- Identifie la catégorie la plus compétitive (remise la plus forte)

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category, calculer_popularity_score`
**📤 Export :** le CSV `dashboard_categories.csv` est exporté dans `outputs/` (pas une fonction Python, mais un fichier de données pour le rapport final 3.4 et le mini-projet 3.5).

### Projet 3.4 — Rapport de qualité des données
**Fichier :** `niveau_3_avance/ex3_4_qualite_donnees.py`

En tant que data analyst, tu dois produire un rapport de qualité du dataset :

- Taux de valeurs manquantes par colonne
- Taux de doublons (`product_id` en double ?)
- Vérification de cohérence : les prix sont-ils tous positifs ?
- Distribution des notes : y a-t-il des valeurs aberrantes ?

Génère un fichier `rapport_qualite.txt` avec un résumé de tes observations.

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques`
**📤 Export :** le fichier `rapport_qualite.txt` est exporté dans `outputs/` (livrable texte, pas une fonction)

### Projet 3.5 — Mini-projet final
**Fichier :** `niveau_3_avance/ex3_5_mini_projet.py`

**Objectif :** Répondre à la question business suivante :

> « Quels types de produits offrent le meilleur équilibre entre attractivité (forte remise), qualité (bonne note) et popularité (nombreux avis) ? »

Construis une analyse complète :

1. Nettoie et prépare les données (reprends tes fonctions des Projets précédents)
2. Calcule un score global combinant remise, note et popularité (définis ta propre formule et justifie-la)
3. Visualise les top 10 produits selon ce score avec leurs infos clés
4. Rédige une conclusion en commentaires dans ton code (3-5 lignes) avec ta recommandation

**📥 Import :** `from common.utils import charger_dataset, nettoyer_colonnes_numeriques, extraire_main_category, calculer_popularity_score, calculer_discount_range`
**📤 Export :** ce fichier consomme TOUT le module commun construit depuis le Projet 1.2 — c'est l'aboutissement du projet, aucune nouvelle fonction n'est nécessaire à exporter.

---

## 📁 Récapitulatif des fichiers

| Fichier | Niveau | Thème |
|---|---|---|
| `ex1_1_exploration.py` | 🟢 | Chargement et première vue |
| `ex1_2_nettoyage.py` | 🟢 | Nettoyage des types |
| `ex1_3_stats_base.py` | 🟢 | Statistiques descriptives |
| `ex1_4_filtrage.py` | 🟢 | Filtrage conditionnel |
| `ex1_5_tri.py` | 🟢 | Tri et sélection |
| `ex2_1_categories.py` | 🟡 | Extraction de catégories |
| `ex2_2_analyse_categories.py` | 🟡 | Groupement et agrégation |
| `ex2_3_remise_vs_note.py` | 🟡 | Analyse croisée |
| `ex2_4_top_par_categorie.py` | 🟡 | GroupBy avancé |
| `ex2_5_anomalies_prix.py` | 🟡 | Détection d'anomalies |
| `ex2_6_visualisation_prix.py` | 🟡 | Visualisation |
| `ex3_1_score_popularite.py` | 🔴 | Feature engineering |
| `ex3_2_analyse_avis.py` | 🔴 | Analyse textuelle |
| `ex3_3_dashboard.py` | 🔴 | Synthèse & export |
| `ex3_4_qualite_donnees.py` | 🔴 | Qualité des données |
| `ex3_5_mini_projet.py` | 🔴 | Projet intégré |

---

## 🛠️ Librairies recommandées

```bash
pip install pandas matplotlib seaborn wordcloud
```

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np
```

---

**Bonne analyse !** Commence par le niveau 1 et avance progressivement. Chaque Projet s'appuie sur le précédent. 🚀