import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

class Processor:
    """Processes content from a Wikipedia article."""
    URL = r'https://en.wikipedia.org/wiki\?curid=\d+'

    def _regex(content: str) -> tuple[str, int]:
        # Remove markdown
        content = re.sub(r'!.*\|', '', content)
        content = re.sub(r'#.*;', '', content)
        # Extract article id from content
        article_id = re.findall(Processor.URL, content)
        article_id = int(re.findall(r'\d+', article_id[0])[0])
        # Remove url
        content = re.sub(Processor.URL, '', content)
        return content, article_id
    
    def _tokenize(content: str) -> list:
        return word_tokenize(content)
    
    def _stem(tokens: list) -> list:
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]
    
    def process(content: str) -> tuple[list, int]:
        content, id = Processor._regex(content)
        tokens = Processor._tokenize(content)
        return Processor._stem(tokens), id

