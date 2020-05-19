from utils import database

# def prompt_add_book(x) meminta nama buku dan penulis
# def list_books(x) menampilkan semua daftar buku
# def prompt_read_book(x) menandai buku yang telah selsai dibaca
# def prompt_delete_book(x) menghapus buku dari judul buku

USER_CHOICE = """
Enter:
- 'a' to menambah buku baru
- 'l' to daftar semua buku
- 'r' to buku yang telah selasi dibaca
- 'd' to menghapus buku
- 'q' to keluar

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
        
def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)

menu()
