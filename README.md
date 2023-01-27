# Using pipeline tools to ensure analyses are reproducible and understandable, using snakemake

This half-day course explains why pipeline tools such as [make](https://www.gnu.org/software/make/), [snakemake](https://snakemake.readthedocs.io/en/stable/tutorial/short.html) and [targets](https://books.ropensci.org/targets/) are indispensible tools in (reproducible) data analyses.

The `snakemake` code was created by [Isaac Ellman](https://github.com/Ellmen).

## Feedback survey
If you have taken this course and are willing to provide a answers to a short (1-2 minute) survey, please fill these in [here](https://forms.gle/r9QZaupsgZvKfBn89).

## Lecture and problem sets
There is a short lecture [here](presentations/pipeline_tools.html).

Applied example: there are two folders:

TODO

## Steps of analysis

1. get and clean data
2. fit a model: `ozone ~ temperature`
3. plot the model's fit versus data
4. diagnose any issues with model fit; if necessary, change the model and rerun the above steps

## Applied target steps

1. Clone this repo <br> `$ git clone https://github.com/open-courses-statistics-data-science/pipeline_tools_snakemake.git`
2. Move to that directory <br> `$ cd pipeline_tools_snakemake`
3. Create the Conda environment and activate it (see [Setup](#setup) section below) <br> `$ conda env create --file environment.yml` <br> `$ conda activate pipeline_tools_snakemake`
4. Create a visualiation of the whole process DAG using the commandline (find more information [here](https://snakemake.readthedocs.io/en/stable/tutorial/basics.html#step-4-indexing-read-alignments-and-visualizing-the-dag-of-jobs)) <br> You will need to open this using your operating system <br> `$ snakemake --dag all | dot -Tsvg > dag.svg`
5. Run the full pipeline <br> `$ snakemake --cores 1 all`
6. Create the visualisation again to see the difference once executed <br> `$ snakemake --dag all | dot -Tsvg > dag_executed.svg`

## Prerequisites

- basic Python skills
- some experience of having done data analysis


## Setup
In order to run the code in this repository, `snakemake` and some other Python packages must be installed.

### Conda
A [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) environment can be created and activated from the `environment.yml` using the following commands:
1. `$ conda env create --file environment.yml`
2. `$ conda activate pipeline_tools_snakemake`

From this environment `snakemake` commands can be executed.

### Pip
Since `snakemake` has non-Python dependencies, installation using `pip` is not recommended.
See [`snakemake` docs](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#installation-via-pip) for more information. 
