import java.util.ArrayList;

public class AsigMultiArr extends Expresion {//x={}
    ArrayList<ArrayList<AST>> lista;
    public AsigMultiArr(String id, AST l){
        super(l,null);
        palabra=id;
        tipo=TablaSimbolos.getTipoConNiv(id);
        this.lista=((LISTAMULTIARRAY)l).getListaNums();
    }
    public void generarCTD(){
        for(int i=0; i<lista.size();i++){
            for(int j=0; j<lista.get(0).size();j++){
            String t0=Generador.nuevaTemp();
                String t1=Generador.nuevaTemp();
                Generador.asignacion(t0,i+" * "+lista.get(0).size());
                Generador.asignacion(t1,t0+" + "+j);
                lista.get(i).get(j).generarCTD();
                Generador.asignacion(palabra+"["+t1+"]",((Expresion) lista.get(i).get(j)).getPalabra());
        }
    }
    }
}
