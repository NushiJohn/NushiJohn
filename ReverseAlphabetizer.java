import java.util.Scanner;

public class ReverseAlphabetizer {

  public static void main (String[] args) {

    // We will use the Scanner class (yay!) to read
    // input from the user while running the class.

    System.out.println("Enter a string to split into words and alphabetize:");
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();

    // Split the string on space (\\s+) into an array of words
    // to create an array of Strings (words) to alphabetize.
    String[] words = s.split("\\s+");


    // Create two StackLL objects: mainstack and tempstack.
    //MainStack = new StackLL();
    //TempStack = new StackLL();

    // Algorithm
    String w;
    String current;
    //initalizing the variables before working
    //with them in the for loop

   /*for (Node n = top; n != null; n = n.next) {
      while (isEmpty == true){
        MainStack.push(current);
        MainStack.peek (current);
      }
    }
    while (compareToIgnoreCase ((w current) -> 0)){
      MainStack.pop (current);
      TempStack.push (current);
      MainStack.push(w);
    }
  }
}
//the for loop is supposed to look through the linked list,
//while the first while loop checks if the main stack is empty before working on it,
//and the second while loop is supposed to compare the two strings in the two stacks,
//however, the compareToIgnoreCase method gives me illegal start of type errors
*/


// (Remember that you cannot peek() or pop() an empty stack! Be sure
// to write code that will handle an empty stack.)


/* Write a for-loop to go through each word in the
array of words[] from the input string. For each word w in words[]:


* peek() at the top word of mainstack. Let's call it current.

* While current comes after w in the alphabet, pop() current off the
mainstack and push() it on to tempstack.

* Reset current to whatever peek() now returns.

* When current finally is a word that comes before w in the alphabet,
push() w onto mainstack.

* Then pop() each element off of tempstack and push() onto mainstack.

Using your for loop, apply the above process to the next word in the
array of words to sort until you have sorted the whole array of words.

When you are done, you should have a sorted stack of words
in mainstack, ordered reverse alphabetically top to bottom "from z to a".
In other words, the bottom of the stack should have words closer to the
beginning of the alpphabet, and the top should have words closer to
the end of the alphabet.

The stack tempstack should be empty.

Print out the original String. Then use toString() to print out the
reverse-sorted stack to prove that your code works correctly.
*/



}



}
