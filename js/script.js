// Comunidade Casa de Deus — interações de front-end (sem dependências)

document.addEventListener('DOMContentLoaded', () => {

  // Menu mobile
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
      const expanded = toggle.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded);
    });
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        toggle.classList.remove('open');
        nav.classList.remove('open');
      });
    });
  }

  // Ano automático no rodapé
  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // Scroll reveal simples
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  // Formulário de contato (sem back-end configurado ainda)
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const feedback = document.querySelector('#form-feedback');
      if (feedback) {
        feedback.textContent = 'Mensagem pronta para ser enviada! Conecte este formulário a um serviço de e-mail (ex: Formspree, EmailJS) ou back-end para receber os envios de verdade.';
        feedback.style.display = 'block';
      }
      contactForm.reset();
    });
  }
});

// Botões de copiar (chave PIX e código copia e cola)
document.querySelectorAll('.copy-btn').forEach(btn => {
  const label = btn.innerHTML;
  btn.addEventListener('click', async () => {
    const source = btn.dataset.copyFrom ? document.getElementById(btn.dataset.copyFrom) : null;
    const text = source ? source.textContent.trim() : btn.dataset.copy;
    let ok = false;
    try {
      await navigator.clipboard.writeText(text);
      ok = true;
    } catch (e) {
      const tmp = document.createElement('textarea');
      tmp.value = text;
      tmp.setAttribute('readonly', '');
      tmp.style.position = 'absolute';
      tmp.style.left = '-9999px';
      document.body.appendChild(tmp);
      tmp.select();
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      tmp.remove();
    }
    const status = document.getElementById('copy-status');
    if (ok) {
      btn.classList.add('copied');
      btn.textContent = btn.dataset.done || 'Copiado';
      if (status) status.textContent = btn.dataset.done || 'Copiado';
      setTimeout(() => { btn.classList.remove('copied'); btn.innerHTML = label; }, 2500);
    } else if (source) {
      const range = document.createRange();
      range.selectNodeContents(source);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      btn.textContent = 'Selecionado, copie com Ctrl+C';
      setTimeout(() => { btn.innerHTML = label; }, 3000);
    }
  });
});
