public class HaversackOfHolding implements EnchantedContainers {
    /*This is a class that implements a stack datastructure.
     it takes in strings and applies all the stack methods */
      protected class Node{
        /*This is an internal node. it gets initiated everytime 
         the user adds a new element to the stack
         */
        String value;
        Node previous=null;
        //constructor of the internal node class
        Node(String e){
            this.value=e;
        }
     }
     // the head of the stack. it is always null when the stack is first initiated
     Node head=new Node(null);
     public HaversackOfHolding(){
        this.head=new Node(null);
     }

     @Override
     /*This method is initially defined in the Enchanted container interface,
      and it adds elements to the stack */

     public void stow(String e){
        Node element=new Node(e);
        element.previous=head;
        this.head=element;
     }
     @Override
     /*This method is initially defined in the Enchanted container interface,
      it returns the top element.
      */
    public String peek(){
        return this.head.value;
    }
    @Override
    /*This method is initially defined in the Enchanted container interface,
     it is used to change discard the top element.
     */
    public String use(){
        if(this.isEmpty()){
            return"the stack is empy";
        }
        String element=this.peek();
        this.head=this.head.previous;
        return element;

    }
    //Stack methods
    //---------------------------------------------------------------------------------------------------------------
    public boolean isEmpty(){
        /*this method test if the stack is empy */
        if(this.head.value==null){
            return true;
        }
        return false;
    }
}