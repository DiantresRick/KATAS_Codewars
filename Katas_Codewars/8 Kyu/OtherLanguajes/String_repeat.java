//  Write a function called repeatStr which repeats the given string string exactly n times.
import org.JUnit.*;

public class String_Repeat{
    
    public static String repeatStr(final int repeat, final String string) {
      int i = 0;
      String g="";
      
      while(i<repeat){
       g = g+string;
        i++;
        }
      return g;
    }
  }
  




    
    // assert(repeatStr(3, "*")== "***");
    // assert(repeatStr(5, "#")== "#####");
    // assert(repeatStr(2, "ha ")== "ha ha ");

