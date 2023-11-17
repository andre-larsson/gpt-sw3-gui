# GPT-SW3

For installation of the GPT-SW3 model (see references) and a very simple user interface for interacting with it.

## Pre-requisites
* nvidia GPU compatible with CUDA 11.8
* Python 3.11
* conda is installed
* Ubuntu or similar Linux distribution

Tested on Ubuntu 22

## Installation

To create a conda environment and install all dependencies, run:
```bash
conda env create -f environment.yml
```

## Usage

To open the user interface, activate the conda environment and run the `run_app.py` script:
```bash
conda activate gpt-sw3
python run_app.py
```

The model will be available at `http://localhost:7860/`.

## Findings

* Smaller models (<1.3B parameters) often get stuck in a loop
* Models with more than 1.3B parameters seem to run out of memory on a RTX4090
* The gpt-sw3-40b model weights will take about 200GB of disk space
* Even the gpt-sw3-1.3b often give weird results (random timestamps, loops, etc)
* Maybe the larger models are better but was not able to test them (might be able to optimize?)
* Still pretty cool to have a gpt-sw3 model :) 

## References

https://huggingface.co/AI-Sweden-Models