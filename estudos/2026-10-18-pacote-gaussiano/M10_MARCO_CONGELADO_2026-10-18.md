# MARCO CONGELADO — M10-TEMPO-01 — DINÂMICA LOCAL

Identificador: M10-LOCAL-GAUSS-FREEZE-20261018-v1
Data: 18/10/2026
Autorização: congelamento solicitado por Josiano de Brito nesta data.
Estado: registro imutável de resultados numéricos exploratórios; futuras alterações exigem novo identificador e comparação explícita.

## Escopo
Preserva o núcleo M10-TEMPO-01 e os fundamentos 10,1−0,1=10; 333−137=196; √196=14; epsilon=3/140. Não altera hardware, firmware R11, PCB ou a formulação congelada anterior.

## Conteúdo congelado
Pacote gaussiano unidimensional com A0=0,1 e mu=1, parâmetros ilustrativos sem calibração física. 635 integrações de mapeamento/refinamento e 369 verificações, total 1.004 integrações. A malha inicial contém 336 condições. Os resultados de 500 e 1.000 ciclos são horizontes finitos.

Envelope dos intervalos da primeira passagem pela barreira em 500 ciclos: eta entre 0,995625 e 1,000625 nas fases testadas. Não é um intervalo de confiança nem limite universal. Refinamento apenas onde houve mudança detectada nas extremidades; janelas estreitas podem ficar fora da busca.
As 123 condições repetidas com precisão maior mantiveram a classificação de passagem e alcance externo em 500 ciclos; um registro de retorno mudou. Em 1.000 ciclos, 16 condições adicionais passaram pela barreira. Resultado dependente do horizonte.

## Alcance
Consistência interna entre equação candidata e aproximação; não constitui medição de alteração temporal, validação de propulsão ou determinação da energia escura. O estudo permanece separado como frente exploratória.

## Integridade SHA-256
- m10_sweep.py: `456290211b944224d09eaccf192d609aefeaccef366d553fd69672aacff16e26`
- M10_resultados_simulacao.zip: `959d09357f8350ac3db4310c0c57ce5fb60fb519fe0aa8966205b67c57f00f49`
- m10_results/LEIA_ME.md: `aa2becead1cc7fca08aa1578c28b5b156450fedb0bb5c455fbc6c19e143a918f`
- m10_results/trajectories.csv: `7b659a63cef5e715e39d062063006c1c47daab8e8d5b5fb595a29e45c1fb0bcf`
- m10_results/transitions.csv: `09a4c395d65f43fdbaf7d20c740c583e32e4a3d8e65dcd376c16acf41d57bd8f`
- m10_results/validation.csv: `6b8924732d164fecec1c736d336418a6180b81e323c213a227eb48fbbc4ade10`
