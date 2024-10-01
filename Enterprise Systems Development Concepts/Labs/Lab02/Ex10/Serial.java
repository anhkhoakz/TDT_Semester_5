package Ex10;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        try {
            Person person = new Person("Anh Khoa", new Address("HCMc", "Vietnam", 70000));

            System.out.println("Person: " + person);

            FileOutputStream fileOutput = new FileOutputStream("person.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(person);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in person.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
