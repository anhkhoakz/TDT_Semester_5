package Ex04;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Student student = null;

        try {
            FileInputStream fileInput = new FileInputStream("student.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            student = (Student) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + student);
    }
}
