import java.util.*;
import java.lang.Comparable;


public class EqualsTest {

    public static void main(String[] args) {
        // 新建2个相同内容的Person对象，
        // 再用equals比较它们是否相等
        Person p1 = new Person("eee", 100);
        Person p2 = new Person("eee", 100);
        System.out.printf("p1.equals(p2) : %s\n", p1.equals(p2));
        System.out.printf("p1==p2 : %s\n", p1 == p2);
    }


    private static class Person {
        int age;
        String name;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String toString() {
            return name + " - " + age;
        }

        /**
         * @desc 覆盖equals方法
         */
        @Override
        public boolean equals(Object obj) {
            if(obj == null) {
                return false;
            }

            //如果是同一个对象返回true，反之返回false
            if(this == obj) {
                return true;
            }

            //判断是否类型相同
            if(this.getClass() != obj.getClass()) {
                return false;
            }

            Person person = (Person)obj;
            return name.equals(person.name) && age == person.age;
        }
    }
}
