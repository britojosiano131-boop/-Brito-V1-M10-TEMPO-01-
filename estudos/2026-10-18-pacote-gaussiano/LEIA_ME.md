# M10-TEMPO-01: teste numerico exploratorio do pacote gaussiano

Data: 18/10/2026. Separado do nucleo congelado. Fundamentos preservados: 10,1-0,1=10; 333-137=196=14²; epsilon=3/140.

Parametros ilustrativos: A0=0.1, mu=1, y0=0. Frequencia adotada 0.05 Hz, periodo 20 s. Nao sao parametros fisicos calibrados.
Equacao: y'' = mu*epsilon*y*A(y)*sin(s+phase)*sech²(A(y)*sin(s+phase))/(1+epsilon*tanh(A(y)*sin(s+phase))), A(y)=0.1 exp(-y²/2).
Normalizacao: y=x/sigma, s=omega*t. Limiar aproximado de dy/ds: 0.0016145083245000563. Barreira aproximada |y|=sqrt(2); regiao externa |y|=3.

## Execucao

336 trajetorias na malha inicial: 16 fases e 21 velocidades entre 80% e 120% do limiar. Horizonte 500 ciclos. 173 cruzaram a barreira, 96 chegaram a |y|=3 e 32 tiveram retorno registrado apos passagem.
Refinamento adaptativo: 635 trajetorias totais, 63 intervalos de mudanca de classificacao e 123 condicoes nas extremidades para verificacao.
Primeira transicao de passagem pela barreira: envelope dos intervalos entre eta=0.995625 e 1.000625 nas 16 fases. Alcance de |y|=3 em 500 ciclos: envelope entre eta=1.090625 e 1.09625. Estes sao intervalos de uma busca finita, nao limiares exatos ou garantias de monotonicidade.

## Verificacao numerica

[
  {
    "cycles": "1000",
    "max_step": "0.2",
    "n": 123,
    "changes_vs_500_base": {
      "barrier": 16,
      "outer": 69,
      "returned": 17
    }
  },
  {
    "cycles": "500",
    "max_step": "0.1",
    "n": 123,
    "changes_vs_500_base": {
      "barrier": 0,
      "outer": 0,
      "returned": 1
    }
  },
  {
    "cycles": "500",
    "max_step": "0.2",
    "n": 123,
    "changes_vs_500_base": {
      "barrier": 0,
      "outer": 0,
      "returned": 1
    }
  }
]

As mudancas de classificacao de retorno perto de fronteiras devem ser tratadas como sensibilidade da deteccao de eventos. O integrador pode perder dois cruzamentos proximos no mesmo passo. Passos e tolerancias menores nao constituem garantia matematica de todos os eventos.
Os casos de 1000 ciclos avaliam dependencia do horizonte, e nao erro numerico isolado. Somente comparacoes com mesmo horizonte permitem comparar diretamente estados finais.
Malhas finitas podem perder janelas estreitas; o refinamento aborda apenas intervalos com classificacoes diferentes nas extremidades. Nao houve busca exaustiva de todas as janelas.
O script usa DOP853/SciPy. Arquivos CSV preservam as trajetorias, intervalos e validacoes.

## Interpretacao

Concordancia interna entre modelo completo e aproximacao em parametros ilustrativos. Nao e ensaio fisico, alteracao temporal medida, calibracao de K_T, nem determinacao de energia escura. Cruzar uma barreira ou nao retornar ate o fim nao prova escape eterno. Nucleo congelado, hardware e firmware nao foram alterados.
