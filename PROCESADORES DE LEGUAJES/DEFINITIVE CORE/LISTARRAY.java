import java.util.ArrayList;

public class LISTARRAY extends Expresion{

    /*basicamente cuando aparece suelto {x1,x2,x3,..}
            Esta clase se encarga de, habiendo recibido una lista de nums(o expresiones), 
            imprimir un vector auxiliar t0[i] = exp_i
            Se llama cuando vamos a hacer x = {exp1,exp2,...},
            ya que en ASIGVECTOR posteriormente se hará x[i] = t0[i]
     */
    
    private ArrayList<AST> lista;
    private int tam;

    public LISTARRAY(ArrayList<AST> l){ // Constructor para arrays
        super(null,null);
        this.lista = l;
        this.tam = l.size();
           this.palabra = TablaSimbolos.declarandoConBloqueSinNiv(Generador.nuevaTemp());
    }

    public int getTam(){
        return this.tam;
    }
    public ArrayList<AST> getListaNums() {//en el caso array:unico metodo q me interesa pq el generarctd nunca se hace en array
        return lista;
    }

    public void generarCTD(){
    //ESTAS LINEAS SON LAS DEFINITIVAS:
///GUAY:solo si es array y si es print SE GENERA ctd , CD PRINT {x1,x2,x3}, y le asigno tipo array q es el q tiene algo asi {xq,x2,..}, ademas le genero size para luego convertir array a string
/// si es array y asig array, no se genera este ctd y el tipo me da igual pq en el constructor de asig arr coge el de la izq con tab simb
/// si es string y print, no puede ser, pq un string es "ffffds" pero no {x1,x2..} asi q esto se usara para convertirlo de array a string, y por eso cd lo imprimo pues le imprimo el lenght
/// si es string y es asig, me la suda tipo, pq la izq d mi asig es string y en asigarr cogera ese tipo y no genera este ctd pq ya lo hace ne asigarray con la lista
/// lo q me interesa es la lista
/// ESTO NO ES VERDAD PQ STRING NO LO USA EN PRINT PQ ES UN ARRAY LO USA EN ASIGARR PARA INICIALIZAR UN STRING A PARTIR DE UN ARRAYsolo se usa en asig array y en proint en print ya controlodao y en asignarray no se genera el ctd, en print si, en asigarray con la lsita voy q chuto y no geenro ctd d eso  y el tipo me da igual pq lo saca del id y no de la lista, mira el constructrod d asigarray dn saca el tipo
/// NO ME LO PUEDO AHORRAR PQ SE HACE PARA PRINT llavesarray en cup y tngo q generar su ctd antes pues ahi se hace este ctd,asi q lo necesito ahi, sino lo tengo devolveria una lista a pelo 

        if(lista.size() < 0){
            Generador.error("error en listaarray.java");
        } else {
            for(int i = 0; i<lista.size(); i++){
                AST e = lista.get(i);
                e.generarCTD();
                //t0[i] = exp_i
                Tipo t1 = ((Expresion)lista.get(0)).getTipo();//asigno aqui el tipo pq en suma el tipo se asigna tras generar su tipo y si aqui lo asigno el tipo en el costructor, da error null tipo si el array es {7+3,4+5,5+6} pq hasta q no egenro codigo de la suma, no tengo el codigo del elemnto 0 del array
                this.tipo = new Tipo(Tipo.ARRAYUNIDIM,t1.tipo(),tam); // Tipo del primer elemento de la lista
                Generador.asignacion(this.palabra+"["+i+"]", ((Expresion)e).getPalabra());
                //se imprime t[i] = numero i de la lista
            }        
            TablaSimbolos.putConNiv(this.palabra, tipo);///////GUAY:te la pela cual le pones , esto nunca se egenra, y fijate q en asigarray el tipo en el constructor se le asigna el de id y no el de listarray asi q perita 
                                                        ////ADEMAS SOLO SE USA EN ASIG ARRAY Q POR LO Q T ACABO D DECIR ESTA CONTROLADO Y EN PRINT Q NUNACA SE COMPRUEBA EL TIPO NI NADA
            Generador.asignacion(palabra+"_length", lista.size()+"");


        }
    }

}
