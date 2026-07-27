# Comunidade Casa de Deus — Site institucional

Site institucional da **Comunidade Casa de Deus**, em Marília/SP. Feito em HTML, CSS e JavaScript puros (sem frameworks, sem build), pronto para publicar no GitHub Pages, Netlify, Vercel ou qualquer hospedagem simples.

Inspirado na estrutura de sites de grandes igrejas do brasil e no mundo, porém com identidade visual própria: paleta clara, tipografia Fraunces + Manrope, e um motivo assinatura (o traço de "casa") usado como marca d'água e divisor ao longo do site.

## Páginas

| Página | Arquivo | Conteúdo |
|---|---|---|
| Início | `index.html` | Boas-vindas, horários, destaques de ministérios, próxima mensagem, próximo evento |
| Sobre | `sobre.html` | História, missão/visão/valores, o que cremos, liderança |
| Ministérios | `ministerios.html` | Grade com os 8 ministérios da igreja |
| Eventos | `eventos.html` | Agenda de eventos |
| Mensagens | `mensagens.html` | Galeria de pregações/vídeos |
| Contato | `contato.html` | Formulário, endereço, telefone, mapa |

## ⚠️ Para eu mesmo lembrar - Antes de publicar — o que editar

Este site foi gerado com **conteúdo de exemplo (placeholder)**. Antes de publicar de verdade, edite:

- **Endereço, telefone, e-mail e horários reais** — aparecem em `contato.html`, no rodapé (repetido em todas as páginas) e em `index.html`.
- **Mapa** — em `contato.html`, troque a URL do `<iframe>` do Google Maps pelo endereço real (busque o endereço no Google Maps, clique em "Compartilhar" → "Incorporar um mapa" e copie o link).
- **Nomes de pastores/liderança** — em `sobre.html`.
- **Redes sociais** — os links `href="#"` nos ícones do rodapé e da página de mensagens.
- **Vídeos de mensagens** — em `mensagens.html`, os cards estão como placeholder; troque por embeds reais do YouTube ou links para o canal.
- **Eventos e datas** — em `eventos.html` e na seção de agenda da home.
- **Formulário de contato** — hoje ele só mostra uma mensagem de confirmação (não envia e-mail de verdade). Para receber os envios, conecte a um serviço como [Formspree](https://formspree.io) ou [EmailJS](https://www.emailjs.com/), ou a um back-end próprio. Veja `js/script.js`, função do `#contact-form`.

## Estrutura do projeto

```
casa-de-deus/
├── index.html
├── sobre.html
├── ministerios.html
├── eventos.html
├── mensagens.html
├── contato.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── build.py        # gera as páginas HTML (opcional, só para manutenção)
├── pages.py         # conteúdo de cada página, usado pelo build.py
└── README.md
```

> `build.py` e `pages.py` são scripts auxiliares usados para gerar as páginas HTML de forma consistente (o mesmo cabeçalho/rodapé em todas). Você **não precisa deles para publicar o site** — pode editar os arquivos `.html` diretamente. Se preferir manter tudo centralizado, edite `pages.py` e rode `python3 build.py` para regenerar as páginas.




## Licença

Use e edite livremente para o site da sua igreja.
