import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    c = len(players.columns)
    r = len(players)
    l = [r,c]
    return l
    # or 
    #* return list(players.shape)