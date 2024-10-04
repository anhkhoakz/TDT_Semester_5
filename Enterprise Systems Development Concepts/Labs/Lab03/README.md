## Java RMI Programming

1.  Define the remote interface

    ```java
    import java.rmi.Remote;
    import java.rmi.RemoteException;

    public interface Hello extends Remote {}
    ```

2.  Developing the Implementation Class

        ```java
        import java.rmi.RemoteException;

        public class HelloImpl implements Hello {
            public HelloImpl() throws RemoteException {}
        }
        ```

3.  Developing the Server Program

        ```java
        import java.rmi.registry.LocateRegistry;
        import java.rmi.registry.Registry;

        public class Server {
            public static void main(String[] args) {
                try {
                    Registry registry = LocateRegistry.createRegistry(Integer.parseInt(args[0]));
                    registry.rebind("Hello", new HelloImpl());
                    System.out.println("Server is ready");
                } catch (Exception e) {
                    System.out.println("Server failed: " + e);
                }
            }
        }
        ```

## Running the Program

You will need to run the following commands in three separate command prompts/ terminal.

### MacOS

#### First Command

```bash

javac \*.java # compile all the java files
rmiregistry 1100 # start the registry with port 1100

```

#### Second Command

```bash
java Server 1100 # start the server with port 1100
```

#### Third Command

```bash

java Client localhost 1100 "ABC" # start the client with host localhost and port 1100 and input "ABC"

```

## Windows

#### First Command

```bash
javac *.java # compile all the java files
start rmiregistry 1100 # start the registry with port 1100
java Server 1100 # start the server with port 1100
```

#### Second Command

```bash
java Client localhost 1100 "ABC" # start the client with host localhost and port 1100 and input "ABC"
```
