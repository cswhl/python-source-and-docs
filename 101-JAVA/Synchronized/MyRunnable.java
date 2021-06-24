public class MyRunnable {

    public static void main(String[] args) {
        RunableTest myRunnable1 = new RunableTest("Runnable1");
        RunableTest myRunnable2 = new RunableTest("Runnable2");

        Thread myThread1 = new Thread(myRunnable1);
        myThread1.start();
        System.out.println("myThread1 id =" + myThread1.getId());
        Thread myThread2 = new Thread(myRunnable2);
        myThread2.start();
        System.out.println("myThread1 id =" + myThread2.getId());
    }

}
class RunableTest implements Runnable {

    private String name;

    public RunableTest(String name) {
        this.name = name;
    }
    @Override
    public void run() {
        System.out.println("RunableTest is " + name);

    }

}
