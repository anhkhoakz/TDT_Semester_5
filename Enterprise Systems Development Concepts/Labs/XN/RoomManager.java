import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface RoomManager extends Remote {
    String listRoomAvailability() throws RemoteException;

    String bookRoom(int roomType, String guestName, String guestSSN) throws RemoteException;

    List<String> listGuests() throws RemoteException;

    void logOut(String username) throws RemoteException;

    String logIn(String username, String password) throws RemoteException;
}
