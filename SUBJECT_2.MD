# 💰 Exercices Data Analyst Junior — Amazon Sales Dataset

**Dataset :** `Amazon_Sales_data.csv` — 100 commandes internationales Amazon avec données financières et géographiques.

**Colonnes disponibles :**

| Colonne | Type | Description |
|---|---|---|
| `Region` | str | Zone géographique (7 régions mondiales) |
| `Country` | str | Pays de la commande |
| `Item Type` | str | Type de produit (12 catégories) |
| `Sales Channel` | str | Canal de vente : `Online` ou `Offline` |
| `Order Priority` | str | Priorité : `H` (High), `M` (Medium), `L` (Low), `C` (Critical) |
| `Order ID` | int | Identifiant unique de la commande |
| `Units Sold` | int | Nombre d'unités vendues |
| `Unit Price` | float | Prix unitaire de vente (€) |
| `Unit Cost` | float | Coût unitaire (€) |
| `Total Revenue` | float | Chiffre d'affaires total |
| `Total Cost` | float | Coût total |
| `Total Profit` | float | Profit total |
| `Order Date` | str | Date de commande |
| `Ship Date` | str | Date d'expédition |

---

## 🟢 Niveau 1 — Débutant : Exploration & Statistiques

### Exercice 1.1 — Chargement et vue d'ensemble
**Fichier :** `ex1_1_exploration.py`

Charge le fichier `Amazon_Sales_data.csv` avec pandas et réponds aux questions suivantes :

1. Combien de commandes contient le dataset ?
2. Quels sont les types de chaque colonne (`dtypes`) ?
3. Y a-t-il des valeurs manquantes ?
4. Combien de **régions** différentes sont représentées ? Lesquelles ?
5. Combien de **types de produits** différents existent ?

```python
import pandas as pd

df = pd.read_csv("DATA_02.csv")
# À toi de jouer !
```

---

### Exercice 1.2 — Statistiques descriptives
**Fichier :** `ex1_2_stats_descriptives.py`

Sans aucune transformation, utilise `.describe()` pour répondre :

1. Quelle est la commande avec le **plus grand nombre d'unités vendues** ?
2. Quel est le **profit total moyen** par commande ?
3. Quelle est la **plage de prix unitaires** (min → max) ?
4. Le `Total Revenue` est-il toujours supérieur au `Total Cost` ? Vérifie-le.

---

### Exercice 1.3 — Conversion des dates
**Fichier :** `ex1_3_dates.py`

Les colonnes `Order Date` et `Ship Date` sont des chaînes de caractères au format `DD-MM-YYYY`.

1. Convertis-les en type `datetime` avec `pd.to_datetime()`
2. Crée une colonne `delivery_days` = nombre de jours entre commande et expédition
3. Quelle est la **livraison la plus rapide** ? La **plus lente** ?
4. Quelle est la **durée de livraison moyenne** ?

**Aide :** `pd.to_datetime(df['Order Date'], format='%d-%m-%Y')`

---

### Exercice 1.4 — Filtrage et sélection
**Fichier :** `ex1_4_filtrage.py`

Filtre le dataset pour obtenir :

1. Toutes les commandes passées **en ligne** (`Online`)
2. Toutes les commandes avec une priorité **critique** (`C`)
3. Toutes les commandes de la région **Europe**
4. Les commandes avec un profit supérieur à **500 000**

Affiche le nombre de lignes pour chaque filtre.

---

### Exercice 1.5 — Tri et classement
**Fichier :** `ex1_5_tri.py`

1. Affiche les **5 commandes les plus rentables** (par `Total Profit`)
2. Affiche les **5 commandes avec le moins d'unités vendues**
3. Trie par `Region` puis par `Total Revenue` décroissant, et affiche le résultat
4. Quelle est la commande la **plus ancienne** du dataset ? La plus récente ?

---

### Exercice 1.6 — Comptages et fréquences
**Fichier :** `ex1_6_frequences.py`

Utilise `.value_counts()` pour répondre :

1. Quelle est la **région la plus fréquente** dans les commandes ?
2. Quel est le **type de produit** le plus commandé ?
3. Quelle est la répartition entre commandes `Online` et `Offline` (en %) ?
4. Quelle priorité de commande (`Order Priority`) est la plus courante ?

---

## 🟡 Niveau 2 — Intermédiaire : Analyse Financière & Groupements

### Exercice 2.1 — Marge bénéficiaire
**Fichier :** `ex2_1_marge.py`

1. Crée une colonne `profit_margin_pct` = `(Total Profit / Total Revenue) * 100`
2. Quel est le **type de produit le plus rentable** (marge moyenne la plus haute) ?
3. Quel est le **moins rentable** ?
4. Visualise les marges par type de produit avec un graphique à barres horizontales

---

### Exercice 2.2 — Analyse par région
**Fichier :** `ex2_2_analyse_region.py`

Pour chaque **région**, calcule :

- Le nombre de commandes
- Le chiffre d'affaires total (`Total Revenue`)
- Le profit total (`Total Profit`)
- La marge moyenne

