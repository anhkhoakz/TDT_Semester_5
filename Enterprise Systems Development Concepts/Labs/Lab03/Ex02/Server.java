import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends CalculatorImpl {
    public Server() {
    }

    public static void main(String[] args) {
        try {
            int index = 0;
            int port = Integer.parseInt(args[index++]);

            CalculatorImpl obj = new CalculatorImpl();

            Calculator skeleton = (Calculator) UnicastRemoteObject.exportObject(obj, 0);

            Registry registry = LocateRegistry.getRegistry(port);
            registry.rebind("Calculator", skeleton);
            System.err.println("Server ready on port " + port);

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}