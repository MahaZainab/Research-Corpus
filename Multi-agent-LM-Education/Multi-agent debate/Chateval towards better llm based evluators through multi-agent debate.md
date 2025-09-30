# Chateval: Towards better LLM-based evaluators through multi agent debate
In machine learining, we were using using accuracy, f1 scores to evaluate our results, however, in large language models, where we do text evaluation, we are using LLM's potential to evaluate our results. Single-agents are used to evluate the response. However, there is a gap between human evaluation quality and current LLM judge's effectiveness.

In multiagent based approach a group of LLMs synergize with an array of intelligent counter parts.
Chateval is a multiagent refree team to autonomusly discuss and evaluate the the quality of generated responses from different models on open ended.
Also, remember that n-grams, rouge, BLEU, and METEOR show a relatively low correlation with human hudgements particularly, in the context of tasks involving open-ended generation or requiring domain-specific expertise.
Studies have shown that multiple LLM can further improve one another through debate and cooperation. By incorporating multiple LLMS into integrated group and designing specific interaction mechanisms, different llms can engage in the proposing and delibrating unique responses and thought processes accross several rounds.

ChatEval is a system that enable each agent to empliy varied communication strategoes in collaborative discussion, working towards formulating final judgements. Every agent within chateval is endowed a unique persona. This deliberate design ensure that each agent focus on distinct perspective and brings specific expertise to the table.

1. Main contribution of this research is proposing multi-agent based framework called chateval that aligns better with human preferences compared with single agent based approach.

2. Various communication strategies and demonstrate the necessity of diverse role prompts in multi-agent debate scenarios.

## Methodology:
There are three main components:

1.debator agents
2. diverse role specification
3. communication strategy

### 1. Debator Agents:
There are multiple LLMs as agents and each one of them is asked to generate their response from the given prompt. Responses from the other agents are served as a chat history which will be replaced in the prompt template.
After configuring the agents, then group debate is started. Where each agent autonomously receives responses from the others and in turn delievers its own responses to them.  

### 2. Diverse Role Specification:

All agents share a common prompt template, they substitute the role description slot with diverse role prompt. Which will specify distinct personalities for different agents.

### Communication strategy:
How to maintain the chat history was a challenge. Three different communication strategies are used.
#### 1. One by one: 
During each round of debate, the ddebater agents take turns in a set of order to generate their responses on the current observation. When it's time for a debator agent to respond, they directly concatenate what previous agents have said into their  history slot.
#### 2. Simultaneous talk
Each debater agents are prompted to asynchronously generate responses in each iteration of the discussion to nullify the impact of speaking order.

#### 3. Simultaneous talk with summarizer:
Along with simulataneous-talk an additional LLM work as a summarizer. At the end of each iteration of the debate, we prompt this extra LLM to summarize the messages conveyed so far and concatenate the summarization into all debator agent's chat history.

There are two methods to reach to a consensus.  One is to ask the debator agent to reach to a consensus at the end of the debate. The otherone is to get the final results from majority of vote among various annotators.

### 4. Experiments:

They evaluate the chateval on two benchmarks, faireval and topical chat, which are open ended question answer and dailogue response generation.

OpenAI' GPT family models are used.(which is homogeneous)
In my research, we will use hetrogeneous group of models.

#### Benchmarks:
1. Open-ended question answer: for each question, they direct three annotators to evaluate the replies given by vicuna 13B and chatgpt model through the rules and then extract the results based on majority of voting.
Baseline: Single-agent: we directly query the LLM to generate the response towards the evaluation
