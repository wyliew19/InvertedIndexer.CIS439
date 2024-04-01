from .article import Article
from .globals import WRITE_DIR, RESOURCE_DIR
import time

class ChunkManager:
    """Class to manage chunks of articles."""

    def __init__(self, chunk_id: int):
        self.id = chunk_id
        self.articles = []
        self.dictionary = {}
        self._load() # load articles from chunk file
        self._make_dict() # create a dictionary for the chunk
        self._write_dict() # write temporary dictionary to a file

    def _load(self) -> None:
        """Load articles from a chunk file."""
        print(f'\nLoading chunk {self.id}...')
        start = time.time()
        with open(RESOURCE_DIR / f'wiki2022_small{self.id:02}.txt', 'r') as file:
            for line in file:
                self.articles.append(Article(line))
        end = time.time()
        print(f'Loaded {len(self.articles)} articles from chunk {self.id}.')
        print(f'Execution time: {end - start:.2f} seconds.')

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

    def _write_dict(self) -> None:
        if not (WRITE_DIR).exists():
            WRITE_DIR.mkdir()
        if not (WRITE_DIR / 'dicts').exists():
            (WRITE_DIR / 'dicts').mkdir()
        """Write the chunk's dictionary to a file."""
        with open(WRITE_DIR / 'dicts' / f'dict{self.id:02}.txt', 'w') as file:
            for word in self.dictionary:
                file.write(f'{word}\n')
        
    def write_index(self, global_dict: dict) -> None:
        """Write the chunk's inverted index to a file."""
        if not (WRITE_DIR / 'indexes').exists():
            (WRITE_DIR / 'indexes').mkdir()
        print(f'\nWriting index for chunk {self.id}...')
        with open(WRITE_DIR / 'indexes' / f'index{self.id:02}.txt', 'w') as file:
            for word in self.dictionary:
                file.write(f'{global_dict[word]} {word} {self.dictionary[word]} ')
                for article in self.articles:
                    if word in article.get_dict():
                        file.write(f'({article.id}, {article.get_dict()[word]}) ')
                file.write('\n')
        print(f'Index for chunk {self.id} written.')
        