import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.List;

public class PersonImpl extends UnicastRemoteObject implements PersonInterface {
    private List<Person> persons;

    public PersonImpl(List<Person> persons) throws RemoteException {
        super();
        this.persons = persons;
    }

    public String findBySurname(String surname) throws RemoteException {
        for (Person person : persons) {
            if (person.getSurname().equals(surname)) {
                return person.toString();
            }
        }
        return "Not found";
    }

    public List<Person> findByPctWhite(double pctwhite) throws RemoteException {
        List<Person> result = new ArrayList<>();
        for (Person person : persons) {
            if (person.getPctwhite() < pctwhite) {
                result.add(person);
            }
        }
        return result;
    }

    public List<Person> listByCount(int count) throws RemoteException {
        List<Person> result = new ArrayList<>();
        for (Person person : persons) {
            if (person.getCount() > count) {
                result.add(person);
            }
        }
        return result;
    }
}