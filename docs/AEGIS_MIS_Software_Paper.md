# AEGIS MIS
## Automated Explainable Guard for Information Security – Misinformation Identification System

### Authors
Bright Duffour  
Alberta Ayitey

---

## Abstract

AEGIS MIS is a lightweight hybrid explainable misinformation detection framework designed to identify potentially misleading textual content using a combination of rule based analysis and machine learning classification.

The framework integrates TF IDF feature extraction with Logistic Regression classification and combines these outputs with interpretable rule based detection mechanisms to improve transparency and explainability in misinformation analysis.

AEGIS MIS was developed as a research prototype focused on balancing interpretability, computational efficiency, and practical deployment simplicity. The system includes a Flask based web interface and REST API for interactive text analysis.

---

## Motivation

Misinformation continues to spread rapidly across digital platforms, creating challenges for trust, security, and information integrity. Many existing detection systems rely heavily on black box machine learning approaches that provide limited interpretability.

AEGIS MIS was developed to explore lightweight explainable AI approaches that combine traditional rule based reasoning with statistical machine learning techniques to improve transparency in misinformation detection workflows.

---

## System Architecture

The framework consists of the following components:

- Input preprocessing layer
- Rule based analysis engine
- TF IDF feature extraction module
- Logistic Regression classifier
- Hybrid scoring engine
- Explainability module
- Flask web interface
- REST API layer

---

## Benchmark Evaluation

The framework was evaluated using both synthetic prototype validation data and a benchmark dataset derived from the publicly available LIAR dataset.

### Benchmark Results

| Model | Accuracy | F1 Score |
|---|---:|---:|
| Logistic Regression | 0.61 | 0.61 |
| Improved Logistic Regression | 0.62 | 0.62 |
| Linear SVM | 0.61 | 0.64 |
| Feature Union SVM | 0.62 | 0.62 |

The benchmark evaluation produced moderate results, reflecting the complexity of real world misinformation detection tasks.

---

## Explainability

AEGIS MIS includes an explainability module that highlights suspicious trigger phrases, AI confidence scores, and contributing reasoning signals used during classification.

This approach improves interpretability compared with purely black box misinformation detection systems.

---

## Limitations

Current limitations include:

- Small scale prototype deployment
- English language focus
- Limited adversarial robustness testing
- Dependence on manually defined rule patterns
- Limited benchmark diversity

The framework is intended for research and educational purposes rather than production level misinformation moderation.

---

## Future Work

Potential future improvements include:

- Transformer based misinformation detection
- Multilingual support
- Expanded benchmark evaluation
- Adversarial robustness analysis
- Real time social media stream analysis
- Improved explainability visualization

---

## Repository

GitHub Repository:

https://github.com/Brightd4/AEGIS-MIS

---

## DOI

Zenodo DOI:

https://doi.org/10.5281/zenodo.20161662