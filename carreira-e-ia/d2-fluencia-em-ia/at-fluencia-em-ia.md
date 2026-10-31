# Assessment — Fluência em IA


## Parte 1 — Contextualização

| **Tarefa escolhida**      | Analisar estatísticas da Copa do Mundo para identificar quais seleções possuem maior probabilidade de chegar às fases finais e conquistar a taça.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Como a IA pode ajudar** | A IA pode auxiliar reunindo e interpretando estatísticas de desempenho das seleções identificando padrões em dados como vitórias, gols marcados, gols sofridos e aproveitamento recente etc... Ela também pode comparar equipes, gerar rankings, resumir tendências e apresentar os resultados em linguagem mais clara facilitando a análise das seleções com maior probabilidade de chegar às fases finais e ganhar o título.                                                                                                                                                                                                                   |
| **Riscos**                | Há diversos riscos que podem afetar essa análise mas destaco principalmente a dependência da qualidade dos dados, caso as estatísticas utilizadas estejam desatualizadas, incompletas ou incorretas as conclusões obtidas podem não refletir a realidade, além disso existem limitações do próprio modelo de IA. O futebol envolve fatores imprevisíveis, como lesões, decisões táticas, pressão psicológica, arbitragem e até mesmo a emoção dos jogadores e torcedores. Por isso a IA pode apenas estimar probabilidades e tendências, não sendo capaz de garantir resultados futuros com 100% de precisão.                                    |
| **Resposta ideal**        | A resposta ideal deve apresentar uma análise clara e organizada das seleções, utilizando tabelas, rankings e explicações objetivas para facilitar a compreensão dos dados, espero que a IA compare o desempenho das equipes com base nas estatísticas fornecidas, destacando seus pontos fortes e fracos e justificando as previsões realizadas. O tom deve ser analítico e imparcial, evitando favoritismos, e o tamanho da resposta deve ser suficiente para detalhar a análise sem se tornar excessivamente extensa. Além disso, é importante que as conclusões sejam baseadas nos dados apresentados e não apenas em opiniões ou suposições. |

## Parte 2 — Os Três Prompts

### Prompt 1 — O prompt fraco

- **Modelo utilizado:** Gemini (Pro) para Estudantes
- **Texto do prompt:** Analise as estatísticas da Copa do Mundo e diga quais seleções têm mais chance de chegar às fases finais e ganhar a taça.
- **Resposta obtida:** Ver resposta completa no Anexo 1.
- **O que faltou:** Embora a resposta tenha apresentado informações relevantes e bem estruturadas, o prompt não definiu critérios específicos para a análise, não foram informadas quais estatísticas deveriam ser priorizadas nem o período de tempo a ser considerado além disso o prompt não solicitava um formato específico de saída como um ranking detalhado, uma metodologia de cálculo ou a explicação dos critérios utilizados para determinar as probabilidades, também não foram estabelecidas restrições quanto às fontes dos dados ou ao tamanho da resposta. Dessa forma, apesar de completa, a análise ficou dependente das escolhas feitas pela própria IA e não necessariamente alinhada ao que o usuário poderia esperar. A ausência de restrições e critérios mais claros também pode aumentar a possibilidade de erros, interpretações incorretas ou conclusões baseadas em dados incompletos, desatualizados ou pouco confiáveis.

### Prompt 2 — Com os 6 ingredientes

- **Modelo utilizado:** Gemini (Pro) para Estudantes
- **Texto do prompt:** Você é um analista esportivo especializado em estatísticas e previsões de competições internacionais de futebol. Sua tarefa é analisar as estatísticas da Copa do Mundo de 2026 para identificar quais seleções possuem maior probabilidade de chegar às fases finais e conquistar a taça. O objetivo desta análise é produzir uma avaliação fundamentada em dados estatísticos, considerando o desempenho recente das seleções, seu histórico em Copas do Mundo, ranking internacional, desempenho nas eliminatórias e outros indicadores relevantes. Utilize como entrada dados estatísticos recentes sobre as principais seleções participantes da Copa do Mundo de 2026, incluindo vitórias, derrotas, gols marcados, gols sofridos, aproveitamento e posição no ranking mundial. Apresente a resposta em formato de relatório organizado, contendo uma introdução, uma tabela com as cinco seleções mais bem avaliadas, uma justificativa para cada posição no ranking e uma conclusão final. Utilize um tom analítico, objetivo e imparcial. A resposta deve possuir entre 400 e 600 palavras. Não faça afirmações sem justificativa estatística, não demonstre favoritismo por nenhuma seleção e deixe claro que as previsões representam probabilidades e não garantias de resultados futuros.
- **Resposta obtida:** Ver resposta completa no Anexo 2.

