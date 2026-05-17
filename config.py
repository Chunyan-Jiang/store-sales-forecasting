from pathlib import Path

ROOT = Path(__file__).parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
OUTPUTS = ROOT / "outputs"
MODELS_DIR = OUTPUTS / "models"
SUBMISSIONS_DIR = OUTPUTS / "submissions"
PLOTS_DIR = OUTPUTS / "plots"

LGBM_PARAMS = {
    "objective": "regression",
    "metric": "rmse",
    "num_leaves": 64,
    "learning_rate": 0.05,
    "n_estimators": 1000,
    "verbosity": -1,
}