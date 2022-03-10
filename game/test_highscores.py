import unittest
import highscores


class Test_highscores(unittest.TestCase):
    def test_init(self):
        res = highscores.highscores()
        exp = highscores.highscores
        self.assertIsInstance(res, exp)

    def test_player_in_file_long(self):
        hs_cls = highscores.highscores()
        hs_cls.long_scores("Jeff", "52", "122")
        with open("highscores_long.txt", "r") as txt_file:
            scores = txt_file.readlines()
        my_player = False
        for i in scores:
            if ("Jeff", "52", "122" in i):
                my_player = True
                break
        self.assertTrue(my_player)

    def test_player_in_file_short(self):
        hs_cls = highscores.highscores()
        hs_cls.short_scores("Jeff", "52", "122")
        with open("highscores_short.txt", "r") as txt_file:
            scores = txt_file.readlines()
        my_player = False
        for i in scores:
            if ("Jeff", "52", "122" in i):
                my_player = True
                break
        self.assertTrue(my_player)

    def test_shorten_list(self):
        hs_cls = highscores.highscores()
        hs_cls.shorten_list("highscores_long.txt")
        with open("highscores_long.txt", "r") as long_file:
            long_scores = long_file.readlines()
        self.assertLessEqual(len(long_scores), 20)

        hs_cls.shorten_list("highscores_short.txt")
        with open("highscores_short.txt", "r") as short_file:
            short_scores = short_file.readlines()
        self.assertLessEqual(len(short_scores), 20)

    def test_sorts_short_game(self):
        """Checking that the higher score is placed before the lower score
        and sorted by the score and not the counter."""

        high_score = 0
        low_score = 0

        """Clear the file first"""
        with open("highscores_short.txt", "r+") as file_to_clear:
            file_to_clear.truncate(0)

        """Insert new records to file"""
        hs_cls = highscores.highscores()
        hs_cls.short_scores("Jeff", "45", "25")
        hs_cls.short_scores("Ish", "0", "26")

        with open("highscores_short.txt", "r") as txt_file:
            scores = txt_file.readlines()
        for i in scores:
            if 45 == int(i.split(" ")[1]):
                high_score = scores.index(i)
            elif 0 == int(i.split(" ")[1]):
                low_score = scores.index(i)
        self.assertLess(high_score, low_score)

    def test_sorts_long_game(self):
        """Checks that the file is sorted by the counter and not the score."""

        high_score = 0
        low_score = 0

        """Clear the file first"""
        with open("highscores_long.txt", "r+") as file_to_clear:
            file_to_clear.truncate(0)

        """Insert new records to file"""
        hs_cls = highscores.highscores()
        hs_cls.long_scores("Jeff", "0", "11")
        hs_cls.long_scores("Ish", "1", "200")

        """Get the index of each record so see that the index of the high score
        is lower than the index of the low score"""
        with open("highscores_long.txt", "r") as txt_file:
            scores = txt_file.readlines()
        for i in scores:
            if 11 == int(i.split(" ")[-1]):
                high_score = scores.index(i)
            elif 200 == int(i.split(" ")[-1]):
                low_score = scores.index(i)
        self.assertLess(high_score, low_score)


if __name__ == "__main__":
    unittest.main()
