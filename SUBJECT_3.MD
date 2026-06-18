# 🛒 Exercices Data Analyst Junior — Supermarket Sales Dataset

**Dataset :** `Amazon_3_.csv` — 1 000 transactions d'un supermarché (Myanmar, Jan–Mar 2019) avec données clients, produits et paiements.

**Colonnes disponibles :**

| Colonne | Type | Description |
|---|---|---|
| `Invoice ID` | str | Identifiant unique de la transaction |
| `Branch` | str | Succursale : `A`, `B` ou `C` |
| `City` | str | Ville : Yangon, Naypyitaw, Mandalay |
| `Customer type` | str | Type client : `Member` ou `Normal` |
| `Gender` | str | Genre : `Male` ou `Female` |
| `Product line` | str | Ligne de produit (6 catégories) |
| `Unit price` | float | Prix unitaire ($) |
| `Quantity` | int | Quantité achetée |
| `Tax 5%` | float | Taxe de 5% appliquée |
| `Total` | float | Montant total TTC |
| `Date` | str | Date de la transaction |
| `Time` | str | Heure de la transaction |
| `Payment` | str | Mode de paiement : Cash, Ewallet, Credit card |
| `cogs` | float | Coût des marchandises vendues (Cost of Goods Sold) |
| `gross margin percentage` | float | Pourcentage de marge brute |
| `gross income` | float | Revenu brut (= Tax 5%) |
| `Rating` | float | Note client de 4.0 à 10.0 |

---

## 🟢 Niveau 1 — Débutant : Exploration & Premières Analyses

### Exercice 1.1 — Chargement et vue d'ensemble
**Fichier :** `ex1_1_exploration.py`

Charge le dataset et réponds aux questions suivantes :

1. Combien de transactions contient le dataset ?
2. Y a-t-il des valeurs manquantes ?
3. Combien de **branches** différentes y a-t-il ? Quelles villes leur correspondent ?
4. Combien de **lignes de produits** différentes existent ?
5. Quels sont les **modes de paiement** disponibles ?

```python
import pandas as pd

df = pd.read_csv("Amazon_3_.csv")
# À toi de jouer !
```

---

### Exercice 1.2 — Statistiques descriptives
**Fichier :** `ex1_2_stats_descriptives.py`

Utilise `.describe()` et réponds :

1. Quel est le **montant moyen** d'une transaction (`Total`) ?
2. Quelle est la **quantité moyenne** achetée par transaction ?
3. Quelle est la **note client moyenne** (`Rating`) ?
4. Quelle est la transaction avec le **montant le plus élevé** ?
5. Quelle est la transaction avec le **montant le plus bas** ?

---

### Exercice 1.3 — Conversion et manipulation des dates
**Fichier :** `ex1_3_dates.py`

La colonne `Date` est au format `YYYY-MM-DD` et `Time` est au format `HH:MM:SS`.

1. Convertis `Date` en type `datetime`
2. Crée les colonnes : `day_of_week` (lundi=0, dimanche=6), `month`, `hour` (depuis `Time`)
3. Quelle est la **journée de la semaine** avec le plus de transactions ?
4. Quel est le **mois** avec le plus grand chiffre d'affaires ?

**Aide :** `pd.to_datetime()`, `.dt.dayofweek`, `.dt.month`

---

### Exercice 1.4 — Filtrage conditionnel
**Fichier :** `ex1_4_filtrage.py`

Filtre le dataset pour obtenir :

1. Toutes les transactions de la **branche A**
2. Toutes les transactions **payées en cash**
3. Toutes les transactions avec une **note ≥ 8.0**
4. Toutes les transactions de **clientes femmes** qui sont **membres**
5. Toutes les transactions dont le **total dépasse 500$**

Affiche le nombre de lignes pour chaque filtre.

---

### Exercice 1.5 — Comptages et fréquences
**Fichier :** `ex1_5_frequences.py`

Utilise `.value_counts()` pour répondre :

