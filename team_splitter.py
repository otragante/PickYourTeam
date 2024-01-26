import random

def split_users_into_teams(users):
    # Shuffle the list of users randomly
    random.shuffle(users)

    # Calculate the midpoint to split the users into two teams
    midpoint = len(users) // 2

    # Assign users to Team A and Team B
    team_a = users[:midpoint]
    team_b = users[midpoint:]

    return team_a, team_b

def main():
    # Input the list of users
    users = input("Enter a list of users (comma-separated): ").split(',')

    # Remove leading and trailing whitespaces from user names
    users = [user.strip() for user in users]

    # Split users into teams
    team_a, team_b = split_users_into_teams(users)

    # Display the teams
    print("Black Team:", team_a)
    print("White Team", team_b)

if __name__ == "__main__":
    main()
