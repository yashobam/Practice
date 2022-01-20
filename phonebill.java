import java.io.*;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
public class phonebill{

    public static void main(String args[]) throws IOException{
        File records= new File("phonerecords.txt");
        String numb="";
        int totalmins=0;
        String Maxnum="";
        Scanner sc = new Scanner(records);
        Scanner ob= new Scanner (System.in);
        String out="MCC Phone Bill Version Z\nNumber\t\tMinutes\tSeconds\tCharge\tCall Type\n==========\t======\t======\t=====\t=======\n";
        int c=0;
        String line="";
        double maxx=0.0;
        while(sc.hasNextLine()){
            if(c%2==0){
                line=sc.nextLine();
                out=out+"("+line.substring(0,3)+") "+ line.substring(3,6)+"-"+ line.substring(6,10)+"\t" ;
                numb= "("+line.substring(0,3)+") "+ line.substring(3,6)+"-"+ line.substring(6,10)+"\t";
            }
            else{
                line=sc.nextLine();
                String secs="";
                int i=0;
                while (!line.substring(i,i+1).equals(" ")){
                    secs=secs+ line.substring(i,i+1);
                    i++;
                }
                int mins=Integer.parseInt(secs)/60;
                int sec= Integer.parseInt(secs)%60;
                String cod=line.substring(i+1,line.length());
                int code=Integer.parseInt(cod);
                int o6= (sec>6)?1:0;
                if (code==1){
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.04)+"\tInterstate\n";
                    if ((double)((mins+o6)*0.04)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.04);
                    }
                    totalmins=totalmins+ mins+o6;
                    
                }
                else if (code==2){
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.03)+"\tIntrastate\n";
                    if ((double)((mins+o6)*0.03)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.03);
                    }
                    totalmins=totalmins+ mins+o6;
                }
                else if(code==3){
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.035)+"\tInterLATA\n";
                    if ((double)((mins+o6)*0.035)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.035);
                    }
                    totalmins=totalmins+ mins+o6;
                }
                else if (code==4){
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.015)+"\tintraLATA\n";
                    if ((double)((mins+o6)*0.015)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.015);
                    }
                    totalmins=totalmins+ mins+o6;
                }
                else if (code==5){
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.01)+"\tLocal\n";
                    if ((double)((mins+o6)*0.01)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.01);
                    }
                    totalmins=totalmins+ mins+o6;
                }
                else{
                    out=out+mins+"\t"+sec+"\t"+(double)((mins+o6)*0.10)+"\tUNKNOWN\n";
                    if ((double)((mins+o6)*0.10)>maxx){
                        Maxnum=numb;
                        maxx=(double)((mins+o6)*0.10);
                    }
                    totalmins=totalmins+ mins+o6;
                }
            }
            c++;
        }
        out=out+"Total mins billed: "+totalmins+" minutes\n";
        out=out+"Highest cost phone call number: "+Maxnum+"\n";
        
        System.out.println("A if you want a file, B if you want to print it");
        String inp=ob.nextLine();
        if (inp.equals("A")){
            
            FileWriter writer= new FileWriter("out.txt");
            writer.write(out);
            
        }
        else{
            System.out.println(out);
        }
    }
}