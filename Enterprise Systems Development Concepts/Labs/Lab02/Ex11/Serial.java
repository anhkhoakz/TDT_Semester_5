package Ex11;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

public class Serial {
    public static void main(String[] args) {
        Student student = new Student("Anh Khoa", 22, new double[] { 9.0, 7.5, 8.3 });

        try (FileOutputStream fileOutput = new FileOutputStream("student.ser");
                ObjectOutputStream out = new ObjectOutputStream(fileOutput)) {
            out.writeObject(student);
            System.out.println("Serialized data is saved in student.ser");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}