Affiche le résultat trié par **profit total décroissant** et visualise avec un graphique à barres empilées (Revenue vs Cost vs Profit).

---

### Exercice 2.3 — Online vs Offline
**Fichier :** `ex2_3_online_vs_offline.py`

Compare les deux canaux de vente sur les métriques suivantes :

1. Nombre de commandes
2. Unités vendues moyennes
3. Profit moyen par commande
4. Marge bénéficiaire moyenne

Présente la comparaison dans un **tableau côte à côte** et dans un graphique de type **barres groupées**.

Réponds : **Quel canal est plus rentable ? Est-ce cohérent avec le volume ?**

---

### Exercice 2.4 — Analyse de la priorité commande
**Fichier :** `ex2_4_priorite.py`

Les priorités sont : `C` (Critical), `H` (High), `M` (Medium), `L` (Low).

1. Recode la colonne `Order Priority` avec les libellés complets dans une nouvelle colonne `priority_label`
2. Calcule la **durée de livraison moyenne** par priorité (réutilise ta colonne `delivery_days`)
3. Les commandes critiques sont-elles vraiment livrées plus vite ? Affiche le résultat.
4. Calcule aussi le **profit moyen** par priorité

---

### Exercice 2.5 — Analyse temporelle
**Fichier :** `ex2_5_temporelle.py`

Après conversion des dates :

1. Crée une colonne `order_year` et une colonne `order_month`
2. Calcule le **profit total par année**
3. Calcule le **chiffre d'affaires moyen par mois** (tous années confondues)
4. Y a-t-il des mois plus performants que d'autres ? Visualise avec un graphique linéaire.

---

### Exercice 2.6 — Top produits par région
**Fichier :** `ex2_6_top_produit_region.py`

Pour chaque **région**, trouve le **type de produit** qui génère le plus de profit total.

Affiche un tableau :

| Région | Meilleur produit | Profit total |
|--------|-----------------|--------------|

**Aide :** Utilise `.groupby(['Region', 'Item Type'])` puis `.idxmax()`

---

### Exercice 2.7 — Corrélations
**Fichier :** `ex2_7_correlations.py`

1. Calcule la **matrice de corrélation** entre les colonnes numériques
2. Visualise avec une **heatmap** (`seaborn`)
3. Quelle paire de variables est la plus corrélée ? Est-ce logique ?
4. Y a-t-il une corrélation entre `Units Sold` et `Total Profit` ?

---

### Exercice 2.8 — Visualisation géographique textuelle
**Fichier :** `ex2_8_geo_analyse.py`

1. Liste tous les **pays distincts** présents dans le dataset
2. Pour chaque pays, calcule le profit total
3. Identifie le **top 10 des pays les plus profitables**
4. Identifie les **5 pays les moins profitables**
5. Affiche un graphique à barres horizontal pour le top 10

---

## 🔴 Niveau 3 — Avancé : KPIs, Optimisation & Reporting

### Exercice 3.1 — Calcul du coût unitaire réel vs déclaré
**Fichier :** `ex3_1_verification_calculs.py`

Vérifie la cohérence interne du dataset :

1. Recalcule `Total Revenue` = `Units Sold × Unit Price` et compare avec la colonne existante
2. Recalcule `Total Cost` = `Units Sold × Unit Cost` et compare
3. Recalcule `Total Profit` = `Total Revenue - Total Cost` et compare
4. Y a-t-il des **incohérences** ? Lesquelles ? Dans combien de lignes ?

---

### Exercice 3.2 — Segmentation des commandes
**Fichier :** `ex3_2_segmentation.py`

Crée une segmentation des commandes en 3 catégories selon le profit :

- `Petit` : profit < 200 000
- `Moyen` : 200 000 ≤ profit < 700 000
- `Grand` : profit ≥ 700 000

1. Ajoute une colonne `order_segment`
2. Quelle est la répartition (en %) de chaque segment ?
3. Calcule les métriques moyennes (unités, prix, marge) pour chaque segment
4. Quel type de produit domine chaque segment ?

**Aide :** Utilise `pd.cut()` avec les bons `bins` et `labels`

---

### Exercice 3.3 — Analyse de saisonnalité
**Fichier :** `ex3_3_saisonnalite.py`

1. Crée une colonne `quarter` (trimestre) à partir de `Order Date`
2. Calcule le **profit total par trimestre** et par **année**
3. Crée un **pivot table** : années en lignes, trimestres en colonnes, valeur = profit total
4. Visualise avec une heatmap
5. Y a-t-il un trimestre systématiquement plus fort ?

---

### Exercice 3.4 — Scoring des types de produits
**Fichier :** `ex3_4_scoring_produits.py`

Construis un **score composite** pour chaque type de produit basé sur :

- Marge bénéficiaire moyenne (poids : 40%)
- Profit total (poids : 40%)
- Nombre de commandes (poids : 20%)

Normalise chaque indicateur entre 0 et 1 avant de les combiner :

