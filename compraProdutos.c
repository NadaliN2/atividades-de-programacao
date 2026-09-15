#include <stdio.h>

int main() {
	int opcao, quantidade, produtosDiferente = 0, TotalUnidades = 0;
	float valorProduto, subTotal, totalCompra = 0, desconto = 0, valorFinal;
	do {
		printf("\nDigite o valor do produto: R$");
		scanf("%f", &valorProduto);
		printf("\nDigite a quantidade comprada: R$");
		scanf("%f", &quantidade);
		subTotal = valorProduto * quantidade;
		totalCompra += subTotal;
		produtosDiferentes++;
		printf("\nSubtotal: R$ %.2f\n", subtotal);
		printf("\nDeseja cadastrar outro produto?\n");
		printf("1 - Sim\n");
		printf("Opcao: ");
		scanf("%d", &opcao);
	} while (opcao == 1);
	if (totalCompra >= 500) {
		desconto= totalCompra * 0.10;
	}
	valorFinal = totalCompra - desconto;
	printf("\n=== RESUMO DA COMPRA ===\n");
	printf("Produtos diferentes %d\n", produtosDiferentes);
	printf("Total de unidades %d\n", totalUnidades);
	pritnf("Total da compra: R$ %.2f\n", totalCompra);
	printf("Desconto: R$ %.2f\n", desconto);
	printf("Valor final: R$ %.2f\n");
	return 0;
}
