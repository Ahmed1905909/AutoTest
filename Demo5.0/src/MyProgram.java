
public class MyProgram {
    @JDartSymbolic("x")
    @JDartSymbolic("y")
    public int add(@JDartPrecondition("x >= 0") int x, @JDartPrecondition("y >= 0") int y) {
        return x + y;
    }
}
