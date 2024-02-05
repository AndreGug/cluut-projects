# Datamuse

This project consists of two Python scripts that utilize the Datamuse API to retrieve information about words. The first script provides functions for finding synonym words, words that rhyme, and antonyms based on a given word. The second script imports these functions from the `word_module` module and tests them with sample inputs.

## Project Structure

`word_module.py`:

1. **synonym_words(word, num_results):**
 
   - Returns top results for synonym words.
   
2. **rhyme_words(word, num_results):**
   
   - Returns top results for word rhymes.
   
3. **antonym_words(word, num_results):**
 
   - Returns a list of antonyms.

`test_module.py`:

- Imports functions from `word_module` to test and demonstrate their usage.

### How to run

- Execute `word_module.py` to define the word analysis functions.
- Run `test_module.py` to test the functions and see sample outputs.
