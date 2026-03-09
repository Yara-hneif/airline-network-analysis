from __future__ import annotations
import pandas as pd
from .paths import DATA_RAW_DIR

NA = "\\N"

def read_airports() -> pd.DataFrame:
    cols = [
        "airport_id", "name", "city", "country", "iata", "icao",
        "lat", "lon", "altitude", "timezone", "dst", "tz_database", "type", "source"
    ]
    return pd.read_csv(
        DATA_RAW_DIR / "airports.dat",
        header=None,
        names=cols,
        quotechar='"',
        encoding="utf-8",
        na_values=NA,
        keep_default_na=True,
    )

def read_airlines() -> pd.DataFrame:
    cols = ["airline_id", "name", "alias", "iata", "icao", "callsign", "country", "active"]
    return pd.read_csv(
        DATA_RAW_DIR / "airlines.dat",
        header=None,
        names=cols,
        quotechar='"',
        encoding="utf-8",
        na_values=NA,
        keep_default_na=True,
    )

def read_routes() -> pd.DataFrame:
    cols = [
        "airline", "airline_id",
        "src_iata", "src_airport_id",
        "dst_iata", "dst_airport_id",
        "codeshare", "stops", "equipment",
    ]
    return pd.read_csv(
        DATA_RAW_DIR / "routes.dat",
        header=None,
        names=cols,
        quotechar='"',
        encoding="utf-8",
        na_values=NA,
        keep_default_na=True,
    )