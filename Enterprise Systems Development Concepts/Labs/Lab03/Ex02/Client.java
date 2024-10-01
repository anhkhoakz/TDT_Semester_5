import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public Client() {
    }

    public static void main(String[] args) {
        // System.out.println("Arguments: " + Arrays.toString(args));
        try {
            if (args.length < 5) {
                System.err.println("Usage: java Client <host> <port> <number> <operator> <number>");
                System.exit(1);
            }

            int index = 0;

            String host = args[index++];
            int port = Integer.parseInt(args[index++]);

            double num1 = Double.parseDouble(args[index++]);
            String operator = args[index++];
            double num2 = Double.parseDouble(args[index++]);

            Registry registry = LocateRegistry.getRegistry(host, port);

            Calculator stub = (Calculator) registry.lookup("Calculator");

            double result = stub.calculate(num1, num2, operator);

            System.out.println("Result: " + result);

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}