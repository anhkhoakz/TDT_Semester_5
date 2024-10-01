import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public Client() {
    }

    public static void main(String[] args) {
        try {
            if (args.length < 4) {
                System.err.println("Usage: java Client <host> <port> <action> <bookTitle>");
                System.exit(1);
            }

            String host = args[0];
            int port = Integer.parseInt(args[1]);
            String action = args[2];
            String bookTitle = args[3];

            Registry registry = LocateRegistry.getRegistry(host, port);
            Library stub = (Library) registry.lookup("Library");

            switch (action) {
                case "search":
                    System.out.println("Searching for books with title: " + bookTitle);
                    for (String book : stub.searchBooks(bookTitle)) {
                        System.out.println(book);
                    }
                    break;
                case "checkout":
                    System.out.println("Checking out book with title: " + bookTitle);
                    if (stub.checkOutBook(bookTitle)) {
                        System.out.println("Book checked out successfully");
                    } else {
                        System.out.println("Book could not be checked out");
                    }
                    break;
                case "return":
                    System.out.println("Returning book with title: " + bookTitle);
                    if (stub.returnBook(bookTitle)) {
                        System.out.println("Book returned successfully");
                    } else {
                        System.out.println("Book could not be returned");
                    }
                    break;
                default:
                    System.err.println("Invalid action: " + action);
                    System.out.println("Valid actions are: search, checkout, return");
                    break;
            }

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}
