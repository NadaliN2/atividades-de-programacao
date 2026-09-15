#include <stdio.h>

int main() {
	float nota, frequencia;
	
	printf("Digite sua nota: ");
	scanf("%f", &nota);
	printf("Digite sua frequencia: ");
	scanf("%f", &frequencia);
	
	if (nota >= 9 && frequencia >= 90) {
		printf("Media: %f\n", nota);
		printf("Media: %f\n", frequencia);
		printf("Resultado: Bolsa Integral");
	} else if (nota >= 7 && frequencia >= 70) {
		printf("Media: %f\n", nota);
		printf("Media: %f\n", frequencia);
		printf("Resultado: Bolsa Parcial");
	} else if (nota < 7 && frequencia < 70) {
		printf("Media: %f\n", nota);
		printf("Media: %f\n", frequencia);
		printf("Resultado: Sem Bolsa");
	}
}

