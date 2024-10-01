import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public Client() {
    }

    public static void main(String[] args) {
        try {
            if (args.length != 2) {
                System.err.println("Usage: java Client <host> <port>");
                System.exit(1);
            }

            String host = args[0];
            int port = Integer.parseInt(args[1]);

            Registry registry = LocateRegistry.getRegistry(host, port);
            Sensor stub = (Sensor) registry.lookup("Sensor");

            for (int i = 0; i < 10; i++) {
                String reading = stub.getLatestReading();
                System.out.println("Latest Sensor Reading: " + reading);

                Thread.sleep(2000);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}