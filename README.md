# WYO Dev Journal

Portal público da **WYO Digital**, publicado com **GitHub Pages** e conteúdo editorial separado do repositório privado [WYO Next Generation](https://github.com/JokerSamaBR).

## Publicações

As publicações e os projetos exibidos estão em [content/site.json](content/site.json). Editar esse arquivo na branch `main` atualiza o conteúdo visível automaticamente na próxima publicação do GitHub Pages, pois o navegador lê o JSON atualizado. Alterações no repositório privado **não são divulgadas automaticamente** — somente os textos aprovados para publicação entram aqui.

## Ativar GitHub Pages

Settings → Pages → Build and deployment: `Deploy from a branch`, `main`, `/(root)` → Save.

Endereço padrão: https://jokersamabr.github.io/

## Subdomínio

Depois de publicar, Settings → Pages → Custom domain: `dev.wyoplay.com`. No provedor DNS, criar `CNAME` `dev` para `jokersamabr.github.io`. Habilitar HTTPS quando o certificado estiver disponível.

**Não modificar** `www.wyoplay.com` ou o domínio raiz. Se migrar para o domínio personalizado, atualizar URLs absolutas em `index.html`, `feed.xml` e `sitemap.xml`.

## Arquivos

- `index.html` página inicial com projetos, novidades, busca e filtros.
- `post.html` artigos gerados a partir dos dados editoriais.
- `content/site.json` conteúdo público. Nunca incluir segredos, dados de usuários ou infraestrutura interna.
- `assets/` apresentação, logo próprio e interatividade.
- `feed.xml`, `sitemap.xml`, `robots.txt` ferramentas de descoberta.

Construído com HTML5/CSS3/JavaScript, sem dependências pagas ou backend.
