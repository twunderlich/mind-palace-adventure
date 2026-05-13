class Dictionary:
    def __init__(self, data):
        self.dictionary = data

    def to_dictionary(self):
        return self.dictionary

    def create_word(
        self, word = None, type = None, phrase_with = None, synonyms = None):
        word = {
            "word": word,
            "type": type,
            "phrase_with": phrase_with or [],
            "synonyms": synonyms or []
        }
        return word
    
    def save_word(self, word_data):
        name = word_data['word']

        if name not in self.dictionary or self.dictionary[name]['type'] == 'placeholder':
            self.dictionary[name] = word_data

            if word_data['synonyms']:
                for synonym in word_data['synonyms']:
                    if synonym not in self.dictionary:
                        self.dictionary[synonym] = self.create_word(synonym, "placeholder")
                        self.dictionary[synonym]['synonyms'].append(name)
            return True
        return False