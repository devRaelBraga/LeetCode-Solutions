import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
    # 558ms - beats 27.96%
    return(employees[:3])
