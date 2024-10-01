package Ex09;

import java.io.ObjectOutputStream;
import java.io.FileOutputStream;

public class Serial {
    public static void main(String[] args) {
        Setting setting = new Setting("anhkhoakzdev", "123541Abc", true);

        try {
            FileOutputStream fileOutput = new FileOutputStream("setting.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(setting);

            out.close();
            fileOutput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Serialized data is saved in setting.ser");
    }

}
