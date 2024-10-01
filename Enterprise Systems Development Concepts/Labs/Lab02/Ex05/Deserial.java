package Ex05;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Team team = null;

        try {
            FileInputStream fileInput = new FileInputStream("team.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            team = (Team) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + team);
    }
}
