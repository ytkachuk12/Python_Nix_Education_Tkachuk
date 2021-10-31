"""create iterator and container_iterator"""
import re


class MultipleSentencesError(Exception):
    """Exception for case multi sentence in the line"""

    def __str__(self):
        return "MultipleSentencesError\n More than one sentence in the line"


class Sentence:
    """Class container"""
    def __init__(self, text: str):
        if self.line_checker(text) and self.sentence_checker(text):
            self.text = text
        self._text = ""
        self.list_other_chars = []
        self.count_other_chars = 0
        self.count_words = 0

    @staticmethod
    def line_checker(text):
        """Check text. Text must be str, else raise TypeError"""
        if isinstance(text, str):
            return True
        raise TypeError

    @staticmethod
    def sentence_checker(text):
        """Check line. Line must have complete sentence and one sentence only. """
        checking = text[-1]
        # check last sentence symbol. it must be one of '!', '.', '?'
        if checking not in ("!", ".", "?"):
            raise ValueError
        # check that before space symbol we have no any symbol from '!', '.', '?'
        if re.search(r"([!?.]\s)", text):
            raise MultipleSentencesError
        return True

    def takeout_symbols(self):
        self._text = self.text
        for symbol in self.text:
            if symbol == " ":
                self.other_chars.append(symbol)
                self.count_other_chars += 1
            elif symbol in (",", ":", ";", ".", "!", "?"):
                self.other_chars.append(symbol)
                self._text = self._text.replace(symbol, "")
                self.count_other_chars += 1
        return self._text

    def _words(self):
        """display one word"""
        return SentenceIterator(self.takeout_symbols())

    @property
    def words(self):
        """display all words from the text"""
        all_words = list(iter(SentenceIterator(self._text)))
        self.count_words = len(all_words)
        return all_words

    @property
    def other_chars(self):
        """display all other chars from text"""
        return self.list_other_chars

    def __repr__(self):
        """display quantity of words and other chars"""
        return f"<Sentence(words={self.count_words}, other_chars={self.count_other_chars})>"

    def __iter__(self):
        return SentenceIterator(self.text)


class SentenceIterator:
    """class iterator"""
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.stop = len(self.text)
        self.word_stop = 0
        self.flag_stop_iteration = False

    def gen_word(self):
        if not self.flag_stop_iteration:
            self.word_stop = self.text.find(" ", self.start, self.stop)
            if self.word_stop == -1:
                self.flag_stop_iteration = True
                return self.text[self.start:self.stop]
            word = self.text[self.start:self.word_stop]
            self.start = self.word_stop + 1
            return word
        raise StopIteration

    def __next__(self):
        return self.gen_word()

    def __iter__(self):
        return self


text1 = "Hello, world!!!"
text2 = "How is it going., looks good!!!"
text3 = "Hello, brave new world!!!"
text4 = "Hello.. world!!!"
sentence = Sentence(text4)
print(next(sentence._words()))
print(sentence.words)
print(sentence.other_chars)
print(sentence)