1. Quelle est la **ligne de produit** la plus achetée ?
2. Quel est le **mode de paiement** le plus utilisé ?
3. Quelle est la répartition **Member vs Normal** (en %) ?
4. Quelle est la répartition **Male vs Female** (en %) ?
5. Quelle **branche** a le plus de transactions ?

---

### Exercice 1.6 — Vérification de la cohérence des calculs
**Fichier :** `ex1_6_coherence.py`

Vérifie que les colonnes calculées sont cohérentes :

1. Recalcule `Tax 5%` = `cogs × 0.05` et compare avec la colonne existante
2. Recalcule `Total` = `cogs + Tax 5%` et compare
3. Recalcule `gross income` = `Total - cogs` et compare
4. Y a-t-il des **écarts** ? Combien de lignes sont affectées ?

**Aide :** Utilise `round()` ou `np.isclose()` pour les comparaisons de float.

---

## 🟡 Niveau 2 — Intermédiaire : Analyse Comportementale & Groupements

### Exercice 2.1 — Analyse par ligne de produit
**Fichier :** `ex2_1_produits.py`

Pour chaque **ligne de produit**, calcule :

- Nombre de transactions
- Quantité totale vendue
- Chiffre d'affaires total (`Total`)
- Note client moyenne (`Rating`)
- Revenu brut total (`gross income`)

Affiche le résultat trié par **chiffre d'affaires décroissant** et visualise avec un graphique à barres horizontales.

---

### Exercice 2.2 — Analyse par branche
**Fichier :** `ex2_2_branches.py`

Compare les 3 branches (A = Yangon, B = Mandalay, C = Naypyitaw) sur :

1. Chiffre d'affaires total
2. Note client moyenne
3. Nombre de membres vs clients normaux
4. Mode de paiement dominant

Présente un tableau comparatif et visualise avec des **graphiques en barres groupées**.

---

### Exercice 2.3 — Comportement d'achat par genre
**Fichier :** `ex2_3_genre.py`

Compare les habitudes d'achat entre **Male** et **Female** :

1. Montant moyen dépensé par transaction
2. Quantité moyenne achetée
3. Lignes de produits préférées (top 3 pour chaque genre)
4. Mode de paiement préféré
5. Note client moyenne donnée

Visualise les différences avec un graphique adapté.

---

### Exercice 2.4 — Membres vs Clients normaux
**Fichier :** `ex2_4_membres.py`

Compare `Member` vs `Normal` sur :

1. Montant moyen par transaction
2. Quantité moyenne achetée
3. Note client moyenne
4. Lignes de produits achetées (répartition en %)
5. Heures d'achat préférées (matin / après-midi / soir)

Réponds : **Les membres dépensent-ils plus que les clients normaux ?**

---

### Exercice 2.5 — Analyse temporelle (heures & jours)
**Fichier :** `ex2_5_temporelle.py`

1. Crée une colonne `hour` depuis la colonne `Time`
2. Regroupe par heure et calcule le **nombre de transactions** et le **CA moyen**
3. Identifie les **heures de pointe** du supermarché
4. Crée une colonne `time_of_day` : `Matin` (6h-12h), `Après-midi` (12h-18h), `Soir` (18h-22h)
5. Quelle période génère le plus de revenu ?
6. Visualise avec un graphique linéaire (CA par heure)

---

### Exercice 2.6 — Analyse des modes de paiement
**Fichier :** `ex2_6_paiement.py`

Pour chaque mode de paiement (`Cash`, `Ewallet`, `Credit card`) :

1. Nombre de transactions
2. Montant moyen par transaction
3. Répartition par genre
4. Répartition par type de client (Member/Normal)
5. Ligne de produit la plus associée à chaque mode

Réponds : **Y a-t-il un profil type d'acheteur selon le mode de paiement ?**

---

### Exercice 2.7 — Analyse des notes clients
**Fichier :** `ex2_7_ratings.py`

