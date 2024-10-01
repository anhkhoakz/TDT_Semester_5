package Ex03;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {

    public static void main(String[] args) {
        Book book = new Book("Cameron Brooks", "George Ochoa MD", 2024);
        Library library = new Library();
        library.addBook(book);

        try {
            FileOutputStream fileOut = new FileOutputStream("library1.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(library);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in library.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
