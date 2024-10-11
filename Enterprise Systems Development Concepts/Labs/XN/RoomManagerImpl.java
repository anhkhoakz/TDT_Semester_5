import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class RoomManagerImpl extends UnicastRemoteObject implements RoomManager {

    private static final long serialVersionUID = 1L;

    private Map<Integer, Integer> roomAvailability;
    private List<String> guestList;
    private List<String> loggedInUsers;
    private Map<String, String> userRoles;

    public RoomManagerImpl() throws RemoteException {
        super();
        roomAvailability = new HashMap<>();
        guestList = new ArrayList<>();
        loggedInUsers = new ArrayList<>();
        userRoles = new HashMap<>(); // Initialize userRoles map

        // Predefined user credentials
        userRoles.put("manager", "manager123"); // manager role
        userRoles.put("receptionist", "reception123"); // receptionist role

        // Room availability initialization
        roomAvailability.put(0, 10); // 10 rooms of type 0
        roomAvailability.put(1, 20); // 20 rooms of type 1
        roomAvailability.put(2, 5); // 5 rooms of type 2
        roomAvailability.put(3, 3); // 3 rooms of type 3
        roomAvailability.put(4, 2); // 2 rooms of type 4
    }

    // List room availability method
    @Override
    public synchronized String listRoomAvailability() throws RemoteException {
        StringBuilder availability = new StringBuilder("Room Availability:\n");

        // Prices per room type
        Map<Integer, Integer> roomPrices = new HashMap<>();
        roomPrices.put(0, 55); // Type 0: 55 Euros per night
        roomPrices.put(1, 75); // Type 1: 75 Euros per night
        roomPrices.put(2, 80); // Type 2: 80 Euros per night
        roomPrices.put(3, 150); // Type 3: 150 Euros per night
        roomPrices.put(4, 230); // Type 4: 230 Euros per night

        for (Map.Entry<Integer, Integer> entry : roomAvailability.entrySet()) {
            int roomType = entry.getKey();
            int availableRooms = entry.getValue();
            int price = roomPrices.get(roomType);

            availability.append("+ ").append(availableRooms)
                    .append(" rooms of type ").append(roomType)
                    .append(" are available for ").append(price)
                    .append(" Euros per night.\n");
        }

        return availability.toString();
    }

    // Method to book a room
    @Override
    public synchronized String bookRoom(int roomType, String guestName, String guestSSN) throws RemoteException {
        if (roomAvailability.get(roomType) > 0) {
            roomAvailability.put(roomType, roomAvailability.get(roomType) - 1);
            String guestInfo = "Guest: " + guestName + ", SSN: " + guestSSN + ", Room Type: " + roomType;
            guestList.add(guestInfo);
            return "Room booked for " + guestName;
        } else {
            return "No rooms of type " + roomType + " available.";
        }
    }

    // Method to list all guests
    @Override
    public List<String> listGuests() throws RemoteException {
        return guestList;
    }

    // Method to log out a user
    @Override
    public synchronized void logOut(String username) throws RemoteException {
        if (username == null || username.isEmpty()) {
            System.out.println("No user is logged in.");
            return;
        }

        if (loggedInUsers.remove(username)) {
            System.out.println(username + " has logged out.");
        } else {
            System.out.println("User " + username + " was not logged in.");
        }
    }

    // Method to log in a user
    @Override
    public synchronized String logIn(String username, String password) throws RemoteException {
        if (userRoles.containsKey(username) && userRoles.get(username).equals(password)) {
            if (loggedInUsers.contains(username)) {
                return "User " + username + " is already logged in.";
            } else {
                loggedInUsers.add(username);
                return "success";
            }
        } else {
            return "Invalid username or password.";
        }
    }
}
