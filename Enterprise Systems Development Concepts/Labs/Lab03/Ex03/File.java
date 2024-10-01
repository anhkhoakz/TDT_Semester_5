import java.rmi.Remote;
import java.rmi.RemoteException;

public interface File extends Remote {
    String readFile(String filename) throws RemoteException;

    void writeFile(String filename, String content) throws RemoteException;
}
