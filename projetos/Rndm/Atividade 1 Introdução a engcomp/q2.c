#include <stdio.h>
#include <stdbool.h>

int main() {
    bool loop = true;

    printf("Bem-vindo(a) à calculadora de divisao\n");

    while (loop) {
        float n1, n2, quociente;
        char resposta;

        printf("Escreva o dividendo: \n");
        scanf("%f", &n1);
        printf("O dividendo e %.2f \n", n1);

        printf("Escreva o divisor: \n");
        scanf("%f", &n2);
        while (n2 == 0) {
            printf("Zero e um valor de divisor invalido. Tente outro numero diferente de zero: \n");
            scanf("%f", &n2);
        }
        printf("O divisor e %.2f \n", n2);

        quociente = n1 / n2;
        printf("O quociente e %.2f \n", quociente);

        // Consumir o caractere de nova linha no buffer
        while (getchar() != '\n');

        // Obter a resposta do usuário
        do {
            printf("Deseja realizar outra divisao? Digite 's' para sim ou 'n' para nao: \n");
            scanf("%c", &resposta);

            // Consumir caracteres extras no buffer
            while (getchar() != '\n');
        } while (resposta != 's' && resposta != 'n');

        if (resposta == 'n') {
            loop = false;
        }
    }

    printf("Obrigado por usar a calculadora. Ate mais!\n");
    return 0;
}