from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def __init__(self):
        self.root = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        def get_frequency(node, string):
            if node is None or len(string) == 0:
                return 0

            head = string[0]
            tail = string[1:]
            if head < node.letter:
                return get_frequency(node.left, string)
            elif head > node.letter:
                return get_frequency(node.right, string)
            else:
                if len(tail) == 0 and node.end_word:
                    return node.frequency
                else:
                    return get_frequency(node.middle, tail)

        return get_frequency(self.root, word)

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        return_bool = [False]

        def insert_letter(node, string, frequency):
            if len(string) == 0:
                return node

            head = string[0]
            tail = string[1:]
            if node is None:
                node = Node(letter=head)

            if head < node.letter:
                node.left = insert_letter(node.left, string, frequency)
            elif head > node.letter:
                node.right = insert_letter(node.right, string, frequency)
            else:
                if len(tail) == 0:
                    return_bool[0] = False if node.end_word else True
                    node.frequency = frequency
                    node.end_word = True
                else:
                    node.middle = insert_letter(node.middle, tail, frequency)

            return node

        self.root = insert_letter(self.root, word_frequency.word.lower(), word_frequency.frequency)
        return return_bool[0]

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        def delete_search(node, string):
            if node is None:
                return False

            head = string[0]
            tail = string[1:]
            if head < node.letter:
                return delete_search(node.left, string)
            elif head > node.letter:
                return delete_search(node.right, string)
            else:
                if len(tail) == 0:
                    if node.end_word:
                        node.frequency = None
                        node.end_word = False
                        return True
                    else:
                        return False
                else:
                    return delete_search(node.middle, tail)

        if self.root is None or len(word) == 0:
            return False
        else:
            return delete_search(self.root, word)

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        def get_suffix(node, string, suffix_list) -> [WordFrequency]:
            if len(string) == 0 or node is None:
                return suffix_list

            if node.end_word:
                suffix_list.append(WordFrequency(string + node.letter, node.frequency))
            if node.middle is not None:
                get_suffix(node.middle, string + node.letter, suffix_list)
            if node.left is not None:
                get_suffix(node.left, string, suffix_list)
            if node.right is not None:
                get_suffix(node.right, string, suffix_list)

            return suffix_list

        def find_node(node, string) -> Node:
            if len(string) == 0 or node is None:
                return node

            head = string[0]
            tail = string[1:]
            if head < node.letter:
                return find_node(node.left, string)
            elif head > node.letter:
                return find_node(node.right, string)
            else:
                # if len(head) == 0:
                #     return node
                # else:
                #     return find_node(node.middle, tail)
                return find_node(node.middle, tail)

        all_suffix = []
        if self.search(word) != 0:
            all_suffix.append(WordFrequency(word, self.search(word)))

        all_suffix = get_suffix(find_node(self.root, word), word, all_suffix)
        all_suffix = sorted(all_suffix, key=lambda node: node.frequency, reverse=True)

        return all_suffix[:3]
