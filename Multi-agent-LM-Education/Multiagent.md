# Literature Review: Multi-Agent Collaboration for Multilingual Code Instruction Tuning

## Goal
The goal of this paper reading is to analyze how **multilingual instruction tuning** is performed through **multi-agent collaboration** and to identify the **strengths and limitations** of the proposed methodology.

---

## Questions and Answers

### 1. What are the research questions of this study?
- How can knowledge in **high-resource programming languages** be effectively transferred to **low-resource languages** through instruction tuning?  
- Can **multi-agent collaboration** generate **higher-quality multilingual instruction data** compared to single-agent pipelines?  
- How does the proposed model (**Qwen2.5-xCoder**) perform relative to **open-source** and **proprietary models** across multilingual code benchmarks?

---

### 2. What is the methodology of instruction tuning?
- **Seed Data (Ds1 & Ds2):** Constructed from GitHub code snippets. Two paths: *instruction-from-code* and *response-from-code*, filtered with an LLM scorer.  
- **Multi-Agent Data Generation (Ds3):**  
  - Specialized agents for different languages.  
  - Agents maintain **memory** of past samples and avoid duplication.  
  - **Reflection mechanism** evaluates Q&A based on consistency, difficulty, correctness, clarity, comments, and educational value.  
  - **Cross-lingual discussion**:  
    - *Centralized*: one main agent coordinates auxiliaries.  
    - *Parallel*: all agents collaborate equally.  
- **Preference Optimization (Ds4):** Multiple candidate solutions are generated, tested, and filtered for **Direct Preference Optimization (DPO)** training.  
- **Training:** Supervised Fine-Tuning (SFT) on Ds1 ∪ Ds2 ∪ Ds3 and DPO on Ds4.

---

### 3. How are the SLMs (agents) interacting with each other?
- **Centralized Communication:** A main agent (A1) coordinates; auxiliaries (A2 … Ad) provide variations.  
- **Parallel Communication:** All agents contribute equally when generating new samples.  
- **Memory & Reflection:**  
  - Memory prevents duplication and encourages novelty.  
  - Reflection uses a rubric (Q&A consistency, code correctness, clarity, comments, difficulty, educational value) to critique and refine outputs.  

---

### 4. What are the metrics used to evaluate?
- **Quantitative Metrics:**  
  - **Pass@k (esp. Pass@1)** for code correctness.  
  - **Benchmarks:** HumanEval (Python), MBPP (Python beginner problems), MultiPL-E (multilingual HumanEval).  
  - **Ablation Studies:** Effect of removing Ds2, Ds3, or Ds4.  
  - **Scaling Analysis:** Effect of dataset size on performance.  

- **Qualitative Metrics (Detailed):**  
  The reflection framework introduces qualitative evaluation based on an **LLM-based rubric**, applied to every generated Q&A pair:  
  - **Q&A Consistency:** logical match between question and answer.  
  - **Q&A Relevance:** relevance to programming/computer science.  
  - **Q&A Difficulty:** ensures problems are not trivial.  
  - **Code Existence:** verifies code is included when necessary.  
  - **Code Correctness:** checks syntax, logic, variable naming, indentation, and best practices.  
  - **Code Clarity:** evaluates readability and structure.  
  - **Code Comments:** examines the presence and usefulness of comments.  
  - **Easy to Learn:** determines educational value for beginners.  
  - **Total Score:** overall 1–5 rating, used to filter or refine samples.  
---

## Findings
- **Qwen2.5-xCoder**, trained on multi-agent–generated data, outperforms base coders and matches or surpasses larger open-source/proprietary models on multilingual tasks.  
- **Ds3 (multi-agent data)** is crucial; removing it significantly reduces performance.  
- Performance improves steadily with dataset size; strong gains appear even at ~50K samples.  

---


## Limitations
- Dataset leans toward **high-resource languages** (Python, Java, C++), with weaker transfer to underrepresented languages.  
- Heavy reliance on **LLM scorers** for evaluation and reflection introduces potential biases.  
---

