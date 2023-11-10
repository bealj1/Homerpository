import string
import phantom_tollbooth

def get_most_common_words(text):
    # Defines a list of stop words

    stop_words = set([
        'the', 'a', 'an', 'and', 'but', 'or', 'of', 'on', 'over', 'above','under', 'below', 'between', 'among', 'through', 'into', 'to', 'in', 'out',
        'for', 'with', 'by', 'at', 'since', 'ago', 'throughout', 'from', 'up', 'down','around', 'after', 'before', 'while', 'during', 
        'though', 'although', 'if', 'unless', 'until', 'because', 'since', 'so', 'such', 'as', 'until', 'when', 'where', 'how', 'who', 'whom',
        'which', 'what', 'whose', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their'
    ])
    #Tokenizes the text into words
    translator = str.maketrans('','', string.punctuation) 
    words = text.lower().translate(translator).split()
   
    words= [word for word in words if word.isalpha() and word not in stop_words]#removes stop words

# Counts how many times a word is said 
    word_freq = {} 
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    most_common_word = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:50]
    return most_common_words





def main():
    #Gets text from The Phantom Tollbooth
    book = phantom_tollbooth.get_text()
    most_common_words = get_most_common_words(book)
    print("Fifty Most Common Words (excluding articles, prepositions, conjunctions, and pronouns):")
    for word, count in most_common_words:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
