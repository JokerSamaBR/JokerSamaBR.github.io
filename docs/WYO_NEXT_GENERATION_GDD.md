# WYO Next Generation — Documento Mestre de Conceito (GDD)

> Versão 1.0 — 10/11/2026 · Planejamento · Fonte de referência para Godot + Codex · Nenhuma funcionalidade aqui está declarada implementada.

## 1. Visão e princípios

**WYO Next Generation** é um MMORPG 3D de fantasia medieval com identidade autoral. Referência de sensação: aventura social clássica, personagens estilizados, cidades acolhedoras e exploração contínua; não copiar personagens, cenários, mapas, classes, nomes, enredo, efeitos ou recursos protegidos de outros jogos.

**Pilares:** (1) mundo persistente com cinco reinos; (2) combate action em tempo real; (3) NPCs com rotinas, relações, memória e consequências; (4) economia regional verificável; (5) política emergente e territórios; (6) progressão longa; (7) expansões que continuam a história sem apagar decisões.

**Estado real:** conceito e pré-produção editorial. Nada nesta especificação implica que o jogo, servidores, mecânicas ou artes finais já foram implementados. Todas as regras numéricas ainda requerem protótipo e balanceamento.

## 2. História original: Aedrath e a Grande Ruptura

**Aedrath** (nome provisório) era administrado por uma coroa única. A exploração de recursos nas profundezas e ruínas de uma civilização anterior sustentava o império. Um evento chamado **Grande Ruptura** rompeu rotas, isolou regiões e abriu passagens para criaturas nas antigas estruturas subterrâneas. Cinco famílias sobreviventes estabeleceram reinos autônomos e um pacto frágil de não agressão. Entre os reinos existem vilarejos livres, rotas disputadas, territórios sem senhor e ruínas que mudam com novos acontecimentos.

A causa exata da Ruptura é um mistério de longo prazo. Cada reino preserva versões contraditórias. A verdade pode ser revelada em capítulos futuros por investigação dos jogadores e eventos persistentes, sem obrigar uma história linear.

**Regra narrativa:** nenhum reino nasce essencialmente bom ou mau; leis, prosperidade, conflitos e alianças dependem de governantes, organizações, NPCs e jogadores. Evitar qualquer reprodução da mitologia ou enredo de outro jogo.

## 3. Cinco reinos e mundo aberto

O continente tem **cinco reinos** com capitais, monarquias, tesouros, leis, patrulhas, estradas, campos de produção, povoados, masmorras e fronteiras. Seus nomes, brasões, capitais e biomas definitivos ainda não foram aprovados; criar arquivos de dados sem fixar nomenclatura não decidida.

Fora da jurisdição real existem áreas independentes passíveis de comércio, colonização e reivindicação futura. A distribuição geográfica deve sustentar viagens, rotas comerciais, conflitos por recursos e exploração cooperativa. Todas as transições importantes devem persistir no servidor.

**Escala de produção:** construir inicialmente uma cidade jogável, uma estrada, um povoado, uma dungeon curta e uma região fronteiriça; expandir por células/setores após validar rede e simulação.

## 4. Personagens e experiência inicial

Cada conta inicia com **um espaço de personagem**. Novos espaços permanentes poderão ser adquiridos na loja oficial dentro de limites configuráveis. Exclusão de personagem exige confirmação explícita, período opcional de recuperação e bloqueio quando existirem contratos, bens, propriedades ou transações pendentes.

Personagens têm identidade, inventário, equipamento, atributos, habilidades, profissão/ocupações, vínculos sociais, moralidade, reputações locais e relações individuais. A definição de classes, níveis máximos e progressão detalhada permanece um documento de balanceamento a ser elaborado, sem inventar números finais.

## 5. Combate action e exploração

Combate **3D em terceira pessoa**, câmera ajustável, movimento livre, mira ativa, ataques, habilidades, esquiva, dash e cambalhotas; teleporte curto apenas onde fizer sentido para classe e custo. Controle no servidor de dano, cooldown, distância, recursos, inventário e recompensas. Primeira pessoa é expansão futura.

Criaturas habitam mundo e dungeons; IA com patrulha, percepção, perseguição, retorno de território e prioridades de combate. Dungeons introduzem exploração, monstros, recursos, missões, chefes e descobertas sobre a Ruptura. Prever instâncias onde necessário, sem supor um mundo totalmente instanciado.

## 6. NPCs vivos: identidade, rotina e decisões

Todo NPC significativo possui identificador persistente; profissão (comerciante, aventureiro, mercenário, assassino, guarda, lorde, família real etc.); objetivos; inventário/estoque e recursos quando pertinentes; rotina/agenda; vínculos familiares/sociais; conhecimento parcial do mundo; memória de eventos; necessidades; emoções; moralidade; reputação pública/regional; relação individual com personagens e outros NPCs.