```python
from sklearn.preprocessing import MinMaxScaler
# ou manuellement : (x - x.min()) / (x.max() - x.min())
```

Affiche le **classement final** des 12 types de produits selon ce score.

---

### Exercice 3.5 — Rapport de performance par région
**Fichier :** `ex3_5_rapport_region.py`

Génère un **rapport complet** par région sous forme de DataFrame avec les colonnes suivantes :

| Région | Nb commandes | CA total | Coût total | Profit total | Marge % | Meilleur produit | Canal dominant |
|--------|-------------|---------|-----------|-------------|---------|-----------------|----------------|

1. Exporte ce tableau en fichier **CSV** : `rapport_performance_regions.csv`
2. Quelle région a le **meilleur ratio profit/commande** ?
3. Rédige en commentaires une **synthèse de 5 lignes** sur les performances globales

---

### Exercice 3.6 — Détection des outliers
**Fichier :** `ex3_6_outliers.py`

Détecte les commandes **atypiques** sur `Total Profit` :

1. Méthode IQR : outlier si < Q1 - 1.5×IQR ou > Q3 + 1.5×IQR
2. Méthode Z-Score : outlier si |z| > 2
3. Compare les deux méthodes — trouvent-elles les mêmes outliers ?
4. Pour chaque outlier identifié, affiche son pays, son type de produit et son profit
5. Visualise avec un **boxplot** annoté

---

### Exercice 3.7 — Mini-projet final : Dashboard analytique
**Fichier :** `ex3_7_mini_projet_final.py`

**Objectif :** Répondre à cette question business :

> *"Quelle combinaison Région × Type de produit × Canal de vente maximise la rentabilité pour Amazon ?"*

Construis une analyse complète :

1. Crée un **pivot table 3D** : Région × Item Type, valeur = marge moyenne
2. Identifie le **top 5 des combinaisons** (Région + Produit + Canal) les plus rentables
3. Calcule pour chaque combinaison : profit total, marge, volume de commandes
4. Visualise les résultats avec au moins **2 graphiques** pertinents
5. Exporte les résultats dans `resultats_combinaisons.csv`
6. Rédige en commentaires une **recommandation stratégique** (5-8 lignes)

---

## 📁 Récapitulatif des fichiers

| Fichier | Niveau | Thème |
|---|---|---|
| `ex1_1_exploration.py` | 🟢 | Chargement et vue d'ensemble |
| `ex1_2_stats_descriptives.py` | 🟢 | Statistiques de base |
| `ex1_3_dates.py` | 🟢 | Manipulation des dates |
| `ex1_4_filtrage.py` | 🟢 | Filtrage conditionnel |
| `ex1_5_tri.py` | 🟢 | Tri et classement |
| `ex1_6_frequences.py` | 🟢 | Comptages et fréquences |
| `ex2_1_marge.py` | 🟡 | Calcul de marge bénéficiaire |
| `ex2_2_analyse_region.py` | 🟡 | Groupement par région |
| `ex2_3_online_vs_offline.py` | 🟡 | Comparaison de canaux |
| `ex2_4_priorite.py` | 🟡 | Analyse par priorité |
| `ex2_5_temporelle.py` | 🟡 | Analyse temporelle |
| `ex2_6_top_produit_region.py` | 🟡 | GroupBy multi-niveaux |
| `ex2_7_correlations.py` | 🟡 | Corrélations & heatmap |
| `ex2_8_geo_analyse.py` | 🟡 | Analyse géographique |
| `ex3_1_verification_calculs.py` | 🔴 | Contrôle qualité des données |
| `ex3_2_segmentation.py` | 🔴 | Segmentation avec pd.cut |
| `ex3_3_saisonnalite.py` | 🔴 | Pivot table & saisonnalité |
| `ex3_4_scoring_produits.py` | 🔴 | Feature engineering & scoring |
| `ex3_5_rapport_region.py` | 🔴 | Reporting complet & export |
| `ex3_6_outliers.py` | 🔴 | Détection d'outliers |
| `ex3_7_mini_projet_final.py` | 🔴 | Projet intégré & recommandation |

---

## 🛠️ Librairies recommandées

```bash
pip install pandas matplotlib seaborn scikit-learn
```

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats  # pour z-score
```

---

## 💡 Rappel des valeurs clés du dataset

- **100 commandes** sur la période 2010–2016
- **7 régions** : Europe, Asia, North America, Sub-Saharan Africa, Middle East and North Africa, Central America and the Caribbean, Australia and Oceania
- **12 types de produits** : Baby Food, Cereal, Office Supplies, Fruits, Household, Vegetables, Personal Care, Clothes, Cosmetics, Beverages, Meat, Snacks
- **2 canaux** : Online / Offline
- **4 priorités** : C (Critical), H (High), M (Medium), L (Low)
- **Profit moyen par commande** : ~441 000
- **Marge bénéficiaire moyenne** : ~36%

---

*Commence par le niveau 1 et avance progressivement. Les exercices de niveau 3 supposent que tu maîtrises les bases des niveaux précédents.* 🚀