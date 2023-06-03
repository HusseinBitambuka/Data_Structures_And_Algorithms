public interface EnchantedContainers{
    //takes an item and adds it into a container
    public void stow(String E);
    //gets the name of the next item
    public String peek();
    //discards the next item from the container
    public String use();

}