NPCs podem viajar, comprar, vender, trabalhar, aventurar-se, contratar, defender-se, formar alianças, mudar objetivos, sofrer perdas, procurar justiça ou vingança. Mudanças devem ocorrer por regras simuláveis e eventos observáveis, não por sorteios sem contexto.

**Escalabilidade:** NPCs próximos usam decisões detalhadas; distantes usam simulação econômica/social agregada por intervalos e eventos. Persistir estados importantes em banco e evitar atualizar todos os NPCs a cada frame.

## 7. Bibliotecas de diálogos modulares

Bibliotecas separadas por assunto: **comércio**, **aventura**, **mercenários**, **organizações clandestinas**, **nobreza e lordes**, **família real**, **guardas e justiça**, **guerra**, **família e sociedade**, **bondade**, **neutralidade**, **maldade**, **vilania**, **vingança**, **luto/medo/raiva/alegria**, **memórias/rumores**, **contratos** e **eventos**.

Uma fala é escolhida a partir de intenção da pergunta ou opção do jogador + papel do NPC + relação com interlocutor + emoção + objetivo + moralidade + leis locais + conhecimento disponível + eventos recentes. O mesmo NPC pode utilizar várias bibliotecas simultaneamente. **Vingança é motivação, não sinônimo de maldade; vilania exige atos graves e persistentes**, não apenas pontuação negativa.

Diálogos têm IDs estáveis, condições, prioridade, variações, localização e efeito permitido. Uma resposta não executa compra, punição, missão ou transferência de item diretamente: o backend valida tudo. NPC não conhece informações que não testemunhou, aprendeu ou recebeu por rumores. Para perguntas livres, usar classificação local de intenções e fallbacks escritos; IA generativa pode ser considerada futuramente, nunca como autoridade sobre o estado do mundo.

## 8. Moralidade, reputação e relacionamentos

**Moralidade** descreve tendências de ações; **reputação pública** descreve como cidades, guildas e reinos percebem o agente; **relacionamento pessoal** descreve a história entre dois indivíduos; **confiança** não é idêntica à simpatia; **emoções** são contextuais e mutáveis. A profissão permanece estável salvo mudança real de ocupação.

Cada jogador terá uma reputação **individual com cada NPC relevante**, começando neutra; ajuda, missões cumpridas, proteção e respeito podem melhorá-la; roubo, ameaça, humilhação, fraude, assassinato de parentes e traição podem reduzi-la. Missões repetitivas não devem gerar amizade ilimitada. Grandes traições podem afetar a confiança mais do que pequenos favores.

Também existem relações **NPC↔NPC**, familiares/sociais e reputação por **região, cidade, guilda e reino**. Um jogador procurado em um reino ainda pode ter um aliado específico. NPC vingativo pode tratar seu amigo de longa data com confiança apesar da hostilidade geral.

**Faixas ilustrativas, não aprovadas como equilíbrio final:** pontuação entre -1000 e +1000, de inimigo a aliado; o significado não é somente numérico. A regra geral está aprovada; pesos, limites e faixas finais ficam em aberto.

## 9. Exemplo canônico de conversa contextual

**Kael**, mercenário, perdeu o irmão e deseja vingança. Com um jogador confiável, diz: “Você sempre me ajudou. Preciso que descubra quem comandou o ataque, mas quero provas.” Com um desconhecido, diz: “Se precisa de uma espada, posso ser contratado; não me pergunte sobre o passado.” Com um inimigo, ameaça encerrar a conversa. Kael pode negociar contrato, investigar, aceitar justiça ou radicalizar, conforme acontecimentos. A profissão não desaparece quando a emoção muda.

**Darian**, comerciante, após uma perda familiar pode manter sua loja e adicionar diálogos de luto e vingança. Se tomar decisões criminosas recorrentes, acessa também variações de maldade/vilania. Uma reconciliação pode reverter o objetivo sem apagar a memória.

## 10. Missões, guildas e mercenários

Missões devem vir de demandas reais do mundo quando possível: coleta, entrega parcial, exploração, escolta, combate, investigação, reparos, suprimentos e defesa. Guildas de aventureiros organizam pedidos e reputação; contratos de mercenários estabelecem preço, duração, obrigações, limites e pagamento garantido. Organizações de assassinos/clandestinas existem como facções narrativas; ações criminosas devem produzir risco, testemunhas e consequências.

Contratos mantêm estado persistente: criado, aceito, ativo, concluído, falhado, cancelado ou litigioso. Toda recompensa deve sair de uma fonte econômica definida ou de emissão controlada, sem duplicação.

