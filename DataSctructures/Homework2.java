import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Homework2 {
    public static void main(String [] args){

        String filename="chest";
        String extention=".txt";
        String [] files=new String [10]; // array of files

        // load the file names into the array

        for (int i=0; i<files.length;i++ ){
            files[i]=filename+i+extention;
        }

        // check files that are packed as polyndromes and print their names
        try{
            System.out.println("Files packed as polyndromes");
            System.lineSeparator();
            System.out.println("-------------------------------------------------------------------------------------------------------\n");
            for (int i=0; i<files.length;i++ ){
                HaversackOfHolding stack= loadStack(files[i]);
                 BandolierOfConvenience Queue=loadQueue(files[i]);
                if(isPolyndrome(stack, Queue)){
                    System.out.print("\n"+ files[i]);
                }
            }

        }
        catch(FileNotFoundException ex){
            System.err.print("the chest file  does not exist");
        }

    }
    public static HaversackOfHolding loadStack(String filename)throws FileNotFoundException{
        /*This method adds element into the stack */

        HaversackOfHolding words=new  HaversackOfHolding (); // stack to add in the strings
        File chest=new File(filename); // file name
        if(!chest.exists()){
            throw new FileNotFoundException(); // throw exception if the file does not exist
        }
        Scanner input=new Scanner(chest); // open the file
        while(input.hasNextLine()){
            String word=input.nextLine(); // loading the strings
            words.stow(word);
        }
        input.close(); // closing the file
        return words;
    }
    public static BandolierOfConvenience loadQueue(String filename)throws FileNotFoundException{
        /*This method adds adds element to the queue */
        BandolierOfConvenience words=new BandolierOfConvenience(); // Queur to add in the strings
        File chest=new File(filename); // file name
        if(!chest.exists()){
            throw new FileNotFoundException(); // throw exception if the file does not exist
        }
        Scanner input=new Scanner(chest); // open the file
        while(input.hasNextLine()){
            String word=input.nextLine(); // loading the strings
            words.stow(word);
        }
        input.close(); // closing the file
        return words;
    }
    public static boolean isPolyndrome(HaversackOfHolding stack,BandolierOfConvenience queue){
        /* This method return true if the data is packed as polyndrome and false otherwise*/

        while(!stack.isEmpty()){
            if(stack.use().compareTo(queue.use())!=0){
                return false;
            }
        }
        return true;
    }
    
}
