import java.lang.ref.WeakReference;

public class WeakReferenceTest {
    public static void main(String[] args) {

    }
    public static void weakReference() throws InterruptedException {
        Object obj = new Object();
        WeakReference<Object> weak = new WeakReference<>(obj);
        obj = null;
        System.out.println(weak.get());
        System.gc();
        System.out.println(weak.get());

    }
}
