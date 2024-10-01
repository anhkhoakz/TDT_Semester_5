package Ex04;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        Student student = new Student("Jamie Reynolds", "522H0046", new double[] { 9.0, 7.5, 8.3 });

        try {
            FileOutputStream fileOutput = new FileOutputStream("student.ser");

            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(student);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in student.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