**Mapeamento dos 6 ingredientes:**

- **Persona:** Você é um analista esportivo especializado em estatísticas e previsões de competições internacionais de futebol
- **Tarefa:** Sua tarefa é analisar as estatísticas da Copa do Mundo de 2026 para identificar quais seleções possuem maior probabilidade de chegar às fases finais e conquistar a taça.
- **Contexto:** O objetivo desta análise é produzir uma avaliação fundamentada em dados estatísticos, considerando o desempenho recente das seleções, seu histórico em Copas do Mundo, ranking internacional, desempenho nas eliminatórias e outros indicadores relevantes.
- **Entrada:** Utilize como entrada dados estatísticos recentes sobre as principais seleções participantes da Copa do Mundo de 2026, incluindo vitórias, derrotas, gols marcados, gols sofridos, aproveitamento e posição no ranking mundial
- **Saída esperada:** Apresente a resposta em formato de relatório organizado, contendo uma introdução, uma tabela com as cinco seleções mais bem avaliadas, uma justificativa para cada posição no ranking e uma conclusão final. Utilize um tom analítico, objetivo e imparcial. A resposta deve possuir entre 400 e 600 palavras
- **Restrições:** Não faça afirmações sem justificativa estatística, não demonstre favoritismo por nenhuma seleção e deixe claro que as previsões representam probabilidades e não garantias de resultados futuros.

### Prompt 3 — Com técnica adicional


- **Modelo utilizado:** Gemini (Pro) para Estudantes
- **Técnica escolhida:** Chain of Thought (Raciocínio em Etapas)
- **Como ela funciona:** A técnica Chain of Thought orienta a IA a dividir um problema em etapas lógicas antes de apresentar a conclusão final dessa forma a análise se torna mais estruturada, transparente e fundamentada, permitindo que cada fator relevante seja avaliado separadamente antes da elaboração do resultado final.
- **Texto do prompt:** Você é um analista esportivo especializado em estatísticas e previsões de competições internacionais de futebol. Sua tarefa é analisar as estatísticas da Copa do Mundo de 2026 para identificar quais seleções possuem maior probabilidade de chegar às fases finais e conquistar a taça. O objetivo desta análise é produzir uma avaliação fundamentada em dados estatísticos, considerando o desempenho recente das seleções, seu histórico em Copas do Mundo, ranking internacional, desempenho nas eliminatórias e outros indicadores relevantes. Utilize como entrada dados estatísticos recentes sobre as principais seleções participantes da Copa do Mundo de 2026, incluindo vitórias, derrotas, gols marcados, gols sofridos, aproveitamento e posição no ranking mundial. Antes de apresentar a conclusão final, realize a análise em etapas. Primeiro avalie o desempenho recente das seleções, depois analise o histórico em Copas do Mundo, em seguida compare os indicadores ofensivos e defensivos, avalie a consistência dos resultados recentes e somente depois elabore o ranking final das seleções com maior probabilidade de chegar às fases finais e conquistar a taça. Explique brevemente o raciocínio utilizado em cada etapa. Apresente a resposta em formato de relatório organizado, contendo uma introdução, uma tabela com as cinco seleções mais bem avaliadas, uma justificativa para cada posição no ranking e uma conclusão final. Utilize um tom analítico, objetivo e imparcial. A resposta deve possuir entre 400 e 600 palavras. Não faça afirmações sem justificativa estatística, não demonstre favoritismo por nenhuma seleção e deixe claro que as previsões representam probabilidades e não garantias de resultados futuros.
- **Resposta obtida:** Ver resposta completa no Anexo 3.

## Parte 3 — Comparação Final

*O que mudou entre o Prompt 1 e 3? A resposta final atendeu ao objetivo da Parte 1? Se não, o que faltou?*



## Anexos — respostas completas da IA


---

### Anexo 1 — resposta do Prompt 1

A Copa do Mundo de 2026 começa exatamente hoje, 11 de junho, e traz um cenário estatístico inédito. Com a expansão para 48 seleções e a introdução de uma fase eliminatória extra (os 16-avos de final), o torneio se tornou matematicamente mais imprevisível. Nenhuma seleção chega com um favoritismo absoluto, pois o caminho até a taça agora exige sobreviver a cinco jogos de mata-mata.

