import java.util.*;

public class SnchronizedList {
    /**
     * 创建一个列表，一个线程进行写入，一个线程读取 iterator 和 listIterator 方法返回的迭代器是快速失败的
     */
    public void readWrite() {

        List<Integer> synNums = Collections.synchronizedList(new ArrayList<Integer>());

        //启动写入线程
        new WriteListThread(synNums).start();

        new ReadListThread(synNums).start();

        //启动删除线程
        new DeleteListThread(synNums).start();
    }

    public static void main(String[] args) {
        new SnchronizedList().readWrite();
    }
}

class WriteListThread extends Thread {
    private List<Integer> nums;

    public WriteListThread(List<Integer> nums) {
        super("WriteListThread");
        this.nums = nums;
    }

    // 不停写入元素1
    public void run() {
        while (true) {
            try {
                nums.add(new Random().nextInt(1000));
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName());
            } catch(Exception e) {
                continue;
            }
        }
    }
}

class DeleteListThread extends Thread {
    private List<Integer> nums;

    public DeleteListThread(List<Integer> nums) {
        super("DeleteListThread");
        this.nums = nums;
    }

    // 删除第一个元素
    public void run() {
        while (true) {
            try {
                System.out.println(Thread.currentThread().getName() + ":" + nums.remove(0));
                Thread.sleep(1000);
            } catch(Exception e) {
                continue ;
            }
        }
    }
}

class ReadListThread extends Thread {
    private List<Integer> nums;

    public ReadListThread(List<Integer> nums) {
        super("ReadListThread");
        this.nums = nums;
    }

    // 不停读取元素,非原子操作，则需要手动加上锁
    public void run() {
        while (true) {
            //休眠，将锁交给其他线程
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e1) {
                e1.printStackTrace();
            }
            synchronized (nums) {
                if (nums.size() > 100) {
                    Iterator<Integer> iter = nums.iterator();
                    while (iter.hasNext()) {
                        System.out.println(Thread.currentThread().getName() + ":" + iter.next());
                    }
                } else {
                    try {
                        nums.wait(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
