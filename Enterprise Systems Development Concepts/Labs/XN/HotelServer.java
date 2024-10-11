import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelServer {
    public static void main(String[] args) {
        try {
            if (args.length < 1) {
                System.out.println("Usage: java HotelServer <port>");
                return;
            }

            int port = Integer.parseInt(args[0]);

            // Get the RMI registry on the specified port
            Registry registry = LocateRegistry.getRegistry(port);

            // Create an instance of RoomManagerImpl and bind it to the registry on the
            // specified port
            RoomManager manager = new RoomManagerImpl();
            registry.rebind("RoomManagerService", manager);

            System.out.println("HotelServer is running and RoomManagerService is bound to port " + port + ".");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
