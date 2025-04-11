from tkinter import *
from tkinter import messagebox
from data_Stucture import BookLibrary


window = Tk()
window.title("Library")
window.iconbitmap("images/book.ico")
library = BookLibrary()


# insert function
def insert_Func(name, author, year):
    library.insert(name, author, year)
    name_input.delete(0, END)
    author_input.delete(0, END)
    year_input.delete(0, END)


# function to search for book
def search_book(text):
    book = library.search(text)
    if book:
        messageBox("library", f"\nFound: {book.name} by {book.author} ({book.year})")
    else:
        messageBox("library", "No book found")


# function delete
def delete_Func(text):
    library.delete(text)


# function to display book
def display_book():
    if library.display_books():
        messageBox("Library", library.display_books())
    else:
        messageBox("Library", "Library don't have book yet.")


# MessageBox
def messageBox(title, text):
    messagebox.showinfo(title, text)


# <------Entry------>

# name_Entry
name_input = Entry()
name_input.grid(row=1, column=1)


# author_Entry
author_input = Entry()
author_input.grid(row=2, column=1)


# year_Entry
year_input = Entry()
year_input.grid(row=3, column=1)

# <------book_image------>
book_image = PhotoImage(file="images/stack-of-books.png")
book_label = Label()
book_label.config(image=book_image)
book_label.grid(row=0, column=1, pady=30)

# <------Label------>

# name_Label
name_label = Label()
name_label.config(text="Book name")
name_label.grid(row=1, column=0, sticky="e")

author_label = Label()
author_label.config(
    text="Author name",
)
author_label.grid(row=2, column=0, pady=10, padx=(30, 0), sticky="e")

year_label = Label()
year_label.config(text="Year")
year_label.grid(row=3, column=0, sticky="e")


# <------Button------>

# insert_button
insert_Button = Button()
insert_Button.config(
    text="Insert",
    command=lambda: insert_Func(
        name=name_input.get(), author=author_input.get(), year=int(year_input.get())
    ),
)
insert_Button.grid(row=4, column=1, pady=(10, 0))

# search_button
search_Button = Button()
search_Button.config(text="Search", command=lambda: search_book(name_input.get()))
search_Button.grid(row=1, column=2, sticky="w", padx=(0, 30))

# delete_button

delete_Button = Button()
delete_Button.config(text="Delete", command=lambda: delete_Func(name_input.get()))
delete_Button.grid(row=6, column=1, pady=(0, 10))

# Display_button
display_Button = Button()
display_Button.config(text="display", width=10, command=display_book)
display_Button.grid(row=5, column=1, pady=10)

exit_button = Button()
exit_button.config(text="exit", command=lambda: window.destroy())
exit_button.grid(row=7, column=1, pady=(0, 10))


window.mainloop()
