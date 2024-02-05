import requests

def synonym_words(word, num_results):
    """Returns top results for synonym words."""
    url = f"https://api.datamuse.com/words?ml={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [(result["word"], result["score"]) for result in response]
    return results

def rhyme_words(word, num_results):
    """Returns top resutls for word rhymes."""
    url = f"https://api.datamuse.com/words?rel_rhy={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [(result["word"], result["score"]) for result in response]
    return results

def antonym_words(word, num_results):
    """Returns a list of antonyms."""
    url = f"https://api.datamuse.com/words?rel_ant={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [result["word"] for result in response]
    return results
    