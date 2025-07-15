import java.util.ArrayList;
import java.util.HashMap;
public class TablaSimbolos {
   private static ArrayList< HashMap<String, Tipo>> tabla ;
   private static int nivel = 0;
   static { //esto siempre se ejecuta al comienzo;
      tabla = new ArrayList<HashMap<String,Tipo>>();
      tabla.add(new HashMap<>());
      nivel = 0;
  }
   public TablaSimbolos() {
      tabla = new ArrayList();
      tabla.add(new HashMap());
      nivel = 0;
   }
   public static void putSinNiv(String var,Tipo tipo) {
      if(!estaEnBloque(var)){
         tabla.get(nivel).put(var, tipo);
     }else{
         Generador.error(var+" Variable ya declarada");
     }
   }
   public static void putConNiv(String var,Tipo tipo) {
      if(!estaEnBloque(var)){
          tabla.get(nivel).put(var, tipo);
      }else{
          Generador.error(var+" Variable ya declarada");
      }
   }

   public static Tipo getTipoSinNiv(String var) {
      if(obtenerBloqueSinNiv(var)!=-1){
      int bloq=obtenerBloqueSinNiv(var);
      return tabla.get(bloq).get(var+"_"+bloq);
      }else{
         Generador.error(var+" no esta declarada en este bloque");
         return null;
      }
   }
   public static Tipo getTipoConNiv(String var) {
      if(obtenerBloqueConNiv(var)!=-1){
      int bloq=obtenerBloqueConNiv(var);
      return tabla.get(bloq).get(var);
   }else{
      Generador.error(var+" no esta declarada en este bloque");
      return null;
   }
   }
   public static boolean estaEnBloque(String var) {
      return tabla.get(nivel).containsKey(var);
   }
   public static void abrirBloque() {
      tabla.add(new HashMap());
      nivel++;
   }
   public static void cerrarBloque() {
      tabla.remove(nivel);
      nivel--;
   }

   public static int obtenerBloqueSinNiv(String var){
         for(int i=nivel;i>=0;i--){
            if(tabla.get(i).containsKey(var+"_"+i)){
                  return i;
            }
         }
         return -1;
   }
   public static int obtenerBloqueConNiv(String var){
      for(int i=nivel;i>=0;i--){
         if(tabla.get(i).containsKey(var)){
               return i;
         }
      }
      return -1;
}
   public static boolean yaDeclaradaSinNiv(String var){
      if(obtenerBloqueSinNiv(var)!=-1){
         return true;
      }
      return false;
   }
   public static boolean yaDeclaradaConNiv(String var){
      if(obtenerBloqueConNiv(var)!=-1){
         return true;
      }
      return false;
   }
   public static int getNivel(){
      return nivel;
   }
   public static String crearConBloqueSinNiv(String var){
      if(yaDeclaradaSinNiv(var)&&obtenerBloqueSinNiv(var)==nivel){
      return var+"_"+nivel;
      }else if(yaDeclaradaSinNiv(var)){
         return var+"_"+obtenerBloqueSinNiv(var);
      }else{
         Generador.error(var+" no esta declarada en ningun bloque abierto");
         return null;
      }
   }
   public static String declarandoConBloqueSinNiv(String var){
      
      return var+"_"+nivel;
     
   }
   public static void imprimir(){
      for(int i=0;i<=nivel;i++){
         System.out.println("Nivel "+i);
         for(String key:tabla.get(i).keySet()){
            System.out.println(key+" "+tabla.get(i).get(key));
         }
      }
   }
   
}
