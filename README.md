# 📊 Data Analyst Kaggle - Learning Journey

[![Portfolio](https://img.shields.io/badge/Portfolio-nassaigael.github.io-blue?style=for-the-badge&logo=github)](https://nassaigael.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-nassaigael-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/nassaigael/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🎯 About This Project

Welcome to my **Data Analysis Learning Repository**! This project showcases a comprehensive journey through data analysis using real-world datasets from Kaggle. Through a **3-level progression** (Beginner → Intermediate → Advanced), I explore data exploration, cleaning, visualization, and advanced analytical techniques.

> **Currently Working On:** Building a strong foundation in data analysis with practical exercises and real-world datasets.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/nassaigael/DATA_ANALYST_KAGGLE.git
cd DATA_ANALYST_KAGGLE

# Install dependencies
pip install -r requirements.txt

# Run a beginner level exercise
python -m beginner_level.ex1_1_exploration
```

---

## 📦 Project Structure

```
DATA_ANALYST_KAGGLE/
│
├── 📁 data/                          # Raw datasets
│   ├── Amazon_3_.csv                 # Amazon product dataset
│   ├── DATA_01.csv
│   └── DATA_02.csv
│
├── 📁 beginner_level/                # 🟢 Foundational skills
│   ├── ex1_1_exploration.py          # Data exploration & overview
│   └── ex1_2_nettoyage.py            # Data cleaning & preprocessing
│
├── 📁 common/                         # 🔧 Shared utilities
│   ├── __init__.py
│   └── utils.py                      # Reusable functions & helpers
│
├── 📁 outputs/                        # 📊 Generated results & reports
│   └── (analysis outputs)
│
├── 📄 main.py                         # Entry point
├── 📄 requirements.txt                # Dependencies
├── 📄 README.md                       # This file
├── SUBJECT_1.MD                       # Amazon Dataset Documentation
├── SUBJECT_2.MD
└── SUBJECT_3.MD
```

---

## 📚 Learning Levels

### 🟢 **Beginner Level** - Foundations
Master the fundamentals of data analysis:

| File | Topic | Goal |
|------|-------|------|
| `ex1_1_exploration.py` | 🔍 Data Exploration | Understand dataset structure and statistics |
| `ex1_2_nettoyage.py` | 🧹 Data Cleaning | Handle missing values and duplicates |

*Estimated Duration: 1-2 weeks*

---

### 🟡 **Intermediate Level** - *(Coming Soon)*
Dive deeper into analysis and visualization:
- Category-based analysis
- Price vs. Rating correlations
- Anomaly detection
- Data visualization techniques

*Estimated Duration: 2-3 weeks*

---

### 🔴 **Advanced Level** - *(Coming Soon)*
Master complex analytical techniques:
- Custom scoring algorithms
- Review sentiment analysis
- Interactive dashboards
- Data quality assessment
- End-to-end mini-projects

*Estimated Duration: 3-4 weeks*

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|---|---|
| **Python 3.8+** | Core programming language |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical computing |
| **Matplotlib & Seaborn** | Data visualization |
| **Jupyter** | Interactive notebooks |

</div>

---

## 📊 Datasets

### Amazon Product Dataset
- **Size:** 1,465 products from Amazon India
- **Features:** 15+ columns including price, ratings, reviews, categories
- **Format:** CSV
- **Use Case:** Real-world e-commerce data analysis

```
Columns: product_id, product_name, category, discounted_price, 
         actual_price, discount_percentage, rating, rating_count,
         review_title, review_content, and more...
```

---

## 🎓 Learning Outcomes

By completing this project, you will:
- ✅ Master data exploration and statistical analysis
- ✅ Clean and preprocess real-world messy data
- ✅ Create meaningful visualizations
- ✅ Perform advanced data analysis
- ✅ Build data-driven insights
- ✅ Develop production-ready Python skills

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify installation
python -c "import pandas; print('✓ Pandas installed')"
```

---

## 📖 How to Use

### Running Exercises

```bash
# Run a specific exercise
python -m beginner_level.ex1_1_exploration

# Or use the main entry point
python main.py
```

### Working with the Code

1. **Review** the exercise comments and docstrings
2. **Study** the dataset structure using `ex1_1_exploration.py`
3. **Practice** data cleaning in `ex1_2_nettoyage.py`
4. **Reference** `common/utils.py` for reusable functions
5. **Save** results to the `outputs/` directory

---

## 📝 Code Example

```python
import pandas as pd
from common.utils import load_data

# Load Amazon dataset
df = load_data('data/Amazon_3_.csv')

# Display basic statistics
print(df.describe())
print(f"Shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")
```

---

## 🤝 Connect With Me

Feel free to reach out and connect!

| Platform | Link |
|----------|------|
| 🌐 **Portfolio** | [nassaigael.github.io](https://nassaigael.github.io/) |
| 💼 **LinkedIn** | [nassaigael](https://www.linkedin.com/in/nassaigael/) |
| 💻 **GitHub** | [GitHub Profile](https://github.com/nassaigael/) |

---

## 📈 Progress Tracker

```
BEGINNER LEVEL
├── [x] Data Exploration
├── [x] Data Cleaning
├── [ ] Basic Statistics
├── [ ] Data Filtering
└── [ ] Sorting & Grouping

INTERMEDIATE LEVEL
├── [ ] Category Analysis
├── [ ] Price Analysis
├── [ ] Anomaly Detection
└── [ ] Visualizations

ADVANCED LEVEL
├── [ ] Custom Scoring
├── [ ] Sentiment Analysis
├── [ ] Dashboard Creation
└── [ ] Mini Projects
```

---

## 📄 License

This project is licensed under the **MIT License** - feel free to use it for learning and development.

---

## ⭐ If You Found This Helpful

If this repository helped you learn data analysis, please consider:
- ⭐ Starring the repository
- 📤 Sharing it with others
- 💬 Providing feedback and suggestions
- 🔗 Connecting on [LinkedIn](https://www.linkedin.com/in/nassaigael/)

---

<div align="center">

**Made with ❤️ by Nassai Gael**

*Keep learning, keep coding, keep analyzing! 🚀*

</div>
