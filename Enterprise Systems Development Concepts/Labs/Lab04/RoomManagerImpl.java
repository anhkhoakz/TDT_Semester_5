import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class RoomManagerImpl extends UnicastRemoteObject implements RoomManager {
    private Map<Integer, Room> rooms;
    private List<Customer> customers;
    private Map<String, User> users;
    private User currentUser;

    public RoomManagerImpl() throws RemoteException {
        rooms = new HashMap<>();
        rooms.put(0, new Room(0, 55, 10));
        rooms.put(1, new Room(1, 75, 20));
        rooms.put(2, new Room(2, 80, 5));
        rooms.put(3, new Room(3, 150, 3));
        rooms.put(4, new Room(4, 230, 2));

        customers = new ArrayList<>();
        users = new HashMap<>();
        loadUsersFromCSV("accountList.csv");
        currentUser = null;
    }

    private void loadUsersFromCSV(String filePath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                if (values.length == 3) {
                    users.put(values[0], new User(values[0], values[1], values[2]));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public boolean logIn(String username, String password) throws RemoteException {
        User user = users.get(username);
        if (user != null && user.getPassword().equals(password)) {
            currentUser = user;
            return true;
        }
        return false;
    }

    @Override
    public void logOut() throws RemoteException {
        currentUser = null;
    }

    @Override
    public List<String> listRooms() throws RemoteException {
        List<String> roomList = new ArrayList<>();
        for (Room room : rooms.values()) {
            roomList.add(room.getAvailability() + " rooms of type " + room.getRoomType() + " are available for "
                    + room.getPrice() + " Euros per night.");
        }
        return roomList;
    }

    @Override
    public boolean bookRoom(int roomType, String guestName, String guestSSN) throws RemoteException {
        Room room = rooms.get(roomType);
        if (room != null && room.getAvailability() > 0) {
            room.setAvailability(room.getAvailability() - 1);
            customers.add(new Customer(guestName, guestSSN, roomType));
            return true;
        }
        return false;
    }

    @Override
    public List<String> listGuests() throws RemoteException {
        if (currentUser != null && "manager".equals(currentUser.getRole())) {
            List<String> guestList = new ArrayList<>();
            for (Customer customer : customers) {
                guestList.add("Guest: " + customer.getName() + ", SSN: " + customer.getSsn() + ", Room Type: "
                        + customer.getRoomType());
            }
            return guestList;
        }
        return Collections.emptyList();
    }
}