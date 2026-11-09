# WYO Dev Journal — portal público

Site: https://dev.wyoplay.com/

Vitrine pública de desenvolvimento com descrição dos projetos, atualizações e imagens de demonstração.

## Política de links

O site **não aponta para repositórios GitHub**. Links externos visíveis ficam restritos a:
- https://www.wyoplay.com/
- https://digital.wyoplay.com/

Os links para artigos são internos ao portal. O feed RSS público foi desativado para evitar a divulgação de endereços antigos.

## Atualizações automáticas

O GitHub Actions prepara o site em `scripts/build_site.py` e publica via GitHub Pages. O sincronizador consulta fontes públicas declaradas em `automation/sources.public.json` e fontes privadas explicitamente autorizadas no segredo `WYO_PUBLIC_SOURCES_JSON`, usando um token de leitura restrita. Importa apenas manifestos aprovados ou, para a base técnica protegida, uma data de atividade autorizada. Nunca exporta código ou mensagens de commit privadas.

Veja `docs/AUTOMACAO.md` para a configuração do token e a política de imagens. O estado do portal não substitui os registros de engenharia nos repositórios de origem.

## Arquivos

- `content/site.json`: conteúdo editorial público base.
- `assets/demos/`: imagens de demonstração aprovadas, hospedadas localmente no Pages.
- Fontes públicas autorizadas ficam em `automation/sources.public.json`. Fontes privadas ficam **somente** no segredo GitHub Actions `WYO_PUBLIC_SOURCES_JSON`, sem expor nomes ou credenciais no site.
- `scripts/build_site.py`: gerador estático e sitemap, sem RSS.
- `.github/workflows/publish.yml`: publicação automática e verificação agendada a cada hora, sem IA paga.
- Projetos catalogados: WYO Next Generation, World Yggdrasil Online, WYO Asset Studio, SuperZIP WYO Digital, WYO Digital, WYO Emulator Base (referência protegida) e Midgard Studio WYO Digital.

Repositório público: não armazene senhas, dados de jogadores, código privado ou informações de infraestrutura neste portal.
