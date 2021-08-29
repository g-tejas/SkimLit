<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/g-tejas/SkimLit">
    <img src="img/logo.png" alt="Logo" width="430" height="100">
  </a>

  <p align="center">
    <a>
        <a style="margin: 0 5px" href="https://github.com/g-tejas/SkimLit/graphs/contributors"><img src="https://img.shields.io/github/contributors/g-tejas/SkimLit.svg?style=plastic" alt="Contributors"></a>
    </a>
    <a>
        <a style="margin: 0 5px" href="https://github.com/g-tejas/SkimLit/network/members"><img src="https://img.shields.io/github/forks/g-tejas/SkimLit.svg?style=plastic" alt="Forks"></a>
    </a>
    <a>
        <a style="margin: 0 5px" href="https://github.com/g-tejas/SkimLit/issues"><img src="https://img.shields.io/github/issues/g-tejas/SkimLit.svg?style=plastic" alt="Issues"></a>
    </a>
    <a>
        <a style="margin: 0 5px" href="https://github.com/g-tejas/SkimLit/stargazers"><img src="https://img.shields.io/github/stars/g-tejas/SkimLit.svg?style=plastic" alt="Stars"></a>
    </a>
    <a>
        <a style="margin: 0 5px" href="https://colab.research.google.com/drive/1iceHKxffz_oLud9Zoxu300FZKANyI6kx?usp=sharing"><img    src="https://colab.research.google.com/assets/colab-badge.svg"></a>
    </a>
  </p>


  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/g-tejas/SkimLit"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/g-tejas/SkimLit">View Demo</a>
    ·
    <a href="https://github.com/g-tejas/SkimLit/issues">Report Bug</a>
    ·
    <a href="https://github.com/g-tejas/SkimLit/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a replication of the deep learning model behind the 2017 paper [PubMed 200k RCT: a Dataset for Sequenctial Sentence Classification in Medical Abstracts](https://arxiv.org/abs/1710.06071).

The paper presents a new dataset called PubMed 200k RCT which consists of ~200,000 labelled Randomized Controlled Trial (RCT) abstracts.

The goal of the dataset was to explore the ability for NLP models to classify sentences which appear in sequential order. In other words, given the abstract of a RCT, what role does each sentence serve in the abstract?

