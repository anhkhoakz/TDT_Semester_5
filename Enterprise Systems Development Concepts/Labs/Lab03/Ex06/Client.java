import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        try {
            if (args.length != 4) {
                System.err.println("Usage: java Client <host> <port> <command> <parameter>");
                System.exit(1);
            }

            String host = args[0];
            int port = Integer.parseInt(args[1]);
            String command = args[2];
            String parameter = args[3];

            Registry registry = LocateRegistry.getRegistry(host, port);
            PersonInterface stub = (PersonInterface) registry.lookup("PersonInterface");

            switch (command) {
                case "find":
                    String found = stub.findBySurname(parameter);
                    System.out.println("Surname " + parameter + " found: " + found);
                    break;
                case "pctwhite":
                    double pctwhite = Double.parseDouble(parameter);
                    List<Person> personsByPctwhite = stub.findByPctWhite(pctwhite);
                    personsByPctwhite.forEach(System.out::println);
                    break;
                case "list":
                    int count = Integer.parseInt(parameter);
                    List<Person> personsByCount = stub.listByCount(count);
                    personsByCount.forEach(System.out::println);
                    break;
                default:
                    System.err.println("Invalid command: " + command);
                    break;
            }

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}