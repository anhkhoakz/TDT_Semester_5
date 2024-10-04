import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.io.IOException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public Server() {
    }

    public static void main(String[] args) {
        try {
            int index = 0;
            int port = Integer.parseInt(args[index++]);

            List<Person> persons = loadPersonsFromCSV("data.csv");

            PersonImpl obj = new PersonImpl(persons);
            PersonInterface skeleton = (PersonInterface) UnicastRemoteObject.exportObject(obj, port);

            Registry registry = LocateRegistry.createRegistry(port);
            registry.rebind("PersonInterface", skeleton);

            System.out.println("Server is ready");
        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }

    private static List<Person> loadPersonsFromCSV(String filePath) throws IOException {
        return Files.lines(Paths.get(filePath))
                .skip(1)
                .map(line -> {
                    String[] fields = line.split(",");
                    String surname = fields[0];
                    int count = Integer.parseInt(fields[1]);
                    double pctwhite = Double.parseDouble(fields[2]);
                    double pctblack = Double.parseDouble(fields[3]);
                    return new Person(surname, count, pctwhite, pctblack);
                })
                .collect(Collectors.toList());
    }
}