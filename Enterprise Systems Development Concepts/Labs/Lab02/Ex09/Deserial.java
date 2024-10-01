package Ex09;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Setting setting = null;

        try {
            FileInputStream fileInput = new FileInputStream("setting.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            setting = (Setting) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + setting);
    }
}
