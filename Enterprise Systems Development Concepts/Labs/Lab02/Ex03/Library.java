package Ex03;

import java.util.ArrayList;
import java.util.List;
import java.io.Serializable;
import java.io.Serial;

public class Library implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;
    private List<Book> books;

    public Library() {
        this.books = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public String toString() {
        return "Library[" + books + "]";
    }
}
