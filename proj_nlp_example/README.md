# project_example

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

My example project is an example

## Project Organization

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Any documentation for the project
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Unclear what should go here vs in the models directory? 
│                         Maybe notebooks are for exploration and models are for final models? 
│                         See https://cookiecutter-data-science.drivendata.org/opinions/#notebooks-are-for-exploration-and-communication-source-files-are-for-repetition
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── project_example                <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes project_example a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── models                
    │   ├── __init__.py 
    │   ├── predict_model_A.py  <- Code to run model inference with trained models
    │   ├── predict_model_B.py  <- Code to run model inference with trained models          
    │   ├── train_model_A.py    <- Code to train models
    │   └── train_model_B.py    <- Code to train models
    │
    └── plots.py                <- Code to create visualizations  
```

--------

