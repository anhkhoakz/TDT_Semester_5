import java.io.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelClient {
    private static final String ACCOUNT_FILE = "status.csv";

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java HotelClient <host> <port> [options]");
            return;
        }

        String host = args[0];
        int port = Integer.parseInt(args[1]);

        try {
            Registry registry = LocateRegistry.getRegistry(host, port);
            RoomManager roomManager = (RoomManager) registry.lookup("RoomManager");

            if (args.length == 2) {
                System.out.println("Usage: java HotelClient <host> <port> [options]");
            } else {
                String option = args[2];
                switch (option.toLowerCase()) {
                    case "-login":
                        if (args.length == 5) {
                            String userName = args[3];
                            String password = args[4];
                            boolean loggedIn = roomManager.logIn(userName, password);
                            if (loggedIn) {
                                System.out.println("Login successful.");
                            } else {
                                System.out.println("Login failed.");
                            }
                        } else {
                            System.out.println("Usage: java HotelClient <host> <port> -logIn <username> <password>");
                        }
                        break;
                    case "-logout":
                        if (isLoggedIn()) {
                            roomManager.logOut();
                            System.out.println("Logged out successfully.");
                        } else {
                            System.out.println("You are not logged in.");
                        }
                        break;
                    case "-list":
                        if (isLoggedIn()) {
                            roomManager.listRooms().forEach(System.out::println);
                        } else {
                            System.out.println("You must log in before performing this action.");
                        }
                        break;
                    case "-book":
                        if (isLoggedIn()) {
                            if (args.length == 5) {
                                boolean success = roomManager.bookRoom(Integer.parseInt(args[3]), args[4], null);
                                System.out.println(success ? "Room booked successfully." : "Booking failed.");
                                return;
                            }
                            if (args.length == 6) {
                                boolean success = roomManager.bookRoom(Integer.parseInt(args[3]), args[4], args[5]);
                                System.out.println(success ? "Room booked successfully." : "Booking failed.");
                                return;
                            } else {
                                System.out.println(
                                        "Usage: java HotelClient <host> <port> -book <room_type> <guest_name> <guest_ssn>");
                                return;
                            }
                        } else {
                            System.out.println("You must log in before performing this action.");
                        }
                        break;
                    case "-guests":
                        if (isLoggedIn() && isAdmin()) {
                            System.out.println("Guests:");
                            roomManager.listGuests().forEach(System.out::println);
                        } else {
                            if (!isLoggedIn()) {
                                System.out.println("You must log in before performing this action.");
                            } else {
                                System.out.println("You must be an admin to perform this action.");
                            }
                        }
                        break;
                    default:
                        System.out.println("Unknown option: " + option);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static boolean isLoggedIn() {
        String statusFilePath = "status.csv";
        try (BufferedReader br = new BufferedReader(new FileReader(statusFilePath))) {
            String line = br.readLine();
            String[] data = line.split(",");
            if (line == null || data.length != 3) {
                return false;
            }
            if (line != null && data.length == 3) {
                String[] values = data;
                return Boolean.parseBoolean(values[2]);
            }
            return false;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    private static boolean isAdmin() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(ACCOUNT_FILE));
            String role = reader.readLine().split(",")[1];
            reader.close();
            return role.equals("admin");
        } catch (IOException e) {
            System.err.println("Error reading account file.");
            return false;
        }

    }
}
