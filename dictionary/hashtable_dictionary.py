from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import operator


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def __init__(self):
        self.dictionary = dict()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for x in words_frequencies:
            self.add_word_frequency(x)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        if word not in list(self.dictionary.keys()):
            return 0
        else:
            return self.dictionary[word]

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        if word_frequency.word in list(self.dictionary.keys()):
            return False
        else:
            self.dictionary[word_frequency.word] = word_frequency.frequency
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        if word not in list(self.dictionary.keys()):
            return False
        else:
            del self.dictionary[word]
            return True

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        new_dict = {}
        final_list = []

        for i in self.dictionary.keys():
            if word == i[0:len(word)]:
                new_dict[i] = self.dictionary[i]
        sorted_dictionary = dict(sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)[:3])

        for i in sorted_dictionary.keys():
            j = sorted_dictionary[i]
            word_frequency = WordFrequency(i, j)
            final_list.append(word_frequency)

        return final_list
