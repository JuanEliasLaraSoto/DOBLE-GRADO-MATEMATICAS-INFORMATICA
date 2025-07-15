public class Generador {
    public static int temp=0;
    public static int label=0;
    public static int numParam=0;

    public static void reiniciarParam(){
        numParam=0;
    }
    public static int numParamIncrementar(){
        numParam++;
        return numParam;
    }
    public static void function(String nombre){
        System.out.println("\t"+"function"+" "+nombre+":");

    }
    public static void end(String nombre){
        System.out.println("\t"+"end"+" "+nombre+";");

    }
    public static void call(String nombre){
        System.out.println("\t"+"call"+" "+nombre+";");

    }
    public static String nuevaTemp(){
        return "t"+temp++;
    }
    public static String nuevaLabel(){
        String l="L"+label;
        label++;
        return l;
    }
    public static void asignacion(String id,String exp){
       
        System.out.println("\t"+id+"="+exp+";");
    }
    public static void print(String id){
        System.out.println("\tprint "+id+";");
    }

    public static void printc(String id){
        System.out.println("\tprintc "+id+";");
    }
    public static void writec(int ascii){
        System.out.println("\twritec " + ascii + ";");
    }
    public static void error(String error){
        System.out.println("\t #"+error);
        System.out.println("\terror;");

        System.out.println("\thalt;");
        System.exit(1);
    }
    public static void comparacion(String izq,String operador,String der,DosEtiq vf){
       if (operador.equals("==")||operador.equals("!=")||operador.equals("<")) {
        System.out.println("\tif ("+izq+" "+operador+" "+der+") goto "+vf.getV()+";");
        System.out.println("\t"+"goto "+vf.getF()+";");
       }else if (operador.equals("<=")){//a<=b == !(b<a) el b<a lo hago con izq der y el ! se hace con getv y getf cambiandolo
        System.out.println("\tif ("+der+" < "+izq+") goto "+vf.getF()+";");//fijate q pongo der en izq y izq en der
        System.out.println("\t"+"goto "+vf.getV()+";");
        
       }else if (operador.equals(">")){//a>b == b<a
        System.out.println("\tif ("+der+" < "+izq+") goto "+vf.getV()+";");
        System.out.println("\t"+"goto "+vf.getF()+";");
       }else if (operador.equals(">=")){//a>=b == !(<) y debido al not cambio el getf y getv, pq el < lo consigo cambian izq por der y el not con getf y getv
        System.out.println("\tif ("+izq+" < "+der+") goto "+vf.getF()+";");
        System.out.println("\t"+"goto "+vf.getV()+";");
       }
    }
    public static void etiq(String etiq){
        System.out.println("\t"+etiq+":");
    }
    public static void salto(String etiq){
        System.out.println("\t"+"goto "+etiq+";");
    }
    
}
