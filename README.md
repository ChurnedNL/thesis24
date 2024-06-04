# thesis24
Public repo for code regarding the Master Thesis of 2024

The `proj_example` directory is an example of the structure that should be followed for your project.  
This structure is based on the [cookiecutter-data-science](
https://cookiecutter-data-science.drivendata.org/) template.

The `proj_example` directory contains a `README.md` file with a description of the project structure. Read it to know how to structure your code. 


On `proj_example/project_nlp_example/modeling/train_main_model_A.py` you will find an example of a script to train an NLP model. You should create a new script for each model you want to train.
You don't need to use the same structure as the example. You can create your own structure. Just make sure you have a train script for each model you want to train (and a predict script if you want to make predictions).


Each model should have its own script to train and evaluate it. The script should be in the `modeling` directory.
model_B is an example of a script to train a new model.


## How to use this repo

1. Copy the contents of this repo to your local machine. (You can also fork it)
2. Create a new directory with the name of your project
3. Copy the contents of `proj_example` to your new directory
4. Start coding!

## What is expected from you
For the models you created, you should:
- Create a script to train the model on the `modeling` directory
- Create a script to make predictions with the model on the `modeling` directory
- Submit notebooks with the analysis on the `notebooks` directory
