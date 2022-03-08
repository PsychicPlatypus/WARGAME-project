"""This class stores highscores from the game."""


class highscores:
    """Keeps highscores in seperate .txt file."""

    def short_scores(self, player, score, victory) -> None:
        """Short scores are based on the number of cards at the end."""
        try:
            with open("highscores_short.txt", "a") as f:
                f.write(f"{player}: {score} ---- Won: {victory}\n")
            self.sort_highscores("highscores_short.txt", 1, True)
            self.shorten_list("highscores_short.txt")
        except Exception as err:
            print(err)

    def long_scores(self, player, score, counter) -> None:
        """Long scores are based on the amount of draws."""
        try:    
            with open("highscores_long.txt", "a") as f:
                f.write(f"{player}: {score} ---- Draws: {counter}\n")
            self.sort_highscores("highscores_long.txt", -1, False)
            self.shorten_list("highscores_long.txt")
        except Exception as err:
            print(err)

    def sort_highscores(self, high_file, type_sort, backwards):
        try:
            """Sorts highscores based on the game type."""
            with open(high_file, "r") as txt_file:
                scores = txt_file.readlines()
                scores = sorted(scores, key=lambda i: int(i.split(" ")[type_sort]),
                                reverse=backwards)
            with open(high_file, "w") as w:
                w.writelines(scores)
        except Exception as err:
            print(err)

    def shorten_list(self, high_file):
        """Only allows a certain amount of highscores."""
        try:
            with open(high_file, "r") as f:
                scores = f.readlines()
                should_del = len(scores) > 20
            if should_del:
                with open(high_file, "w") as w:
                    w.writelines(scores[0:20])
        except Exception as err:
            print(err)

if __name__ == "__main__":
    highscores.sort_highscores("abc.txt", 1, False)