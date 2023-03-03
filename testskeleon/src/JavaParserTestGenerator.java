import java.io.File;
import java.io.FileInputStream;
import java.util.Scanner;


import org.junit.jupiter.api.Test;
//import org.junit.jupiter.api.Assertions;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.github.javaparser.StaticJavaParser;


import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class JavaParserTestGenerator {

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the file path: ");
        String filePath = scanner.nextLine();
        File file = new File(filePath);
        FileInputStream inputStream = new FileInputStream(file);
        CompilationUnit compilationUnit = StaticJavaParser.parse(inputStream);
        TestMethodVisitor visitor = new TestMethodVisitor();
        visitor.visit(compilationUnit, null);
        Class<?> testClass = visitor.getTestClass();
        if (testClass != null) {
            Result result = JUnitCore.runClasses(testClass);
            for (Failure failure : result.getFailures()) {
                System.out.println(failure.toString());
            }
            System.out.println("Test run finished with result: " + result.wasSuccessful());
        }
    }

    private static class TestMethodVisitor extends VoidVisitorAdapter<Void> {
        private Class<?> testClass = null;

        @Override
        public void visit(MethodDeclaration md, Void arg) {
            //Test testAnnotation = md.getAnnotation(Test.class);
            //if (testAnnotation != null) {
                if (testClass == null) {
                    testClass = createTestClass();
                }
                createTestMethod(md);
            }


        public Class<?> getTestClass() {
            return testClass;
        }

        private Class<?> createTestClass() {
            return org.junit.jupiter.api.Assertions.class;
        }

        private void createTestMethod(MethodDeclaration md) {
            String methodName = md.getNameAsString();
            TestMethodGenerator.generateTestMethod(testClass, methodName);
        }
    }

    private static class TestMethodGenerator {
        public static void generateTestMethod(Class<?> testClass, String methodName) {
            String testMethodName = "test" + methodName.substring(0, 1).toUpperCase() + methodName.substring(1);
            String methodBody = "// TODO: Write test code here\n";
            String testMethod = "@Test\n" +
                    "public void " + testMethodName + "() {\n" +
                    methodBody +
                    "}\n";
            System.out.println(testMethod);
        }
    }
}
