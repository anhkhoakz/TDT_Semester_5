package Ex07;

import java.util.Date;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        Task task = new Task("Task 1", new Date());

        try {
            FileOutputStream fileOutput = new FileOutputStream("task.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(task);

            out.close();
            fileOutput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Serialized data is saved in task.ser");
    }
}
