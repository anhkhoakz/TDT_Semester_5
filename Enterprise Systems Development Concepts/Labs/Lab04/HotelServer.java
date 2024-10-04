import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelServer {
    public static void main(String[] args) {
        try {
            RoomManagerImpl roomManager = new RoomManagerImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("RoomManager", roomManager);
            System.out.println("HotelServer is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}