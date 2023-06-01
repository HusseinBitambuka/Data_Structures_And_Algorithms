import java.util.ArrayList;
public class BeltOfUtility {
    //modified mergeSort.
    //------------------------------------------------------------------------------------------------
    public static int MergeSort(ArrayList<String> A){
        /* This method is a modified version of merge sort algorithm.
         For input larger than a thousand, this method implements the regular merge sort to sort data,
         and for input smaller than a thousand, it implements insertion sort. It returns the number of critical operation.
         */
        if (A.size()>1000){ // C1*1
            final int START=0; // C2* tz where tz belongs {0,1}
            int r=A.size(); // C3* tz where tz belongs {0,1}
            int critical_operation1=mergeSort(A, START, r); // C4* tz where tz belongs {0,1}
            return critical_operation1;
        }
        return insertionSort(A); // C5* tz where tz belongs {0,1}
        
    }
    
    public static int mergeSort(ArrayList<String> A, int p,int r){
        /* This is the actual merge sort method. The merge sort method sorts data by implementing the divide-and-conquer paradigm.
        The divide step consists of  divide the data  into two.
        The conquer step consits of recusrively sorts the two subcontainers divided in the divide step
        The combine step consits of refilling our data container by inserting the least element of the two subcontainers
        This method returns the number of critical operation.
         */
        // check if we have reached the base case.
        if (r-p>1){ // C1*1

            //  halve the data

            int q=(r+p)/2; // // C2* tz where tz belongs {0,1}
            
            // conquer step
            mergeSort(A, p, q); // C3* tz where tz belongs {0,1}
            mergeSort(A, q, r);// C4* tz where tz belongs {0,1}

            // combine step
            int critical_operation=merge(A, p, q, r); // C5*  tz where tz belongs {0,1}

            // critical operation

            return critical_operation; 
        }
        return 0;
    }
    public static int merge(ArrayList<String> A,int p, int q, int r){
        /*This method implements the combine step of merge sort. it returns the number of critical operation */

        // critical operation
        int critical_operation=0;
        // halve the array
        int n1=q-p; // C1*1
        int n2=r-q; // C2*1

        // cop the data in  two new arrays

        String []left=new String[n1]; //C3*1
        String []right=new String[n2]; // C4*1
        for (int i=0; i<n1; i++){ // C5*n1
            left[i]=A.get(i+p); // C6*(n1-1)
        }

         for (int j=0; j<n2; j++){ // C7*n2
            right[j]=A.get(j+q); // C8*(n2-1)
        }
        
        // compare the elements in the two new arrays, and refill the the main array with the least of the two element
        int i=0,j=0; // C9*1
        int k=p; //C10*1
        while(i<n1 && j<n2){ // C11*k. K is the least number between n1 and n2
            if(left[i].compareTo(right[j])<=0){ // C12*(k-1)

                // fill the least element in the input array

                critical_operation++; // critical operation incrementation
                String value1=left[i]; // C13* (k-1)*sum tk where tk belongs {0.1}
                A.set(k, value1);      // C14* (k-1)* sum tk where tk belongs {0.1}
                i++;                    // C15* (k-1)* sum tk where tk belongs {0.1}
            }
            else{
                critical_operation++; // Critical operation incrementation
                String value2=right[j]; // C16* (k-1)* sum tk where tk belongs {0.1}
                A.set(k, value2);  // C17* (k-1)* Sum tk where tk belongs {0.1}
                j++;               // C18* (k-1)* Sum tk where tk belongs {0.1}
            }

            // increment the value of the position in the input array to fill out other element
            k++;    // C19* (k-1)
        }

        // refilling the remainig element in the input array

        while(i<n1){  // C20*K1. k1= n-k
            critical_operation++; // critical operation incrementation
            String value4=left[i]; // C21* (k1-1)
            A.set(k, value4);      // C22* (k1-1)
            i++;                   // C23* (k1-1)
            k++;                   // C24* (k1-1)
        }
        while(j<n2){             // C25*K1
            critical_operation++; // critical operation incrementation
            String value5=right[j]; // C26* (k1-1)
            A.set(k, value5);       // C27* (k1-1)
            j++;                    // C28* (k1-1)
            k++;                    // C29* (k1-1)

        }

        // return the critical operation

        return critical_operation;
    }

