# GPT-SW3

Instructions for how you can install the GPT-SW3 mode and a very simple user interface for interacting with it.

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

### Sample outputs
* model: gpt-sw3-1.3b
* prompt: `Och där mitt på kullen, stod en livs levande dromedar`
* temperature: 0.7
* max_length: 128
* top_p: 1.0
* number of samples: 3

####  Sample 1 

Och där mitt på kullen, stod en livs levande dromedar. Så himla söt!

Har ni varit på någon djurpark?

2016-07-25 @ 21:23:00<|endoftext|>

####  Sample 2 

Och där mitt på kullen, stod en livs levande dromedar.

– Jag var tvungen att fota den, säger Stefan.

BILD: Privat |

– Jag är ju född i Östersund och där finns det en dromedarpark. Jag fick en idé att åka dit och fota den.

Stefan hade som mål att få med sig tre dromedarer hem.

– Men det hade varit alldeles för lätt att bara ha med sig två, säger han.

BILD: Privat |

– Jag skulle ha fått ta med mig min kompis också, säger Stefan.<|endoftext|>

####  Sample 3 

Och där mitt på kullen, stod en livs levande dromedar. Han hade stora öron, och en stor haka. Och han log när han såg på mig. Jag kunde inte låta bli att le. Han log när han såg på mig. Jag kunde inte låta bli att le med. Vi stod där och såg på varandra. Och jag tänkte på honom. På den där dagen. Det var så vackert. Det var som om någon hade blåst in en ny dag i mitt liv. Jag vet inte vem som blåste in den, men jag visste att det var jag."

"Mannen som jag mötte på kullen, han hade ett ljus i sitt ansikte. Jag vet inte om det var ett

## References

https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

https://huggingface.co/AI-Sweden-Models