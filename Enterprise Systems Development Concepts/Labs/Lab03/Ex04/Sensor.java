import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Sensor extends Remote {
    String getLatestReading() throws RemoteException;
}