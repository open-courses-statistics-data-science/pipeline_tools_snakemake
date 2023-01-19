rule all:
    input:
        "outputs/reg_plot.pdf"

rule clean_data:
    input:
        "data/raw/airquality.csv"
    output:
        "data/cleaned/airquality_cleaned.csv"
    script:
        "scripts/clean_data.py"

rule fit_linear_model:
    input:
        "data/cleaned/airquality_cleaned.csv"
    output:
        "models/linear_model.joblib"
    script:
        "scripts/fit_linear_model.py"

rule plot_regression:
    input:
        "models/linear_model.joblib",
        "data/cleaned/airquality_cleaned.csv"
    output:
        "outputs/reg_plot.pdf"
    script:
        "scripts/plot_linear_model.py"
