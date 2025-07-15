import java.util.ArrayList;

public class ListaArrayAAST extends Expresion {
    protected ArrayList<AST> l;
    public ListaArrayAAST (ArrayList<AST> lista){
        super(null,null);
        this.l=lista;
        palabra=Generador.nuevaTemp();
    }
    public void generarCTD(){
      
        for(int i=0;i<l.size();i++){ 
            if(((Expresion)l.get(i)).getTipo().tipo().equals("char")){
           Generador.printc(((Expresion)l.get(i)).getPalabra());
            }else{
                Generador.print(((Expresion)l.get(i)).getPalabra());
            }
        }
   
    }
    
}
