
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity  = activity.sort_values('event_date')
    df = activity[['player_id' , 'event_date']].drop_duplicates(subset='player_id')
    df.columns = ['player_id' , 'first_login']
    #return  df
    return activity

d = {
  'player_id': [1, 1, 1, 3, 3],
  'device_id': [2, 2, 3, 1, 4],
  'event_date': ['2016-03-01', '2016-05-02', '2015-06-25', '2016-03-02', '2016-02-03'],
  'games_played': [5, 6, 1, 0, 5]
}

d = pd.DataFrame(d)
print(game_analysis(d))

