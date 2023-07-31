class Diary:
    def __init__(self, title):
        self.title = title
        self._entries = []

    def addrntry(self, entry):
        self._entries.append(entry)

    def _lastentry(self):
        return self._entries[-1]

mydiary = Diary("This is title.")
mydiary.addrntry("It was a good day!")
print(mydiary.title)