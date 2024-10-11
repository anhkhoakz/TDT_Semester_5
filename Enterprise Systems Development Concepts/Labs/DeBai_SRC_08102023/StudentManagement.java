// DO NOT USE PACKAGE

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;

public interface StudentManagement extends Remote {

    public int getNoOfStudent() throws RemoteException;

    public int getNoOfStudent_byGender(String gender) throws RemoteException;

    public int getNoOfStudent_byMajor(String major) throws RemoteException;

    public int getNoOfStudent_byGPA(double gpa) throws RemoteException;

    public Student findStudent_byName(String name) throws RemoteException;

    public Student findStudent_byID(String id) throws RemoteException;

    public Student getHighestGPA_byGender(String gender) throws RemoteException;

    public Student getHighestGPA_byFName(String fname) throws RemoteException;

    public Student getHighestGPA_byLName(String lname) throws RemoteException;

    public Student getHighestGPA_byMajor(String major) throws RemoteException;

    public Student getLowestGPA_byMajor(String major) throws RemoteException;

    public ArrayList<Student> findStudent_byMajor(String major) throws RemoteException;

    public ArrayList<Student> findStudent_byGPA(double GPA) throws RemoteException;

    public double getAvgGPA() throws RemoteException;

    public ArrayList<Student> getTop10_byGPA() throws RemoteException;

    public ArrayList<Student> getTop10GPA_byGender(String gender) throws RemoteException;

    public ArrayList<Student> getTop10GPA_byMajor(String major) throws RemoteException;

    public ArrayList<Student> getLast10GPA_byGender(String gender) throws RemoteException;

    public ArrayList<Student> getLast10GPA_byMajor(String major) throws RemoteException;

    public ArrayList<String> getMajors() throws RemoteException;

}
