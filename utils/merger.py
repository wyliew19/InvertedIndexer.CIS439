from .globals import WRITE_DIR
import heapq

class Merger:
    """Class to merge dictionaries from chunks.
    Create a global dictionary from the dictionaries of the chunks.
    Write the global dictionary to a file."""

    def __init__(self, dict_name: str):
        self.dict_name = dict_name
        self.global_dict = {}
        self._merge_dicts()

    def _merge_dicts(self) -> None:
        """Merge the dictionaries from the chunks."""
        print('\nMerging dictionaries...')
        # Open all the dictionary files
        files = [open(WRITE_DIR / 'dicts' / f'dict{i:02}.txt', 'r') for i in range(32)]
        # Create a heap to merge the dictionaries
        # The heap will contain a tuple with the word and chunk id
        heap = [(next(f).strip(), i) for i, f in enumerate(files) if f is not None]
        heapq.heapify(heap)
        # Merge the dictionaries
        word_code = 0
        while heap:
            # Get the word and the chunk id
            word, i = heapq.heappop(heap)
            # Ignore duplicates
            if word not in self.global_dict:
                self.global_dict[word] = word_code
                word_code += 1

            next_word = next(files[i], None) # Get the next word from the chunk
            if next_word is not None:
                heapq.heappush(heap, (next_word.strip(), i)) # Push the next word to the heap

        for f in files:
            f.close()
        
        # Delete the temporary dictionary folder and files
        for i in range(32):
            (WRITE_DIR / 'dicts' / f'dict{i:02}.txt').unlink()
        (WRITE_DIR / 'dicts').rmdir()
        
        print('Dictionaries merged.')

        # Write the global dictionary to a file
        with open(WRITE_DIR / f'{self.dict_name}.txt', 'w') as file:
            for word, code in self.global_dict.items():
                file.write(f'{code} {word}\n')
    
    def get_dict(self) -> dict:
        """Return the global dictionary."""
        return self.global_dict