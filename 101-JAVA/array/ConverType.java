import java.util.*;

public class ConverType {
    public static void main(String[] args) {
        ArrayList<?> aList = null; //ArrayList<E> implement List<E>

        List<?> list = null; //List<E> extends Collection<E>

        Collection<?> colle = null;

        aList = (ArrayList) list;//下←上，强转

        aList = (ArrayList) colle;//下←上，强转

        list = (List) colle;//下←上，强转

        list = aList;//父类←子类，上←下

        colle = list;//父接口←子接口，上←下

        colle = aList;//父接口←子类实现，上←下
    }
}
