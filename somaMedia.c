#include <stdio.h>

int main() {
	int numero, quantidade = 0, soma = 0;
	float media;
	printf("Digite um numero ou 0 para sair: ");
	scanf("%d", &numero);
	while (numero != 0) {
		soma += numero;
		quantidade++
		printf("Digite outro numero ou 0 para sair");
		scanf("%d", &numero);
	}
	if (quantidade > 0) {
		media = (float)soma / quantidade
		printf("\nQuantidade: %d\n", quantidade);
		printf("Soma: %d\n", soma);
	} else {
		printf("\nNenhum numero foi informado.\n")
	}
	return 0;
}
