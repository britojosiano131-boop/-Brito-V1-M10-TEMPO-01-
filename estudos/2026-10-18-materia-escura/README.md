# Matéria escura: a proposta investigada pela Matriz 10

**Josiano de Brito · Registro explicativo de 18/10/2026**

## Fundação preservada

10,1 − 0,1 = 10; 333 − 137 = 196; √196 = 14.

Este desenvolvimento parte das definições internas da Matriz 10 e preserva os documentos congelados.

## Por que investigar a matéria escura?

A pergunta de Josiano de Brito é direta: os efeitos galácticos atribuídos à matéria escura poderiam ser descritos pela dinâmica de um fluido gravitacional, com fluxos, ondas e interações nodais?

A hipótese procura descrever a coesão e as curvas de rotação usando a matéria comum e a resposta desse meio, sem acrescentar uma componente de matéria escura ao modelo. Essa é a proposta em investigação.

## O que fechou matematicamente na V2

O Dossiê Mestre V2 e o código brito_v1_matriz10_lambda_v2.py utilizam a mesma candidata. Com x = r/r_c:

- H₁₀(x) = x²/(1 + x²)
- Λ₁₀(r) = K_Λ [1 + α x H₁₀(x)] = K_Λ [1 + α x³/(1 + x²)]
- v₁₀²(r) = Λ₁₀(r) M(r)/r

K_Λ define a escala de acoplamento; α é o ganho; r_c é o raio de transição.

Para massa total finita M_∞ e parâmetros positivos, o termo x³/(1+x²) cresce como x no limite externo. Esse comportamento compensa o fator 1/r e fornece:

**v₁₀²(∞) = K_Λ α M_∞/r_c.**

Esse é o sentido preciso do fechamento analítico: a fórmula produz um platô assintótico nas condições declaradas. A expressão racional não satura; é a velocidade que tende a um valor constante.

## Versões separadas

| Registro | Fator de correção |
| --- | --- |
| Auditoria histórica da NGC 3198 | 1 + x |
| Dossiê Mestre V2 e código Python | 1 + α x³/(1 + x²) |

A razão r_c/R_d = 1,736 permanece um parâmetro histórico declarado, com origem pendente de rastreamento. Esta auditoria não estabeleceu uma derivação desse número a partir da fundação.

## O que o código calcula e o que falta conferir

O script gera curvas com perfis de massa idealizados: núcleo finito, aproximação exponencial e massa pontual. Ele não carrega uma tabela observacional do SPARC. Sua configuração padrão usa unidades normalizadas e 401 pontos; a configuração de uma execução histórica precisa ser conferida em suas saídas ou no comando utilizado.

As saídas previstas são serie_lambda10_v10.csv, resumo_lambda10_v10.json e grafico_lambda10_v10.png. Esses arquivos não foram localizados na busca documental desta rodada.

Para a comparação quantitativa com a NGC 3198, seguem pendentes a tabela observacional primária, suas incertezas, a distribuição de massa adotada e os parâmetros efetivamente utilizados. O platô é uma propriedade matemática demonstrada da candidata; a avaliação com dados reais é uma etapa própria.

## Onde entra a bancada?

Os sinais de 333 Hz e o ciclo relativo de 20 segundos fazem parte da instrumentação do Brito V1. A M10-TEMPO-01 é a formulação principal dos próximos testes, centrada na taxa e no gradiente do tempo local.

A telemetria permite confrontar previsões locais e examinar vibração, aquecimento e acoplamento dos cabos. A ponte entre esse mecanismo local, o fluido gravitacional e a dinâmica galáctica exige dedução específica; os blocos documentais mantêm seus escopos.

## Separação do pacote gaussiano

O marco M10-LOCAL-GAUSS-FREEZE-20261018-v1 trata de confinamento e dispersão local sob modulação temporal. Continua preservado em sua pasta. A investigação de matéria escura nesta frente galáctica e a investigação de energia escura na expansão cosmológica são perguntas distintas.

## Situação consolidada

Candidata analítica com comportamento assintótico demonstrado, implementação histórica identificada e comparação observacional pendente de procedência documental. A proposta de explicar os efeitos atribuídos à matéria escura por fluxo e ondas permanece em investigação.

[Explicação no site público](https://britov1-matriz10-registro.higgsfield.app/#materia-escura)
