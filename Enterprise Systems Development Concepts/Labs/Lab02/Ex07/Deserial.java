package Ex07;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Task task = null;

        try {
            FileInputStream fileInput = new FileInputStream("task.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            task = (Task) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + task);
    }
}
