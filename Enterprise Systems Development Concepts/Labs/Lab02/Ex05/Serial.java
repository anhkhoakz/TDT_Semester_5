package Ex05;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        Team team = new Team("Real Madrid");

        team.getPlayers().add(new Player("Jason Ibarra", "Tien ve", 9));
        team.getPlayers().add(new Player("Denise Singh", "Thu mon", 1));
        team.getPlayers().add(new Player("Teresa Gregory", "Hau ve", 10));
        team.getPlayers().add(new Player("Marcelle Riviere", "Tien ve", 4));

        try {
            FileOutputStream fileOutput = new FileOutputStream("team.ser");

            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(team);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in team.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

}
