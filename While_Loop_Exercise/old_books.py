# Library search system (Linear Search Algorithm)
target_book = input()

books_checked_counter = 0

while True:
    current_book_input = input()

    # Case 1: The library collection is exhausted
    if current_book_input == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked_counter} books.")
        break

    # Case 2: The target book is found
    if current_book_input == target_book:
        print(f"You checked {books_checked_counter} books and found it.")
        break

    # Increment counter only if the book was not the target
    books_checked_counter += 1