Abaixo, apresento a análise detalhada das seleções com maiores chances de chegar às fases finais e conquistar o título, baseada nas simulações mais recentes de supercomputadores (que rodam o torneio dezenas de milhares de vezes) e na precificação do mercado de apostas para o início da competição.

#### 🏆 Probabilidades de Título: As Principais Favoritas

A tabela a seguir consolida as estatísticas dos modelos preditivos focados na Copa de 2026 e as cotações médias globais (odds):

| Seleção    | Probabilidade de Título (Simulações) | Cotação Média (Mercado) | Destaque Analítico                                                                                                |
|------------|--------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Espanha    | 14,5% a 17,0%                        | 5.50                    | Atual líder do ranking da FIFA e campeã da Eurocopa. Domínio tático focado em posse e juventude.                  |
| França     | 12,4% a 16,1%                        | 6.00                    | Elenco mais profundo do torneio e histórico de peso (duas finais consecutivas nas últimas edições).               |
| Inglaterra | 12,4% a 15,0%                        | 7.50                    | Alta eficiência no ciclo preparatório, mas enfrenta o peso histórico em fases decisivas.                          |
| Argentina  | 10,0% a 24,0%\*                      | 10.00                   | Atual campeã mundial. \*Alguns modelos baseados em sistema Elo dão favoritismo pela facilidade da fase de grupos. |
| Alemanha   | 11,2% a 13,0%                        | 12.00                   | Renovação tática sob o comando de Nagelsmann, superando as decepções dos ciclos anteriores.                       |
| Brasil     | 4,7% a 10,0%                         | 9.50                    | Maior campeão histórico, mas entra com probabilidades diluídas em relação aos líderes europeus.                   |

#### 📈 Análise de Chegada às Fases Finais

Com o novo chaveamento, chegar à reta final exige uma consistência defensiva altíssima. Veja como as estatísticas projetam o avanço das principais potências:

- O Domínio Europeu (Espanha e França): A Espanha e a França são as seleções que mais aparecem nas simulações alcançando as semifinais. A Espanha se destaca por sofrer, em média, menos de 0,8 gols por partida no ciclo recente, um fator determinante para sobreviver a cinco jogos eliminatórios.

- O Caminho da Argentina: O modelo estatístico da Universidade de Reading aponta que o chaveamento inicial da Argentina (cruzando com seleções de ranking inferior na fase de grupos) infla suas chances de chegar, pelo menos, até as quartas de final sem grande desgaste físico.

- O Cenário do Brasil: O supercomputador da *Fast Company*, que simulou a Copa 100 mil vezes, traçou o seguinte caminho probabilístico para a Seleção Brasileira:

  - Avançar da fase de grupos: 92%

  - Chegar às oitavas de final: 56%

  - Alcançar as quartas de final: 33%

  - Conquistar o título: 4,7%

#### ⚖️ O Fator "48 Seleções" e a Margem para Zebras

As estatísticas de 2026 deixam um aviso claro: este é o torneio mais propenso a surpresas da história moderna.

No formato antigo de 32 times, a base histórica mostrava que os grandes campeões concentravam quase 90% das chances de vitória. Agora, o meio do pelotão ganhou força. Seleções como Holanda, Portugal, Colômbia e os anfitriões (Estados Unidos e México) diluem as probabilidades dos líderes.

Mesmo a Espanha, que lidera a maioria absoluta dos modelos de previsão com cerca de 14,5% de chance de título, carrega estatisticamente 85,5% de chance de não ser campeã. O torneio exigirá elencos longos, já que o desgaste físico e o risco de lesões na fase de 16-avos de final podem derrubar favoritos precocemente.

---

### Anexo 2 — resposta do Prompt 2

#### Relatório Analítico: Probabilidades Estruturais para a Copa do Mundo FIFA 2026

#### Introdução

O presente relatório analisa o panorama competitivo da Copa do Mundo FIFA 2026 com base em métricas de desempenho recente, histórico na competição, posições no ranking internacional e eficiência nas fases preparatórias. Com a expansão do torneio para 48 seleções, a complexidade estatística das fases eliminatórias aumentou significativamente. As avaliações a seguir foram extraídas de cruzamentos de dados do sistema de pontuação global e de modelos de simulação esportiva, visando mensurar o potencial matemático de chegada às fases decisivas. Cumpre ressaltar que as estimativas apresentadas representam probabilidades calculadas a partir de dados concretos e não constituem, em nenhuma hipótese, garantias de resultados futuros no esporte.

