# CIS439 - Checkpoint 2
# Author: Will Wylie
# Using NLTK || Citation:
# Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
# Installation: https://www.nltk.org/install.html#installing-nltk

# You will also need to download the 'words' and 'stop-words' corpuses from nltk, along with the 'punkt' tokenizer:
# >>> import nltk
# >>> nltk.download('words')
# >>> nltk.download('stopwords')
# >>> nltk.download('punkt')

# It is recommended to visit the GitHub for this project here: https://github.com/wyliew19/InvertedIndexer.CIS439
# The README file will provide more information on how to run the project.
# Additonally, there is a prebuild provided to run this in a codespace for easier testing.


from utils.chunk import ChunkManager
from utils.merger import Merger

def load_chunks() -> list[ChunkManager]:
    """Load the chunks of articles."""
    chunks = [ChunkManager(i) for i in range(32)]
    return chunks

def merge_dicts() -> dict:
    """Merge the dictionaries from the chunks."""
    merger = Merger('dictionary')
    return merger.get_dict()

def main():
    chunks = load_chunks()
    global_dict = merge_dicts()
    for chunk in chunks:
        chunk.write_index(global_dict)

if __name__ == '__main__':
    main()