    // Insertion Sort
    //-------------------------------------------------------------------------------------------------
    public static int insertionSort(ArrayList<String> A){
        /* This method sorts the input data by picking an element in the data
         and compares it with every element in the input data. if the compared element is greater than
         the comparing element, the compared and the comparing element swap positions. 
         it also returns critical operation.
         */

        int critical_operation=0;         // ciritical operation

        // compare every element in the data input with the comparing element(the key) and swap it with that element if that element is greater.

        for (int j=1; j<A.size(); j++){   // C1*n
            String key=A.get(j);          // C2*(n-1)
            int i=j-1;                    // C3*(n-1)
            while(i>=0 && A.get(i).compareTo(key)>0){ // C4 *k with sum[0...n] if the value of A[i]> key
            critical_operation++;                       // critical operation
                String k=A.get(i);                      // C5*(k-1)
                A.set(i+1, k);                          // C6*(k-1)
                i--;                                    // C7*(k-1)
            }
             
            String z=key;                               // C8*(n-1)
            A.set(i+1, z);                              // C9*(n-1)
        }
        return critical_operation;

    
    }
    /*
     Analysis
     --------------------------------------------------------------------------------------------------
     Merge (combine)
----------------
Since the it executes one of the two while loops, I am going to count one of the two.

C(n)=C1*1+C2*1+C3*1+C4*1+C5*n1+C6*(n1-1)+C7*n2+C8*(n2-1)+C9*1+C10*1+C11*k+C12*(k-1)+C13*(k-1)* Sum tk
+C14*(k-1)*Sum tk+C15* (k-1)*Sum tk+C16* (k-1)*Sum tk+C16* (k-1)*Sum tk+C17* (k-1)*Sum tk+C18*(k-1)*Sum tk+C19*(k-1)
+C20*K1+C22* (k1-1)+C21*(k1-1)+C22* (k1-1)+C23* (k1-1)+C24* (k1-1)

C(n)=C1*1+C2*1+C3*1+C4*1+C5*n1+C6*n1-C6+C7*n2+C8*n2-C81+C9*1+C10*1+C11*k+C12*k-C12+(C13*k-C13*1) sum tk
	+(C14*k-C14*1) sum tk++(C15*k-C15*1) sum tk+(C16*k-C16*1) sum tk+(C17*k-C17*1) sum tk +(C18*k-C18*1) sum tk+(C19*k-C19*1) sum tk
	C20k1+(C21*k1-C21*1)+(C22*k1-C22*1)+(C23*k1-C23*1)+(C24*k1-C24*1)

putting all the constant and the term n terms and k and k1 terms together, we realize sum tk+k1=n.

Then C(n) is linear function of form: A(n)+B which means that C(n)=Theta(n)

Merge Sort
-----------------
input>1000
---------------
T(n)=C1*1+C2*tz+2T(n/2)tz+C(n)tz

Tn(n){1 (best case)
	2T(n/2)+Theta(n)+ C1+C2
By applying the master algorith, we see that 

T(n)=Theta(nlogn).

input<=1000 (insertion sort)
----------------------------
T(n)=C1n+C2*(n-1)+C3(n-1)+C4K+C5(K-1)+C6(K-1)+C7(K-1)+C8*(n-1)+C9*(n-1)
    =

note that k=sum[0..n]=(n(n+1))/2

Best case: when the term with k=0
		
		T(n) has the form of A(n)+B, which is Theta(n)
Worst case:
		T(n) has the form of A(n^2)+Bn+C, which is Theta(n^2)
Avarage case:

		T(n) has the form of A(n^2)+Bn+C, which is Theta(n^2)
     */



