package Ex00;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Deserializing {
    public static void main(String[] args) {
        Employee employee = null;
        try {
            FileInputStream fileIn = new FileInputStream("employee.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            employee = (Employee) in.readObject();

            in.close();
            fileIn.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);

        }

        System.out.println("Deserialized Employee...");
        System.out.println("Name: " + employee.getName());
        System.out.println("Address: " + employee.getAddress());
        System.out.println("SSN: " + employee.getSSN());
    }
}
