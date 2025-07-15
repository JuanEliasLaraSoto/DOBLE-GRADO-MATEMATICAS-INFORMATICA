public class ArrayUnidim extends Expresion{//me acaban de declarar un array: int x[8]
    public ArrayUnidim(String id,Tipo t){
        super(null,null);
        this.tipo=t;//Es un tipoi con tipo,subtipo y la longitud en numerin
        palabra=id;//no la genero con codigo pq estoy en declaracion : int x[3]
    }
    public void generarCTD(){
        if(tipo.getSubtipo().equals("char")||tipo.getSubtipo().equals("int")){
            Generador.asignacion(palabra+"_length",tipo.getLongitud().toString());
        }
    }
}
