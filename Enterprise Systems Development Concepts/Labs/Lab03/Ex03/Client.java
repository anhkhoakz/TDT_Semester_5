import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;

public class Client {

    public Client() {
    }

    public static void main(String[] args) {
        try {
            if (args.length < 3 || args.length > 4) {
                System.err.println("Usage: java Client <host> <port> <filename> [<content>]");
                System.exit(1);
            }

            String host = args[0];
            int port = Integer.parseInt(args[1]);
            String filename = args[2];

            Registry registry = LocateRegistry.getRegistry(host, port);
            File stub = (File) registry.lookup("File");

            if (args.length == 3) {
                String content = stub.readFile(filename);
                System.out.println("File content: " + content);
            } else {
                String content = args[3];
                stub.writeFile(filename, content);
                System.out.println("File written successfully");
                content = stub.readFile(filename);
                System.out.println("File content: " + content);
            }

        } catch (Exception e) {
            System.err.println("Error:" + e.getMessage());
        }
    }
}