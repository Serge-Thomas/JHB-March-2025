class Book:
    # class attribute (shared by all instances)
    book_type = "Paperback"
    
    # initializer method (runs when creating a new object)
    def __init__(self, title, author, pages):
        # Instance atttributes (unique to each object)
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.bookmark = None
        
    # instance methods
    def read(self, num_pages):
        self.current_page += num_pages
        if self.current_page > self.pages:
            self.current_page = self.pages
            
    def place_bookmark(self):
        self.bookmark = self.current_page
        print(f"Bookmark placed at page {self.bookmark}")
        
    def go_to_bookmark(self):
        if self.bookmark:
            self.current_page = self.bookmark
            print(f"Returned to bookmarked page {self.bookmark}")
        else:
            print("No bookmark noticed")
            
    # def book_info(self):
    #     return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    # special method in python: String representation method
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}, {self.pages} pages"
    
    # representation method (for debugging)
    def __repr__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"


# Creating oBook objects with attributes
harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320)
hunger_games = Book("The Hunger Games", "Suzanne Collins", 378)


# Acessing attributes
# print(harry_potter.title)   
# print(hunger_games.author)
# print(harry_potter.book_type)


print(harry_potter)
print(hunger_games)


# you call the object ==> object.method()
# you call the attribute ==> object.attribute

harry_potter.read(54)
harry_potter.place_bookmark()
print(harry_potter.bookmark)


hunger_games.read(100)
hunger_games.go_to_bookmark()
print(hunger_games.bookmark)