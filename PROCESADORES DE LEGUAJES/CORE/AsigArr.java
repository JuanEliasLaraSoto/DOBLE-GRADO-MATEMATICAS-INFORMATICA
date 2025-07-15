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
        }
    }else{
        Generador.error("Distinto numero de elementos entre x y {x1,x2,...}");
    }
    }
}
