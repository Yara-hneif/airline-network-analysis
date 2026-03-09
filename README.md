# Airline Network Analysis (OpenFlights)

## Overview
Baseline v0: reproducible project scaffold using Docker Dev Containers + structured notebooks.

## How to run
1) Open in Cursor
2) Dev Containers: Rebuild and Reopen in Container
3) Inside container:
   - `pip install -e .`
4) Run notebooks in order:
   - 01_ingest_raw
   - 02_clean_transform
   - 03_eda_overview
   - 04_build_graph_metrics

## Data
Raw OpenFlights `.dat` files are stored in `data/raw/`.
Clean outputs are generated locally into `data/processed/` (ignored by git in training mode).