1. Trace un **histogramme** de la distribution des notes (`Rating`)
2. Y a-t-il une différence de note selon la **branche** ?
3. Y a-t-il une différence de note selon la **ligne de produit** ?
4. La note est-elle corrélée au **montant dépensé** ? Au nombre d'articles ?
5. Visualise avec une **heatmap de corrélation** sur les colonnes numériques

---

### Exercice 2.8 — Panier moyen par combinaison
**Fichier :** `ex2_8_panier_moyen.py`

Calcule le **panier moyen** (montant `Total`) pour chaque combinaison :

1. `Branch` × `Product line`
2. `Gender` × `Product line`
3. `Customer type` × `Payment`

Affiche chaque résultat sous forme de **pivot table** avec `pd.pivot_table()`.

---

## 🔴 Niveau 3 — Avancé : Insights Business & Reporting

### Exercice 3.1 — Segmentation RFM simplifiée
**Fichier :** `ex3_1_rfm.py`

Le modèle RFM classifie les clients selon :
- **R**ecency : depuis combien de temps n'ont-ils pas acheté ?
- **F**requency : combien de fois ont-ils acheté ?
- **M**onetary : combien ont-ils dépensé au total ?

Comme ce dataset n'a pas d'identifiant client unique, applique l'analyse **par branche** :

1. Pour chaque branche, calcule :
   - La date de la dernière transaction (Recency)
   - Le nombre total de transactions (Frequency)
   - Le CA total (Monetary)
2. Attribue un score de 1 à 3 pour chaque dimension
3. Classe les branches en segments : `Top`, `Moyen`, `Faible`

---

### Exercice 3.2 — Détection des heures et jours creux
**Fichier :** `ex3_2_creux.py`

1. Crée une **matrice heures × jours de la semaine** avec le nombre de transactions (pivot table)
2. Visualise avec une **heatmap** (seaborn)
3. Identifie les **3 créneaux les plus chargés** et les **3 plus creux**
4. Propose en commentaires une **recommandation opérationnelle** (staffing, promotions...)

---

### Exercice 3.3 — Analyse de la rentabilité produit
**Fichier :** `ex3_3_rentabilite.py`

La colonne `gross margin percentage` est constante (4.76%). Creuse plus loin :

1. Calcule le **revenu brut total** (`gross income`) par ligne de produit
2. Calcule le **coût total** (`cogs`) par ligne de produit
3. Crée un graphique **waterfall** ou **barres empilées** : cogs vs gross income vs total
4. Quelle ligne de produit est la **plus contributive** au revenu brut ?
5. Si la marge augmentait à 6% pour la catégorie la moins performante, quel serait l'impact ?

---

### Exercice 3.4 — Scoring des lignes de produit
**Fichier :** `ex3_4_scoring.py`

Construis un **score composite** pour chaque ligne de produit :

- CA total (poids 35%)
- Note client moyenne (poids 30%)
- Nombre de transactions (poids 20%)
- Revenu brut total (poids 15%)

1. Normalise chaque métrique entre 0 et 1
2. Calcule le score final pondéré
3. Affiche le **classement des 6 lignes de produit**
4. Compare avec le classement par CA seul — la conclusion change-t-elle ?

```python
# Normalisation manuelle
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())
```

---

### Exercice 3.5 — Rapport mensuel complet
**Fichier :** `ex3_5_rapport_mensuel.py`

Génère un rapport synthétique **par mois** (Jan / Fév / Mar 2019) :

| Mois | Nb transactions | CA total | Revenu brut | Note moyenne | Produit star | Paiement dominant |
|------|----------------|---------|-------------|-------------|-------------|-------------------|

1. Exporte ce tableau en `rapport_mensuel.csv`
2. Quel mois a été le **plus performant** ? Selon quel critère ?
3. Y a-t-il une **tendance à la hausse ou à la baisse** sur les 3 mois ?
4. Rédige une **synthèse en commentaires** (5-8 lignes)

---

### Exercice 3.6 — Détection des outliers de transaction
**Fichier :** `ex3_6_outliers.py`

