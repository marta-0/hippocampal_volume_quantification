## Project Instructions

### Section 2: Training a segmentation CNN

<img src="./readme.img/loss.png" width=400em>

You will perform this section in the same workspace as Section 1: **Workspace 1**. This workspace has a Python virtual environment called **medai** [TODO: how are we doing this?] which is set up with everything that you need to analyze inspect the dataset and prepare it for machine learning.

In the directory called `section2/src` you will find the source code that forms the framework for your machine learning pipeline.

You will be using [PyTorch](https://pytorch.org/) to train the model, similar to our Segmentation&Classification Lesson, and we will be using [Tensorboard](https://www.tensorflow.org/tensorboard/) to visualize the results.

You will use the script `run_ml_pipeline.py` to kick off your training pipeline. You can do so right now! The script will not get far, though. It only contains the skeleton of the final solution and a lot of comments. You will need to follow the instructions inside the code files to complete the section and train your model. Same convention is used as in Section 1:

* Comments that start with `# TASK` are tasks, instructions, or questions you **have** to complete
* All other types of comments provide additional background, questions or contain suggestions to make your project stand out.

You will need to complete all the instructional comments in the code in order to complete this section. You can do this in any order, but it makes most sense to start with the code in `run_ml_pipeline.py`.

The code has hooks to log progress to Tensorboard. In order to see the Tensorboard output you need to launch Tensorboard executable from the same directory where `run_ml_pipeline.py` is located using the following command:

> `tensorboard --logdir runs --bind_all`

After that, Tensorboard will write logs into directory called `runs` and you will be able to view progress by opening the browser and navigating to default port 6006 of the machine where you are running it.

#### Expected Outcome

Navigate to the directory `section2/out` to find the [README.md](section2/out/README.md) with instructions on what is expected as the outcome.
