import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords, words

class Processor:
    """Processes content from a Wikipedia article."""
    
    URL = r'https://en.wikipedia.org/wiki\?curid=\d+'
    STOP_WORDS = set(stopwords.words('english'))
    WORDS_SET = set(words.words())

    def _regex(content: str) -> tuple[str, int]:
        """Extract the article id and remove the URL/markdown from the content."""
        # Remove markdown
        content = re.sub(r'!.*\|', '', content)
        content = re.sub(r'#.*;', '', content)

        # Extract article id from content
        article_id = re.findall(Processor.URL, content)
        article_id = int(re.findall(r'\d+', article_id[0])[0])

        # Remove url
        content = re.sub(Processor.URL, '', content)
        return content, article_id
    
    def _tokenize(content: str) -> list[str]:
        """Tokenize the content removing stop words and invalid tokens."""
        tokens = word_tokenize(content)
        # Remove stopwords and non-words
        return [ 
            word for word in tokens 
                if word.lower() not in Processor.STOP_WORDS 
                    and word.lower() in Processor.WORDS_SET 
                        ] 
    
    def _stem(tokens: list) -> list[str]:
        """Stem the tokens."""
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]
    
    def process(content: str) -> tuple[list[str], int]:
        """Process the content of an article. Return the filtered/stemmed tokens and the article id."""
        content, id = Processor._regex(content)
        tokens = Processor._tokenize(content)
        return Processor._stem(tokens), id