Identifie les transactions **atypiques** sur le montant `Total` :

1. Méthode IQR : calcule Q1, Q3, IQR et identifie les outliers
2. Méthode Z-score : identifie les transactions avec |z| > 2
3. Pour chaque outlier : affiche la branche, le produit, le mode de paiement, le montant
4. Ces outliers sont-ils plutôt associés à un type de client particulier ?
5. Visualise avec un **boxplot par ligne de produit**

---

### Exercice 3.7 — Mini-projet final : Analyse 360°
**Fichier :** `ex3_7_mini_projet_final.py`

**Objectif :** Répondre à cette question business :

> *"Quel est le profil de la transaction idéale pour maximiser la satisfaction client (Rating) et le revenu brut (gross income) ?"*

Construis une analyse complète :

1. Identifie les variables les plus corrélées à `Rating` et à `gross income`
2. Crée un profil de la transaction "idéale" : heure, jour, genre, type client, produit, paiement
3. Valide ce profil en filtrant les transactions qui correspondent et calcule leurs KPIs moyens
4. Compare avec les transactions qui ne correspondent pas au profil
5. Génère 3 visualisations pertinentes
6. Exporte les insights dans `profil_transaction_ideale.csv`
7. Rédige une **recommandation managériale** en commentaires (8-10 lignes)

---

## 📁 Récapitulatif des fichiers

| Fichier | Niveau | Thème |
|---|---|---|
| `ex1_1_exploration.py` | 🟢 | Chargement et vue d'ensemble |
| `ex1_2_stats_descriptives.py` | 🟢 | Statistiques de base |
| `ex1_3_dates.py` | 🟢 | Manipulation des dates et heures |
| `ex1_4_filtrage.py` | 🟢 | Filtrage conditionnel |
| `ex1_5_frequences.py` | 🟢 | Comptages et fréquences |
| `ex1_6_coherence.py` | 🟢 | Vérification de cohérence |
| `ex2_1_produits.py` | 🟡 | Analyse par ligne de produit |
| `ex2_2_branches.py` | 🟡 | Comparaison des branches |
| `ex2_3_genre.py` | 🟡 | Comportement d'achat par genre |
| `ex2_4_membres.py` | 🟡 | Membres vs Clients normaux |
| `ex2_5_temporelle.py` | 🟡 | Heures de pointe & creux |
| `ex2_6_paiement.py` | 🟡 | Analyse des modes de paiement |
| `ex2_7_ratings.py` | 🟡 | Analyse des notes clients |
| `ex2_8_panier_moyen.py` | 🟡 | Pivot tables & panier moyen |
| `ex3_1_rfm.py` | 🔴 | Segmentation RFM |
| `ex3_2_creux.py` | 🔴 | Heatmap heures × jours |
| `ex3_3_rentabilite.py` | 🔴 | Analyse de rentabilité |
| `ex3_4_scoring.py` | 🔴 | Scoring pondéré |
| `ex3_5_rapport_mensuel.py` | 🔴 | Rapport mensuel & export |
| `ex3_6_outliers.py` | 🔴 | Détection d'outliers |
| `ex3_7_mini_projet_final.py` | 🔴 | Projet intégré 360° |

---

## 🛠️ Librairies recommandées

```bash
pip install pandas matplotlib seaborn numpy
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

- **1 000 transactions** sur Jan–Mar 2019
- **3 branches** : A (Yangon), B (Mandalay), C (Naypyitaw)
- **6 lignes de produits** : Health & beauty, Electronic accessories, Home & lifestyle, Sports & travel, Food & beverages, Fashion accessories
- **3 modes de paiement** : Ewallet, Cash, Credit card
- **2 types de clients** : Member / Normal
- **Montant moyen** par transaction : ~322$
- **Note client moyenne** : 6.97 / 10
- **Marge brute fixe** : 4.76% sur toutes les transactions

---

*Ce dataset est idéal pour pratiquer l'analyse comportementale et les insights retail. Commence par le niveau 1 et progresse ! 🚀*