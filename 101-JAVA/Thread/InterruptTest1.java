import java.io.IOException;

public class InterruptTest1 {

    public static void main(String[] args) throws IOException  {
        InterruptTest1 test = new InterruptTest1();
        MyThread thread = test.new MyThread();
        thread.start();
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
        }
        thread.interrupt();
    }

    class MyThread extends Thread {
        @Override
        public void run() {
            int i = 0;
            while(i < Integer.MAX_VALUE) {
                System.out.println(i + " while循环");
                i++;
            }
        }
    }
}
