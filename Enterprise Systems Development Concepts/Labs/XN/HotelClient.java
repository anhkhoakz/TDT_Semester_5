import java.rmi.Naming;
import java.util.List;

public class HotelClient {
    public static void main(String[] args) {
        if (args.length < 3 || args[0].equalsIgnoreCase("-help")) {
            System.out.println("Usage: java HotelClient <host> <port>");
            System.out.println("   Or: java HotelClient <host> <port> -help");
            System.out.println("Commands:");
            // Login
            System.out.println("   java HotelClient <host> <port> -logIn <username> <password>");
            System.out.println("     - A manager or receptionist logs in to the system with the given user account.");
            System.out.println("       There are two roles in the system (manager and receptionist). Both roles");
            System.out.println("       can reserve or register a room for guests.");

            // list
            System.out.println("   java HotelClient <host> <port> -list");
            System.out.println("     - List avalable number of rooms in each price range.");

            // book
            System.out.println("   java HotelClient <host> <port> -book <room_type> <guest_name> [guest_ssn]");
            System.out.println(
                    "     - Book a room of a specified type (if available) and register guest's name abd his/her information.");

            // guests
            System.out.println("   java HotelClient <host> <port> -guests");
            System.out.println("     - List the information of all registered guests in the system.");

            // logout
            System.out.println("   java HotelClient <host> <port> -logOut");
            System.out.println("     - Sign out the current user's session.");
            return;
        }

        try {
            String host = args[0];
            String port = args[1];
            String username = "";

            RoomManager manager = (RoomManager) Naming.lookup("//" + host + ":" + port + "/RoomManagerService");

            String option = args[2];
            switch (option) {
                case "-logIn":
                    username = args[3];
                    String password = args[4];
                    String loginResult = manager.logIn(username, password);
                    if (!loginResult.equals("success")) {
                        System.out.println(loginResult);
                        return;
                    }
                    break;
                case "-list":
                    System.out.println(manager.listRoomAvailability());
                    break;
                case "-book":
                    if (args.length < 4 || args.length > 6) {
                        System.out.println(
                                "Usage: java HotelClient <host> <port> -book <room_type> <guest_name> [guest_ssn]");
                        break;
                    }
                    int roomType = Integer.parseInt(args[3]);
                    String guestName = args[4];
                    String guestSSN = args.length == 6 ? args[5] : "";
                    System.out.println(manager.bookRoom(roomType, guestName, guestSSN));
                    break;
                case "-guests":
                    List<String> guests = manager.listGuests();
                    System.out.println("Guest List:");
                    for (String guest : guests) {
                        System.out.println(guest);
                    }
                    break;
                case "-logOut":
                    manager.logOut(username);
                    break;
                default:
                    System.out.println("Invalid command. Try -help.");
                    return;
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