#### As Cinco Seleções com Maior Probabilidade de Título

| Posição | Seleção    | Ranking FIFA | Probabilidade Estimada | Indicador Estatístico de Destaque                   |
|---------|------------|--------------|------------------------|-----------------------------------------------------|
| 1       | Argentina  | 1º           | 24,0%                  | Retrospecto defensivo recente nulo em amistosos     |
| 2       | Espanha    | 2º           | 14,5%                  | Média ofensiva (\> 2 gols/jogo na última temporada) |
| 3       | França     | 3º           | 12,4%                  | Aproveitamento de 68% no ciclo pós-2022             |
| 4       | Inglaterra | 4º           | 12,4%                  | 90% de vitórias nos últimos 10 jogos oficiais       |
| 5       | Brasil     | 6º           | 4,7% a 9,0%            | Probabilidade de 92% de avanço aos mata-matas       |

#### Justificativas Estatísticas

- 1\. Argentina: A seleção sul-americana retomou recentemente o topo do ranking mundial da FIFA, somando 1877.27 pontos. A equipe sustenta um aproveitamento altamente consistente no atual ciclo, validado por vitórias em testes preparatórios sem sofrer gols (com um saldo positivo de 8 gols nas partidas mais recentes). De acordo com modelos de simulação computacional baseados no sistema Elo, a equipe detém 24% de probabilidade de conquista, favorecida pelo cruzamento analítico de sua chave inicial.

- 2\. Espanha: Atual campeã continental na Europa e vice-líder do ranking global (1874.71 pontos), a seleção apresenta métricas de domínio de posse de bola superiores à média. O registro aponta um alto volume ofensivo, com mais de dois gols marcados por partida contra uma defesa que cede apenas 0,8 gols em média. Essa margem de segurança a consolida com cerca de 14,5% de chance de título em projeções de longo prazo.

- 3\. França: Posicionada em terceiro lugar (1870.70 pontos), a seleção europeia demonstra extrema consistência estrutural. A equipe manteve uma taxa de vitórias próxima a 68% nos confrontos recentes. Aliada ao histórico de eficácia em fases eliminatórias nos últimos dois mundiais, a modelagem estatística atribui-lhe uma probabilidade de 12,4% para a conquista da taça.

- 4\. Inglaterra: Ocupando a quarta colocação mundial (1828.02 pontos), o grupo chega com índices robustos de eficiência na conversão de chances. Com nove vitórias nos últimos dez compromissos em campo, os dados refletem uma maturação tática. Pelos mesmos modelos algorítmicos que avaliam a França, a Inglaterra apresenta empatadas 12,4% de probabilidade matemática de ser campeã.

- 5\. Brasil: Embora ocupe atualmente a sexta posição no ranking (1765.86 pontos) após oscilações pontuais nas eliminatórias, o histórico do país mais vezes campeão influencia fortemente os modelos de projeção. Simulações indicam que a equipe possui 92% de chance de superar a fase de grupos e 56% de avançar até as oitavas de final. Devido ao aproveitamento mais volátil recentemente, sua probabilidade de título direto sofreu decréscimo, ficando entre 4,7% e 9%, mas seu alto volume de criação ofensiva garante a permanência no grupo de elite.

#### Conclusão

A análise puramente estatística evidencia que o escalão de elite do futebol mundial encontra-se altamente equilibrado. A Argentina desponta numericamente tracionada por sua impenetrabilidade defensiva de curto prazo, sendo acompanhada de perto pela supremacia da posse de bola da Espanha e pelas eficiências convergentes de França e Inglaterra. O Brasil compensa instabilidades recentes com a mais alta probabilidade matemática de progressão primária nas chaves. Reforça-se, por fim, que o acréscimo de uma nova etapa eliminatória eleva a imprevisibilidade geral, restando à estatística a função de mensurar tendências, jamais prever o imprevisível.

---

### Anexo 3 — resposta do Prompt 3

Relatório Analítico: Previsões e Probabilidades para a Copa do Mundo FIFA 2026

Introdução

