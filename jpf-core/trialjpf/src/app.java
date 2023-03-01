public class app {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java Adder <a> <b>");
            System.exit(1);
        }
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int sum = a + b;
        System.out.println(a + " + " + b + " = " + sum);
    }
}    
