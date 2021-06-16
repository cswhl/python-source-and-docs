public class ArrayTest {
    public static void main(String[] aras) {
        Integer[] num = new Integer[]{1,2,3,4};
        Integer[] num1 = {1,2,3,4};

        print(num);
        print(num1);
    }

    private static void print(Integer[] num) {
        System.out.println(num);
        for(Integer i: num) {
            System.out.println(i);
        }

    }
}
