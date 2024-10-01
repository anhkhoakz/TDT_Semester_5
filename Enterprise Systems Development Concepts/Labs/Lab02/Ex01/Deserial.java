package Ex01;

import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.io.IOException;

public class Deserial {
    public static void main(String[] args) {
        Person person = null;
        try {
            FileInputStream fileIn = new FileInputStream("person.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            person = (Person) in.readObject();

            in.close();
            fileIn.close();
        } catch (IOException i) {
            throw new RuntimeException(i);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized Person...");
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
        System.out.println("Address: " + person.getAddress());
    }
}
