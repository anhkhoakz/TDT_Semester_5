import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public Server() {
    }

    public static void main(String[] args) {
        try {
            int index = 0;
            int port = Integer.parseInt(args[index++]);

            FileImpl obj = new FileImpl();

            File skeleton = (File) UnicastRemoteObject.exportObject(obj, 0);

            Registry registry = LocateRegistry.getRegistry(port);
            registry.rebind("File", skeleton);
            System.err.println("Server ready on port " + port);

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}
