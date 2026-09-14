#include <stdio.h>

int main() {
	float A1, A2, media;
	printf("Digite a primeira nota do aluno: ");
	scanf("%f", &A1);
	printf("Digite a segunda nota do aluno: ");
	scanf("%f", &A2);
	
	media = (A1 + A2) / 2;
	
	if (media >= 6){
		printf("Aprovado!");
	}	else	{
		printf("Reprovado!");
	}
}
