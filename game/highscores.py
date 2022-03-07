class highscores:
    """Keep highscores in a seperate .txt file."""

    def short_scores(self, player, score, counter) -> None:
        with open("game/highscores_short.txt", "a") as f:
            f.write(f"{player}: {score} ---- Draws: {counter}\n")
        self.sort_highscores("game/highscores_short.txt", 1, True)
        self.shorten_list("game/highscores_short.txt")

    def long_scores(self, player, score, counter) -> None:
        with open("game/highscores_long.txt", "a") as f:
            f.write(f"{player}: {score} ---- Draws: {counter}\n")
        self.sort_highscores("game/highscores_long.txt", -1, False)
        self.shorten_list("game/highscores_long.txt")

    def sort_highscores(self, high, t, b):
        with open(high, "r") as f:
            scores = f.readlines()
            scores = sorted(scores, key=lambda i: int(i.split(" ")[t]), reverse=b)
        with open(high, "w") as w:
            w.writelines(scores)

    def shorten_list(self, high):
        with open(high, "r") as f:
            scores = f.readlines()
            should_del = len(scores) > 20
        if should_del:
            with open(high, "w") as w:
                w.writelines(scores[0:20])