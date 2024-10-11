// DO NOT USE PACKAGE

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {

    public static void main(String[] args) {
        try {
            // Parse the input arguments
            if (args.length < 1) {
                System.err.println("usage  : java Server <port>");
                System.err.println("example: java Server 1100");
                System.exit(1);
            }
            int index = 0;
            int port = Integer.parseInt(args[index++]);

            // Instantiating the implementation class
            StudentManagementImpl obj = new StudentManagementImpl("testcase.txt");

            // Exporting the object of implementation class
            // (here we are exporting the remote object to the skeleton)
            StudentManagement skeleton = (StudentManagement) UnicastRemoteObject.exportObject(obj, 0);

            // Binding the remote object (stub) in the registry
            Registry registry = LocateRegistry.getRegistry(port);
            registry.rebind("StuManagement", skeleton);

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }

}
