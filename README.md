# LLM-eval-using-Kazakh

This repository provides the datasets and prompts utilized in the paper titled "Do LLMs Speak Kazakh? A Pilot Evaluation of Seven Models."


`prompts.py` This script introduces the prompts used in the experiment.

`math_english_instructions` - this function is english-instructed prompt for the 'NIS Math' dataset.

`math_kazakh_instructions` - this function is kazakh-instructed prompt for the 'NIS Math' dataset.


## Datasets for "Do LLMs Speak Kazakh? A Pilot Evaluation of Seven Models"

### [Belebele](./Datasets/Belebele.jsonl) (Bandarkar et al., 2023)
**Task:** Multiple-choice QA  
**Size:** 900  
**Metric:** Accuracy  
**Language:** Human-translated  
**Description:** A dataset containing multiple-choice questions and answers used to evaluate the ability of language models to understand and generate Kazakh text.

### [kkCOPA](./Datasets/kkCOPA.jsonl)
**Task:** Causal reasoning  
**Size:** 500  
**Metric:** Accuracy  
**Language:** Machine-translated  
**Description:** The Kazakh version of the Choice of Plausible Alternatives (COPA) dataset is used to test commonsense reasoning by providing scenarios with multiple-choice questions.

### [NIS Math](./Datasets/NIS_Math.jsonl)
**Task:** School Math  
**Size:** 100  
**Metric:** Accuracy  
**Language:** Originally in Kazakh  
**Description:** This dataset contains mathematical problems and prompts sourced from the Nazarbayev Intellectual Schools' curriculum, used to assess mathematical reasoning in Kazakh.

### [KazQad_part](./Datasets/KazQad_part.jsonl) (Yeshpanov et al., 2024)
**Task:** Reading comprehension  
**Size:** 1,000  
**Metric:** Token-level F1  
**Language:** Originally in Kazakh  
**Description:** KazQad is a comprehensive dataset designed to test the question-answering capabilities of language models in Kazakh, covering a wide range of topics.

### [KazQad](./Datasets/KazQad.jsonl) (Yeshpanov et al., 2024)
**Task:** Generative QA  
**Size:** 1,927  
**Metric:** Token-level recall  
**Language:** Originally in Kazakh  
**Description:** A subset of the KazQad dataset, providing a focused selection of question-answering prompts for more targeted evaluation.

### [kkWikiSpell](./Datasets/kkWikiSpell.jsonl)
**Task:** Spelling correction  
**Size:** 160  
**Metric:** Token-level Jaccard  
**Language:** Originally in Kazakh  
**Description:** A spelling correction dataset derived from Kazakh Wikipedia entries, aimed at evaluating the spelling and grammatical correction capabilities of language models in Kazakh.

### [Flores-101](./Datasets/Flores-101.jsonl) (Goyal et al., 2022)
**Task:** Machine translation  
**Size:** 500  
**Metric:** BLEU  
**Language:** Human-translated  
**Description:** This dataset is part of the Flores-101 initiative, aimed at providing high-quality translations and prompts for evaluating multilingual language models, including Kazakh.

