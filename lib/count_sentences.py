#!/usr/bin/env python3

class MyString:
    
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string.")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        
        sentences = [sentence for sentence in re.split(r'[.!?]', self._value) if sentence]
        return len(sentences)


if __name__ == "__main__":
    
    my_string_instance = MyString(value="This is a string! It has three sentences. Right?")

    
    print(f"Value: {my_string_instance.value}")

    
    print(f"Is Sentence? {my_string_instance.is_sentence()}")
    print(f"Is Question? {my_string_instance.is_question()}")
    print(f"Is Exclamation? {my_string_instance.is_exclamation()}")

    
    sentence_count = my_string_instance.count_sentences()
    print(f"Number of Sentences: {sentence_count}")

  
    