import requests

def synonym_words(word, num_results):
    url = f"https://api.datamuse.com/words?ml={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [(result["word"], result["score"]) for result in response]
    return results

def rhyme_words(word, num_results):
    url = f"https://api.datamuse.com/words?rel_rhy={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [(result["word"], result["score"]) for result in response]
    return results

def antonym_words(word, num_results):
    url = f"https://api.datamuse.com/words?rel_ant={word}&max={str(num_results)}"
    response = requests.get(url).json()
    results = [result["word"] for result in response]
    return results
    
if __name__ == "__main__":
    print(synonym_words("on+top+of", 5))
    print(rhyme_words("grape", 5))
    print(antonym_words("bright", 5))
