package Ex03;

import java.io.Serializable;
import java.io.Serial;

public class Book implements Serializable {

    @Serial
    private static long serialVersionUID = 1L;
    private String title;
    private String author;
    private int publicationYear;

    public Book(String title, String author, int publicationYear) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
    }

    public String getTitle() {
        return this.title;
    }

    public String getAuthor() {
        return this.author;
    }

    public int getPublicationYear() {
        return this.publicationYear;
    }

    public String toString() {
        return "Book[Title: " + getTitle() + ", Author: " + getAuthor() + ", Publication Year: " + getPublicationYear()
                + "]";
    }

}
