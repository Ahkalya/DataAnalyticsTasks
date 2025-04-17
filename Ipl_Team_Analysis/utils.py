team_name_map = {
    'Royal Challengers Bengaluru': 'Royal Challengers Bangalore',
    'Punjab Kings': 'Kings XI Punjab',
    'Delhi Daredevils': 'DC',
    'Rising Pune Supergiant': 'Rising Pune Supergiants',
    'Mumbai Indians': 'MI',
    'Kolkata Knight Riders': 'KKR',
    'Chennai Super Kings': 'CSK',
    'Sunrisers Hyderabad': 'SRH',
    'Rajasthan Royals': 'RR',
    'Deccan Chargers': 'DC',
    'Gujarat Lions': 'GL'
}

def standardize_team_names(df, cols):
    for col in cols:
        df[col] = df[col].str.strip().str.title().replace(team_name_map)
    return df