[![Product Name Screen Shot][product-screenshot]](https://github.com/g-tejas/SkimLit)
*Example inputs [harder to read abstract from PubMed](https://pubmed.ncbi.nlm.nih.gov/28942748/) and outputs [easier to read abstract](https://pubmed.ncbi.nlm.nih.gov/32537182/) of the model we're going to build. The model will take an abstract wall of text and predict the section label each sentence should have*

#### Model Input

For example, can we train an NLP model which takes the following input (note: the following sample has had all numerical symbols replaced with "@"):

> To investigate the efficacy of @ weeks of daily low-dose oral prednisolone in improving pain , mobility , and systemic low-grade inflammation in the short term and whether the effect would be sustained at @ weeks in older adults with moderate to severe knee osteoarthritis ( OA ). A total of @ patients with primary knee OA were randomized @:@ ; @ received @ mg/day of prednisolone and @ received placebo for @ weeks. Outcome measures included pain reduction and improvement in function scores and systemic inflammation markers. Pain was assessed using the visual analog pain scale ( @-@ mm ). Secondary outcome measures included the Western Ontario and McMaster Universities Osteoarthritis Index scores , patient global assessment ( PGA ) of the severity of knee OA , and @-min walk distance ( @MWD )., Serum levels of interleukin @ ( IL-@ ) , IL-@ , tumor necrosis factor ( TNF ) - , and high-sensitivity C-reactive protein ( hsCRP ) were measured. There was a clinically relevant reduction in the intervention group compared to the placebo group for knee pain , physical function , PGA , and @MWD at @ weeks. The mean difference between treatment arms ( @ % CI ) was @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; and @ ( @-@ @ ) , p < @ , respectively. Further , there was a clinically relevant reduction in the serum levels of IL-@ , IL-@ , TNF - , and hsCRP at @ weeks in the intervention group when compared to the placebo group. These differences remained significant at @ weeks. The Outcome Measures in Rheumatology Clinical Trials-Osteoarthritis Research Society International responder rate was @ % in the intervention group and @ % in the placebo group ( p < @ ). Low-dose oral prednisolone had both a short-term and a longer sustained effect resulting in less knee pain , better physical function , and attenuation of systemic inflammation in older patients with knee OA ( ClinicalTrials.gov identifier NCT@ ).


#### Model Output
And returns the following output:
```sh
['###24293578\n',
 'OBJECTIVE\tTo investigate the efficacy of @ weeks of daily low-dose oral prednisolone in improving pain , mobility , and systemic low-grade inflammation in the short term and whether the effect would be sustained at @ weeks in older adults with moderate to severe knee osteoarthritis ( OA ) .\n',
 'METHODS\tA total of @ patients with primary knee OA were randomized @:@ ; @ received @ mg/day of prednisolone and @ received placebo for @ weeks .\n',
 'METHODS\tOutcome measures included pain reduction and improvement in function scores and systemic inflammation markers .\n',
 'METHODS\tPain was assessed using the visual analog pain scale ( @-@ mm ) .\n',
 'METHODS\tSecondary outcome measures included the Western Ontario and McMaster Universities Osteoarthritis Index scores , patient global assessment ( PGA ) of the severity of knee OA , and @-min walk distance ( @MWD ) .\n',
 'METHODS\tSerum levels of interleukin @ ( IL-@ ) , IL-@ , tumor necrosis factor ( TNF ) - , and high-sensitivity C-reactive protein ( hsCRP ) were measured .\n',
 'RESULTS\tThere was a clinically relevant reduction in the intervention group compared to the placebo group for knee pain , physical function , PGA , and @MWD at @ weeks .\n',
 'RESULTS\tThe mean difference between treatment arms ( @ % CI ) was @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; and @ ( @-@ @ ) , p < @ , respectively .\n',
 'RESULTS\tFurther , there was a clinically relevant reduction in the serum levels of IL-@ , IL-@ , TNF - , and hsCRP at @ weeks in the intervention group when compared to the placebo group .\n',
 'RESULTS\tThese differences remained significant at @ weeks .\n',
 'RESULTS\tThe Outcome Measures in Rheumatology Clinical Trials-Osteoarthritis Research Society International responder rate was @ % in the intervention group and @ % in the placebo group ( p < @ ) .\n',
 'CONCLUSIONS\tLow-dose oral prednisolone had both a short-term and a longer sustained effect resulting in less knee pain , better physical function , and attenuation of systemic inflammation in older patients with knee OA ( ClinicalTrials.gov identifier NCT@ ) .\n',
 '\n']
 ```

### Problem Statement
The number of RCT papers released is continuing to increase, those without structured abstracts can be hard to read and in turn slow down researchers moving through the literature.

### Solution
Create an NLP model to classify abstract sentences into the role they play (e.g. objective, methods, results, etc) to enable researchers to skim through the literature (hence SkimLit 🤓🔥) and dive deeper when necessary.


A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This section lists the major frameworks this project uses. 
* Tensorflow
* scikit-learn
* numpy
* pandas
* spacy




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/g-tejas/SkimLit.git
   ```
2. Install dependencies and libraries
   ```sh
   pip install -r requirements.txt
   ```
3. Run the jupyter notebook, `skimlit.ipynb`, and experiment!
   ```JS
   jupyter notebook
   ```



<!-- USAGE EXAMPLES -->
## Usage

Possible usage ideas would be a browser extension called SkimLit that reads the html of a RCT website, and automatically preprocesses and formats the abstract with the predicted labels

_If you would like to contribute and implement the above feature, please refer to the  [Contributing](#contributing) section_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/g-tejas/SkimLit/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. 

All ideas – no matter how outrageous – **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


Project Link: [https://github.com/g-tejas/SkimLit](https://github.com/g-tejas/SkimLit)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [TFHub Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/4)
* [PubMed 200k RCT: a Dataset for Sequential Sentence Classification in Medical Abstracts
](https://arxiv.org/abs/1710.06071)
* [Neural Networks for Joint Sentence Classification
in Medical Paper Abstracts](https://arxiv.org/pdf/1612.05251.pdf)
* [Daniel Bourke's version](https://github.com/mrdbourke/tensorflow-deep-learning/blob/main/09_SkimLit_nlp_milestone_project_2.ipynb)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: https://camo.githubusercontent.com/de191b8b8fd152f21862c26f84ad75b979eef5d4/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6d7264626f75726b652f74656e736f72666c6f772d646565702d6c6561726e696e672f6d61696e2f696d616765732f30392d736b696d6c69742d6f766572766965772d696e7075742d616e642d6f75747075742e706e67