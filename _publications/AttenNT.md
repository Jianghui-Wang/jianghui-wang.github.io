---
layout: pub
type: inproceedings
key: 
title: >
    NONPARAMETRIC TEACHING OF ATTENTION LEARNERS
author: Zhang, Chen and Wang, Jianghui and Cheng, Bingyang and Chen, Zhongtao and Xu, Wendong and Wang, Cong and Canini, Marco and Orabona, Francesco and Wu, Yik-Chung and Wong, Ngai
equalauthor: Zhang, Chen and Wang, Jianghui
correspondance: Zhang, Chen and Wang, Jianghui
website:
abbr: ICLR'26
booktitle: International Conference on Learning Representations（ICLR）
supp: 
video: 
code: https://github.com/Jianghui-Wang/AttenNT
year: 2026
sticky: true
abstract: >
    Attention learners, neural networks built on the attention mechanism, e.g., transformers, excel at learning the implicit relationships that relate sequences to their corresponding properties, e.g., mapping a given sequence of tokens to the probability of the next token. However, the learning process tends to be costly. To address this, we present a novel paradigm named Attention Neural Teaching (AtteNT) that reinterprets the learning process through a nonparametric teaching perspective. Specifically, the latter provides a theoretical framework for teaching mappings that are implicitly defined (i.e., nonparametric) via example selection. Such an implicit mapping is embodied through a dense set of sequence-property pairs, with the AtteNT teacher selecting a subset to accelerate convergence in attention learner training. By analytically investigating the role of attention on parameter-based gradient descent during training, and recasting the evolution of attention learners, shaped by parameter updates, through functional gradient descent in nonparametric teaching, we show for the first time that teaching attention learners is consistent with teaching importance-adaptive nonparametric learners. These new findings readily commit AtteNT to enhancing learning efficiency of attention learners. Specifically, we observe training time reductions of 13.01% for LLMs and 20.58% for ViTs, spanning both fine-tuning and training-from-scratch regimes. Crucially, these gains are achieved without compromising accuracy; in fact, performance is consistently preserved and often enhanced across a diverse set of downstream tasks.
bibtex: >
    @inproceedings{zhang2026nonparametric,
    title={Nonparametric Teaching for Attention Learners},
    author={Zhang, Chen and Wang, Jianghui and Cheng, Bingyang and Chen, Zhongtao and Xu, Wendong and Wang, Cong and Canini, Marco and Orabona, Francesco and Wu, Yik-Chung and Wong, Ngai},
    booktitle={ICLR},
    year={2026}
    }

---