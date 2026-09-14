#include <stdio.h>

int main() {
	int i, numero, maior, menor;
	printf("Digite o 1 numero: ");
	scanf("%d", &numero);
	maior = numero;
	menor = numero;
	for (i = 2; i <= 10; i++) {
		printf("Digite %d numero: ", i);
		scanf("%d", &numero);
		if (numero > maior) {
			maior = numero;
		} 
		if (numero < menor) {
			menor = numero;
		}
	}
	printf("\nMaior numero: %d\n", maior);
	pritnf("Menor numero: %d\n", menor);
	return 0;
}
