# Word Auto-Completion System

This project is implemented by Om Khokhar(s3886577) and Ashmit Sachan(s3879594). It focuses on creating a dictionary of English words to support word auto-completion functionality. Different data structures, including Python’s List, Dictionary, and Ternary Search Tree (TST), are used to implement the solution.

## Project Description

The project aims to provide understanding of:

- Real-world problem-solving using different data structures and algorithms.
- Performance evaluation and contrast of data structures and algorithms in different usage scenarios and input data.

The specific data structure focused here is the Ternary Search Tree (TST), which allows for memory-efficient storage of strings and fast operations such as spell checking and auto-completion.

## Tasks

The assignment is divided into different tasks:

### Task A: Implement the Nearest Neighbour Data Structures and their Operations

In this task, a dictionary of English words that allows auto-completion is implemented using three different data structures:

1. Python’s list (array)
2. Python’s dictionary (hash table)
3. Ternary search tree

Each implementation supports the following operations:

- Build a dictionary from a list of words and frequencies.
- Add (A) a word and its frequency to the dictionary.
- Search (S) for a word in a dictionary and return its frequency (return 0 if not found).
- Delete (D) a word from the dictionary.
- Auto-complete (AC) a given string and return a list of three most frequent words (if any) in the dictionary that have the string as a prefix.

## Usage

The operations take the following form:

- `S word` – Searches for a word in the dictionary and returns its frequency (returns 0 if not found).
- `A word frequency` – Adds a new word and its frequency to the dictionary. Returns True if succeeded and False if the word already exists in the dictionary.
- `D word` – Deletes a word from the dictionary. If the operation fails (word is not in the dictionary), it returns False.
- `AC partial word` – Returns a list of three words of highest frequencies in the dictionary that has the partial word as a prefix. These words should be listed in a decreasing order of frequencies. The returned list can contain between zero and three words.

## How to Run

The implementation can be tested using the provided command-line interface. 

To test the "hashtable" implementation with `test1.in` on Windows, use the following command:

```
python .\dictionary_test_script.py -v .\ hashtable .\sampleData.txt test1.in
```

To test the "hashtable" implementation with `test1.in` on Linux, use the following command:

```
python dictionary_test_script.py -v $PWD hashtable sampleData.txt test1.in
```

There are three implementations that you can test: `list`, `hashtable`, and `tst`.

There are also two datasets that can be used for testing:

1. `sampleDataToy.txt` -- The input file for it is `testToy.in`
2. `sampleData.txt` -- The input file for it is `test1.in`

The provided Python files handle the necessary input and output formats. Your task is to implement the missing methods in the provided classes.

## Contributors

- Om Khokhar (s3886577)
- Ashmit Sachan (s3879594)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
