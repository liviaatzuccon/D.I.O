import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) throws Exception {
        int conta;
        String agencia;
        String nomeCliente;
        float saldo;

        Scanner teclado = new Scanner(args[0]);
        System.out.println("Por favor, informe o nome cliente: ");
        nomeCliente = teclado.nextLine();
        System.out.println("Por favor, informe a agência: ");
        agencia = teclado.nextLine();
        System.out.println("Por favor, informe a conta: ");
        conta = teclado.nextInt();
        System.out.println("Por favor, informe o saldo: ");
        saldo = teclado.nextFloat();

        System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agencia é " + agencia + " conta " + conta + " e seu saldo é " + saldo + " já está disponivel para saque.");
        

    }
}
