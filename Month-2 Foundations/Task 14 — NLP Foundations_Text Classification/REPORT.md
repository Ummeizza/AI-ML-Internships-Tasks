# Task 14 — NLP Foundations: Text Classification

## 1. Objective

The objective of this task was to develop an NLP-based sentiment classification system using the IMDB movie reviews dataset and evaluate traditional machine learning approaches against a target accuracy of 90%+.

## 2. Dataset

The IMDB Reviews dataset was used for binary sentiment classification.

* Total reviews: 49,582
* Training set: 39,665
* Testing set: 9,917
* Classes: Positive and Negative

A stratified split was used, and feature extraction was performed only on training data to avoid data leakage.

## 3. Methodology

The workflow included text preprocessing with tokenization, stemming, lemmatization, and stopword handling.

Three text representations were evaluated:

* Bag of Words
* TF-IDF
* Word2Vec

Three traditional classifiers were compared:

* Logistic Regression
* Multinomial Naive Bayes
* Linear SVM

Confusion matrices and standard classification metrics were used for evaluation.

## 4. Results

### Classifier Comparison

| Model               |   Accuracy |  Precision |     Recall |         F1 |
| ------------------- | ---------: | ---------: | ---------: | ---------: |
| Logistic Regression | **89.09%** | **88.25%** | **90.28%** | **89.25%** |
| Naive Bayes         |     86.01% |     85.07% |     87.48% |     86.26% |
| Linear SVM          |     88.34% |     88.05% |     88.83% |     88.44% |

### Representation Comparison

| Representation |   Accuracy |         F1 |
| -------------- | ---------: | ---------: |
| **TF-IDF**     | **89.09%** | **89.25%** |
| Bag of Words   |     87.77% |     87.82% |
| Word2Vec       |     86.84% |     87.01% |

## 5. Final Model

**TF-IDF + Logistic Regression** was selected as the final model because it achieved the highest overall performance.

Final results:

* Accuracy: **89.09%**
* Precision: **88.25%**
* Recall: **90.28%**
* F1-Score: **89.25%**

The confusion matrix showed 4,342 correctly classified negative reviews and 4,493 correctly classified positive reviews.

## 6. Business Target

The required target was **90%+ accuracy**.

The final model achieved **89.09%**, falling short by **0.91 percentage points**. However, it provided strong and balanced sentiment classification performance.

## 7. Limitations & Future Work

TF-IDF and averaged Word2Vec have limited contextual understanding and may struggle with sarcasm, negation, and complex sentiment expressions.

Future work could use hyperparameter tuning and contextual transformer models such as BERT to improve performance.

## 8. Conclusion

The task successfully implemented an end-to-end NLP text classification workflow. TF-IDF with Logistic Regression produced the best results and established a strong baseline, while further improvements are required to consistently achieve the 90% business target.