import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class MyProgramTest {
    @Test
    public void testMyProgram() {
        // specify inputs
        int x = 5;
        int y = 10;

        // specify expected output
        int expected = 15;

        // run program and check output
        MyProgram program = new MyProgram();
        int result = program.add(x, y);
        assertEquals(expected, result);
    }
}
