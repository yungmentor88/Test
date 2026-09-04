/* SHUMI wireframe — vanilla JS, only where an interaction genuinely needs it.
   Nothing here is decorative. 9ja LDA */
(function () {
  'use strict';

  /* --- Mobile menu: full-screen, focus-trapped, Escape closes ----------- */
  var menu = document.getElementById('mobile-menu');
  var openBtn = document.querySelector('[data-menu-open]');
  var closeBtn = document.querySelector('[data-menu-close]');

  function focusables(root) {
    return Array.prototype.filter.call(
      root.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])'),
      function (el) { return el.offsetParent !== null; }
    );
  }

  function openMenu() {
    menu.hidden = false;
    openBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    document.body.classList.add('menu-open');
    closeBtn.focus();
  }
  function closeMenu() {
    menu.hidden = true;
    openBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    document.body.classList.remove('menu-open');
    openBtn.focus();
  }
  if (openBtn && menu) {
    openBtn.addEventListener('click', openMenu);
    closeBtn.addEventListener('click', closeMenu);
    menu.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeMenu(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(menu);
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  /* --- Mobile accordions. Label and toggle are separate targets. -------- */
  Array.prototype.forEach.call(document.querySelectorAll('[data-acc]'), function (btn) {
    btn.addEventListener('click', function () {
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      btn.textContent = open ? '+' : '−';
      panel.hidden = open;
    });
  });

  /* --- Desktop nav dropdowns. Click, not hover: nothing on this site
         may depend on hover to be discoverable. ------------------------- */
  var openPanel = null;
  function shutPanel() {
    if (!openPanel) return;
    openPanel.btn.setAttribute('aria-expanded', 'false');
    openPanel.panel.hidden = true;
    openPanel = null;
  }
  Array.prototype.forEach.call(document.querySelectorAll('[data-drop]'), function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var wasOpen = openPanel && openPanel.btn === btn;
      shutPanel();
      if (!wasOpen) {
        btn.setAttribute('aria-expanded', 'true');
        panel.hidden = false;
        openPanel = { btn: btn, panel: panel };
      }
    });
  });
  document.addEventListener('click', shutPanel);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && openPanel) { var b = openPanel.btn; shutPanel(); b.focus(); }
  });

  /* --- Contact dialog -------------------------------------------------- */
  var dlg = document.getElementById('contact-dialog');
  if (dlg) {
    Array.prototype.forEach.call(document.querySelectorAll('[data-contact-open]'), function (b) {
      b.addEventListener('click', function (e) {
        e.preventDefault();
        if (menu && !menu.hidden) closeMenu();
        if (typeof dlg.showModal === 'function') dlg.showModal();
        else dlg.setAttribute('open', '');           /* fallback for old browsers */
        var f = dlg.querySelector('input,textarea');
        if (f) f.focus();
      });
    });
    dlg.querySelector('[data-contact-close]').addEventListener('click', function () { dlg.close(); });

    /* Validation that names the field and says what to fix. */
    var form = dlg.querySelector('form');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = null;
      Array.prototype.forEach.call(form.querySelectorAll('[data-required]'), function (input) {
        var wrap = input.closest('.field');
        var err = wrap.querySelector('.err');
        var empty = !input.value.trim();
        var badEmail = input.type === 'email' && input.value.trim() && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(input.value);
        if (empty || badEmail) {
          wrap.classList.add('is-bad');
          err.hidden = false;
          err.textContent = empty
            ? 'Enter ' + input.dataset.label + ' so we can reply to you.'
            : 'That email address is missing an @ or a domain. Check it and try again.';
          input.setAttribute('aria-invalid', 'true');
          if (!bad) bad = input;
        } else {
          wrap.classList.remove('is-bad');
          err.hidden = true;
          input.removeAttribute('aria-invalid');
        }
      });
      if (bad) { bad.focus(); return; }
      form.hidden = true;
      var ok = dlg.querySelector('.form-ok');
      ok.hidden = false;
      ok.focus();
    });
  }

  /* --- Collection filters (Stories). Works at 3 items and at 30. ------- */
  var grid = document.getElementById('story-grid');
  if (grid) {
    var cards = Array.prototype.slice.call(grid.children);
    var count = document.getElementById('result-count');
    var empty = document.getElementById('empty-state');
    Array.prototype.forEach.call(document.querySelectorAll('[data-filter]'), function (btn) {
      btn.addEventListener('click', function () {
        var want = btn.dataset.filter;
        Array.prototype.forEach.call(document.querySelectorAll('[data-filter]'), function (b) {
          b.setAttribute('aria-pressed', String(b === btn));
        });
        var shown = 0;
        cards.forEach(function (c) {
          var match = want === 'all' || c.dataset.cat === want;
          c.hidden = !match;
          if (match) shown++;
        });
        count.textContent = shown === 1 ? '1 story' : shown + ' stories';
        empty.hidden = shown !== 0;
        grid.hidden = shown === 0;
      });
    });
  }

  /* The preview panel covers a corner of the page on a phone, so it can be
     dismissed. Wireframe-only chrome. */
  var wfTool = document.getElementById('wf-tool');
  var wfShow = document.getElementById('wf-show');
  if (wfTool && wfShow) {
    document.querySelector('[data-wf-hide]').addEventListener('click', function () {
      wfTool.hidden = true; wfShow.hidden = false; wfShow.focus();
    });
    wfShow.addEventListener('click', function () {
      wfTool.hidden = false; wfShow.hidden = true;
      document.querySelector('[data-wf-hide]').focus();
    });
  }

  /* --- WIREFRAME PREVIEW CONTROL ONLY.
         Swaps the 11 October band between its before and after states so the
         client can see both. Not part of the real site. ------------------ */
  var swap = document.querySelector('[data-state-toggle]');
  if (swap) {
    swap.addEventListener('click', function () {
      var before = document.getElementById('state-before');
      var after = document.getElementById('state-after');
      var showingAfter = !after.hidden;
      before.hidden = !showingAfter;
      after.hidden = showingAfter;
      swap.textContent = showingAfter
        ? 'Now showing: before 11 Oct — switch to after'
        : 'Now showing: after 11 Oct — switch to before';
    });
  }
})();
