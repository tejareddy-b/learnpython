def break_words(stuff):
	words = stuff.split(' ')
	return words
def sort_words(words):
	sorted(words)
def print_first_words(words):
	word = words.pop(0)
	print word
def print_last_word(words):
	word = words.pop(-1)
	print word
def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words
def print_first_and_last(words):
	words = break_words(sentence)
	print print_first_word(words)
	print print_last_word(words)
