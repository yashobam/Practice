import java.util.Scanner;

public class Histogram {
  
    private static final int SENTINAL = -999;          // sentinal value to signal endo of input
    private static final int MAX_NUMBERS = 20;         // maximum number of numbers to input
    private static final double UPPER_BOUND = 100.0;   // largest numbers accepted as data
    private static final double LOWER_BOUND = 0.0;     // smallest numbers accepted as adata
    private static final int NUM_BINS = 10;            // number of bins in range [0..100]

    //private static final int BIN_SIZE = ??           // size of each bin

    /*
     * Method to show an example of using StringBuilder.
     *
     * You will also notice that this method is called from the
     * main function.
     *
     */
    public static String getHeaderAsString( String me ) {

        // Create an instance of the StringBuilder class
        // which allows us to create an object of
        // a series of strings that can then be converted
        // into one large string via the toString method.
        //
        StringBuilder sb=new StringBuilder();

        sb.append( System.getProperty("line.separator") );
        sb.append( "Welcome to the Histogram Program " + me + "!" );
        me = getFirstName(me);
        sb.append( System.getProperty("line.separator") );
        sb.append( System.getProperty("line.separator") );
        sb.append( "This program will print out a histogram of the numbers" );
        sb.append( System.getProperty("line.separator") );
        sb.append( "input by you " + getFirstName(me) + "." );
        sb.append( System.getProperty("line.separator") );
        sb.append( System.getProperty("line.separator") );
        sb.append( "Please enter up to " + MAX_NUMBERS + " doubles or " + SENTINAL + " to stop input!" );
        sb.append( System.getProperty("line.separator") );

        return sb.toString();
    }

    /*
     * Method to return the first name of the user in case
     * the full name was entered.
     */
    public static String getFirstName(String name ) {
        // Note that add the " " to string to be sure
        // there is something to split
        return (name+" ").split(" ")[0];
    }

    /*
     * local main test driver
     *
     */
    public static void main(String[] args) {

        // Connect to the keyboard as the input stream
        Scanner userInput = new Scanner( System.in );

        System.out.print( "And who am I working with today? " );
        String user = userInput.nextLine();

        String heading = getHeaderAsString( user );

        // Print out welcome message
        System.out.println( heading );
      
        // Call the method which prompts the user
        // to input the numbers that will be used
        // to build the histogram.
        double[] numbers = inputNumbers( userInput );

        // Call the method to reate the array histogram
        int[] histogram = calculateHistogram( numbers );

        // Print the historgram
        System.out.println( toString( histogram ) );
    }

    /*
     *
     * COMPLETE YOUR METHODS
     *
     */
    //method calulateHistogram that computes the histogram from the array of numbers passed to it.
    public static int [] calculateHistogram( double [] numbers) {

                int buckets[] = new int[NUM_BINS];
                int adder=(int) ((UPPER_BOUND-LOWER_BOUND)/NUM_BINS);
                for(int i=0; i<numbers.length; i++) {
                        double h = numbers[i];
                        
                        int index;
                        if(h % 10 == 0) {
                                index =  (int) ((h - 1) / 10);
                        } else {
                                index = (int) (h / 10);
                        }

                        buckets[index] += 1;
                }
                
                return buckets;
                
        }
    public static String toString( int [] histogram ) {
        // This method must also use a loop that iterates
        // over the histogram array to form the string
        // representaion of it.

        // The histogram can be visualzed as a series of
        // buckets, where each bucket represents one range
        // of the histogram:
      
        // The string returned should only contain the string representation
        // of the histogram and no other verbeage. It should function
        // like the toString method of the Array class but specific to
        // creating a histogram.

        // You may want to create an instance of the
        // StringBuilder class to assist you in this method.
        // Follow the code in the method getHeaderAsString
        // as a guide.
       StringBuilder sb=new StringBuilder();
       int adder=(int) ((UPPER_BOUND-LOWER_BOUND)/NUM_BINS);
       int temp=(int) ((UPPER_BOUND-LOWER_BOUND)/NUM_BINS);
        int tem=(int) LOWER_BOUND;
        // This method must determine the appropriate bin of the
        // histogram to update by using a loop. To be clear,
        // you may NOT just explicitly account for all
        // possibilities, e.g., the following is a bad solution:
       for(int i=0;i<histogram.length;i++) {
           sb.append("["+tem+".."+adder+"]: ");
           for(int j=0;j<histogram[i];j++) {
               sb.append('*');
           }
           sb.append( System.getProperty("line.separator") );
           tem=adder;
           adder+=temp;
       }
       return sb.toString();
    }
   /*
    * a method to determine if the integer passed to the method is in the legal range of valid inputs
    * as specified by the static variables of the class, LOWER_BOUND and UPPER_BOUND
    */
  
    public static boolean validInput( double num ) {
       if(num<LOWER_BOUND|| num>UPPER_BOUND) {
           return false;
       }
       return true;
    }
    /*
     * method that performs the user input
     * This method accepts an object of the scanner class, uses this object to perform user input
     * by calling the apporopriate methods, and returns an array of the floating point values that were input
     */
    public static double[] inputNumbers( Scanner scan ) {
       double[] input=new double[MAX_NUMBERS];
       int i=0;
       while(i<MAX_NUMBERS) {
           double num=scan.nextDouble();
           if(num!=SENTINAL) {
               if(validInput(num)) {
                   input[i]=num;
                   i++;
               }
           }
           else {
               break;
           }
       }
       return input;
    }

} // end of class