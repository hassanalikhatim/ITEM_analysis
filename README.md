# ITEM_analysis

The analysis code of the variability, reliability and bias analysis of our paper, ["AI-Enhanced Interview Simulation in the Metaverse: Transforming Professional Skills Training through VR and Generative Conversational AI"](https://www.sciencedirect.com/science/article/pii/S2666920X24001504). You can find the implementation code here: [https://github.com/hassanalikhatim/ITEM](https://github.com/hassanalikhatim/ITEM).

## Abstract
Interviewing skills play a pivotal role in the job application and search, professional development to prepare for interviewing is a neglected area of research. Professional training methods are available but are often prohibitively expensive, limiting opportunities primarily to privileged individuals. To bridge this accessibility gap and democratize access to job opportunities, there is a need to develop automated interview simulation platforms. The advent of Generative AI (GenAI) technology, in particular Large Language Models (LLMs), makes this is viable proposition but progress is hindered by the absence of open-source implementations for reproducibility and comparison, as well as the lack of suitable evaluation benchmarks and experimental setups. In particular, we do not yet know how robust such systems are and if they will be bias-free, factors that will contribute to their acceptability and use. To this end, we propose Interview Training and Education Module (ITEM), a job interview training module that combines Virtual Reality-based metaverse technology with LLM-based GenAI models. Our module creates realistic interview experiences for skill enhancement, complete with personalized feedback and improvement guidelines based on user responses. In this paper, we present an experimental evaluation of the module to ascertain its robustness, including a bias analysis. Firstly, we establish an experimental setup to gauge platform robustness by examining question similarity across varied prompts using Bidirectional and Auto-Regressive Transformers (BART) and topic modeling. Subsequently, we explore biases in three categories—country of origin, religion, and gender—by analyzing ITEM's evaluation scores while manipulating candidate backgrounds, all while keeping their responses unchanged. Our findings indicate potential biases replicated by ITEM, highlighting the need for caution in its application for personal development and training. This pioneering initiative introduces the first open-source module for job interview training within a virtual metaverse, leveraging LLM-based Generative AI, designed for extension and testing by the scientific community, thereby enhancing insights into the limitations and ethical considerations of AI-driven interview simulation platforms.

## Citation
```
@article{nofal2025ai,
  title={AI-enhanced interview simulation in the metaverse: Transforming professional skills training through VR and generative conversational AI},
  author={Nofal, Abdullah Bin and Ali, Hassan and Hadi, Muhammad and Ahmad, Aizaz and Qayyum, Adnan and Johri, Aditya and Al-Fuqaha, Ala and Qadir, Junaid},
  journal={Computers and Education: Artificial Intelligence},
  volume={8},
  pages={100347},
  year={2025},
  publisher={Elsevier}
}
```
