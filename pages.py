# -*- coding: utf-8 -*-
"""Conteúdo de cada página do site da Comunidade Casa de Deus."""

def build(write_page, icon, house_watermark, HOUSE_MARK):

    # ============================================================ INÍCIO
    index_content = f'''
  <section class="hero">
    {house_watermark("hero-watermark")}
    <div class="container">
      <div class="hero-inner reveal in">
        <div class="eyebrow">{icon('pin')} Marília · SP</div>
        <h1>Um lugar para chamar<br>de casa.</h1>
        <p class="lead">A Comunidade Casa de Deus é uma família de fé que existe para acolher, cuidar e apontar cada pessoa para Jesus — em qualquer fase da vida em que você esteja.</p>
        <div class="hero-actions">
          <a href="contato.html" class="btn btn-primary">Planeje sua visita</a>
          <a href="mensagens.html" class="btn btn-ghost">Assistir mensagens</a>
        </div>
      </div>
    </div>
  </section>

  <section class="info-strip">
    <div class="container">
      <div class="info-item">{icon('clock')} <span><strong>Domingo</strong> 9h e 18h · <strong>Discipulado toda quinta às</strong> 19h30</span></div>
      <div class="info-item">{icon('pin')} <span>Rua Brasil, 350 — Centro, Marília/SP</span></div>
      <div class="info-item">{icon('whatsapp')} <span>(14) 00000-0000</span></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('heart')} Quem somos</div>
          <h2>Fé simples, portas abertas.</h2>
          <p>Cremos que a igreja é, antes de tudo, uma casa: um lugar de pertencimento, onde ninguém precisa fingir ser quem não é para ser bem recebido. Buscamos viver o evangelho de Jesus de forma prática, no cuidado uns com os outros e no serviço à cidade de Marília.</p>
        </div>
        <a href="sobre.html" class="btn btn-ghost">Nossa história</a>
      </div>
      <div class="grid grid-3">
        <div class="stat reveal"><div class="num">1</div><div class="label">Anos de história</div></div>
        <div class="stat reveal"><div class="num">5</div><div class="label">Ministérios ativos</div></div>
        <div class="stat reveal"><div class="num">1</div><div class="label">Cultos por semana</div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('users')} Comunidade</div>
          <h2>Um espaço para cada pessoa da família.</h2>
        </div>
        <a href="ministerios.html" class="btn btn-ghost">Ver todos os ministérios</a>
      </div>
      <div class="grid grid-3">
        <div class="card reveal">
          <div class="card-icon">{icon('baby')}</div>
          <h3>Casa Kids</h3>
          <p>Um ambiente seguro e divertido para as crianças conhecerem o amor de Deus enquanto os pais estão no culto.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('users')}</div>
          <h3>Juventude</h3>
          <p>Encontros semanais para adolescentes e jovens viverem a fé com propósito, amizade e identidade.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('hand')}</div>
          <h3>Ação Social</h3>
          <p>Projetos de cuidado com famílias em vulnerabilidade social nos bairros ao redor da igreja.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-teal">
    <div class="container text-center">
      <div class="divider-house">{HOUSE_MARK.replace('class="house-mark"', 'class="house-mark" style="width:34px;height:34px;"')}</div>
      <div class="eyebrow" style="justify-content:center;">{icon('book')} Próxima mensagem</div>
      <h2 style="max-width:640px; margin-left:auto; margin-right:auto;">"A casa que Deus constrói sempre tem lugar para mais um."</h2>
      <p style="max-width:560px; margin:0 auto 30px;">Assista às últimas pregações e acompanhe nossa programação de estudos bíblicos direto do nosso canal.</p>
      <a href="mensagens.html" class="btn btn-gold">Ver mensagens</a>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('clock')} Agenda</div>
          <h2>O que está acontecendo</h2>
        </div>
        <a href="eventos.html" class="btn btn-ghost">Ver agenda completa</a>
      </div>
      <div class="event-card reveal">
        <div class="event-date"><div class="day">24</div><div class="month">Ago</div></div>
        <div class="event-info">
          <h3>Noite de Louvor e Adoração</h3>
          <div class="event-meta"><span>{icon('clock')} 19h30</span><span>{icon('pin')} Templo sede</span></div>
        </div>
        <a href="eventos.html" class="btn btn-ghost">Detalhes</a>
      </div>
      <div class="event-card reveal">
        <div class="event-date"><div class="day">06</div><div class="month">Set</div></div>
        <div class="event-info">
          <h3>Retiro de Casais</h3>
          <div class="event-meta"><span>{icon('clock')} 8h</span><span>{icon('pin')} Sítio Recanto, Marília</span></div>
        </div>
        <a href="eventos.html" class="btn btn-ghost">Detalhes</a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container text-center reveal">
      <div class="eyebrow" style="justify-content:center;">{icon('gift')} Primeira vez aqui?</div>
      <h2 style="max-width:560px; margin:0 auto .4em;">Sua primeira visita merece um café e uma boa conversa.</h2>
      <p style="max-width:520px; margin:0 auto 30px;">Conte pra gente que você vem e alguém da equipe de recepção vai te esperar na entrada.</p>
      <a href="contato.html" class="btn btn-primary">Avisar que vou visitar</a>
    </div>
  </section>
'''
    write_page(
        "index.html",
        "Comunidade Casa de Deus — Igreja em Marília, SP",
        "A Comunidade Casa de Deus é uma igreja em Marília, SP. Conheça nossos horários de culto, ministérios, eventos e mensagens.",
        "index.html",
        index_content,
    )

    # ============================================================ SOBRE
    sobre_content = f'''
  <section class="page-hero">
    {house_watermark("hero-watermark", 380)}
    <div class="container reveal in">
      <div class="eyebrow">{icon('heart')} Sobre nós</div>
      <h1>Nossa história é a<br>história de uma casa.</h1>
      <p class="lead">De um pequeno grupo reunido numa sala de estar a uma comunidade que hoje recebe centenas de pessoas em Marília — contamos com você para escrever os próximos capítulos.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="align-items:center; gap:60px;">
        <div class="reveal">
          <div class="eyebrow">{icon('book')} Nossa trajetória</div>
          <h2>Como tudo começou</h2>
          <div class="timeline" style="margin-top:32px;">
            <div class="timeline-item"><div class="year">2004</div><p>Um pequeno grupo de famílias começa a se reunir semanalmente para orar pela cidade de Marília.</p></div>
            <div class="timeline-item"><div class="year">2009</div><p>A Comunidade Casa de Deus é oficialmente constituída e recebe seu primeiro espaço próprio.</p></div>
            <div class="timeline-item"><div class="year">2015</div><p>Nascem os ministérios de ação social, alcançando famílias em situação de vulnerabilidade.</p></div>
            <div class="timeline-item"><div class="year">2024</div><p>Celebramos duas décadas de história com uma comunidade viva, diversa e em constante crescimento.</p></div>
          </div>
        </div>
        <div class="card-photo ph-1 reveal">{icon('globe')}</div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('users')} Missão, visão e valores</div>
          <h2>O que nos move</h2>
        </div>
      </div>
      <div class="grid grid-3">
        <div class="card reveal">
          <div class="card-icon">{icon('globe')}</div>
          <h3>Missão</h3>
          <p>Apresentar Jesus Cristo a Marília e região, formando pessoas que vivem o evangelho em casa, no trabalho e na cidade.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('heart')}</div>
          <h3>Visão</h3>
          <p>Ser uma casa que multiplica famílias saudáveis, discípulos maduros e novas comunidades de fé.</p>
        </div>
        <div class="card reveal">
          <div class="card-icon">{icon('hand')}</div>
          <h3>Valores</h3>
          <p>Acolhimento genuíno, verdade com amor, generosidade e compromisso com a Palavra de Deus.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('book')} O que cremos</div>
          <h2>Nossa declaração de fé</h2>
        </div>
      </div>
      <div class="grid grid-2">
        <div class="card reveal">
          <h3>As Escrituras</h3>
          <p>Cremos que a Bíblia é a Palavra inspirada por Deus, nossa regra de fé e prática.</p>
        </div>
        <div class="card reveal">
          <h3>Deus Trino</h3>
          <p>Cremos em um só Deus, eternamente existente em três pessoas: Pai, Filho e Espírito Santo.</p>
        </div>
        <div class="card reveal">
          <h3>Jesus Cristo</h3>
          <p>Cremos na divindade de Jesus, seu nascimento virginal, morte substitutiva, ressurreição e volta.</p>
        </div>
        <div class="card reveal">
          <h3>Salvação</h3>
          <p>Cremos que a salvação é um presente de Deus, recebido pela graça, mediante a fé em Jesus.</p>
        </div>
      </div>
      <p style="margin-top:20px; font-size:.85rem; color:var(--ink-faint);">Texto de exemplo — substitua pela declaração de fé oficial da sua igreja.</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head reveal">
        <div class="head-text">
          <div class="eyebrow">{icon('users')} Liderança</div>
          <h2>Quem caminha à frente</h2>
        </div>
      </div>
      <div class="grid grid-3">
        <div class="card reveal">
          <div class="card-photo ph-2">{icon('users')}</div>
          <h3>Pr. Nome Sobrenome</h3>
          <p>Pastor titular</p>
        </div>
        <div class="card reveal">
          <div class="card-photo ph-3">{icon('users')}</div>
          <h3>Pra. Nome Sobrenome</h3>
          <p>Pastora de famílias</p>
        </div>
        <div class="card reveal">
          <div class="card-photo ph-4">{icon('users')}</div>
          <h3>Nome Sobrenome</h3>
          <p>Líder de louvor</p>
        </div>
      </div>
    </div>
  </section>
'''
    write_page(
        "sobre.html",
        "Sobre nós — Comunidade Casa de Deus",
        "Conheça a história, missão, visão, valores e liderança da Comunidade Casa de Deus em Marília, SP.",
        "sobre.html",
        sobre_content,
    )

    # ============================================================ MINISTÉRIOS
    ministries = [
        ("baby", "Casa Kids", "Do berçário ao pré-adolescente, um ambiente seguro e alegre para as crianças aprenderem sobre o amor de Deus.", "ph-1"),
        ("users", "Juventude", "Encontros semanais, retiros e discipulado para adolescentes e jovens construírem sua fé e identidade.", "ph-2"),
        ("heart", "Casais", "Encontros e aconselhamento para fortalecer casamentos e famílias em todas as fases.", "ph-3"),
        ("music", "Louvor e Adoração", "Equipe de música e produção responsável por conduzir a igreja em adoração nos cultos e eventos.", "ph-4"),
        ("hand", "Ação Social", "Projetos de apoio a famílias em vulnerabilidade social nos bairros ao redor da igreja.", "ph-1"),
        ("book", "Discipulado", "Trilhas de crescimento espiritual, estudos bíblicos e grupos pequenos durante a semana.", "ph-2"),
        ("globe", "Missões", "Envio e apoio a missionários no Brasil e no exterior, levando o evangelho além dos nossos muros.", "ph-3"),
        ("gift", "Recepção e Acolhimento", "A primeira equipe que você encontra: recebe visitantes com um sorriso e um cafezinho.", "ph-4"),
    ]
    cards = ""
    for icon_name, title, desc, ph in ministries:
        cards += f'''
        <div class="card reveal">
          <div class="card-photo {ph}">{icon(icon_name)}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>'''

    ministerios_content = f'''
  <section class="page-hero">
    {house_watermark("hero-watermark", 380)}
    <div class="container reveal in">
      <div class="eyebrow">{icon('users')} Ministérios</div>
      <h1>Um lugar para servir<br>com seus dons.</h1>
      <p class="lead">Cada pessoa tem um papel na casa. Encontre o ministério onde você pode crescer, servir e fazer parte de algo maior.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-4">{cards}
      </div>
    </div>
  </section>

  <section class="section section-teal">
    <div class="container text-center reveal">
      <div class="eyebrow" style="justify-content:center;">{icon('hand')} Quer servir?</div>
      <h2 style="max-width:560px; margin:0 auto .4em;">Ainda não sabe onde encaixar seus dons?</h2>
      <p style="max-width:520px; margin:0 auto 30px;">Fale com a nossa equipe de integração e a gente ajuda você a encontrar o ministério certo para essa temporada da sua vida.</p>
      <a href="contato.html" class="btn btn-gold">Quero servir</a>
    </div>
  </section>
'''
    write_page(
        "ministerios.html",
        "Ministérios — Comunidade Casa de Deus",
        "Conheça os ministérios da Comunidade Casa de Deus: Casa Kids, Juventude, Casais, Louvor, Ação Social, Discipulado, Missões e mais.",
        "ministerios.html",
        ministerios_content,
    )

    # ============================================================ EVENTOS
    events = [
        ("24", "Ago", "Noite de Louvor e Adoração", "19h30", "Templo sede"),
        ("06", "Set", "Retiro de Casais", "8h", "Sítio Recanto, Marília"),
        ("14", "Set", "Culto de Ação de Graças", "18h", "Templo sede"),
        ("21", "Set", "Encontro de Jovens", "19h", "Salão multiuso"),
        ("05", "Out", "Batismo nas águas", "16h", "Clube de Campo, Marília"),
        ("19", "Out", "Conferência de Família", "9h às 17h", "Templo sede"),
    ]
    ev_html = ""
    for day, month, title, time, place in events:
        ev_html += f'''
      <div class="event-card reveal">
        <div class="event-date"><div class="day">{day}</div><div class="month">{month}</div></div>
        <div class="event-info">
          <h3>{title}</h3>
          <div class="event-meta"><span>{icon('clock')} {time}</span><span>{icon('pin')} {place}</span></div>
        </div>
        <a href="contato.html" class="btn btn-ghost">Inscrever-se</a>
      </div>'''

    eventos_content = f'''
  <section class="page-hero">
    {house_watermark("hero-watermark", 380)}
    <div class="container reveal in">
      <div class="eyebrow">{icon('clock')} Agenda</div>
      <h1>O que está<br>acontecendo na casa.</h1>
      <p class="lead">De noites de louvor a retiros e conferências — confira os próximos encontros e separe a data na sua agenda.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {ev_html}
      <p style="margin-top:24px; font-size:.85rem; color:var(--ink-faint);">Datas de exemplo — atualize com a agenda real da igreja.</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container text-center reveal">
      <div class="eyebrow" style="justify-content:center;">{icon('mail')} Não perca nada</div>
      <h2 style="max-width:520px; margin:0 auto .4em;">Receba os próximos eventos no seu WhatsApp</h2>
      <p style="max-width:480px; margin:0 auto 30px;">Entre no nosso grupo de avisos e fique por dentro da agenda semanal da igreja.</p>
      <a href="contato.html" class="btn btn-primary">Entrar no grupo</a>
    </div>
  </section>
'''
    write_page(
        "eventos.html",
        "Eventos — Comunidade Casa de Deus",
        "Confira a agenda de eventos da Comunidade Casa de Deus em Marília: cultos especiais, retiros, conferências e encontros.",
        "eventos.html",
        eventos_content,
    )

    # ============================================================ MENSAGENS
    sermons = [
        ("ph-1", "Série: Casa", "A casa que Deus constrói", "Pr. Nome Sobrenome · 14 Jul 2026"),
        ("ph-2", "Série: Casa", "Fundamentos que sustentam", "Pr. Nome Sobrenome · 07 Jul 2026"),
        ("ph-3", "Tema livre", "Graça para os dias difíceis", "Pra. Nome Sobrenome · 30 Jun 2026"),
        ("ph-4", "Série: Família", "Pais, filhos e propósito", "Pr. Nome Sobrenome · 23 Jun 2026"),
        ("ph-1", "Tema livre", "O que significa perdoar", "Pr. Nome Sobrenome · 16 Jun 2026"),
        ("ph-2", "Série: Família", "Casamentos que duram", "Pra. Nome Sobrenome · 09 Jun 2026"),
    ]
    sm_html = ""
    for ph, tag, title, meta in sermons:
        sm_html += f'''
        <div class="sermon-card reveal">
          <div class="sermon-thumb {ph}"><div class="play-btn">{icon('play')}</div></div>
          <div class="sermon-body">
            <div class="sermon-tag">{tag}</div>
            <h3>{title}</h3>
            <p style="margin-bottom:0; font-size:.88rem;">{meta}</p>
          </div>
        </div>'''

    mensagens_content = f'''
  <section class="page-hero">
    {house_watermark("hero-watermark", 380)}
    <div class="container reveal in">
      <div class="eyebrow">{icon('book')} Mensagens</div>
      <h1>Palavra que edifica<br>a casa.</h1>
      <p class="lead">Assista ou reveja as pregações mais recentes da Comunidade Casa de Deus, direto do nosso canal.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-3">{sm_html}
      </div>
      <p style="margin-top:24px; font-size:.85rem; color:var(--ink-faint);">Conecte os cards acima aos vídeos reais do seu canal do YouTube.</p>
    </div>
  </section>

  <section class="section section-teal">
    <div class="container text-center reveal">
      <div class="eyebrow" style="justify-content:center;">{icon('youtube')} Ao vivo</div>
      <h2 style="max-width:560px; margin:0 auto .4em;">Não pode vir? Assista ao vivo, de onde estiver.</h2>
      <p style="max-width:480px; margin:0 auto 30px;">Transmitimos nossos cultos de domingo pelo YouTube, todos os domingos às 9h e 18h.</p>
      <a href="#" class="btn btn-gold">Ir para o canal</a>
    </div>
  </section>
'''
    write_page(
        "mensagens.html",
        "Mensagens — Comunidade Casa de Deus",
        "Assista às mensagens e pregações da Comunidade Casa de Deus em Marília, SP.",
        "mensagens.html",
        mensagens_content,
    )

    # ============================================================ CONTATO
    contato_content = f'''
  <section class="page-hero">
    {house_watermark("hero-watermark", 380)}
    <div class="container reveal in">
      <div class="eyebrow">{icon('mail')} Contato</div>
      <h1>Vamos conversar?</h1>
      <p class="lead">Quer visitar a igreja, tirar uma dúvida ou pedir oração? Preencha o formulário ou fale direto com a gente.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-2" style="align-items:flex-start; gap:60px;">
        <div class="reveal">
          <form id="contact-form">
            <div class="grid grid-2">
              <div class="field">
                <label for="name">Nome completo</label>
                <input type="text" id="name" name="name" placeholder="Seu nome" required>
              </div>
              <div class="field">
                <label for="phone">Telefone / WhatsApp</label>
                <input type="tel" id="phone" name="phone" placeholder="(14) 00000-0000">
              </div>
            </div>
            <div class="field">
              <label for="email">E-mail</label>
              <input type="email" id="email" name="email" placeholder="voce@email.com" required>
            </div>
            <div class="field">
              <label for="subject">Assunto</label>
              <select id="subject" name="subject">
                <option>Primeira visita</option>
                <option>Pedido de oração</option>
                <option>Quero servir em um ministério</option>
                <option>Dúvida geral</option>
              </select>
            </div>
            <div class="field">
              <label for="message">Mensagem</label>
              <textarea id="message" name="message" placeholder="Escreva aqui..."></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Enviar mensagem</button>
            <p id="form-feedback" style="display:none; margin-top:16px; font-size:.88rem; color:var(--teal);"></p>
          </form>
        </div>

        <div class="reveal">
          <div class="card" style="margin-bottom:24px;">
            <h3 style="margin-bottom:18px;">Informações</h3>
            <div style="display:flex; flex-direction:column; gap:16px;">
              <div class="info-item">{icon('pin')} <span>Rua Exemplo, 123 — Centro, Marília/SP</span></div>
              <div class="info-item">{icon('phone')} <span>(14) 0000-0000</span></div>
              <div class="info-item">{icon('whatsapp')} <span>(14) 00000-0000</span></div>
              <div class="info-item">{icon('mail')} <span>contato@casadedeusmarilia.org.br</span></div>
              <div class="info-item">{icon('clock')} <span>Domingo 9h e 18h · Quarta 19h30</span></div>
            </div>
          </div>
          <div class="map-frame">
            <iframe src="https://www.google.com/maps?q=Mar%C3%ADlia,SP&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de localização"></iframe>
          </div>
          <p style="margin-top:12px; font-size:.85rem; color:var(--ink-faint);">Substitua o endereço acima pelo endereço real para o mapa apontar para o local certo.</p>
        </div>
      </div>
    </div>
  </section>
'''
    write_page(
        "contato.html",
        "Contato — Comunidade Casa de Deus",
        "Entre em contato com a Comunidade Casa de Deus em Marília, SP. Endereço, telefone, horários de culto e formulário de contato.",
        "contato.html",
        contato_content,
    )
