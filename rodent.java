import java.io.*;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
public class rodent{

    public static void main(String args[]) throws IOException{
        
        File records= new File("Observation.txt");
        Scanner sc = new Scanner(records);
        Scanner ob= new Scanner (System.in);
        BufferedReader reader = new BufferedReader(new FileReader("Observation.txt"));
        int linenum = 0;
        while (reader.readLine() != null) linenum++;
        reader.close();
        String out="Refnum\tLocation\tDays\tStart\tEnd\tDifference\tPercentage\n";
        String line="";
        String num="";
        int refnum[]=new int [linenum];
        String location[]=new String[linenum];
        int days[]=new int [linenum];
        int scount[]=new int [linenum];
        int ecount[]=new int [linenum];
        double diff[]=new double [linenum];
        double perc[]=new double [linenum];
        int c=0;
        int i=0;
        while(sc.hasNextLine()){
            line=sc.nextLine();
            if(c%3==0){
                refnum[(int)(c/3)]=Integer.parseInt(line);
            }
            else if (c%3==1){
                location[(int)(c/3)]=line;
                }
            else{
                i=0;num="";
                while (!line.substring(i,i+1).equals(" ")){
                    num=num+ line.substring(i,i+1);
                    i++;
                }
                days[(int)(c/3)]=Integer.parseInt(num);
                
                i=i+1;num="";
                while (!line.substring(i,i+1).equals(" ")||num.equals("")){
                    num=num+ line.substring(i,i+1);
                    i++;
                }
                
                scount[(int)(c/3)]=Integer.parseInt(num.trim());
                ecount[(int)(c/3)]=Integer.parseInt(line.substring(i+1,line.length()));
            }
            c++;
        }
        diff=difference(scount,ecount);
        perc=percent(scount,ecount);
        for (i=0; i<c/3;i++){
            out=out+refnum[i]+"\t"+location[i]+"\t"+days[i]+"\t"+scount[i]+"\t"+ecount[i]+"\t";
            out=out+diff[i]+"\t"+perc[i]+"\n";
        }

        System.out.println("A if you want a file, B if you want to print it, and C if you want both");
        String inp=ob.nextLine();
        if (inp.equals("A")){
            FileWriter writer= new FileWriter("out.txt");
            writer.write(out);
            writer.close();
        }
        else if (inp.equals("B")) {
            System.out.println(out);
        }
        else{
            FileWriter writer= new FileWriter("out.txt");
            writer.write(out);
            writer.close();
            System.out.println(out);
        }
    }
    public static double[] percent (int[] scount, int[] ecount){
        double[]perc=new double[scount.length];
        for(int i=0;i<scount.length;i++)
            perc[i]=100.0*((double)ecount[i]-(double)scount[i])/((double)scount[i]);
        return perc;
    }
    public static double[] difference (int[] scount, int[] ecount){
        double[]diff=new double[scount.length];
        for(int i=0;i<scount.length;i++)
            diff[i]=scount[i]-ecount[i];
        return diff;
    }
}