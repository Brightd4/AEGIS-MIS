# A Hybrid Explainable Misinformation Detection Framework Using Rule Based Analysis and Machine Learning

## Authors

Bright Duffour  
Alberta Ayitey

---

# Abstract

Misinformation continues to pose significant challenges to information integrity, digital trust, and online security. Existing misinformation detection systems often rely heavily on black box machine learning models that provide limited interpretability for end users and analysts.

This paper presents AEGIS MIS, an Automated Explainable Guard for Information Security – Misinformation Identification System, designed as a lightweight hybrid explainable misinformation detection framework. The system combines rule based linguistic analysis with TF IDF feature extraction and Logistic Regression classification to improve interpretability while maintaining computational simplicity.

The framework includes an explainability module capable of identifying suspicious linguistic patterns, risk indicators, and AI confidence signals contributing to misinformation classification decisions. Experimental evaluation was performed using both synthetic prototype validation data and a benchmark dataset derived from the LIAR dataset. Benchmark evaluation produced moderate performance results, with model accuracy ranging from 0.61 to 0.62 and F1 scores ranging from 0.61 to 0.64 across multiple classifier configurations.

The results demonstrate the feasibility of lightweight explainable misinformation detection approaches while highlighting the challenges associated with real world misinformation classification. AEGIS MIS is intended as a research prototype for educational, academic, and experimental cybersecurity research applications.

---

# Introduction

The rapid spread of misinformation across digital platforms has created significant societal, political, and cybersecurity concerns. False or misleading information can influence public opinion, undermine institutional trust, and contribute to harmful real world consequences. Social media platforms and online communication systems have accelerated the speed and scale at which misinformation can propagate.

Recent advances in artificial intelligence and natural language processing have improved automated misinformation detection capabilities. However, many existing systems rely on complex black box architectures that provide limited transparency regarding how classification decisions are made. This lack of interpretability creates challenges for trust, accountability, and human verification.

AEGIS MIS was developed to explore hybrid explainable approaches that combine interpretable rule based reasoning with lightweight machine learning classification techniques. The framework prioritizes transparency, modularity, reproducibility, and computational efficiency while maintaining practical misinformation detection functionality.

The primary contributions of this work include:

- Development of a lightweight hybrid misinformation detection framework
- Integration of explainable rule based analysis with machine learning classification
- Benchmark evaluation using misinformation related datasets
- Deployment of an interactive Flask based misinformation analysis system
- Emphasis on interpretability and transparency in misinformation detection workflows

---

# Related Work

Misinformation detection has become an important research area within natural language processing, cybersecurity, and information integrity. Early approaches to misinformation and fake news detection commonly relied on traditional machine learning methods such as Logistic Regression, Support Vector Machines, Naive Bayes, and feature engineering methods based on term frequency and inverse document frequency. These approaches remain useful in lightweight systems because they are computationally efficient and easier to interpret than many large deep learning models.

A widely used benchmark in misinformation research is the LIAR dataset, introduced by Wang. The LIAR dataset contains short political statements labeled according to truthfulness categories and has been widely used for evaluating fake news and misinformation classification models. Although the dataset is challenging because of the short and context dependent nature of the statements, it remains useful for benchmarking text based misinformation detection systems.

More recent work has explored deep learning and transformer based models for fake news detection. FakeBERT, proposed by Kaliyar and colleagues, combines BERT based language representation with deep learning layers for fake news detection in social media contexts. Transformer based models often improve semantic representation, but they can require more computational resources and may provide limited interpretability compared with simpler models.

Explainable Artificial Intelligence has also become increasingly important in security sensitive AI systems. Adadi and Berrada provided a broad survey of explainable AI and emphasized the need to make black box systems more transparent and understandable. In misinformation detection, explainability is especially important because users and analysts need to understand why a statement is classified as suspicious or misleading.

Recent studies and surveys continue to show that fake news detection remains a difficult problem because misinformation is context dependent, linguistically diverse, and often designed to exploit emotional or social biases. Reviews of machine learning and deep learning approaches show that while complex models may improve performance, challenges remain in interpretability, dataset bias, generalization, and real world deployment.

AEGIS MIS builds on this body of work by focusing on a lightweight hybrid architecture that combines rule based analysis with TF IDF feature extraction and Logistic Regression classification. Rather than claiming to replace large scale misinformation detection systems, AEGIS MIS is positioned as an explainable research prototype that emphasizes transparency, reproducibility, and practical deployment simplicity.

---

# Methodology

[To be completed]

---

# System Architecture

[To be completed]

---

# Experimental Evaluation

[To be completed]

---

# Results and Discussion

[To be completed]

---

# Limitations

[To be completed]

---

# Ethical Considerations

[To be completed]

---

# Conclusion

[To be completed]

---

# References

[To be completed]
