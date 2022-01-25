import pickle
from collections import Counter

from constants import DICTIONARY_SIZE, GET_DIGIT_FREQUENCY_TOP_WORD_COUNT, PREDICT_WORD_COUNT


class WordleSolver:
    def __init__(self):
        with open("data/five_words_with_freq.pkl", "rb") as mypicklefile:
            self.word_list = pickle.load(mypicklefile)
            self.word_list = self.word_list[:DICTIONARY_SIZE]
        self.available_words_list = self.word_list
        self.calculate_digit_frequencies()
        self.update_most_probable_words_list()

    def initialize_digit_counters(self):
        self.first_digit_counter = Counter()
        self.second_digit_counter = Counter()
        self.third_digit_counter = Counter()
        self.fourth_digit_counter = Counter()
        self.fifth_digit_counter = Counter()

    def calculate_digit_frequencies(self):
        self.initialize_digit_counters()
        for word in self.available_words_list:
            self.first_digit_counter[word[0]] += 1
            self.second_digit_counter[word[1]] += 1
            self.third_digit_counter[word[2]] += 1
            self.fourth_digit_counter[word[3]] += 1
            self.fifth_digit_counter[word[4]] += 1

    def update_most_probable_words_list(self):
        self.words_value_dict = {}
        for word in self.available_words_list:
            word_prediction_value = (
                self.first_digit_counter[word[0]]
                + self.second_digit_counter[word[1]]
                + self.third_digit_counter[word[2]]
                + self.fourth_digit_counter[word[3]]
                + self.fifth_digit_counter[word[4]]
            )

            word_prediction_value = word_prediction_value * len(set(word)) / 5
            self.words_value_dict[word] = word_prediction_value
        self.words_value_dict = {k: v for k, v in sorted(self.words_value_dict.items(), key=lambda item: item[1], reverse=True)}

    def predict(self):
        print(f"You should predict one of the following:")
        top_words_used_frequency_dict = {}
        for top_word, value in list(self.words_value_dict.items())[:GET_DIGIT_FREQUENCY_TOP_WORD_COUNT]:
            top_words_used_frequency_dict[top_word] = self.word_list.index(top_word)

        top_words_used_frequency_dict = {k: v for k, v in sorted(top_words_used_frequency_dict.items(), key=lambda item: item[1])[:PREDICT_WORD_COUNT]}
        predicted_word_counter = 1
        for word, freq in top_words_used_frequency_dict.items():
            print(f"{predicted_word_counter}. {word}: {self.words_value_dict[word]} {freq}")
            predicted_word_counter += 1


    def prompt_for_prediction(self):
        predicted_word = input("Your prediction: ")
        predicted_result = input("Result: ")
        return predicted_word, predicted_result

    def update_calculations_with_last_prediction(self, predicted_word, predicted_result):
        if predicted_result == "+++++":
            print(f"Congratulations you found the word!")
            exit(0)
        for idx in range(5):
            if predicted_result[idx] == '+':
                self.update_word_list_correct_pred(idx, predicted_word[idx])
            elif predicted_result[idx] == '.':
                self.update_word_list_wrong_pred(predicted_word[idx])
            elif predicted_result[idx] == '-':
                self.update_word_list_wrong_place_pred(idx, predicted_word[idx])
        self.calculate_digit_frequencies()
        self.update_most_probable_words_list()

    def update_word_list_correct_pred(self, digit_idx, correct_char):
        next_list = []
        for word in self.available_words_list:
            if word[digit_idx] == correct_char:
                next_list.append(word)
        self.available_words_list = next_list

    def update_word_list_wrong_place_pred(self, digit_idx, pred_char):
        next_list = []
        for word in self.available_words_list:
            if word[digit_idx] != pred_char and pred_char in word:
                next_list.append(word)
        self.available_words_list = next_list

    def update_word_list_wrong_pred(self, pred_char):
        next_list = []
        for word in self.available_words_list:
            if pred_char not in word:
                next_list.append(word)
        self.available_words_list = next_list

    def start(self):
        while True:
            self.predict()
            predicted_word, predicted_result = self.prompt_for_prediction()
            self.update_calculations_with_last_prediction(predicted_word, predicted_result)


ws = WordleSolver()
ws.start()





