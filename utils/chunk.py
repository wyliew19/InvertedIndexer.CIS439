from .article import Article
from pathlib import Path

class ChunkManager:
    """Class to manage chunks of articles."""

    # Path to the resources and write directory
    RESOURCE_DIR = Path('resources').resolve()
    WRITE_DIR = Path('output').resolve()


    def __init__(self, chunk_id: int):
        self.id = chunk_id
        self.articles = []
        self.dictionary = {}
        self._load()
        self._make_dict()

    def _load(self) -> None:
        """Load articles from a chunk file."""
        print(f'\nLoading chunk {self.id}...')
        with open(ChunkManager.RESOURCE_DIR / f'wiki2022_small{self.chunk_id:02}.txt', 'r') as file:
            for line in file:
                self.articles.append(Article(line))
        print(f'Loaded {len(self.articles)} articles from chunk {self.id}.')

    def _make_dict(self) -> None:
            """Create a chunk-wide dictionary."""
            for article in self.articles:
                for word in article.get_dict():
                    if word in self.dictionary:
                        self.dictionary[word] += 1
                    else:
                        self.dictionary[word] = 1
            # Sort the dictionary in alphabetical order
            self.dictionary = dict(sorted(self.dictionary.items()))

    def write_dict(self) -> None:
        """Write the chunk's dictionary to a file."""
        with open(ChunkManager.WRITE_DIR / 'dicts' / f'dict{self.chunk_id:02}.txt', 'w') as file:
            for word in self.dictionary:
                file.write(f'{word}\n')
        
    def write_index(self, global_dict: dict) -> None:
        """Write the chunk's inverted index to a file."""
        with open(ChunkManager.WRITE_DIR / f'index{self.chunk_id:02}.txt', 'w') as file:
            for word in self.dictionary:
                file.write(f'{global_dict[word]} {word}')
        