# Atualização automática e privacidade — WYO Dev Journal

**Portal:** https://dev.wyoplay.com/

## Conteúdo público
O portal apresenta informações e imagens de demonstração autorizadas. Não publica links para repositórios. Os únicos links externos da interface apontam para:
- https://www.wyoplay.com/
- https://digital.wyoplay.com/

As publicações são acessadas por links internos do próprio portal. As imagens ficam hospedadas em assets/demos/, sem apontar para o repositório de origem.

## Como funciona

O GitHub Actions gera e publica o portal após alterações na branch principal, quando acionado manualmente e **a cada hora** (o agendamento do GitHub pode sofrer atrasos).

- **Fontes públicas:** registradas em `automation/sources.public.json`. Atualmente Asset Studio e MidgardStudio. A leitura é automática e não precisa de token extra.
- **Fontes privadas:** somente as aprovadas no segredo `WYO_PUBLIC_SOURCES_JSON`, com um fine-grained PAT de acesso **Contents: Read-only** no segredo `WYO_PUBLIC_FEED_READ_TOKEN`. O token deve ter acesso apenas aos repositórios selecionados.
- **Publicação editorial:** um manifesto `docs/PUBLIC_SHOWCASE.json` com `publish=true` permite importar descrição, status e atualizações verificadas. O campo `updates` deve conter objetos estruturados.
- **Base protegida:** a fonte `emulator` pode usar `metadata_only=true` (opção explícita) para mostrar apenas a data de atividade. Nenhum arquivo, commit ou código desse repositório é modificado.
- **Imagens:** só são importadas do diretório `docs/public-showcase/images/` da fonte, com assinatura de arquivo válida e até 4 MiB. Sem manifesto/imagem autorizada, o portal mantém suas imagens locais existentes.
- **Privacidade:** nenhuma URL do GitHub, segredo, mensagem de commit ou código privado é exportado no site.

Sem os segredos, **os projetos privados permanecem visíveis como cartões editoriais**, mas a atividade deles não será atualizada automaticamente.

## Ativar monitoramento dos repositórios privados

Abra o repositório do portal, em **Settings → Secrets and variables → Actions**.

1. Cadastre `WYO_PUBLIC_FEED_READ_TOKEN` com um token fine-grained de leitura, restrito aos repositórios privados escolhidos e à permissão **Contents: Read-only**.
2. Cadastre `WYO_PUBLIC_SOURCES_JSON` no formato abaixo. Substitua os identificadores pelos nomes completos reais apenas dentro do campo secreto:

```json
{
  "sources": [
    {"project_id":"next", "repository":"OWNER/REPO_NEXT", "visibility":"private"},
    {"project_id":"superzip", "repository":"OWNER/REPO_SUPERZIP", "visibility":"private"},
    {"project_id":"emulator", "repository":"OWNER/REPO_BASE_PROTEGIDA", "visibility":"private", "metadata_only":true}
  ]
}
```

Não cadastre fontes privadas em `automation/sources.public.json`. O segredo de fontes **não concede acesso** sem o token de leitura. O sincronizador só publica os dados autorizados e não altera os repositórios de origem.

**IDs aceitos no portal:** `next`, `online`, `assetstudio`, `superzip`, `digital`, `emulator`, `midgardstudio`. Outros projetos exigem cadastro prévio em `content/site.json`.

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

Os projetos cadastrados em `content/site.json` recebem atualizações das fontes que forem explicitamente autorizadas.

## Proteções
- Não copiar repositórios privados integralmente.
- Não divulgar infraestrutura, senhas, endereços internos, dados de jogadores, código, planos de segurança ou conteúdos sujeitos a licenças de terceiros.
- Não inventar imagens. Publicar somente demonstrações autorizadas e com nome identificado.
- Não alterar o repositório protegido rathena-wyo-clean.
- Não usar APIs de IA pagas.

## Demonstrações iniciais
- SuperZIP: telas de compactação, configuração e instaladores (mantidas no portal).
- WYO Asset Studio: sheet de oito direções existente.
- Outros projetos: ficam sem imagens até haver uma demonstração apropriada.

## Correção de privacidade

O RSS público foi desativado, e os arquivos estáticos existentes não devem mencionar endereços antigos do domínio GitHub Pages nem nomes de repositórios privados. Atenção: remover um arquivo de um repositório público **não apaga suas versões antigas no histórico Git**. Para eliminar essas versões do histórico, é necessária uma operação separada de reescrita, com avaliação de impacto nos clones, builds e referências já compartilhadas. A hospedagem gratuita do GitHub Pages permanece associável à conta pública pelo DNS e pelo próprio GitHub.
