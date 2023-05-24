import requests
base_url = "https://api.datamuse.com"

def synonym_words(word, num_results):
    """Returns top results for synonym words."""
    # define URL
    word_param = word.replace(" ", "+")
    url = base_url + "/words" + "?ml=" + word_param + "&max=" + str(num_results)
    # get response + convert to Python object with json()
    response = requests.get(url).json()
    # filter for information in dictionary
    top_results = [(res["word"], res["score"]) for res in response]
    return top_results


def rhyme_words(word, num_results):
    """Returns top resutls for word rhymes."""
    url = base_url + "/words" + "?rel_rhy=" + word + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_results = [(res["word"], res["score"]) for res in response]
    return top_results

def antonym_words(word, num_results):
    """Returns a list of antonyms."""
    url = base_url + "/words" + "?rel_ant=" + word + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_results = [res["word"] for res in response]
    return top_results
    
if __name__ == "__main__":
    print(synonym_words("clever", 5))
    print(rhyme_words("clever", 5))
    print(antonym_words("bright", 5))