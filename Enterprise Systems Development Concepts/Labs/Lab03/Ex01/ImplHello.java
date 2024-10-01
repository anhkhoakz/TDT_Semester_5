// package Ex00;

import java.rmi.RemoteException;

/**
 * ImplHello
 */
public class ImplHello implements Hello {

    public void printMsg(String name) throws RemoteException {
        System.out.println(name + " is trying to contact!");
    }
}