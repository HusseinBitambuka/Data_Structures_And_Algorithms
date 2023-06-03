public class BandolierOfConvenience implements EnchantedContainers{
    /*This is a class that implements a Queue datastructure.
     it takes in strings and applies all the Queue methods */
     protected class Node{
        /*This is an internal node. it gets initiated everytime 
         the user adds a new element to the Queue
         */
        String value;
        Node next=null;
        Node previous=null;
        //constructor of the internal node class
        Node(String e){
            this.value=e;
        }
     }
     Node head;// the head of the Queue. it is always null when the Queue is first initiated
     Node tail;// the tail of the Queue. it is always null when the Queue is first initiated

     public BandolierOfConvenience(){
        // no args contructor. it binds the tail and the head together

        this.head=new Node(null);
        this.tail =new Node(null);
        this.head.previous=this.tail;
        this.tail.next=this.head;
     }
     @Override
     /*This method is initially defined in the Enchanted container interface,
      and it adds elements to the Queue */

     public void stow(String e){
        Node element=new Node(e);
        element.previous=this.head.previous;
        this.head.previous.next=element;
        this.head.previous=element;
        element.next=this.head;
        
        
     }
     @Override
     /*This method is initially defined in the Enchanted container interface,
      it returns the first to be added in the stack.
      */
    public String peek(){
        return this.tail.next.value;
    }
    @Override
    /*This method is initially defined in the Enchanted container interface,
     it is used to change discard the top element.
     */
    public String use(){
        String value=this.peek();
        if(this.isEmpty()){
            return "The Queue is empty";
        }
        this.tail=this.tail.next;
        return value;

    }
    //Queue methods
    //---------------------------------------------------------------------------------------------------------------
    public boolean isEmpty(){
        /*this method test if the stack is empy */
        if(this.tail.next.value==null){
            return true;
        }
        return false;
    }
}
