from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def __init__(self):
        self.list = list()

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
        if word not in [y[0] for y in self.list]:
            return 0
        else:
            ind = [x[0] for x in self.list].index(word)
            return self.list[ind][1]

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
            add a word and its frequency to the dictionary
            @param word_frequency: (word, frequency) to be added
            :return: True whether succeeded, False when word is already in the dictionary
            """
        a = word_frequency.word
        b = word_frequency.frequency
        word_frequency = (a, b)

        if len(self.list) == 0:
            self.list.append(word_frequency)
            return True
        else:
            for x in range(len(self.list)):
                if word_frequency[0] == self.list[x][0]:
                    return False
                else:
                    self.list.append(word_frequency)
                    return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        if word not in [y[0] for y in self.list]:
            return False
        else:
            ind = [y[0] for y in self.list].index(word)
            self.list.pop(ind)
            return True

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        new_dict = []
        final_list = []
        for x in range(len(self.list)):
            if prefix_word == self.list[x][0][0:len(prefix_word)]:
                new_dict.append(self.list[x])
                new_dict.sort(key=lambda y: y[1], reverse=True)
        new_dict = new_dict[:3]

        for x in new_dict:
            a = x[0]
            b = x[1]
            word_frequency = WordFrequency(a, b)
            final_list.append(word_frequency)
        return final_list
