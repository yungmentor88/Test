/* SHUMI Concept B — shared JS */
(function(){
  const nav=document.querySelector('.nav');
  const onScroll=()=>nav&&nav.classList.toggle('scrolled',window.scrollY>24);
  onScroll();addEventListener('scroll',onScroll,{passive:true});

  const burger=document.querySelector('.burger'),menu=document.querySelector('.m-menu');
  if(burger&&menu){
    burger.addEventListener('click',()=>{
      const open=menu.classList.toggle('open');
      burger.classList.toggle('open',open);
      burger.setAttribute('aria-expanded',open);
      document.body.style.overflow=open?'hidden':'';
    });
    menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      menu.classList.remove('open');burger.classList.remove('open');document.body.style.overflow='';
    }));
  }

  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{threshold:.12});
  document.querySelectorAll('.rv').forEach(el=>io.observe(el));

  // Quotes
  const quotes=[
    {t:'“There is no limit to what we, as women, can accomplish.”',c:'Michelle Obama'},
    {t:'“When women support each other, incredible things happen.”',c:'A SHUMI Belief'},
    {t:'“I am not free while any woman is unfree.”',c:'Audre Lorde'},
    {t:'“Empowered women don’t wait for doors to open — we build new rooms.”',c:'SHUMI Original'},
    {t:'“Each time a woman stands up for herself, she stands up for all women.”',c:'Maya Angelou'}
  ];
  const bq=document.querySelector('[data-quote]'),cite=document.querySelector('[data-cite]');
  if(bq&&cite){
    let i=0;
    const show=n=>{i=(n+quotes.length)%quotes.length;bq.style.opacity=0;cite.style.opacity=0;
      setTimeout(()=>{bq.textContent=quotes[i].t;cite.textContent='— '+quotes[i].c;bq.style.opacity=1;cite.style.opacity=1;},320);};
    bq.style.transition=cite.style.transition='opacity .3s ease';
    document.querySelectorAll('[data-qprev],[data-qnext]').forEach(btn=>btn.addEventListener('click',()=>show(i+(btn.hasAttribute('data-qnext')?1:-1))));
    setInterval(()=>show(i+1),7000);
  }

  // Countdown to Oct 11 2026
  const cd=document.querySelector('[data-countdown]');
  if(cd){
    const target=new Date('2026-10-11T09:00:00');
    const cells={d:cd.querySelector('[data-d]'),h:cd.querySelector('[data-h]'),m:cd.querySelector('[data-m]'),s:cd.querySelector('[data-s]')};
    const tick=()=>{
      let diff=Math.max(0,target-Date.now());
      const d=Math.floor(diff/864e5);diff-=d*864e5;
      const h=Math.floor(diff/36e5);diff-=h*36e5;
      const m=Math.floor(diff/6e4);diff-=m*6e4;
      const s=Math.floor(diff/1e3);
      cells.d.textContent=d;cells.h.textContent=String(h).padStart(2,'0');
      cells.m.textContent=String(m).padStart(2,'0');cells.s.textContent=String(s).padStart(2,'0');
    };
    tick();setInterval(tick,1000);
  }

  // Forms (demo)
  document.querySelectorAll('form[data-demo]').forEach(f=>f.addEventListener('submit',e=>{
    e.preventDefault();
    const note=f.querySelector('.form-note')||f;
    note.textContent='Thank you — this demo form is not connected yet. In the live site, submissions go straight to the SHUMI team.';
    note.style.color='#ff7aa8';
  }));

  // Count-up
  const counters=document.querySelectorAll('[data-count]');
  const cio=new IntersectionObserver(es=>es.forEach(e=>{
    if(!e.isIntersecting)return;cio.unobserve(e.target);
    const el=e.target,end=+el.dataset.count,suf=el.dataset.suffix||'';
    let t0=null;const dur=1400;
    const step=ts=>{if(!t0)t0=ts;const p=Math.min((ts-t0)/dur,1);
      el.firstChild.textContent=Math.round(end*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(step);};
    requestAnimationFrame(step);
  }),{threshold:.4});
  counters.forEach(el=>cio.observe(el));
})();
