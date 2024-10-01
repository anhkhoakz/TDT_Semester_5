import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.rmi.RemoteException;

public class FileImpl implements File {
    public FileImpl() {
    }

    public String readFile(String filename) throws RemoteException {
        try {
            return new String(Files.readAllBytes(Paths.get(filename)));
        } catch (Exception e) {
            throw new RemoteException("Error reading file: " + e.getMessage());
        }
    }

    public void writeFile(String filename, String content) throws RemoteException {
        try {
            Files.write(Paths.get(filename), content.getBytes());
        } catch (IOException e) {
            throw new RemoteException("Error writing file: " + e.getMessage());
        }
    }

}
