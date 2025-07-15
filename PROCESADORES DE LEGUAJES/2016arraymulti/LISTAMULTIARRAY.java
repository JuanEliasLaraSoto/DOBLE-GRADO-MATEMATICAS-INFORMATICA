import java.util.ArrayList;

public class LISTAMULTIARRAY extends Expresion {
    private ArrayList<ArrayList<AST>> lista;
    private int tam;
    public LISTAMULTIARRAY(ArrayList<ArrayList<AST>> l){
        super(null,null);
        lista=l;
        tam=l.size();
        
    }
    public int getTam(){
        return this.tam;
    }
    
    public ArrayList<ArrayList<AST>> getListaNums() {
        return lista;
    }
}
