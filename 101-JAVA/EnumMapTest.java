import java.util.*;

public class EnumMapTest {

    public static void main(String[] args) {
        Map<Color, String> enumMap = new EnumMap<Color,String>(Color.class);
        enumMap.put(Color.BLACK, "黑色");
        enumMap.put(Color.BLUE, "蓝色");
        enumMap.put(Color.YELLOW, null);
        System.out.println(enumMap);
        System.out.println(enumMap.get(Color.BLUE));
    }
}

enum Color {
    YELLOW, RED, BLUE, PURPLE, BLACK;
}
