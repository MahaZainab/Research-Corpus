# Small-Model Multi-Agent Debate for Improving Reasoning in LLMs

## Overview
This project explores how **multi-agent debate among Small Language Models (SLMs)** can improve the **reasoning capabilities of Large Language Models (LLMs)** in the domain of **source-code comprehension**.  
It extends prior work on *Theory of Mind (ToM) teacher–student frameworks* by replacing a single strong teacher with multiple lightweight debating agents.

## Motivation
- LLMs handle factual and surface-level tasks well but struggle with **abstract reasoning, clarity, and completeness**.  
- ToM teacher–student methods improved evaluation reliability but remain costly and dependent on a strong teacher model.  
- This work proposes a **multi-agent SLM debate framework** to approximate teacher interventions while lowering computational costs.

## Research Questions
1. Can multi-agent SLM debate improve comprehension reasoning beyond single-LLM and ToM baselines?  
2. How do debate protocols (rounds, critique styles) compare to ToM teacher interventions?  
3. Does SLM debate achieve competitive improvements at lower cost?  
4. Do debate-based gains extend across categories (*What, Why, How, Algorithm, Error reasoning*)?  
5. Does debate reduce unreliable judgments (fluent-but-wrong answers)?  

## Methodology
- **Datasets**: CS1QA (educational comprehension Qs) and CodeQA (program reasoning tasks).  
- **Baseline**: retrieval-augmented prompting + ToM teacher–student judge.  
- **Extension**:  
  - Replace single teacher with 3–7 SLM debaters.  
  - Debate protocol: proposal → critique/refutation → arbitration by a judge.  
  - Suspicion triggers extend debate when unreliable patterns appear.  
  - Optional *Lesson Bank* to store reusable corrections.  

## Debate Protocol
1. **Input construction**: demos + code + question.  
2. **Round 0 (Propose)**: each SLM outputs answer + rationale.  
3. **Debate rounds**: agents critique peers and update answers.  
4. **Suspicion trigger**: adds extra debate rounds if necessary.  
5. **Judge arbitration**: selects final answer based on evidence and convergence.  

## Evaluation Metrics
- **Correctness**: Accuracy, Completeness, Relevance, Clarity.  
- **Faithfulness**: Error refutation rate, Evidence grounding, Contradiction rate.  
- **Efficiency**: Token usage, **Latency per question (p50/p95)**, Accuracy/cost trade-off.  
- **Robustness**: Reduction in suspicious patterns, stress tests (abstract “Why/How” questions, adversarial inputs).  

## Baselines
- Single LLM (e.g., Mistral, CodeLlama).  
- ToM teacher–student judge (AAAI-AISI baseline).  
- Majority voting / self-consistency of SLMs.  
- Proposed SLM multi-agent debate.  

## Ablation Studies
- Vary **#agents** (1, 3, 5, 7).  
- Vary **#rounds** (0–3, with/without suspicion triggers).  
- Compare intervention types: ToM vs Debate vs Hybrid.  
- Judge variants: Rule-based vs small-LLM vs hybrid.  
- Lesson Bank: enabled vs disabled.  

## Contributions
- Extend ToM-based evaluation with **scalable SLM debate**.  
- Demonstrate improved **faithfulness and robustness** at lower cost.  
- Provide an open framework for **reliable reasoning in code comprehension**.  

