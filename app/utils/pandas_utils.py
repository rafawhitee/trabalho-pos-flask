from typing import Any
import pandas as pd

def do_basic_statistics_by_column(df: Any, column: str) -> dict:
    df_filtered: Any = remove_not_numbers_values(remove_percentage(df[column]))
    return {
        "media": df_filtered.mean(),
        "mediana": df_filtered.median(),
        "desvio_padrao": df_filtered.std()
    }

def remove_percentage(df: Any) -> Any:
    return df.apply(lambda x: float(x.replace('%', '')) if isinstance(x, str) and '%' in x else x)
                    
def remove_not_numbers_values(df: Any) -> Any:
    return df.apply(pd.to_numeric, errors='coerce').dropna()