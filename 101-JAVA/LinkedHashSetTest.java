import java.util.*;

public class LinkedHashSetTest {
    public static void main(String[] args) {
        LinkedHashSet<String> books = new LinkedHashSet<String>();
        books.add("Java");
        books.add("LittleHann");
        System.out.println(books);

        //删除 Java
        books.remove("Java");
        //重新添加 Java
        books.add("Java");
        System.out.println(books);
    }
}
