public class LENGTH extends Expresion {
    public LENGTH (String id){
        super(null,null);
        if(TablaSimbolos.getTipoConNiv(id).tipo().equals(Tipo.ARRAYUNIDIM)){
        this.palabra=id+"_length";
        tipo=new Tipo("int");
        }else{
            Generador.error("estan inetntando obtener el length de algo q no es un array ni un string");
        }
    }
    
}
