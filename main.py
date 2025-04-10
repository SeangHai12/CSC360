from tkinter import *
from tkinter import messagebox
from data_Stucture import BookLibrary


window = Tk()

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
    messageBox("Library", library.display_books())


# MessageBox
def messageBox(title, text):
    messagebox.showinfo(title, text)


# <------Entry------>

# name_Entry
name_input = Entry()
name_input.pack()

# author_Entry
author_input = Entry()
author_input.pack()

# year_Entry
year_input = Entry()
year_input.pack()


# <------Button------>

# insert_button
insert_Button = Button()
insert_Button.config(
    text="Insert",
    command=lambda: insert_Func(
        name=name_input.get(), author=author_input.get(), year=int(year_input.get())
    ),
)
insert_Button.pack()


# search_button
search_Button = Button()
search_Button.config(text="Search", command=lambda: search_book(name_input.get()))
search_Button.pack()

# delete_button

delete_Button = Button()
delete_Button.config(text="Delete", command=lambda: delete_Func(name_input.get()))
delete_Button.pack()

# Display_button
display_Button = Button()
display_Button.config(text="display", command=display_book)
display_Button.pack()

window.mainloop()
