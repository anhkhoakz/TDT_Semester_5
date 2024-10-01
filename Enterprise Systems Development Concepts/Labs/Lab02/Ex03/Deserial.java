package Ex03;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Library library = null;
        try {
            FileInputStream fileIn = new FileInputStream("library1.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            library = (Library) in.readObject();

            in.close();
            fileIn.close();

        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println(library.toString());
    }

}
