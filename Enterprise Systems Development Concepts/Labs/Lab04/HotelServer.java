import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class HotelServer {
    public static void main(String[] args) {
        try {
            if (args == null || args.length < 1) {
                System.err.println("usage  : java HotelServer <port>");
                System.out.println("example: java HotelServer 1100");
                System.exit(1);
            }
            int index = 0;
            int port = Integer.parseInt(args[index++]);

            RoomManagerImpl obj = new RoomManagerImpl();
            RoomManager skeleton;
            try {
                skeleton = (RoomManager) UnicastRemoteObject.exportObject(obj, 0);
            } catch (java.rmi.server.ExportException e) {
                // If the object is already exported, use the existing exported object
                skeleton = obj;
            }

            Registry registry = LocateRegistry.getRegistry(port);
            registry.rebind("RoomManager", skeleton);

            System.out.println("HotelServer is running...");
        } catch (Exception e) {
            System.err.println("HotelServer exception: " + e.toString());
        }
    }
}