    // Buble Sort
    //--------------------------------------------------------------------------------------------------
    public static long bubleSort(ArrayList<String> A){ 
        long critical_operation=0;
        for(int i=0; i<A.size()-1;i++){ //C1*n
            
            for(int j=A.size()-1; j>i;j--){ //C2*k1
                if(A.get(j).compareTo(A.get(j-1))<0){ //c3*k2
                    // swaping the two element
                    critical_operation++; // increment the critical operation
                    String temp1=A.get(j); // c4*k2*tz  with tz belongs {0,1}
                    String temp2=A.get(j-1); // c5*k2*tz with  tz belongs{0,1}
                    A.set(j, temp2); // c6*k2*tz  with tz belongs{0,1}
                    A.set(j-1, temp1); // c7*k2*tz,  with tz belongs {0,1}
                }
            }
        }
        return critical_operation;
    }
    /*
    Analysis

     T(n)=C1*n+C2*k1+C3*k2+C4*k2*tz+C5*k2*tz*tz+C6*k2*tz+C7*k2*tz

it is reasonable to assume that :
K1 =sum[0..n-2]=1/2(n(n-1)-2)=1/2(n^2-n-2)
k2=sum[0...n-3]=1/2((n-2)(n+1))=1/2(n^2-3n-2)
and C4=C5=C6=C7

=> T(n)=C1*n+C2*1/2(n^2-n-2)+C3*1/2(n^2-3n-2)+2C4*(n^2-3n-2)*tz
Best case: tz=0

		T(n)=C1*n+C2*1/2(n^2-n-2)+C3*1/2(n^2-3n-2)
			=n^2/2(C2+C3)+n(1/2*C2+C1+4C3)+C3+C2
			=An^2+Bn+C
			=Theta(n^2)
Worst case: tz=1

		T(n)=C1*n+C2*1/2(n^2-n-2)+C3*1/2(n^2-3n-2)+2C4*(n^2-3n-2)
			=n^2/2(C1+C23+4C4)+n(1/2*C2+C1+4C3-6C4)+C3+C2-4C4
			=An^2+Bn+C
			=Theta(n^2)
			

Average case: tz=1 for half of the tz

		T(n)=C1*n+C2*1/2(n^2-n-2)+C3*1/2(n^2-3n-2)+C4*(n^2-3n-2)
			=n^2/2(C1+C23+2C4)+n(1/2*C2+C1+4C3-3C4)+C3+C2-2C4
			=An^2+Bn+C
			=Theta(n^2)
     */


   // Quick Sort
//----------------------------------------------------------------------------------------------------
public static int QuickSort(ArrayList<String> A){
    /*This is a helper method of the actual Quick sort
     that is found below. This method helps remove the absatraction
     by allowing the user to only input an array. It also return the number of critical operation
     */
    final int START=0; //  starting point
    int r=A.size(); // length of the data
    int critical_operation=quickSort(A, START, r); // quicksort method that returns the number of critical operation
    return critical_operation; // 
}
public static int quickSort(ArrayList<String>A, int p, int r){
    /* This is the actual Quick Sort method.if the data is already sorted, the method 
    returns zero. if the data is not sorted,
     this method has two part:
     the first part is the partitioning part that partition the data in two.
     the second part is the recursion part that repetes the calling of the Quick Sort method
     until it reaches the base case.
     */
    if(p-r<0){ // C1*
        // the partioning method. it returns two elements: the critical operation and the pivot.
        int [] return_values=partitioning(A, p, r); //C2* tz with tz {0,1}
        // the pivot for partitioning
        int q=return_values[1]; // C3* tz with tz {0,1}
        quickSort(A, p, q); // C4* tz with tz {0,1}
        quickSort(A, q+1, r); // C5* tz with tz {0,1}
        return return_values[0]; // C6* tz with tz {0,1}
    }
    return 0; // C1*1
}
/*
 Analysis
 -----------------------------------------------------------------------------------
 Quick Sort
----------------

Partitioning
----------------------------------------------

P(n)=C1+C2+C3(n-1)+C4(n-2)tj+C5(n-2)tj+C6(n-2)tj+C7(n-2)tj+C8(n-2)tj+C9(n-2)tj+C10+C11+C12

	(C1+C2+C10+C11+C12-2C4)+C4n+(C5+C6+C7+C8+C9)(n-2)tj

	best case: tj=0

	P(n) has a form of A(n)+B which Theta(n)

	Worst case: tj=1
	
	P(n) has the form of A(n)+B which Theta(n)


Quicksort
-----------------------------------------

T(n)= C1+P(n)tz+T(k)+T(n-K-1)


The best case: k=n-k-1

	T(n)=2T(k/2)+Theta(n)+C1. By applying the master algorithm, T(n)=Thetha(nlogn)

Worst case: k !=n-k-1

	
	T(n)= C1+P(n)tz+T(k)+T(n-K-1) which gives us T(n)=Thetha(n^2)

 */
public static int [] partitioning(ArrayList<String> A, int p, int r){
    /*This is the partitioning method. It divides the input 
     such that every element before the pivot is less the pivot
     and every element after the pivot is greater than the pivot.
     This method returns the number of execution of the critical operation. I do not 
     count the cost of the critical operation
     */

    int critical_operation=0; // critical operation
    String x=A.get(r-1); //C1*1
    int i=p-1; //C2*1
    for (int j=p; j<r-1;j++){ //C3*(n-1)
        if(A.get(j).compareTo(x)<=0){ //C4*(n-2)
            critical_operation++; //  increment the critical operation
            i++;                 // C5(n-2)*tj belongs to {0,1}

            //swaping the element at i with the element at j

            String k=A.get(i);   // C6(n-2)*tj belongs to {0,1}
            String z=A.get(j);   // C7(n-2)*tj belongs to {0,1}
            A.set(j,k);          // C8(n-2)*tj belongs to {0,1}
            A.set(i,z);         // C9(n-2)*tj belongs to {0,1}
        }
    }

    // swaping the element at i+1 with the last element

    String value1=A.get(r-1); // C10*1
    String value2=A.get(i+1); // C11*1
    A.set(i+1,value1);        // C12*1
    A.set(r-1,value2);        // C13*1

    // return the time of execution of the critical operation and the pivot=i+1

    int [] return_values={critical_operation, i+1};
    
    return return_values;
}

