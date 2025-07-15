
public class ANADIRELEM extends Expresion{
    public ANADIRELEM(String id,AST exp){
        super(null,exp);
        tipo=TablaSimbolos.getTipoConNiv(id);
        palabra=id;
    }
    public void generarCTD(){
        der.generarCTD();
        String v2=Generador.nuevaLabel();
        String f2=Generador.nuevaLabel();
        String i2=Generador.nuevaTemp();
        String aux2=Generador.nuevaLabel();
        String v3=Generador.nuevaLabel();
        String f3=Generador.nuevaLabel();
        String fuera=Generador.nuevaLabel();
        
        String temp=Generador.nuevaTemp();
        Generador.asignacion(temp, palabra+"_length");

        //vamos a ver si ya esta el elem y no loañdimo si ya esta
        Generador.asignacion(i2, "0");
        Generador.etiq(aux2);
        Generador.comparacion(i2, "<", palabra+"_length", new DosEtiq(v3, f3));
        Generador.etiq(v3);
        Generador.comparacion(palabra+"["+i2+"]", "==", temp, new DosEtiq(v2, f2));
        Generador.etiq(v2);
        Generador.salto(fuera);
        Generador.etiq(f2);
        Generador.asignacion(i2,i2+"+1");
        Generador.salto(aux2);
        Generador.etiq(f3);


        Generador.asignacion(palabra+"["+temp+"]", ((Expresion)der).getPalabra());

        Generador.asignacion(palabra+"_length",palabra+"_length"+"+"+"1");
        Generador.etiq(fuera);
    }
    
}
