"""Runs all the laboratory scripts in sequence.

Regenerates: data (data/*.csv) and, in FIG = volumes/lecture_notes/lecture_notes_1_lp_modelling/figure/,
the data for the pgfplots figures (FIG/dat/*.csv), TikZ diagrams (FIG/*.tex), matplotlib
previews (FIG/*.pdf); then the chapter notebooks (notebooks/*.ipynb).

Usage:  python3 run_all.py
"""
import subprocess
import sys
import time
from pathlib import Path

SCRIPT = [
    "lab05_production.py",
    "lab06_ev_charging.py",
    "lab07_dea.py",
    "lab08_newsvendor.py",
    "lab09_var_cvar.py",
    "lab10_arbitrage.py",
    "lab11_regression.py",
]

base = Path(__file__).resolve().parent
inizio = time.time()
for s in SCRIPT:
    print(f"\n{'#' * 72}\n# {s}\n{'#' * 72}")
    esito = subprocess.run([sys.executable, str(base / s)], cwd=base)
    if esito.returncode != 0:
        print(f"ERROR in {s}: stopping.")
        sys.exit(1)
print(f"\n{'#' * 72}\n# make_notebooks.py\n{'#' * 72}")
esito = subprocess.run([sys.executable, str(base / "make_notebooks.py")], cwd=base)
if esito.returncode != 0:
    print("ERROR while generating the notebooks: stopping.")
    sys.exit(1)

print(f"\nAll scripts completed in {time.time() - inizio:.1f} s.")
