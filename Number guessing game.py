import random


def get_difficulty():
    """Ask the player to choose a difficulty level."""
    print("\n🎮 NUMBER GUESSING GAME")
    print("=" * 30)
    print("Choose difficulty:")
    print("  1. Easy   (1–50,  8 attempts)")
    print("  2. Medium (1–100, 7 attempts)")
    print("  3. Hard   (1–200, 6 attempts)")

    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 50, 8, "Easy"
        elif choice == "2":
            return 1, 100, 7, "Medium"
        elif choice == "3":
            return 1, 200, 6, "Hard"
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(min_num, max_num):
    """Keep asking until the user gives a valid number."""
    while True:
        try:
            guess = int(input(f"\nYour guess: "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"⚠️  Please enter a number between {min_num} and {max_num}.")
        except ValueError:
            print("⚠️  That's not a valid number. Try again.")


def play_round(min_num, max_num, max_attempts, difficulty):
    """Play one round of the game. Returns True if player wins."""
    secret = random.randint(min_num, max_num)
    attempts = 0

    print(f"\n🔒 I'm thinking of a number between {min_num} and {max_num}.")
    print(f"   Difficulty: {difficulty} | Attempts: {max_attempts}")
    print("-" * 40)

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"[{'●' * attempts}{'○' * remaining}]  {remaining} attempt(s) left")

        guess = get_valid_guess(min_num, max_num)
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Correct! You guessed it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            return True, attempts
        elif guess < secret:
            print("📈 Too low! Try higher.")
        else:
            print("📉 Too high! Try lower.")

    print(f"\n❌ Out of attempts! The number was {secret}.")
    return False, attempts


def show_stats(wins, losses, streak, best_streak):
    """Display the current stats."""
    total = wins + losses
    win_rate = round((wins / total) * 100) if total > 0 else 0
    print("\n📊 STATS")
    print(f"   Wins: {wins}  |  Losses: {losses}  |  Win rate: {win_rate}%")
    print(f"   Current streak: {streak}  |  Best streak: {best_streak}")


def main():
    """Main game loop."""
    wins, losses, streak, best_streak = 0, 0, 0, 0

    print("\nWelcome to the Number Guessing Game!")

    while True:
        min_num, max_num, max_attempts, difficulty = get_difficulty()

        won, attempts = play_round(min_num, max_num, max_attempts, difficulty)

        if won:
            wins += 1
            streak += 1
            best_streak = max(best_streak, streak)
        else:
            losses += 1
            streak = 0

        show_stats(wins, losses, streak, best_streak)

        again = input("\n🔁 Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Keep coding! 🚀\n")
            break


if __name__ == "__main__":
    main()