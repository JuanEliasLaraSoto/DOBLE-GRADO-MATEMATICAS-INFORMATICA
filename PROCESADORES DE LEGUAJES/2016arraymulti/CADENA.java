public class CADENA extends Expresion{
    protected String cadena;
    public CADENA (String c){
        super(null,null);
        cadena=c;
        String t0=Generador.nuevaTemp();
        TablaSimbolos.putConNiv(TablaSimbolos.declarandoConBloqueSinNiv(t0),new Tipo(Tipo.STRING));
        palabra=TablaSimbolos.crearConBloqueSinNiv(t0);
        tipo=new Tipo(Tipo.STRING);
    }
    public void generarCTD(){
        for(int i=0;i<cadena.length();i++){
            Generador.asignacion(palabra+"["+i+"]",(int)cadena.charAt(i)+"");

        }
        Generador.asignacion(palabra+"_length", cadena.length()+"");
    }
}
