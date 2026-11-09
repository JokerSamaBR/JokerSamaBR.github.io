# WYO Dev Journal — portal público

Site: https://dev.wyoplay.com/

Vitrine pública de desenvolvimento com descrição dos projetos, atualizações e imagens de demonstração.

## Política de links

O site **não aponta para repositórios GitHub**. Links externos visíveis ficam restritos a:
- https://www.wyoplay.com/
- https://digital.wyoplay.com/

Os links para artigos são internos ao portal. O feed RSS público foi desativado para evitar a divulgação de endereços antigos.

## Atualizações automáticas

O GitHub Actions prepara o site em `scripts/build_site.py` e publica via GitHub Pages. O sincronizador consulta **somente** fontes declaradas no segredo `WYO_PUBLIC_SOURCES_JSON` e usa um token de leitura restrita para importar manifestos aprovados de projetos privados. Nunca exporta código ou mensagens de commit privadas.

Veja `docs/AUTOMACAO.md` para a configuração do token e a política de imagens. O estado do portal não substitui os registros de engenharia nos repositórios de origem.

## Arquivos

- `content/site.json`: conteúdo editorial público base.
- `assets/demos/`: imagens de demonstração aprovadas, hospedadas localmente no Pages.
- As fontes de repositórios ficam **somente** no segredo GitHub Actions `WYO_PUBLIC_SOURCES_JSON`; nenhum nome de repositório monitorado deve ser versionado neste repositório público.
- `scripts/build_site.py`: gerador estático e sitemap, sem RSS.
- `.github/workflows/publish.yml`: publicação automática sem IA paga.

Repositório público: não armazene senhas, dados de jogadores, código privado ou informações de infraestrutura neste portal.
