---
layout: pub
type: arxiv
key: wang2023moviepuzzle
title: >
    MoviePuzzle: Visual Narrative Reasoning through Multimodal Order Learning
author: Jianghui Wang, Yuxuan Wang, Dongyan Zhao, Zilong Zheng
equalauthor: Jianghui Wang, Yuxuan Wang
correspondance: Zilong Zheng
website: https://yzhu.io/publication/teaming2022scirob/
abbr: ArXiv
journal: ArXiv
supp: 
video: 
code: https://github.com/MoviePuzzle
year: 2023
sticky: true
abstract: >
    We introduce MoviePuzzle, a novel challenge that targets visual narrative reasoning and holistic movie understanding. Despite the notable progress that has been witnessed in the realm of video understanding, most prior works fail to present tasks and models to address holistic video understanding and the innate visual narrative structures existing in long-form videos. To tackle this quandary, we put forth MoviePuzzle task that amplifies the temporal feature learning and structure learning of video models by reshuffling the shot, frame, and clip layers of movie segments in the presence of video-dialogue information. We start by establishing a carefully refined dataset based on MovieNet by dissecting movies into hierarchical layers and randomly permuting the orders. Besides benchmarking the MoviePuzzle with prior arts on movie understanding, we devise a Hierarchical Contrastive Movie Clustering (HCMC) model that considers the underlying structure and visual semantic orders for movie reordering. Specifically, through a pairwise and contrastive learning approach, we train models to predict the correct order of each layer. This equips them with the knack for deciphering the visual narrative structure of movies and handling the disorder lurking in video data. Experiments show that our approach outperforms existing state-of-the-art methods on the \MoviePuzzle benchmark, underscoring its efficacy.
bibtex: >
    @misc{wang2023moviepuzzle,
      title={MoviePuzzle: Visual Narrative Reasoning through Multimodal Order Learning}, 
      author={Jianghui Wang and Yuxuan Wang and Dongyan Zhao and Zilong Zheng},
      year={2023},
      eprint={2306.02252},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2306.02252}, 
    }
---