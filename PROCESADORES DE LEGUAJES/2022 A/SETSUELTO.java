import java.util.ArrayList;

public class SETSUELTO extends Expresion {




    /*basicamente cuando aparece suelto {x1,x2,x3,..}
            Esta clase se encarga de, habiendo recibido una lista de nums(o expresiones), 
            imprimir un vector auxiliar t0[i] = exp_i
            Se llama cuando vamos a hacer x = {exp1,exp2,...},
            ya que en ASIGVECTOR posteriormente se hará x[i] = t0[i]
     */
    
    private ArrayList<AST> lista;
    private int tam;

    public SETSUELTO(ArrayList<AST> l){ // Constructor para arrays
        super(null,null);
        this.lista = l;
        this.tam = l.size();
           palabra=TablaSimbolos.declarandoConBloqueSinNiv(Generador.nuevaTemp());
    }

    public int getTam(){
        return this.tam;
    }
    
    public ArrayList<AST> getListaNums() {
        return lista;
    }

    public void generarCTD(){

        if(lista.size() < 0){
            Generador.error("error en setsuelto.java");
        } else {
            for(int i = 0; i<lista.size(); i++){
                AST e = lista.get(i);
                e.generarCTD();
                //t0[i] = exp_i
                Generador.asignacion(this.palabra+"["+i+"]", ((Expresion)e).getPalabra());
                //se imprime t[i] = numero i de la lista
            }
            Tipo t1 = ((Expresion)lista.get(0)).getTipo();//asigno aqui el tipo pq en suma el tipo se asigna tras generar su tipo y si aqui lo asigno el tipo en el costructor, da error null tipo si el array es {7+3,4+5,5+6} pq hasta q no egenro codigo de la suma, no tengo el codigo del elemnto 0 del array
            this.tipo = new Tipo(Tipo.SET,t1.tipo()); // Tipo del primer elemento de la lista
            TablaSimbolos.putConNiv(palabra,tipo);
            Generador.asignacion(palabra+"_length", lista.size()+"");

        }
    }

}