## 11. Política, lordes, propriedades e justiça

Reinos têm famílias reais, nobres, lordes, guardas, instituições e tesouros; administram impostos, patrulhas, segurança, oficinas, hospitais, estradas e fortalezas. **Reivindicação de terras, titulação e administração política por jogadores** entram na expansão Era dos Lordes, com liberação administrativa.

Propriedades incluem casas, oficinas, terrenos, lojas e aluguel de **5 a 30 dias** (regra conceitual atual). Venda inicial de terrenos destina **50% à coroa e 50% ao lorde** conforme regra indicada no site; manter configurável por transação/território e auditar distribuição.

Guardas investigam crimes a partir de evidências, testemunhas, alertas e leis locais. Relações pessoais podem influenciar decisões de NPCs, mas não ignorar validação de sistema nem permitir exploração sem consequência.

## 12. Guerras, territórios e sucessão

**Expansão futura, não lançamento:** declarações de guerra territorial com janela de preparação de **5 a 10 dias**, recrutamento de mercenários/jogadores, suprimentos, equipamentos de cerco e batalhas por fortalezas. Resultado transfere controles territoriais sob regras auditáveis.

**Guerra das Coroas** é expansão posterior: jogadores e NPCs podem desafiar a autoridade dos cinco tronos por eventos políticos e militares. Sucessão precisa respeitar propriedade, contratos, tesouro, lealdades e histórico persistente.

## 13. Economia regional e moedas

Moedas comuns: **100 bronze = 1 prata; 100 prata = 1 ouro**. Cada reino tem tesouro inicial **conceitual de 100.000.000 de ouro** registrado no site, sujeito a análise de equilíbrio. Produção, mineração, caça, comércio, reparo, consumo, aluguel, contratos, manutenção, salários e impostos causam fluxos rastreáveis.

**Regra econômica:** transferências não criam moedas; emissões por sistema (loot/recompensas, se previstas) são explicitamente balanceadas e registradas. Preço dos itens considera produção, escassez, demanda real e histórico de vendas concluídas, não apenas anúncios.

NPCs e entidades possuem estoques e saldos apropriados; a simulação distante pode ser agregada para não sobrecarregar o servidor. Separar geração de recursos, circulação monetária e mecanismos de retirada de moeda da economia.

## 14. Cristais, loja oficial e marketplace

**Cristais** é o nome premium provisório (alternativas debatidas: Rubis e Esmeraldas). Emissão inicial mediante pagamentos confirmados; depois os Cristais podem circular entre jogadores. **Nunca converter automaticamente Cristais em ouro** nem permitir saque em dinheiro real por governantes.

Loja oficial: skins originais, animações/efeitos visuais sem dano extra, expansões permanentes e limitadas de inventário, armazém, capacidade de peso e espaços de personagem. A loja oficial é administrada pelo projeto e **não paga o imposto de marketplace**. Evitar pay-to-win; peso extra não deve contornar regras de PvP. Skins de personagens/franquias alheias só com licença.

Marketplace de itens entre jogadores por Cristais: comprador paga 100%; vendedor recebe **80%**; tesouro do reino associado à transação recebe **20%**. Exemplo: venda de 1000 Cristais → 800 vendedor, 200 reino. Usar reserva/escrow, atomicidade, auditoria, prevenção de duplicação, medidas antimanipulação e preços mínimos por categoria. Tesouro real guarda saldos **separados** em moedas comuns e Cristais.

**Marketplace de personagens:** expansão futura; transferência segura entre contas sem compartilhar senhas; bloquear alterações e vendas simultâneas; excluir da transferência saldos premium da conta e bens não pertencentes ao personagem.

## 15. Arte, linguagem visual e produção de assets

Objetivo: fantasia medieval **3D estilizada** com personagens de proporções expressivas, cenários acolhedores, leitura clara de equipamentos e criaturas memoráveis; atmosfera de MMORPG clássico em mundo tridimensional, **com elementos, história e identidade originais**. Não reutilizar logos, sprites, nomes de classes proprietárias, mapas, personagens, trilhas ou elementos reconhecíveis de franquias sem permissão.

Produzir: capa ilustrada; **cinco** visuais de reinos, mapa evolutivo, capitais, vilarejos e dungeons; ícones de bronze/prata/ouro/Cristais; concept sheets de personagens/monstros/NPCs; interfaces de inventário, comércio, diálogo, reputação, mapa, guildas, propriedades e tesouros.

