#!/usr/bin/env python3
"""Gera as páginas HTML do site da Comunidade Casa de Deus a partir de um
header/footer compartilhados, garantindo consistência entre as páginas."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HOUSE_MARK = '''<svg class="house-mark" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M3 11.5 12 4l9 7.5"/>
  <path d="M5.5 10v9.5a1 1 0 0 0 1 1H9a1 1 0 0 0 1-1V15a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4.5a1 1 0 0 0 1 1h2.5a1 1 0 0 0 1-1V10"/>
  <circle cx="12" cy="12.6" r="1"/>
</svg>'''

def house_watermark(extra_class="", size=520):
    return f'''<svg class="house-mark house-watermark {extra_class}" width="{size}" height="{size}" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M2 11.5 12 3l10 8.5"/>
  <path d="M5 10v10a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1V10"/>
  <circle cx="12" cy="13" r="1"/>
</svg>'''

ICONS = {
"clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
"pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.4"/></svg>',
"phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M4 5c0-.6.4-1 1-1h3l2 5-2 1.4a11 11 0 0 0 5.6 5.6L15 14l5 2v3c0 .6-.4 1-1 1C10.3 20 4 13.7 4 5Z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 6.5 8 6.5 8-6.5"/></svg>',
"insta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17" cy="7" r="0.6" fill="currentColor" stroke="none"/></svg>',
"facebook": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M14 21v-7h2.5l.5-3H14V9c0-.9.3-1.5 1.7-1.5H17V4.8C16.6 4.7 15.6 4.6 14.5 4.6 12.1 4.6 10.5 6 10.5 8.7V11H8v3h2.5v7Z"/></svg>',
"youtube": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><rect x="2.5" y="6" width="19" height="12" rx="3"/><path d="m10.5 9.5 5 2.5-5 2.5Z" fill="currentColor" stroke="none"/></svg>',
"whatsapp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M4 20l1.3-3.8A8 8 0 1 1 8.6 19Z"/><path d="M8.5 9.6c.3 2.6 2.3 4.6 4.9 4.9.9.1 1.1-.5 1.1-1v-.7l1.9.6c.2 1.4-.6 2.6-2 2.7-3.5.3-7-3.2-6.7-6.7.1-1.4 1.3-2.2 2.7-2l.6 1.9h-.7c-.5 0-1.1.2-1 1.1Z" fill="currentColor" stroke="none"/></svg>',
"play": '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M8 5v14l11-7Z"/></svg>',
"heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M12 20s-7.5-4.6-9.8-9C.6 7.4 2.6 4 6.2 4c2 0 3.4 1 5.8 3.6C14.4 5 15.8 4 17.8 4c3.6 0 5.6 3.4 4 7C19.5 15.4 12 20 12 20Z"/></svg>',
"users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="9" cy="8.5" r="3"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9.5" r="2.5"/><path d="M15.5 20a5.2 5.2 0 0 1 6-5"/></svg>',
"music": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/></svg>',
"book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21Z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/></svg>',
"globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3Z"/></svg>',
"baby": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="8" r="4"/><path d="M6 21c0-4 2.5-6.5 6-6.5s6 2.5 6 6.5"/></svg>',
"hand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M8 12.5V5a1.5 1.5 0 0 1 3 0v6"/><path d="M11 11V4a1.5 1.5 0 0 1 3 0v7"/><path d="M14 11.3V6a1.5 1.5 0 0 1 3 0v9c0 3.9-2.5 6.5-6 6.5-2.4 0-3.8-.9-5.4-3l-2.8-4a1.4 1.4 0 0 1 2.2-1.7L7 15"/></svg>',
"gift": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="9" width="18" height="4"/><rect x="5" y="13" width="14" height="8"/><path d="M12 9v12M12 9C10 6 6 6 6 9c0 1.3 1.3 1.3 3 0 1.7 1.3 3 1.3 3 0-2.7 0 0-6 3-3.5S18 9 12 9Z"/></svg>',
}

def icon(name):
    return ICONS[name]

NAV_ITEMS = [
    ("index.html", "Início"),
    ("sobre.html", "Sobre"),
    ("ministerios.html", "Ministérios"),
    ("eventos.html", "Eventos"),
    ("mensagens.html", "Mensagens"),
    ("contato.html", "Contato"),
]

def render_head(title, description):
    return f'''<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><path d=%22M3 11.5 12 4l9 7.5%22 fill=%22none%22 stroke=%22%23B8863E%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M5.5 10v9.5h4V15h5v4.5h4V10%22 fill=%22none%22 stroke=%22%23B8863E%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,600;1,9..144,500&family=Manrope:wght@400;500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">'''

def render_header(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    links_html = "\n        ".join(links)
    return f'''<header class="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">{HOUSE_MARK}Casa de Deus<span>Marília</span></a>
      <nav class="main-nav" id="main-nav">
        {links_html}
      </nav>
      <div class="header-cta">
        <a href="contato.html" class="btn btn-ghost">Visite-nos</a>
        <button class="nav-toggle" id="nav-toggle" aria-label="Abrir menu" aria-expanded="false"><span></span></button>
      </div>
    </div>
  </header>'''

FOOTER = f'''<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-logo">{HOUSE_MARK}Casa de Deus</div>
          <p>Uma comunidade em Marília, SP, aberta para receber você como parte da família. Fé, cuidado e propósito, todos debaixo do mesmo teto.</p>
          <div class="social-row">
            <a href="#" aria-label="Instagram">{icon('insta')}</a>
            <a href="#" aria-label="Facebook">{icon('facebook')}</a>
            <a href="#" aria-label="YouTube">{icon('youtube')}</a>
            <a href="#" aria-label="WhatsApp">{icon('whatsapp')}</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Navegação</h4>
          <ul>
            <li><a href="sobre.html">Sobre nós</a></li>
            <li><a href="ministerios.html">Ministérios</a></li>
            <li><a href="eventos.html">Agenda de eventos</a></li>
            <li><a href="mensagens.html">Mensagens</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Cultos</h4>
          <ul>
            <li>Domingo · 9h e 18h</li>
            <li>Quarta-feira · 19h30</li>
            <li>Círculos de oração · Sexta 20h</li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contato</h4>
          <ul>
            <li>Rua Exemplo, 123 — Centro, Marília/SP</li>
            <li>(14) 0000-0000</li>
            <li>contato@casadedeusmarilia.org.br</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year></span> Comunidade Casa de Deus. Todos os direitos reservados.</span>
        <span>Site placeholder — substitua textos e imagens pelos dados reais da igreja.</span>
      </div>
    </div>
  </footer>'''

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  {head}
</head>
<body>
  {header}

  {content}

  {footer}

  <script src="js/script.js"></script>
</body>
</html>
'''

def write_page(filename, title, description, active, content):
    html = PAGE_TEMPLATE.format(
        head=render_head(title, description),
        header=render_header(active),
        content=content,
        footer=FOOTER,
    )
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"gerado: {filename}")

# As páginas em si são montadas em pages.py (conteúdo específico de cada uma)
if __name__ == "__main__":
    import pages
    pages.build(write_page, icon, house_watermark, HOUSE_MARK)
