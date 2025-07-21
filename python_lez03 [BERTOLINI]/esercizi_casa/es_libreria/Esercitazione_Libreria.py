import random
######################################################################################
# ESERCITAZIONE 21/05/2024
# @author: Andrea Bertolini
######################################################################################

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

class BookShop():

    BOOK_PRICE_FROM_SUPPLIER     = 10
    NEW_BOOK_CUSTOMER_PRICE      = 20
    USED_BOOK_CUSTOMER_PRICE     = 12   # in good state
    USED_BOOK_MAX_PRICE_POSSIBLE = int(USED_BOOK_CUSTOMER_PRICE/2)
    INITIAL_BOOKS                = 1000	# mettere un numero minore per debuggare
    INITIAL_COPIES               = 2

    def __init__(self, shop_name, initial_account):
        self.shop_name       = shop_name
        self.current_account = initial_account
        self.on_sale_new_books : list[Book] = []
        self.on_sale_used_books: list[Book] = []

    def buy_from_suppliers(self, quantity, copies_number):
        # scrivete il codice voi..
        books_to_buy_number = quantity * copies_number
        for idx in range(books_to_buy_number):
            book = Book(100,f'Title-{idx}',f'Author-{idx}',self.NEW_BOOK_CUSTOMER_PRICE)
            self.on_sale_new_books.append(book)
	# aggiornate self.current_account!! quanti soldi ha Andrea dopo l'acquisto?

    def sell_new_book(self,) -> Book | None:
        pass
        
    def sell_used_book(self,):
        pass

    def _is_in_good_state(self, book: Book) -> bool:
        pass

    def _decide_price(self) -> int:
        pass

    def estimate_book_conditions(self, book: Book) -> int:
        pass

    def on_sale_goods_summary(self):
        pass

    def find_book_by_title(self,) -> int:
        pass

    def find_book_by_author(self,) -> int:
        pass

    def total_books_on_sale(self):
        pass


andrea_shop = BookShop('Le Pagine di Andrea',1000)

andrea_shop.buy_from_suppliers(10,2)
# continua tu..