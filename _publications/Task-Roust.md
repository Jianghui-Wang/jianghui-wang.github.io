---
layout: pub
type: inproceedings
key: 
title: >
    Task-Robust Pre-Training for Worst-Case Downstream Adaptation
author: Jianghui Wang, Yang Chen, Xingyu Xie, Cong Fang, Zhouchen Lin
equalauthor: Jianghui Wang, Yang Chen
correspondance: Cong Fang, Zhouchen Lin
website: 
abbr: NeurIPS'23
Booktitle: Advances in Neural Information Processing Systems 2023
supp: 
video: 
code: 
year: 2023
sticky: true
abstract: >
    Pre-training has achieved remarkable success when transferred to downstream tasks. In machine learning, we care about not only the good performance of a model but also its behavior under reasonable shifts of condition. The same philosophy holds when pre-training a foundation model. However, the foundation model may not uniformly behave well for a series of related downstream tasks. This happens, for example, when conducting mask recovery regression where the recovery ability or the training instances diverge like pattern features are extracted dominantly on pre-training, but semantic features are also required on a downstream task. This paper considers pre-training a model that guarantees a uniformly good performance over the downstream tasks. We call this goal as downstream-task robustness. Our method first separates the upstream task into several representative ones and applies a simple minimax loss for pre-training. We then design an efficient algorithm to solve the minimax loss and prove its convergence in the convex setting. In the experiments, we show both on large-scale natural language processing and computer vision datasets our method increases the metrics on worse-case downstream tasks. Additionally, some theoretical explanations for why our loss is beneficial are provided. Specifically, we show fewer samples are inherently required for the most challenging downstream task in some cases.
bibtex: >
    @inproceedings{wang2023taskrobust,
        author = {Wang, Jianghui and Chen, Yang and Xie, Xingyu and Fang, Cong and Lin, Zhouchen},
        booktitle = {Advances in Neural Information Processing Systems},
        editor = {A. Oh and T. Naumann and A. Globerson and K. Saenko and M. Hardt and S. Levine},
        pages = {9458--9478},
        publisher = {Curran Associates, Inc.},
        title = {Task-Robust Pre-Training for Worst-Case Downstream Adaptation},
        url = {https://proceedings.neurips.cc/paper_files/paper/2023/file/1e4322fddd833f83c855660ac65e428d-Paper-Conference.pdf},
        volume = {36},
        year = {2023}
    }
---