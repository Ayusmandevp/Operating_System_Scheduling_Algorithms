5. Write a Java program to implement Stack operations 
 
import java.io.*; 
import java.util.*; 
  class Stack  
    { 
      Scanner sc =new Scanner(System.in); 
  int s[]=new int[5]; 
  int top; 
  Stack() 
  { 
   top=-1; 
  } 
  public void push() 
  { 
   int item ; 
   if (top==s.length-1) 
   { 
    System.out.println("Stack is Full\n"); 
    return; 
   } 
   top++; 
   try 
   { 
   System.out.println("Enter Item\n"); 
   item=sc.nextInt(); 
   s[top]=item; 
   } 
   catch(Exception e) 
   { 
   } 
  } 
  public void pop() throws Exception 
  { 
   int item; 
   if (top==-1) 
   { 
    System.out.println("Stack is Empty\n");return; 
   } 
   item=s[top]; 
   top--; 
   System.out.println(item +"popped out of stack\n"); 
  } 
9 
 
 
 
  
       public void display() 
        { 
   if (top==-1) 
   { 
    System.out.println("Stack is empty\n"); 
    return; 
   } 
   System.out.println("stack in LIFO\n"); 
   for(int i=top;i>=0;i--) 
          System.out.println(s[i]); 
         
          } 
 } 
 
 class StackTest 
  { 
 public static void main(String args[]) throws Exception 
 { 
  Scanner sc =new Scanner(System.in); 
  Stack s=new Stack(); 
  int opt; 
  do 
  { 
   System.out.println("1.push"); 
   System.out.println("2.pop");    
   System.out.println("3.display"); 
   System.out.println("4.quit"); 
   System.out.println("Enter Ur Option"); 
   opt=sc.nextInt(); 
   switch (opt) 
   { 
    case 1: 
          s.push(); 
          break; 
   case 2: 
         s.pop(); 
         break; 
   case 3: 
          s.display(); 
        break; 
10 
 
   case 4: 
    System.out.println("Program is over\n"); 
    break; 
   default: 
                                System.out.println("Invalid Option"); 
   } 
  }while(opt!=4); 
 } 
} 
 
 
 
 
 
