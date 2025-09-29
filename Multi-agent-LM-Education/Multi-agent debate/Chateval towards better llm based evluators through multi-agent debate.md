# Chateval: Towards better LLM-based evaluators through multi agent debate
In machine learining, we were using using accuracy, f1 scores to evaluate our results, however, in large language models, where we do text evaluation, we are using LLM's potential to evaluate our results. Single-agents are used to evluate the response. However, there is a gap between human evaluation quality and current LLM judge's effectiveness.

In multiagent based approach a group of LLMs synergize with an array of intelligent counter parts.
Chateval is a multiagent refree team to autonomusly discuss and evaluate the the quality of generated responses from different models on open ended.
Also, remember that n-grams, rouge, BLEU, and METEOR show a relatively low correlation with human hudgements particularly, in the context of tasks involving open-ended generation or requiring domain-specific expertise.
Studies have shown that multiple LLM can further improve one another through debate and cooperation. By incorporating multiple LLMS into integrated group and designing specific interaction mechanisms, different llms can engage in the proposing and delibrating unique responses and thought processes accross several rounds.

ChatEval is a system that enable each agent to empliy varied communication strategoes in collaborative discussion, working towards formulating final judgements. Every agent within chateval is endowed a unique persona. This deliberate design ensure that each agent focus on distinct perspective and brings specific expertise to the table.

Main contribution of this research is proposing multi-agent based framework