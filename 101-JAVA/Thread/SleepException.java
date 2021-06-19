public class SleepException {
    public static void main(String[] args) {
        final Thread t1 = new Thread() {
            public void run() {
                System.out.println("Thread1 start!");
                while (true) {
                    System.out.println("Thread1 sleep start!");
                    try {
                        Thread.sleep(10000);

                    } catch (InterruptedException e) {
                        System.out.println("Thread1 sleep exception e=" + e.getMessage());
                        e.printStackTrace();

                    }

                }

            }

        };

        Thread t2 = new Thread() {
            public void run() {
                System.out.println("Thread2 start!");
                while (true) {
                    System.out.println("Thread2 sleep start!");
                    try {
                        Thread.sleep(2000);

                    } catch (InterruptedException e) {
                        System.out.println("Thread2 sleep exception e=" + e);
                        e.printStackTrace();

                    }
                    t1.interrupt();

                }

            }

        };
        t1.start();
        t2.start();

    }

}
