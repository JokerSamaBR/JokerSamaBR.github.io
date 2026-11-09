# WYO Dev Journal — portal público

Site: https://dev.wyoplay.com/

Vitrine pública de desenvolvimento com descrição dos projetos, atualizações e imagens de demonstração.

## Política de links

O site **não aponta para repositórios GitHub**. Links externos visíveis ficam restritos a:
- https://www.wyoplay.com/
- https://digital.wyoplay.com/

Os links dos próprios artigos e do RSS são internos ao portal.

## Atualizações automáticas

O GitHub Actions prepara o site em `scripts/build_site.py` e publica via GitHub Pages. O sincronizador consulta fontes públicas selecionadas e, quando um token de leitura restrita estiver configurado, também pode importar **somente** manifestos aprovados para publicação de repositórios privados. Nunca exporta código ou mensagens de commit privadas.

Veja `docs/AUTOMACAO.md` para a configuração do token e a política de imagens. O estado do portal não substitui os registros de engenharia nos repositórios de origem.

## Arquivos

- `content/site.json`: conteúdo editorial público base.
- `assets/demos/`: imagens de demonstração aprovadas, hospedadas localmente no Pages.
- `automation/sources.json`: lista interna de fontes, que não aparece no site.
- `scripts/build_site.py`: gerador estático, RSS e sitemap.
- `.github/workflows/publish.yml`: publicação automática sem IA paga.

Repositório público: não armazene senhas, dados de jogadores, código privado ou informações de infraestrutura neste portal.
