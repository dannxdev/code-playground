import os


os.system('cls')


class Library:

    def __init__(self) -> None:
        self.categories = []

    def add_category(self, category):
        """Añade una categoria a la biblioteca."""

        if isinstance(category, Category):
            if not category in self.categories:
                self.categories.append(category)
                return True
        return False

    def register_book(self, category_id, book):
        """Añade libros a la biblioteca"""

        if isinstance(book, Book):
            for category in self.categories:
                if category_id == category.category_id:
                    return category.add_book(book)
        return False

    def show_all_books(self):
        """Muestra todos los libros de la biblioteca."""

        for category in self.categories:
            print(f"\n{category.category_name}\n")

            if len(category.books) > 0:
                for book in category.books:
                    book.show_info()

            else:
                print('Vacio')

    def show_all_categories(self):
        print("Categorias:")
        for category in self.categories:
            print(
                f"- ID: '{category.category_id}' | '{category.category_name}'")

    def all_categories_id_list(self):
        categories_id = []

        for category in self.categories:
            categories_id.append(category.category_id)

        return categories_id

    def all_books_id_list(self):
        """Crea una lista con todos los ID de los libros registrados"""

        all_books_id = []

        for category in self.categories:
            if len(category.books) > 0:
                for book in category.books:
                    all_books_id.append(book.book_id)

        return all_books_id


class Category:

    def __init__(self, category_id, category_name, category_price) -> None:
        self.category_id = category_id
        self.category_name = category_name
        self.category_price = float(category_price)
        self.books = []

    def add_book(self, book):
        """Añade un libro a la categoria."""

        if isinstance(book, Book):
            if not book in self.books:
                self.books.append(book)
                return True
        return False


class Book:

    def __init__(self, book_id, book_title, book_author, book_edition) -> None:
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_edition = book_edition

    def show_info(self):
        """Muestra en consola la info del libro."""

        print(
            f"ID LIBRO: {self.book_id}\n- Titulo: {self.book_title}\n- Autor: {self.book_author}\n- Edicion: {self.book_edition}")


# creando a la biblioteca:
mi_biblioteca = Library()

# Creando las categorias:
ciencia = Category('C1', 'Ciencia', 80000)
literatura = Category('C2', 'Literatura', 50000)
tecnologia = Category('C3', 'Tecnologia', 100000)
historia = Category('C4', 'Historia', 60000)

# Anadiendo las categorias a la biblioteca:
mi_biblioteca.add_category(ciencia)
mi_biblioteca.add_category(literatura)
mi_biblioteca.add_category(tecnologia)
mi_biblioteca.add_category(historia)


def register_books(library: Library):

    print('REGISTRO DE LIBROS')

    num_registers = 0

    while True:
        print('Ingrese los datos del libro')

        while True:
            book_id = input('ID del libro: ').upper()
            if not book_id in library.all_books_id_list():
                break
            print('El ID ingresado ya esta ocupado.')

        book_name = input('Nombre del libro: ').title()
        book_author = input('Autor del libro: ').title()
        book_edition = input('Edicion del libro: ')

        new_book = Book(book_id, book_name, book_author, book_edition)

        library.show_all_categories()

        while True:
            book_category_id = input('ID Categoria: ').upper()
            if book_category_id in library.all_categories_id_list():
                break
            print('No existe ninguna categoria con ese ID.')

        # Anadiendo el libro:
        if library.register_book(book_category_id, new_book):
            num_registers += 1
            print('Se ha registrado el libro exitosamente')
        else:
            print('Ocurrio un error al registrar el libro. Intentelo denuevo.')

        while True:
            reg_opcion = input(
                '\nIniciar un nuevo registro (s/n): ').lower()
            if reg_opcion in ("s", "n"):
                break
            print('Opcion no valida.')

        if reg_opcion == "n":
            break

    print(f"Se registraron {num_registers} libros.")

    library.show_all_books()

    print("Fin del registro.")


register_books(mi_biblioteca)
