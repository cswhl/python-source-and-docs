import java.io.*;

public class JoinTest {

    public static void main(String[] args) throws IOException  {
        System.out.println("进入线程" + Thread.currentThread().getName());
        JoinTest test = new JoinTest();
        MyThread thread1 = test.new MyThread();
        thread1.start();
        try {
            System.out.println("线程" + Thread.currentThread().getName() + "等待");
            thread1.join();
            System.out.println("线程" + Thread.currentThread().getName() + "继续执行");

        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            //             e.printStackTrace();
            //
        }

    }

    class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("进入线程" + Thread.currentThread().getName());
            try {
                Thread.currentThread().sleep(5000);

            } catch (InterruptedException e) {
                // TODO: handle exception
                //
            }
            System.out.println("线程" + Thread.currentThread().getName() + "执行完毕");

        }

    }

}
