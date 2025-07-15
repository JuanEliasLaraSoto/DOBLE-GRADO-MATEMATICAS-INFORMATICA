public class OperandoCond{
    protected String operadorExplicito;
    public OperandoCond(String opImplicito){
        switch (opImplicito) {
            case "EQ":
                operadorExplicito="==";
                break;
            case "NE":
                operadorExplicito="!=";
                break;
            case "GE":
                operadorExplicito=">=";
                break;
            case "GT":
                operadorExplicito=">";
                break;
            case "LE":
                operadorExplicito="<=";
                break;
            case "LT":
                operadorExplicito="<";
                break;
            case "AND":
                operadorExplicito="&&";
                break;
            case "OR":
                operadorExplicito="||";
                break;
            case "NOT":
                operadorExplicito="!";
                break;
            default:
                System.out.println("operador condicional erroneo introducido");
                System.exit(-1);
                break;
        }
    }

    public String getOperadorExplicito() {
        return this.operadorExplicito;
    }


}