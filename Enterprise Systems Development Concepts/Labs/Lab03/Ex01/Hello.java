// package Ex00;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Hello extends Remote {
    public void printMsg(String name) throws RemoteException;
}