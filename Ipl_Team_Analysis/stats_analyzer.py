import pandas as pd
import plotly.express as px
from utils import standardize_team_names

class IPLStatsAnalyzer:
    def __init__(self, conn):
        self.conn = conn

    def show_team_stats(self):
        try:
            df = pd.read_sql("SELECT winner, team1, team2, match_type FROM matches", self.conn)
            df = standardize_team_names(df, ['winner', 'team1', 'team2'])

            # Total Match Wins
            wins = df['winner'].value_counts().reset_index()
            wins.columns = ['Team', 'Wins']
            wins = wins.sort_values('Wins', ascending=False)

            print("\n🏆 Total Match Wins:\n", wins.to_string(index=False))
            px.bar(wins, x='Team', y='Wins', title='Most IPL Match Wins by Team',
                   color='Wins', color_continuous_scale='Rainbow').show()

            # IPL Trophies (Final Wins)
            finals = df[df['match_type'].str.lower() == 'final']
            trophies = finals['winner'].value_counts().reset_index()
            trophies.columns = ['Team', 'Trophies']
            trophies = trophies.sort_values('Trophies', ascending=False)

            print("\n IPL Trophies:\n", trophies.to_string(index=False))
            px.bar(trophies, x='Team', y='Trophies', title='IPL Trophies by Team',
                   color='Trophies', color_continuous_scale='Viridis').show()

        except Exception as e:
            print("Error in show_team_stats:", e)

    def show_team_performance(self):
        try:
            df = pd.read_sql("SELECT batting_team, bowling_team, total_runs, dismissal_kind FROM deliveries", self.conn)
            df = standardize_team_names(df, ['batting_team', 'bowling_team'])

            self.show_runs(df)
            self.show_wickets(df)

        except Exception as e:
            print(" Error in show_team_performance:", e)

    def show_runs(self, df=None):
        try:
            if df is None:
                df = pd.read_sql("SELECT batting_team, total_runs FROM deliveries", self.conn)
                df = standardize_team_names(df, ['batting_team'])

            runs = df.groupby('batting_team', as_index=False)['total_runs'].sum()
            runs = runs.sort_values('total_runs', ascending=False)

            print("\n Total Runs by Team:\n", runs.to_string(index=False))
            px.bar(runs, x='batting_team', y='total_runs',
                   title='Total Runs by Each IPL Team',
                   color='total_runs', color_continuous_scale='Viridis').show()

        except Exception as e:
            print(" Error in show_runs:", e)

    def show_wickets(self, df=None):
        try:
            if df is None:
                df = pd.read_sql("SELECT bowling_team, dismissal_kind FROM deliveries", self.conn)
                df = standardize_team_names(df, ['bowling_team'])

            dismissals = ['bowled', 'caught', 'lbw', 'stumped', 'caught and bowled', 'hit wicket']
            df['is_wicket'] = df['dismissal_kind'].isin(dismissals).astype(int)

            wickets = df.groupby('bowling_team', as_index=False)['is_wicket'].sum()
            wickets.columns = ['Team', 'Wickets']
            wickets = wickets.sort_values('Wickets', ascending=False)

            print("\n Total Wickets by Team:\n", wickets.to_string(index=False))
            px.bar(wickets, x='Team', y='Wickets',
                   title='Total Wickets by Each IPL Team',
                   color='Wickets', color_continuous_scale='Viridis').show()

        except Exception as e:
            print(" Error in show_wickets:", e)

    def show_top_scorers(self):
        try:
            df = pd.read_sql("SELECT batter, batsman_runs FROM deliveries", self.conn)
            player_runs = df.groupby('batter', as_index=False)['batsman_runs'].sum()
            top_players = player_runs.sort_values('batsman_runs', ascending=False).head(10)

            print("\n Top 10 Run Scorers:\n", top_players.to_string(index=False))
            px.bar(top_players, x='batter', y='batsman_runs',
                   title='Top 10 IPL Players by Runs Scored',
                   color='batsman_runs', color_continuous_scale='Viridis').show()

        except Exception as e:
            print(" Error in show_top_scorers:", e)

    def run_phase_analysis(self):
        try:
            df = pd.read_sql("SELECT batting_team, total_runs, `over` FROM deliveries", self.conn)
            df = standardize_team_names(df, ['batting_team'])

            df['phase'] = df['over'].apply(self.classify_phase)
            phase_data = df.groupby(['batting_team', 'phase'], as_index=False)['total_runs'].sum()
            phase_data.columns = ['Team', 'Phase', 'Runs']

            # Sort teams by total run contribution
            team_order = phase_data.groupby('Team')['Runs'].sum().sort_values(ascending=False).index.tolist()
            phase_data['Team'] = pd.Categorical(phase_data['Team'], categories=team_order, ordered=True)

            print("\n Run Distribution by Phase:\n", phase_data.to_string(index=False))
            px.bar(phase_data, x='Team', y='Runs', color='Phase',
                   barmode='group', title='Run Distribution by Match Phase',
                   color_discrete_sequence=px.colors.qualitative.Set2).show()

        except Exception as e:
            print(" Error in run_phase_analysis:", e)

    def classify_phase(self, over):
        if 1 <= over <= 6:
            return 'Powerplay'
        elif 7 <= over <= 15:
            return 'Middle Overs'
        else:
            return 'Death Overs'
