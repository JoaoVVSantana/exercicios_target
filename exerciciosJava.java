package Exercicios;

import java.util.Scanner;

class exerciciosJava {
    public static void main(String[] args) {
        int soma=0;
        int indice=13;
        for(int k=0; k<indice; k++){
            soma+=k;
            System.out.println(soma);
        }
        System.out.println(soma);



    }
    
}

class exercicio02{
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Informe um valor para verificar se está em Fibonacci:");
        int n=sc.nextInt();

        boolean presente=false;

        int anterior=0;
        int atual=1;
        int posterior=anterior+atual;
        

        while(posterior<=n)
        {
            if(posterior==n) {
                presente=true; 
                break;
            }
            anterior=atual;
            atual=posterior;
            posterior=anterior+atual;        
        }
        String resultado = (presente) ? "Está na sequencia": "Não está na sequência";
        System.out.println(resultado);
        sc.close();
        
    }
}
class exercicio03 {
    public static void main(String[] args) {
        /*
         * Feito em python
         */
    }
}

class exercicio04 {
    public static void main(String[] args) {
        String [] cidade= {"São Paulo", "Rio De Janeiro", "Minas Gerais","Espírito Santo", "Outros Estados"};
        double [] faturamento={67836.43,36678.66,29229.88,27165.48,19849.53 };

        double valorTotal=0;
        for(int i=0; i<5;i++){
            valorTotal+=faturamento[i];
        }
        System.out.println("Valor total do faturamento da empresa: "+valorTotal);

        for(int j=0; j<5;j++)
        {
            double representacao=(faturamento[j]*100)/valorTotal;
            System.out.printf("%s representa %.2f%% do faturamento total da empresa%n", cidade[j], representacao);

        }
    }
}

class exercicio05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Informe uma frase para ser invertida: ");
        String frase = sc.nextLine();

        String[]letrasDaFrase=new String[frase.length()];
        String fraseInvertida=new String();
        for(int i=0, j=frase.length()-1;j>=0;i++,j--){
            
            letrasDaFrase[i]=Character.toString(frase.charAt(j));
            fraseInvertida+=letrasDaFrase[i];
            

        }

        System.out.println(fraseInvertida);
        sc.close();
    }
}