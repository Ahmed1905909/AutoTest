import com.sun.codemodel.JCodeModel;
import com.sun.codemodel.JDefinedClass;
import com.sun.codemodel.JMethod;
import com.sun.codemodel.JMod;
import org.junit.Test;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.OutputStream;


import static org.junit.Assert.assertEquals;

public class MyTestGenerator {

    public static void main(String[] args) throws Exception {
        // Create a new JCodeModel instance
        JCodeModel codeModel = new JCodeModel();

        // Create a new JDefinedClass for the test class
        JDefinedClass testClass = codeModel._class("com.example.MyTest");

        // Create a new JMethod for the test case
        JMethod testMethod = testClass.method(JMod.PUBLIC, void.class, "testAdd");

        // Add the @Test annotation to the test method
        testMethod.annotate(Test.class);

        // Generate the test cases
        testMethod.body().directStatement("assertEquals(5, add(2, 3));");
        testMethod.body().directStatement("assertEquals(-1, add(-4, 3));");
        testMethod.body().directStatement("assertEquals(-6, add(-2, -4));");



        // Generate the add method
        JMethod addMethod = testClass.method(JMod.PRIVATE, int.class, "add");
        addMethod.param(int.class, "a");
        addMethod.param(int.class, "b");
        addMethod.param(codeModel.INT, "a");
        addMethod.param(codeModel.INT, "b");

        // Print the generated code
        File outputFile = new File("MyTestClass.java");
        FileWriter writer = new FileWriter(outputFile);
        String code = codeModel.build();
        writer.write(code);
        writer.close();




    }
}
