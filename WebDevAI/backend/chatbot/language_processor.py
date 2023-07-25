```python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class LanguageProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def process(self, text):
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        # Remove stop words
        tokens = [token for token in tokens if token not in self.stop_words]
        # Lemmatize the tokens
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return tokens

# Create an instance of the language processor
language_processor_instance = LanguageProcessor()
```