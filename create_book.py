def create_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = input("Enter price: ")

    book = {
        "title": title,
        "author": author,
        "price": price
    }

    print("Book created successfully!")
    print(book)

create_book()