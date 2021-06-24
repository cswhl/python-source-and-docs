import java.util.*;

public class EnumTest {
    public static void main(String[] args) {
        EnumTest ee = new EnumTest();
        EnumTest.TrafficLight tt =  ee.new TrafficLight();
        tt.change();
    }

    enum Signal {
        GREEN, RED, YELLOW;
    }

    class TrafficLight {
        Signal color = Signal.RED;

        public void change() {
            switch (color) {
                case RED:
                    color = Signal.GREEN;
                    break;
                case YELLOW:
                    color = Signal.RED;
                    break;
                case GREEN:
                    color = Signal.YELLOW;
                    break;
            }
            System.out.println(color);
        }
    }
}
