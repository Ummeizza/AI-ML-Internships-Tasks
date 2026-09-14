# Task 14 — NLP Foundations: Text Classification

## Overview

This task focuses on Natural Language Processing (NLP) and sentiment classification using the IMDB movie reviews dataset.

The objective was to preprocess text, generate different text representations, train traditional machine learning classifiers, compare their performance, and select the best-performing approach.

## Business Scenario

An e-commerce platform receives approximately 50,000 reviews per day. Manual moderation is costly and time-consuming.

The goal is to develop an automated sentiment classifier capable of achieving **90%+ accuracy** for identifying positive and negative reviews.

## Dataset

**IMDB Movie Reviews Dataset**

* Total reviews used: 49,582
* Training samples: 39,665
* Testing samples: 9,917
* Classes: Positive and Negative

A stratified train-test split was used, and feature extraction was fitted only on training data to prevent data leakage.

## Key Skills

* Text preprocessing
* Tokenization, stemming and lemmatization
* Stopword handling
* Bag of Words
* TF-IDF
* Word2Vec
* Traditional text classification
* Confusion matrix analysis
* Model comparison

## Methodology

Three text representations were evaluated:

* **Bag of Words** — word and phrase frequency representation
* **TF-IDF** — weighted representation of important terms
* **Word2Vec** — dense 100-dimensional word embeddings

The following classifiers were compared:

* Logistic Regression
* Multinomial Naive Bayes
* Linear SVM

## Results

### Classifier Comparison

| Model                   |   Accuracy |   F1-Score |
| ----------------------- | ---------: | ---------: |
| **Logistic Regression** | **89.09%** | **89.25%** |
| Linear SVM              |     88.34% |     88.44% |
| Naive Bayes             |     86.01% |     86.26% |

### Representation Comparison

| Representation |   Accuracy |   F1-Score |
| -------------- | ---------: | ---------: |
| **TF-IDF**     | **89.09%** | **89.25%** |
| Bag of Words   |     87.77% |     87.82% |
| Word2Vec       |     86.84% |     87.01% |

The best approach was **TF-IDF + Logistic Regression**.

## Final Evaluation

The final model achieved:

* Accuracy: **89.09%**
* Precision: **88.25%**
* Recall: **90.28%**
* F1-Score: **89.25%**

The model was **0.91 percentage points below** the required 90% accuracy target.

## Limitations

Traditional TF-IDF features have limited understanding of context, word order, sarcasm, and complex sentiment expressions. Averaged Word2Vec embeddings also lose some word-level information.

Future improvement could involve transformer-based models such as BERT and further hyperparameter tuning.

## Repository Structure

```text
Task_14_NLP_Text_Classification/
├── data/
├── notebook/
├── src/
├── visualizations/
├── README.md
├── REPORT.md
├── requirements.txt
└── .gitignore
```

## Conclusion

The task demonstrated a complete NLP classification workflow. TF-IDF with Logistic Regression achieved the strongest performance and provided a solid baseline for automated sentiment classification, although further improvement is required to reach the 90% business target.