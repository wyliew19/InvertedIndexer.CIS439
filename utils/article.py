from .processor import Processor

class Dictionary:
    def __init__(self, doc_id: int, content: list) -> None:
        self.dictionary = {}
        self.id = doc_id
        for word in content:
            self.__add(word)

    def __add(self, key: str) -> None:
        """Add a key to the dictionary. If the key already exists, increment the count."""
        if key in self.dictionary:
            self.dictionary[key] += 1
        else:
            self.dictionary[key] = 1

    def get_dict(self) -> dict:
        """Return the dictionary."""
        return self.dictionary
    

class Article:
    """Class to represent a Wikipedia article."""
    def __init__(self, content: str):
        self.content = content
        tokens, self.id = Processor.process(content)
        self.dictionary = Dictionary(self.id, tokens)

    def get_dict(self) -> dict:
        """Return the dictionary for this article."""
        return self.dictionary.get_dict()
    