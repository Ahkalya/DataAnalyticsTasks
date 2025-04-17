
from db_connection import get_connection
from stats_analyzer import IPLStatsAnalyzer

def display_welcome_page():
    print("==============================")
    print("Welcome to IPL Status Analyzer!")
    print("==============================")
    print("1. Show Team Status (Match Wins & Trophies)")
    print("2. Show Team Performance (Runs & Wickets)")
    print("3. Show Top Scorers")
    print("4. Run Phase Analysis (Run Distribution by Phase)")
    print("5. Exit")
    print("==============================")

def show_team_stats(analyzer):
    print("\nSelect Metric:")
    print("1. Total Match Wins")
    print("2. IPL Trophies (Final Wins)")
    choice = input("Enter your choice (1-2): ")
    
    if choice == '1':
        analyzer.show_team_stats()
    elif choice == '2':
        analyzer.show_team_stats()  
    else:
        print("Invalid choice. Please try again.")
def show_team_performance(analyzer):
    print("\nSelect Metric:")
    print("1. Total Runs by Team")
    print("2. Total Wickets by Team")
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        analyzer.show_runs()
    elif choice == '2':
        analyzer.show_wickets()
    else:
        print("Invalid choice. Please try again.")


def main():
    # Establish database connection
    conn = get_connection()
    
    analyzer = IPLStatsAnalyzer(conn)
    
    while True:
        display_welcome_page()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_team_stats(analyzer)
        elif choice == '2':
            show_team_performance(analyzer)
        elif choice == '3':
            analyzer.show_top_scorers()
        elif choice == '4':
            analyzer.run_phase_analysis()
        elif choice == '5':
            print("Exiting IPL Stats Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
