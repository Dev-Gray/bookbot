import sys
from stats import count_characters, count_words, sort_characters

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	book_text = get_book_text(book_path)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")

	num_words = count_words(book_text)
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	print("--------- Character Count -------")
	char_counts = count_characters(book_text)
	sorted_char_list = sort_characters(char_counts)

	for item in sorted_char_list:
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

if __name__ == "__main__":
	main()