Pipeline gratuito: Blender para modelos/rig/animações; Krita/GIMP/Inkscape para texturas, ilustrações e ícones; Godot para cena e shaders. Arquivos-fonte editáveis e licenças de todos os assets devem ser preservados. SVGs já presentes no site são **arte conceitual**, não imagens finais de jogo.

## 16. Arquitetura Godot e segurança

**Engine cliente:** Godot 4.x, GDScript, recursos e cenas modulares. **Arte:** Blender; formatos GLB/glTF. **Servidor:** arquitetura autoritativa com serviços próprios/open source; a implementação e infraestrutura serão escolhidas após provas de carga, sem afirmar que Godot sozinho garante escala massiva.

Separar: cliente/apresentação; simulação de combate; entidades/NPCs; eventos e agenda; diálogos; economia; inventário; contas; relações; política; persistência; autenticação; observabilidade. O servidor valida inventário, moeda, combate, contratos e permissões. Usar transações de banco para transferências e IDs únicos para itens e operações.

**Contrato de evento sugerido:** `event_id`, `type`, `actor_id`, `target_id`, `region_id`, `timestamp`, `payload`, `visibility`; consumidores idempotentes. **Dados dos NPCs sugeridos:** `npc_id`, `role`, `routine`, `goals`, `morality`, `emotions`, `relationships`, `knowledge`, `memory`, `inventory`, `wallet`, `location`.

O jogo deve suportar localização PT-BR e inglês ao menos como estrutura, e permitir ampliar idiomas posteriormente. Definir política de privacidade, logs mínimos, backups, permissões, anti-cheat e recuperação de dados antes de receber jogadores.

## 17. Codex: instruções de execução por etapas

**Regra mestra:** este documento é fonte da visão; não implementar módulos enormes em uma única tarefa nem inventar decisões abertas. Cada entrega precisa de teste reproduzível, documentação e commit claro em **repositório de jogo separado**, preservando este portal como vitrine.

**Fase 0 — base:** Godot 4.x, projeto versionado, README, estrutura de cenas, convenções GDScript, CI gratuita, importação de um modelo GLB original e movimentação local.

**Fase 1 — vertical slice offline:** personagem, câmera em terceira pessoa, movimentação, ataque, esquiva, inimigo simples, cidade pequena, comércio fictício, UI e save local de teste.

**Fase 2 — multiplayer autoritativo mínimo:** login de teste, sincronização de dois jogadores, inventário e combate validados no servidor, persistência e testes de reconexão.

**Fase 3 — NPCs e diálogos:** agenda, uma profissão comercial, uma profissão mercenária, memória e relação individual, biblioteca contextual e três histórias ramificadas com efeitos auditáveis.

**Fase 4 — economia e sociedade:** moedas comuns, tesouro, contratos, NPCs comerciantes, preços, estoques, guildas, reputação regional, crimes/guardas.

**Fase 5 — conteúdo e segurança:** cinco regiões progressivas, dungeons, ferramentas de GM, telemetria, antiabuso, escalabilidade em simulação distante, backups.

**Fase 6 — loja e lançamento:** somente após auditoria de transações e conformidade de pagamentos, Cristais, skins, expansões e marketplace de itens; testes de carga e beta fechada antes de qualquer lançamento.

**Após lançamento:** territórios/lordes, guerras, sucessão real, personagens negociáveis, primeira pessoa, novas regiões e capítulos.

**Definição de pronto por tarefa:** código que inicia, testes que passam, nenhuma regressão evidente, arquivos-fonte abertos, sem dependência paga obrigatória, log do que mudou e do que ainda falta.

## 18. Matriz de status e decisões em aberto

**Conceitos acordados:** cinco reinos; narrativa original; 3D action; NPCs com memória, profissão, humor, reputação e relações individuais; diálogos modulares; economia comum bronze/prata/ouro; Cristais separados; imposto premium de 20% ao tesouro real em marketplace entre jogadores; expansões futuras de política e personagens.

**Regras propostas/ajustáveis:** faixas numéricas de reputação, tesouro inicial dos reinos, conversões monetárias, prazos de aluguel, preparação de guerra, preços mínimos, limites de inventário/peso, rotinas de NPC, nomes regionais.

**Ainda não definido:** nome definitivo dos cinco reinos; mapa jogável preciso; classes e árvore de habilidades; nível máximo; equipamentos; interface definitiva; requisitos mínimos; número de jogadores simultâneos; topologia de servidores; orçamento operacional; nomes definitivos de moedas premium; cronograma de lançamento. Não apresentar essas lacunas como decisões tomadas.

**Histórico do conceito:** consolidação editorial em 10/11/2026 das discussões disponíveis. Manter este documento sob controle de versão; mudanças de regra devem ter registro de decisão (ADR) e não apagar histórico.
