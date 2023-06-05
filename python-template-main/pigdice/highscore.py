"""saves Highscore in txt file."""
class Highscore:

    def __init__(self):
        self.filename = "high_scores.txt"

    # Function to update the high score file (high score = minimum number of turns necessary to win a game
    def update_high_scores(self, player_name, game_turns):
        high_scores = {}
        try:
            # Read the high score file
            with open(self.filename, "r") as file:
                for line in file:
                    name, turns = line.strip().split(",")
                    high_scores[name] = int(turns)
        except FileNotFoundError:
            pass

        # Update the high score for the player or add a new entry
        if player_name in high_scores:
            if high_scores[player_name] > int(game_turns):
                high_scores[player_name] = int(game_turns)
        else:
            high_scores[player_name] = int(game_turns)

        # Write the updated high scores to the file
        with open(self.filename, "w") as file:
            for name, turns in high_scores.items():
                file.write(f"{name},{turns}\n")

    # Function to display the high score record
    def display_high_scores(self):
        high_scores = {}
        try:
            # Read the high score file
            with open(self.filename, "r") as file:
                for line in file:
                    name, turn = line.strip().split(",")
                    high_scores[name] = int(turn)

            # Sort the high scores by the least number of rounds
            sorted_scores = sorted(high_scores.items(), key=lambda x: x[1])

            # Display the high score record
            print("\nHigh Scores:")
            print("-" * 13)
            for i, (name, turn) in enumerate(sorted_scores, start=1):
                print(f"{i}. {name}: {turn} rounds")

        except FileNotFoundError:
            print("No high scores available.")
