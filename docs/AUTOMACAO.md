# Atualização automática e privacidade — WYO Dev Journal

**Portal:** https://dev.wyoplay.com/

## Conteúdo público
O portal apresenta informações e imagens de demonstração autorizadas. Não publica links para repositórios. Os únicos links externos da interface apontam para:
- https://www.wyoplay.com/
- https://digital.wyoplay.com/

As publicações são acessadas por links internos do próprio portal. As imagens ficam hospedadas em assets/demos/, sem apontar para o repositório de origem.

## Como funciona
O GitHub Actions gera o site a cada push e verifica fontes selecionadas **a cada seis horas**. Horários podem atrasar conforme disponibilidade do GitHub.

- Projetos públicos: somente a data de atividade pode ser consultada automaticamente. Não são mostrados mensagens de commits, branches ou URLs de repositórios. Novidades detalhadas dependem de manifesto editorial opt-in.
- Projetos privados: o workflow só lê docs/PUBLIC_SHOWCASE.json, caso exista e tenha publish=true. Não varre código, commits, PRs nem dados internos.
- Imagens novas: somente itens indicados no manifesto e guardados em docs/public-showcase/images/, com extensões PNG, JPEG ou WebP e até 4 MiB por imagem.

**O portal não transforma automaticamente todo commit em notícia.** É necessário que o projeto registre explicitamente informações públicas verificadas. Isso evita divulgar trabalhos incompletos e dados restritos.

## Ativar a consulta de projetos privados
No GitHub, crie um **Personal access token (fine-grained)** somente para os repositórios privados escolhidos. Permissão mínima: **Contents: Read-only**. Em Settings → Secrets and variables → Actions, no repositório público JokerSamaBR.github.io, cadastre o segredo chamado WYO_PUBLIC_FEED_READ_TOKEN.

Nunca cole tokens no chat, README ou arquivos do repositório.

A lista de fontes deve ficar exclusivamente no **segredo GitHub Actions `WYO_PUBLIC_SOURCES_JSON`**, pois esta conta e os nomes dos repositórios monitorados não devem ser publicados em arquivos do portal. O repositório privado precisa conter `docs/PUBLIC_SHOWCASE.json` com `project_id` e `publish=true`. O exemplo editorial fica em `automation/PUBLIC_SHOWCASE.example.json`.

No **Settings → Secrets and variables → Actions**, crie também `WYO_PUBLIC_SOURCES_JSON` com este formato (substitua cada `OWNER/REPO` pelos identificadores reais apenas dentro da área de Secrets, sem publicá-los):

```json
{"sources":[{"project_id":"next","repository":"OWNER/REPO_PRIVADO_1","visibility":"private"},{"project_id":"superzip","repository":"OWNER/REPO_PRIVADO_2","visibility":"private"},{"project_id":"assetstudio","repository":"OWNER/REPO_PUBLICO","visibility":"public"}]}
```

Sem esse segredo, o portal continua público e funcional, mas a importação dos manifestos de origem fica desativada. O segredo de fontes não concede acesso por si só: `WYO_PUBLIC_FEED_READ_TOKEN` continua necessário para os repositórios privados.

## Habilitar deploy automático
No repositório público, Settings → Pages → **Build and deployment → Source: GitHub Actions**. Isso é necessário porque o workflow usa actions/deploy-pages para implantar o artefato compilado; sem essa troca, as execuções podem falhar enquanto o modo de publicação por branch continuar ativo.

Depois, em Actions → Publicar portal WYO Dev Journal → Run workflow, inicie uma execução manual para conferir.

## Modelo de manifesto
```json
{
  "publish": true,
  "project_id": "next",
  "status": "Planejamento",
  "description": "Descrição pública do que o projeto faz.",
  "images": [],
  "updates": [
    {
      "slug": "marco-publico-unico",
      "title": "Nova etapa concluída",
      "date": "2026-11-09",
      "category": "Atualizações",
      "summary": "Resumo publicável, sem prometer recursos inexistentes.",
      "sections": [
        {"title": "O que mudou", "body": "Explicação de uma melhoria confirmada."}
      ]
    }
  ]
}
```

IDs atualmente suportados: next, superzip, assetstudio. Para incluir um novo projeto, adicionar o cartão no conteúdo base e uma fonte correspondente no cadastro privado da automação, se necessário.

## Proteções
- Não copiar repositórios privados integralmente.
- Não divulgar infraestrutura, senhas, endereços internos, dados de jogadores, código, planos de segurança ou conteúdos sujeitos a licenças de terceiros.
- Não inventar imagens. Publicar somente demonstrações autorizadas e com nome identificado.
- Não alterar o repositório protegido rathena-wyo-clean.
- Não usar APIs de IA pagas.

## Demonstrações iniciais
- SuperZIP: telas de compactação, configuração e instaladores.
- WYO Asset Studio: sheet de oito direções existente.
- Outros projetos: ficam sem imagens até haver uma demonstração apropriada.

## Correção de privacidade

O RSS público foi desativado, e os arquivos estáticos existentes não devem mencionar endereços antigos do domínio GitHub Pages nem nomes de repositórios privados. Atenção: remover um arquivo de um repositório público **não apaga suas versões antigas no histórico Git**. Para eliminar essas versões do histórico, é necessária uma operação separada de reescrita, com avaliação de impacto nos clones, builds e referências já compartilhadas. A hospedagem gratuita do GitHub Pages permanece associável à conta pública pelo DNS e pelo próprio GitHub.
