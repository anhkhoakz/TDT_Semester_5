package Ex00;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Serializing {
    public static void main(String[] args) {
        Employee employee = new Employee("John", "TDTU", 1111);

        try {
            FileOutputStream fileOut = new FileOutputStream("employee.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(employee);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in employee.ser");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
