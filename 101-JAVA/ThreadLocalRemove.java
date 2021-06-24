import java.lang.*;

public class ThreadLocalRemove {

    public static void main(String[] args) {

        ThreadLocal<Integer> tlocal = new ThreadLocal<Integer>();

        /* sets the current thread's copy of this thread-local variable
        to the specified value. */

        tlocal.set(50);
        // returns the current thread's value of this thread-local
        System.out.println("value = " + tlocal.get());

        // removes the current thread's value
        tlocal.remove();
        // returns the current thread's value of this thread-local
        System.out.println("value = " + tlocal.get());
    }
}
