import java.util.Scanner;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
//import com.github.javaparser.ast.type.Type;
import com.microsoft.z3.*;

public class FunctionExtractor{

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the Java source code:\n");
        String sourceCode = scanner.useDelimiter("\\Z").next();
        fun(sourceCode);
    }







    public static void fun(String source)
    {
         // read the whole input as a string
        String intConstraintWithVar = "(declare-const intVar Int)\n\n" + "(assert (and (<= 99 intVar) (<= intVar 100)))\n";
        String strConstraintWithVar = "(declare-const stringVar String)\n" + "(assert (and (<= 9 (str.len stringVar)) (<= (str.len stringVar) 10)))\n";
        // Parse the Java source code
        CompilationUnit cu = StaticJavaParser.parse(source);

        // Visit each method declaration in the source code
        cu.accept(new VoidVisitorAdapter<Object>() {
            // @Override
            // public void visit(MethodDeclaration method, Object arg) {
            //     super.visit(method, arg);
            //     String methodName = String.valueOf(method.getName());
            //     System.out.println("Method name: " + methodName);
            //     String methodPar = String.valueOf(method.getParameters());
            //     System.out.println("Method parameters: " + methodPar);
            //     String methodtype = String.valueOf(method.getType());
            //     System.out.println("Method return type: " + methodtype);
            //     String type = "Null"; 
            //     for (Parameter parameter : method.getParameters()) {
            //          type = String.valueOf(parameter.getType());
            //         System.out.println("Parameter type: " + type);
            //         if(type=="String") {
            //             //Z3TestDataGenerator.generateStringTestData(type);
            //         }
            //         else if (type=="int") {
            //             generateIntegerTestData(intConstraintWithVar);
            //         }
            //     }
            //     if (type=="int"){
            //         generateIntegerTestData(intConstraintWithVar);
            //     }
            //     else if (type=="String") {
            //         //generateIntegerTestData(intConstraintWithVar);
            //     }
            // }


            public void visit(MethodDeclaration method, Object arg) {
                super.visit(method, arg);
                String methodName = String.valueOf(method.getName());
                System.out.println("Method name: " + methodName);
                String methodPar = String.valueOf(method.getParameters());
                System.out.println("Method parameters: " + methodPar);
                String methodtype = String.valueOf(method.getType());
                System.out.println("Method return type: " + methodtype);
                for (Parameter parameter : method.getParameters()) {
                    String type = String.valueOf(parameter.getType());
                    System.out.println("Parameter type: " + type);
                    
                    if (type.equals("int")) {
                        generateIntegerTestData(intConstraintWithVar);
                    } else if (type.equals("String")) {
                        generateStringTestData(strConstraintWithVar);
                    }
                }
            }
        }, null);
    }

    public static void generateIntegerTestData(String constraint) {
        Context ctx = new Context();
        Solver solver = ctx.mkSolver();

        Sort intSort = ctx.mkIntSort();
        Expr intVar = ctx.mkConst("intVar", intSort);

        BoolExpr[] exprs = ctx.parseSMTLIB2String(constraint, null, null, null, null);
        solver.add(exprs);


        while (solver.check() == Status.SATISFIABLE) {
            Model model = solver.getModel();
            Expr intVal = model.eval(intVar, true);
            int testData = ((IntNum) intVal).getInt();
            System.out.println("Generated test data: " + testData);

            BoolExpr newConstraint = ctx.mkNot(ctx.mkEq(intVar, intVal));
            solver.add(newConstraint);
        }

        ctx.close();
    }

    public static void generateStringTestData(String constraint) {
        Context ctx = new Context();
        Solver solver = ctx.mkSolver();

        Sort stringSort = ctx.mkStringSort();
        Expr stringVar = ctx.mkConst("stringVar", stringSort);

        BoolExpr[] exprs = ctx.parseSMTLIB2String(constraint, null, null, null, null);
        solver.add(exprs);


        while (solver.check() == Status.SATISFIABLE) {
            Model model = solver.getModel();
            Expr stringVal = model.eval(stringVar, true);
            String testData = stringVal.toString().replaceAll("\"", "");
            System.out.println("Generated test data: " + testData);

            BoolExpr newConstraint = ctx.mkNot(ctx.mkEq(stringVar, stringVal));
            solver.add(newConstraint);
        }

        ctx.close();
    }


}
