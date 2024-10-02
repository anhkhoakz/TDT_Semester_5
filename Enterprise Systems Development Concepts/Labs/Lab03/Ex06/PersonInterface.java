import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface PersonInterface extends Remote {

    String findBySurname(String surname) throws RemoteException;

    List<Person> findByPctWhite(double pctwhite) throws RemoteException;

    List<Person> listByCount(int count) throws RemoteException;

}