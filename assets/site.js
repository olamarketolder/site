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

/* Telefone no computador: em vez de tentar ligar, mostra o número e permite copiá-lo */
(function(){
  var tel=document.querySelector('.canal[href^="tel:"]'), caixa=document.getElementById('canal-num');
  if(!tel||!caixa)return;
  var semToque=window.matchMedia&&window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if(!semToque)return;
  tel.addEventListener('click',function(e){e.preventDefault();caixa.hidden=!caixa.hidden});
  var b=caixa.querySelector('.copiar'), num=caixa.querySelector('span');
  b.addEventListener('click',function(){
    var ok=function(){b.textContent='Copiado';setTimeout(function(){b.textContent='Copiar'},1800)};
    var sel=function(){var r=document.createRange();r.selectNodeContents(num);var s=window.getSelection();s.removeAllRanges();s.addRange(r)};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText('+351913499910').then(ok,sel)}else sel();
  });
})();

/* Instagram: últimas publicações a partir do feed JSON do Behold (data-feed na secção #instagram) */
(function(){
  var sec=document.getElementById('instagram');
  if(!sec||sec.hidden)return;
  var feed=sec.getAttribute('data-feed'), conta=(sec.getAttribute('data-conta')||'').replace(/^@/,'');
  var seguir=sec.querySelector('.ig-seguir');
  if(conta){seguir.href='https://www.instagram.com/'+encodeURIComponent(conta)+'/';sec.querySelector('.ig-nome').textContent='Seguir @'+conta};
  var grelha=sec.querySelector('.ig-grelha');
  var semFeed=function(){sec.classList.add('ig-sem-feed')};
  if(!feed||!window.fetch){semFeed();return}
  var carrega=function(){
    fetch(feed).then(function(r){if(!r.ok)throw r.status;return r.json()}).then(function(d){
      var posts=(Array.isArray(d)?d:(d&&d.posts)||[]).slice(0,6);
      if(!posts.length)return semFeed();
      grelha.innerHTML='';
      posts.forEach(function(p){
        var tam=p.sizes&&(p.sizes.medium||p.sizes.small||p.sizes.large);
        var src=(tam&&tam.mediaUrl)||(p.mediaType==='VIDEO'?p.thumbnailUrl:p.mediaUrl)||p.thumbnailUrl;
        if(!src)return;
        var legenda=(p.prunedCaption||p.caption||'').replace(/\s+/g,' ').trim();
        var li=document.createElement('li'), a=document.createElement('a'), img=document.createElement('img');
        a.href=p.permalink||seguir.href; a.target='_blank'; a.rel='noopener';
        a.setAttribute('aria-label','Ver no Instagram'+(legenda?': '+legenda.slice(0,90):''));
        img.src=src; img.alt=legenda?legenda.slice(0,120):'Publicação da Marketolder no Instagram';
        img.loading='lazy'; img.decoding='async'; img.width=(tam&&tam.width)||600; img.height=(tam&&tam.height)||600;
        a.appendChild(img);
        if(p.mediaType==='VIDEO'){var v=document.createElement('span');v.className='ig-video';v.setAttribute('aria-hidden','true');a.appendChild(v)}
        li.appendChild(a); grelha.appendChild(li);
      });
      if(!grelha.children.length)semFeed();
    }).catch(semFeed);
  };
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();carrega()}},{rootMargin:'600px 0px'});
    io.observe(sec);
  } else carrega();
})();
