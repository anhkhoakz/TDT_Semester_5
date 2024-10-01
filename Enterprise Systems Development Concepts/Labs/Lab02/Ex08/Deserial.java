package Ex08;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Employee employee = null;

        try {
            FileInputStream fileInput = new FileInputStream("employee.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            employee = (Employee) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + employee);
    }
}
