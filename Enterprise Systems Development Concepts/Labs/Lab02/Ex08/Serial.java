package Ex08;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        Employee employee = new Employee("Ruben Torres", 1234.5, "passwordne");

        try {
            FileOutputStream fileOutput = new FileOutputStream("employee.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(employee);

            out.close();
            fileOutput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Serialized data is saved in employee.ser");
    }
}
