from __future__ import annotations
from pathlib import Path
import pandas as pd
from .paths import DATA_PROCESSED_DIR

def ensure_processed_dir() -> None:
    DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def clean_routes_minimal(routes: pd.DataFrame) -> pd.DataFrame:
    """
    Baseline cleaning (no advanced logic):
    - drop rows missing key identifiers
    - ensure numeric IDs where possible
    - keep stops as int
    """
    out = routes.copy()

    # Keep only rows that have source/destination airport IDs
    out = out.dropna(subset=["src_airport_id", "dst_airport_id"])

    # Convert IDs to numeric (invalid -> NaN -> dropped)
    out["src_airport_id"] = pd.to_numeric(out["src_airport_id"], errors="coerce")
    out["dst_airport_id"] = pd.to_numeric(out["dst_airport_id"], errors="coerce")
    out = out.dropna(subset=["src_airport_id", "dst_airport_id"])
    out["src_airport_id"] = out["src_airport_id"].astype(int)
    out["dst_airport_id"] = out["dst_airport_id"].astype(int)
   
    # Stops as int (unknown -> 0)
    out["stops"] = pd.to_numeric(out["stops"], errors="coerce").fillna(0).astype(int)
    return out

def save_csv(df: pd.DataFrame, filename: str) -> Path:
    ensure_processed_dir()
    path = DATA_PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    return path