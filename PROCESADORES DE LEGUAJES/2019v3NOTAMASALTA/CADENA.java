public class CADENA extends Expresion{
    protected String cadena;
    public CADENA (String c){//DIFERENCIA CON ARRAY, NADA MAS RECIBIRLA LA GENERO APRA Q SE MUESTRE SINO LA PIERDO
        super(null,null);
        cadena=c;
        String t0=Generador.nuevaTemp();
        TablaSimbolos.putConNiv(TablaSimbolos.declarandoConBloqueSinNiv(t0),new Tipo(Tipo.STRING));
        palabra=TablaSimbolos.crearConBloqueSinNiv(t0);
        tipo=new Tipo(Tipo.STRING);
    }
    public void generarCTD(){
        for(int i=0;i<cadena.length();i++){//lo paso a su ascii con charat(i) pq trabajamos con el asci d cada elem del string
            Generador.asignacion(palabra+"["+i+"]",(int)cadena.charAt(i)+"");

        }
        Generador.asignacion(palabra+"_length", cadena.length()+"");
    }
}