     //Selection Sort
     //--------------------------------------------------------------------------------------------
     public static long selectionSort(ArrayList<String> A){
        /*This algorithm sorts elements in an array by first picking the smallest element and places it at the first spot 
         * I am not going to count in the new variable critical_operation to count the number of times my program
         * enters the if-statement
        */
        long critical_operation=0; 
        for (int i=0; i<A.size()-1;i++){ // C1*n 
            int Smallest=0; // C2*(n-1)
            for(int j=i+1; j<A.size();j++){ //C3*k
                if(A.get(j).compareTo(A.get(Smallest))<0){ // C4*(k-1)
                    critical_operation++; // increment the critical operation
                    Smallest=j; //C5*(k-2)*tk where belongs {0,1}
                }
            }
            // swaping the smallest element with the ith element in the array
            String temp1=A.get(i); // C6*(n-1)
            String temp2=A.get(Smallest); // C7*(n-1)
            A.set(i, temp2); // C8*(n-1)
            A.set(Smallest, temp1); // C9*(n-1)
        }
        return critical_operation;
        }   
}
/*
 T(n)=C1*n+C2*(n-1)+C3*k+C4*(k-1)+C5*(k-2)*tk+C6*(n-1)+C7*(n-1)+C8*(n-1)+C9*(n-1)

 let's assume that:
  C9, C8, C7, C6, and C2 are equal
  k=sum[1..n-1]=1/2(n(n+1))-1=n^2+n+1

  => T(n)= C1*n+5C2(n-1)+C3(n^2+n+1)+C4(n^2+n)+C5(n^2+n-1)*tk

  Best case: tk=0

             T(n)= C1*n+5C2(n-1)+C3(n^2+n+1)+C4(n^2+n)
                 =C1*n+5C2*n-5C2+C3*n^2+C3n+C3+C4*n^2+C4n
                 =n^2(C3+C4)+n(C1+5C2+C3+C4)+5C2+C3
                 =An^2+Bn+C
                 =Theta(n^2)

    Worst case: tk=1
            T(n)= C1*n+5C2(n-1)+C3(n^2+n+1)+C4(n^2+n)+C5(n^2+n-1)
                =C1*n+5C2*n-5C2+C3*n^2+C3n+C3+C4*n^2+C4n+C5*n^2+C5n-C5
                =n^2(C3+C4+C5)+n(C1+5C2+C3+C4+C5)+5C2+C3-C5
                =An^2+Bn+C
                =Theta(n^2)
    The avarage case is Theta(n^2) since the sorting has only one more operation for the worst-case.

 */



    
