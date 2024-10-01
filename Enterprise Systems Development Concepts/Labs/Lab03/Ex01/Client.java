// package Ex00;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.*;

public class Client {
    public Client() {

    }

    public static void main(String[] args) {
        try {
            if (args.length < 3) {
                System.err.println("Usage: java Client <host> <port> <inputs>");
                System.exit(1);
            }

            int index = 0;

            String host = args[index++];
            int port = Integer.parseInt(args[index++]);

            String input = Arrays.toString(Arrays.copyOfRange(args, index, args.length));

            Registry registry = LocateRegistry.getRegistry(host, port);

            Hello stub = (Hello) registry.lookup("Hello");

            stub.printMsg(input);

            System.err.println("Remote method invoked");
        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}
