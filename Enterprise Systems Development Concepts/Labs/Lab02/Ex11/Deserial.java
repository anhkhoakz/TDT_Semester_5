package Ex11;

import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.io.IOException;

public class Deserial {
    public static void main(String[] args) {
        Student student = null;

        try (FileInputStream fileInput = new FileInputStream("student.ser");
                ObjectInputStream in = new ObjectInputStream(fileInput)) {
            student = (Student) in.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Deserialized data: " + student);
    }
}