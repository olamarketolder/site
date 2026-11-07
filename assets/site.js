/* Marketolder · comportamento partilhado por todas as páginas */
(function(){
  var d=document;

  /* Cabeçalho com fundo depois de descer um pouco */
  var nav=d.getElementById('nav');
  function fundo(){if(nav)nav.classList.toggle('sol',window.scrollY>40)}
  window.addEventListener('scroll',fundo,{passive:true});fundo();

  /* Ano no rodapé */
  var ano=d.getElementById('ano');if(ano)ano.textContent=new Date().getFullYear();

  /* Separadores: o fio camel fica por baixo da página atual e acompanha o rato */
  var sep=d.getElementById('separadores');
  if(sep){
    var ol=sep.querySelector('ol'), ind=sep.querySelector('.indicador');
    var links=[].slice.call(sep.querySelectorAll('li:not(.indicador) a'));
    var atual=sep.querySelector('a[aria-current="page"]');
    var poe=function(a){
      if(!a){ind.style.opacity=0;return}
      ind.style.width=a.offsetWidth+'px';
      ind.style.transform='translateX('+a.parentNode.offsetLeft+'px)';
      ind.style.opacity=1;
    };
    links.forEach(function(a){
      a.addEventListener('mouseenter',function(){poe(a)});
      a.addEventListener('focus',function(){poe(a)});
    });
    ol.addEventListener('mouseleave',function(){poe(atual)});
    sep.addEventListener('focusout',function(e){if(!sep.contains(e.relatedTarget))poe(atual)});
    var arruma=function(){
      poe(atual);
      if(atual && ol.scrollWidth>ol.clientWidth) ol.scrollLeft=atual.parentNode.offsetLeft-(ol.clientWidth-atual.offsetWidth)/2;
    };
    arruma();
    if(d.fonts&&d.fonts.ready)d.fonts.ready.then(arruma);
    window.addEventListener('resize',function(){poe(atual)});
    var preso=function(){sep.classList.toggle('preso',sep.getBoundingClientRect().top<=73)};
    window.addEventListener('scroll',preso,{passive:true});preso();
  }

  /* Revelações suaves ao fazer scroll */
  var els=d.querySelectorAll('.rv,.mapa');
  if(!('IntersectionObserver' in window)){for(var i=0;i<els.length;i++)els[i].classList.add('in');return}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.12});
  els.forEach(function(e){io.observe(e)});
})();

/* Contadores dos resultados: sobem até ao valor real quando aparecem (o valor final já está no HTML) */
(function(){
  var alvo=document.querySelector('.numeros');
  if(!alvo||!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var nums=[].slice.call(alvo.querySelectorAll('[data-n]'));
  var fmt=function(v,dec){return v.toFixed(dec).replace('.',',')};
  var io=new IntersectionObserver(function(es){
    if(!es[0].isIntersecting)return; io.disconnect();
    var t0=null, dur=1600;
    nums.forEach(function(el){el.textContent=fmt(0,+(el.dataset.dec||0))});
    var passo=function(t){
      if(!t0)t0=t; var k=Math.min(1,(t-t0)/dur), e=1-Math.pow(1-k,3);
      nums.forEach(function(el){el.textContent=fmt(parseFloat(el.dataset.n)*e,+(el.dataset.dec||0))});
      if(k<1)requestAnimationFrame(passo);
    };
    requestAnimationFrame(passo);
  },{threshold:.4});
  io.observe(alvo);
})();
