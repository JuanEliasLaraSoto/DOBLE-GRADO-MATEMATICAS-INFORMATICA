import java.util.ArrayList;

public class AsigArr extends Expresion {//cuando tengo x={x1,x2,...}
    protected Tipo tipodeloselementos;
    public AsigArr(String id, AST lista){
        super(lista,null);
            
        tipo=TablaSimbolos.getTipoConNiv(id);
        tipodeloselementos=new Tipo(TablaSimbolos.getTipoConNiv(id).getSubtipo());
        palabra=id;//no le genro codigo pera la guardo por si
    }
    public void generarCTD(){
        if(tipo.tipo().equals(Tipo.ARRAYUNIDIM)){
        ArrayList<AST> l=((LISTARRAY)izq).getListaNums();
       Tipo tipoIzq=TablaSimbolos.getTipoConNiv(palabra);
       if(l.size()<=tipo.getLongitud()){
        for(int i=0;i<l.size();i++){ 
            l.get(i).generarCTD();
            if(tipoIzq.getSubtipo().equals(((Expresion)l.get(i)).getTipo().tipo())){
                Generador.asignacion(palabra+"["+i+"]",((Expresion)l.get(i)).getPalabra());

            }else{//si el de izq es float y dere es int, es decir si en {x1,x2,..} hay algun int y x={x1,x2,..} es de float pues se genetera error, ahora bien siu luego hago x[i]=int entonces se hace cast(ver en arrayunidim)
                Generador.error("ERROR DE TIPOS");
            }
        }}

        }else if(tipo.tipo().equals(Tipo.SET)){
            izq.generarCTD();
            if(tipo.getSubtipo().equals(((Expresion)izq).getTipo().getSubtipo())){
            
            String v=Generador.nuevaLabel();
            String f=Generador.nuevaLabel();
            String aux=Generador.nuevaLabel();
            String i=Generador.nuevaTemp();
            String t0=Generador.nuevaTemp();
    
            Generador.asignacion(i,"0");
            Generador.etiq(aux);
            Generador.comparacion(i, "<", ((Expresion)izq).getPalabra()+"_length", new DosEtiq(v, f));
            Generador.etiq(v);
            Generador.asignacion(t0, ((Expresion)izq).getPalabra()+"["+i+"]");
            Generador.asignacion(palabra+"["+i+"]", t0);
            Generador.asignacion(i,i+"+1");
            Generador.salto(aux);
            Generador.etiq(f);
            Generador.asignacion(palabra+"_length",((Expresion)izq).getPalabra()+"_length");
            }else{
                Generador.error("set de dstinto tipo intentnado asignarse");
            }
        }else{
            Generador.error("Distinto numero de elementos entre x y {x1,x2,...}");
        }
    }
}
