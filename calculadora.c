#include <stdio.h>

int main() {
	int opcao, n1, n2, resultado;
	printf("\n--- MENU ---\n");
	printf("1 - Somar\n");
	printf("2 - Subtrair\n");
	printf("3 - Multiplicar\n");
	printf("4 - Dividir\n");
	printf("escolha uma opcao: ");
	scanf("%d", &opcao);
	
	switch (opcao) {
		case 1:
			printf("Opcao Somar \n");
			printf("digite o primero numero da soma: \n");
			scanf("%d", &n1);
			printf("digite o segundo numero da soma: \n");
			scanf("%d", &n2);
			
			resultado = n1 + n2;
			
			printf("o resultado da soma e: %d\n", resultado);
			break;
		case 2:
			printf("Opcao Subtrair \n");
			printf("digite o primero numero da subtracao: \n");
			scanf("%d", &n1);
			printf("digite o segundo numero da subtracao: \n");
			scanf("%d", &n2);
			
			resultado = n1 - n2;
			
			printf("o resultado da subtracao e: %d\n", resultado);
			break;
		case 3:
			printf("Opcao Multiplicar \n");
			printf("digite o primero numero da multiplicacao: \n");
			scanf("%d", &n1);
			printf("digite o segundo numero da multiplicacao: \n");
			scanf("%d", &n2);
			
			resultado = n1 * n2;
			
			printf("o resultado da multiplicacao e: %d\n", resultado);
			break;
		case 4:
			printf("Opcao Dividir \n");
			printf("digite o primero numero da divisao: \n");
			scanf("%d", &n1);
			printf("digite o segundo numero da divisao: \n");
			scanf("%d", &n2);
			
			resultado = n1 / n2;
			
			printf("o resultado da divisao e: %d\n", resultado);
			break;
		default:
			printf("Opcao Invalida! \n");
	}
}
