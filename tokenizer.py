import json
from statement import Statement_Tokenizer
from data import Dict_Data


class QTokenizer(Statement_Tokenizer):
    """Tokenizes all english words that start with Q"""
    
    def __init__(self, text:str) -> None:
        super().__init__(text)
        ref = Dict_Data("Q")
        self.__ref = ref.data
        self.__tokens = {
            "noun":[], 
            "pronoun":[], 
            "verb":[],
            "article":[],
            "adjective":[],
            "adverb":[],
            "preposition":[],
            "conjunction":[],
            "interjection":[],
            "no_match":[]
        }
        self.__parse_words()

    
    def __parse_words(self):
        """Will be called at the appropria moment at run time"""
        words = list(filter(lambda w: w.startswith("Q"), self.words))
        for word in words:
            for key, value in self.__ref.items():
                if word in value:
                    self.__tokens[key].append(word)
                    break
            else:
                self.__tokens["no_match"].append(word)

    

    def get_listed_tokens(self) ->  dict:
        """Returns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a list of such words found in 
        the _tokens property"""

        return  self.__tokens

    def get_tokens_with_number(self)->dict:
        """Returns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a total number of such words found in the 
        _tokens property"""

        return {key : len(value)  for key, value in self.__tokens.items()
        }

    def get_total_word(self) -> int:
        return sum(self.get_tokens_with_number().values())

    def __str__(self) -> str:
        return super().__str__()

if __name__ == "__main__":
    q_t = QTokenizer("Qatar 2022. I went, to be : qualified. Question? not Question")
    print(q_t)
    print(q_t.get_listed_tokens())
    print(q_t.get_tokens_with_number())
    print("Total words: ", q_t.get_total_word())