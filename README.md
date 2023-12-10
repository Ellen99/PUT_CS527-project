# PUT_CS527-project
This repository presents the work done in the scope of CS527 course project.
____________________
There are several scripts and components in the repository. Here is what each of them are:
- `find_puts_in_repo.py` is a script to identify parameterized unit tests in the Apache Hadoop repository. It analyzes a Java codebase, identified by the specified GitHub repository URL (in this case, the Apache Hadoop repository), to find and extract information about parameterized tests. The script uses regular expressions to identify test methods and their associated packages, saving the results in a CSV file. The final output includes the project URL, module path, and fully-qualified test names, providing a convenient summary of parameterized tests within the repository.
- `run_puts.py` - this Python script executes Maven test commands for parameterized tests identified in the 'hadoop_parameterized_tests.csv' file. For each test, it dynamically constructs a Maven command, runs it using the subprocess module, and logs the output to individual files within a timestamped folder ('hadoop_puts_logs_{current_datetime}/'). The script provides a detailed log of each test execution, facilitating easy tracking and analysis of the testing process.
- `get_coverage_Cartesian.py` - this Python script analyzes coverage data and test execution results for parameterized tests in the Apache Hadoop project. It uses Jacoco coverage reports and Maven test commands to assess the test coverage and behavior of parameterized tests. The script dynamically modifies the test files for running Cartesian products of parameterized tests and logs the results, producing a detailed CSV file ('put_data.csv') that includes various metrics such as coverage changes, test pass/fail outcomes, and the number of parameter combinations. The script also handles potential exceptions during execution and prints relevant information. 

- `Parameterized runner component`, which runs the parameterized unit tests with the cartesian product set of initially provided values in order to achieve higher coverage. The Parameterized Java class extends the original org.junit.runners.Parameterized class to enhance parameterized unit testing capabilities. The modifications enable the execution of tests with Cartesian product sets of initial parameter values. The code incorporates features such as logging for informative output and the ability to generate unique combinations of parameters, providing a versatile tool for parameterized testing in Java applications.

 
     In order to use Parameterized Cartesian runner for your tests,
     - add the following into the root pom file of your project 
  
  ```
    <dependency>
         <groupId>edu.illinois</groupId>
         <artifactId>Parameterized</artifactId>
         <version>1.0-SNAPSHOT</version>
         <scope>compile</scope>
   </dependency>
   ```
  
    - and `import edu.illinois.Parameterized;` into the test java file.

 

