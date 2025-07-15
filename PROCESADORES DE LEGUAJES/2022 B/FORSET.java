public class FORSET extends Expresion{
    String i1,i2;
    public FORSET(String i1,String i2,AST sent){
        super(sent,null);
        this.i1=i1;
        this.i2=i2;

    }
    public void generarCTD(){
        if(TablaSimbolos.getTipoConNiv(i1).tipo().equals(TablaSimbolos.getTipoConNiv(i2).getSubtipo())){
        String it=Generador.nuevaTemp();
        String v=Generador.nuevaLabel();
        String f=Generador.nuevaLabel();
        String aux=Generador.nuevaLabel();

        Generador.asignacion(it,"0");
        Generador.etiq(aux);
        Generador.comparacion(it, "<",i2 +"_length", new DosEtiq(v,f));
        Generador.etiq(v);
        Generador.asignacion(i1, i2+"["+it+"]");
        izq.generarCTD();
        Generador.asignacion(it, it+"+1");
        Generador.salto(aux);
        Generador.etiq(f);
        }else{
            Generador.error("error forset.java");
        }
    }
    
}
