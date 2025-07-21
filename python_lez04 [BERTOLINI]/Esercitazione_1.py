class Book():

    def read(self, pages):
        if ((self.pages_read + pages) > self.pages):
            print("You can not read that many pages!")
            print(f"\tPages available to read: {self.pages - self.pages_read}")
            return

        self.pages_read += pages
        print(f"You have read {self.pages_read} pages.")

        if self.pages_read == self.pages:
            print("You have read the entire book!")

    def __init__(self, pages, title, author, price):
        self.pages      = pages
        self.title      = title
        self.author     = author
        self.pages_read = 0
        self.price      = price



on_sale_new_books = [ ]

book = Book(100, "Harry Potter", "J.K. Rowling", 20)
on_sale_new_books.append(book)

book = Book(100,'La storia infinita', "", 20)
on_sale_new_books.append(book)

book = Book(100, 'Game of Thrones', "George R.R. Martin", 20)
on_sale_new_books.append(book)

for idx in range(3):
    on_sale_new_books.append(Book(100, f"Title-{idx}", f"Author-{idx}", 20))


prezzo_singolo_libro        = 10

# Dobbiamo inserire 2 copie di un numero determinato di libri.
numero_determinato_di_libri = 1000
copies_number               = 2

soldi_richiesti             = prezzo_singolo_libro * numero_determinato_di_libri * copies_number
current_account             = 50_000

if soldi_richiesti <= current_account:                  # ho abbastanza soldi!?

    for idx in range(numero_determinato_di_libri):
        book = Book(100, f"Title-{idx}", f"Author-{idx}", 20,)
        for i in range(copies_number):
            on_sale_new_books.append(book)
    
    current_account         = current_account - soldi_richiesti
    # current_account        -= soldi_richiesti   ## è uguale

else:
    print("Ciccio non hai abbastanza soldi!!")

# # Dobbiamo inserire 2 copie di un numero determinato di libri.        ## 2° modo valido
# numero_determinato_di_libri = 1000
# copies_number               = 2
# for idx in range(numero_determinato_di_libri):
#     book = Book(100, f"Title-{idx}", f"Author-{idx}", 20,)
#     on_sale_new_books.append(book)

# second_list = on_sale_new_books.copy()
# on_sale_new_books = on_sale_new_books + second_list

print(on_sale_new_books)


l = [ ]
l.append(2)
print(l)