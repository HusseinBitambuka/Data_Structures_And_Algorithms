import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Homework1 {
    public static void main(String[] args){ 

        String magicien="magicien.txt"; // name of the file

        try{
            // Buble sort test
            System.err.print("\n"+"-------------------------------------------------------------------------"+System.lineSeparator());
            ArrayList<String>bubletest=loadingArrayList(magicien);
            long start= System.currentTimeMillis();
            long critical_operation=BeltOfUtility.bubleSort(bubletest);
            long bubleSortTime=System.currentTimeMillis()-start;
            System.err.println("\n"+"Buble Sort: Critical operation= "+critical_operation+" and time elapsed is "+bubleSortTime+ "ms");
            System.err.print("\n"+"-------------------------------------------------------------------------"+System.lineSeparator());
            
            // Merge sort test
            ArrayList<String>mergetest=loadingArrayList(magicien);
            long start1= System.currentTimeMillis();
            long critical_operation1=BeltOfUtility.MergeSort(mergetest);
            long mergeSortTime=System.currentTimeMillis()-start1;
            System.err.println("\n"+"Modified Merge Sort: Critical operation= "+critical_operation1+" and time elapsed is "+mergeSortTime+ "ms");
            System.err.print("\n"+"-------------------------------------------------------------------------"+System.lineSeparator());

            // Quick Sort test
            ArrayList<String>quicktest=loadingArrayList(magicien);
            long start2= System.currentTimeMillis();
            long critical_operation2=BeltOfUtility.QuickSort(quicktest);
            long quickSortTime=System.currentTimeMillis()-start2;
            System.err.println("\n"+"Quick Sort: Critical operation= "+critical_operation2+" and time elapsed is "+quickSortTime+ "ms");
            System.err.print("\n"+"-------------------------------------------------------------------------"+System.lineSeparator());

            // Selection Sort test
            ArrayList<String>selectiontest=loadingArrayList(magicien);
            long start3= System.currentTimeMillis();
            long critical_operation3=BeltOfUtility.selectionSort(selectiontest);
            long selectionSortTime=System.currentTimeMillis()-start3;
            System.err.println("\n"+"Selection Sort: Critical operation= "+critical_operation3+" and time elapsed is "+selectionSortTime+ "ms");
            System.err.print("\n"+"-------------------------------------------------------------------------"+System.lineSeparator());

            
        }
        catch(FileNotFoundException ex){
            System.err.print("the magicient.txt does not exist");
        }   
    }
    // File handling method
    public static ArrayList<String>loadingArrayList(String filename)throws FileNotFoundException{
        ArrayList<String>words=new ArrayList<>(); // array to add in the strings
        File magicien=new File(filename); // file name
        if(!magicien.exists()){
            throw new FileNotFoundException(); // throw exception if the file does not exist
        }
        Scanner input=new Scanner(magicien); // open the file
        while(input.hasNextLine()){
            String word=input.nextLine(); // loading the strings
            words.add(word);
        }
        input.close(); // closing the file
        return words;
    }
}
