"""
OOP Assignment
CSIS 250
2018 - 10 - 30
Author: Robert Schult
"""

class Poem:
    _number_of_poems = 0

    def __init__(self, author = "", title = ""):
        self.author = author
        self.title = title
        self.text = [""]
        self.isHaiku = False
        Poem._number_of_poems += 1

    def __str__(self):
        fullText = self.title + " - a " + ("haiku" if self.getIsHaiku() else "poem") + " by " + self.author + "\n"
        for line in self.text:
            fullText += line + "\n"
        return fullText

    def setText(self, text = [""]):
        self.text = text

    def setIsHaiku(self, isHaiku):
        self.isHaiku = isHaiku

    def printText(self):
        fullText = ""
        for line in self.text:
            fullText += line + "\n"
        print(fullText)

    def getIsHaiku(self):
        return self.isHaiku

    def getNumberOfPoems():
        return Poem._number_of_poems


if __name__ == '__main__':
    poem1 = Poem("Margret Atwood", "You Fit Into Me")
    poem1.setText(["you fit into me", "like a hook into an eye", "", "a fish hook", "an open eye"])
    print(poem1)

    poem2 = Poem("Edna St. Vincent Millay", "First Fig")
    poem2.setText(["My candle burns at both ends;", "It will not last the night;",
                  "But ah my foes, and oh, my friends-", "It gives a lovely light!"])
    print(poem2)

    poem3 = Poem("Matsuo Bashō", "Old pond")
    poem3.setIsHaiku(True)
    poem3.setText([ "ふるいけや", # Old pond
                    "かわずとびこむ", # Frog jumps in
                    "みずのおと"]) # Water's sound
    print(poem3)

    print("The number of poems is - " + str(Poem.getNumberOfPoems()))
