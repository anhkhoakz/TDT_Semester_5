import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface Library extends Remote {
    List<String> searchBooks(String query) throws RemoteException;

    boolean checkOutBook(String bookTitle) throws RemoteException;

    boolean returnBook(String bookTitle) throws RemoteException;

}
