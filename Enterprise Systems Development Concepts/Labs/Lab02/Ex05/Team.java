package Ex05;

import java.io.Serializable;
import java.io.Serial;
import java.util.ArrayList;

public class Team implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private ArrayList<Player> players;

    public Team(String name) {
        this.name = name;
        this.players = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public ArrayList<Player> getPlayers() {
        return this.players;
    }

    public void setPlayers(ArrayList<Player> players) {
        this.players = players;
    }

    public String toString() {
        return "Team [name=" + getName() + ", players=" + getPlayers() + "]";
    }

}