import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    views  = views.rename(
        columns={'author_id':'id'}
    )
    
    return (views[views['id'] == views['viewer_id'] ][['id']]).drop_duplicates().sort_values(by = ['id'])