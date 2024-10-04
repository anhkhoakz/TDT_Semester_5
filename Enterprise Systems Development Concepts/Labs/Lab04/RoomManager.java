import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface RoomManager extends Remote {
    boolean logIn(String username, String password) throws RemoteException;

    void logOut() throws RemoteException;

    List<String> listRooms() throws RemoteException;

    boolean bookRoom(int roomType, String guestName, String guestSSN) throws RemoteException;

    List<String> listGuests() throws RemoteException;
}