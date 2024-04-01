# Project Title: Inverted Indexer

This project is an implementation of an Inverted Indexer using Python and the Natural Language Toolkit (NLTK).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Alternatively

You may open a codespace using the provided prebuild to run the program without downloading all of the resources.

### Prerequisites

You will need to have Python installed on your machine. Additionally, you will need to install [NLTK](https://www.nltk.org/install.html#installing-nltk) and download the 'words', 'stop-words' corpuses from NLTK, along with the 'punkt' tokenizer. You can do this using the following commands:

```python
import nltk
nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
```

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/wyliew19/InvertedIndexer.CIS439.git
```

Navigate to the project directory:

```sh
cd InvertedIndexer.CIS439
```

Run the main script:

```sh
python main.py
```

## Project Structure

The project has the following structure:

- [`main.py`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/main.py): The main script that runs the Inverted Indexer.
- [`utils/`](https://github.com/wyliew19/InvertedIndexer.CIS439/tree/main/utils): This directory contains utility scripts used by the main script.
  - [`chunk.py`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/utils/chunk.py): Contains the `ChunkManager` class for managing chunks of articles.
  - [`merger.py`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/utils/merger.py): Contains the `Merger` class for merging dictionaries from chunks.
  - [`article.py`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/utils/article.py): Contains the `Article` class for holding article contents and `Dictionary` class to manage those tokens
  - [`processor.py`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/utils/processor.py): Contains the `Processor` class that wraps all functions related to the processing of data in each article
- [`resources/`](https://github.com/wyliew19/InvertedIndexer.CIS439/tree/main/resources): This directory contains the text files to be indexed.
- [`.devcontainer/`](https://github.com/wyliew19/InvertedIndexer.CIS439/tree/main/.devcontainer): Contains the [`devcontainer.json`](https://github.com/wyliew19/InvertedIndexer.CIS439/blob/main/.devcontainer/devcontainer.json) file for setting up a development container.

## Author

- Will Wylie

## Acknowledgments

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