Este relatório técnico avalia as probabilidades de sucesso das principais seleções na Copa do Mundo de 2026. Utilizando um modelo baseado em dados estatísticos objetivos — incluindo o ranking mundial atualizado de junho de 2026, métricas de eficiência e histórico —, o objetivo é traçar o panorama das equipes com maiores chances de alcançar as finais, mantendo rigorosa imparcialidade.

Análise em Etapas

- 1\. Desempenho Recente das Seleções: O primeiro filtro avalia a pontuação no ranking oficial e os resultados pré-torneio. Seleções como Argentina (1ª colocada com 1877 pontos) e Espanha (2ª com 1874) demonstraram excelente forma. O raciocínio estatístico é que o momento de vitórias recentes reflete o grau de entrosamento tático e físico da equipe.

- 2\. Histórico em Copas do Mundo: Em seguida, pondera-se a tradição e a experiência em competições de alto nível. O Brasil lidera a métrica histórica geral, seguido por Alemanha e Argentina. Equipes com lastro de títulos possuem vantagem estatística documentada ao lidar com cenários de alta pressão mental e mata-mata.

- 3\. Indicadores Ofensivos e Defensivos: A terceira etapa confronta a média de gols marcados e sofridos por jogo no último ciclo. A França destaca-se pela letalidade e volume ofensivo, enquanto equipes como a Inglaterra têm apresentado métricas severas de solidez defensiva. O saldo de gols consistente é o preditor mais forte de avanço em torneios curtos.

- 4\. Consistência dos Resultados Recentes: Por fim, mede-se a variância técnica. Portugal e Espanha mostraram alta capacidade de evitar derrotas contra adversários do "top 10" global, minimizando desvios padrão. A consistência reduz a probabilidade estatística de eliminações precoces para zebras.

Classificação Probabilística (Top 5)

A tabela abaixo consolida as variáveis analisadas para elencar as maiores probabilidades estatísticas de título para o torneio de 2026:

| Posição | Seleção    | Pontos Atuais | Probabilidade Projetada | Indicador Estatístico Principal         |
|---------|------------|---------------|-------------------------|-----------------------------------------|
| 1       | Argentina  | 1877          | Altíssima               | Baixa variância de resultados recentes  |
| 2       | Espanha    | 1874          | Alta                    | Alto volume de controle e posse de bola |
| 3       | França     | 1870          | Alta                    | Elevada conversão de chances no ataque  |
| 4       | Inglaterra | 1828          | Média-Alta              | Baixa média de gols sofridos por jogo   |
| 5       | Portugal   | 1767          | Média-Alta              | Consistência em jogos eliminatórios     |

Justificativas do Ranking

- 1\. Argentina: Retornou ao topo do ranking global em junho de 2026 após vitórias contundentes (com saldo positivo de oito gols nos últimos dois jogos preparatórios). Sendo a atual campeã, a seleção alia excelente retrospecto recente à experiência inquestionável para gerenciar os minutos finais de partidas decisivas.

- 2\. Espanha: Consolidada na vice-liderança global. A equipe apresenta métricas de posse de bola superiores à média, o que reduz substancialmente as finalizações permitidas ao adversário. A recente vitória por 3 a 1 sobre o Peru confirma a confiabilidade deste sistema.

- 3\. França: Apesar de uma ligeira oscilação que a rebaixou ao terceiro posto, possui os melhores indicadores de transição ofensiva rápida do ciclo. O histórico de chegar às duas últimas finais consecutivas aumenta consideravelmente suas projeções em modelos matemáticos esportivos.

- 4\. Inglaterra: A equipe fundamenta sua quarta posição na eficiência de sua defesa, sofrendo pouquíssimos gols no ciclo de eliminatórias europeias. Em formatos de torneio eliminatório, bloquear os adversários apresenta alta correlação com a chegada às semifinais.

- 5\. Portugal: Fechando o top 5 (superando estatisticamente o Brasil no ranking de junho), o elenco combina alta produção de gols por partida e regularidade contra os times mais bem ranqueados da Europa, demonstrando maturidade tática para enfrentar diferentes estilos de jogo.

Conclusão

Os cruzamentos de dados sugerem que Argentina, Espanha e França adentram a Copa do Mundo de 2026 com as estruturas de probabilidade mais robustas do torneio, justificadas pelos seus balanços de gols e consistência. Contudo, é fundamental ressaltar que estas avaliações técnicas representam estritamente projeções de probabilidade baseadas em dados passados e não são garantias de resultados futuros, respeitando a inerente aleatoriedade do esporte.
