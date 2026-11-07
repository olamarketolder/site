# Fragmentos partilhados para gerar as páginas
TABS=[('./','Início','inicio'),('abordagem.html','Abordagem','abordagem'),('servicos.html','Serviços','servicos'),('sobre.html','Sobre','sobre'),('pedido.html','Contacto','contacto')]
def separadores(atual):
    lis=[]
    for href,t,k in TABS:
        cur=' aria-current="page"' if k==atual else ''
        lis.append(f'    <li><a href="{href}"{cur}><span class="n" aria-hidden="true"></span><span class="t">{t}</span></a></li>')
    return ('<nav class="separadores" id="separadores" aria-label="Páginas do site">\n  <ol>\n'+'\n'.join(lis)+
            '\n    <li class="indicador" aria-hidden="true"></li>\n  </ol>\n</nav>\n')
SIMBOLO='''<!-- Símbolo reutilizável: feixes laterais em currentColor, feixe central camel -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="leque" viewBox="-170 -100 340 190">
    <g stroke-width="26" stroke-linecap="round">
      <line x1="-44.9" y1="48.1" x2="-134.8" y2="4.2" stroke="currentColor"/>
      <line x1="-26.5" y1="27.6" x2="-79.5" y2="-57.2" stroke="currentColor"/>
      <line x1="0" y1="20" x2="0" y2="-80" stroke="#B08D57"/>
      <line x1="26.5" y1="27.6" x2="79.5" y2="-57.2" stroke="currentColor"/>
      <line x1="44.9" y1="48.1" x2="134.8" y2="4.2" stroke="currentColor"/>
    </g>
  </symbol>
</svg>
'''
USE='<use href="#leque" x="-170" y="-100" width="340" height="190"/>'
def cabecalho(cta=True):
    c='\n    <a class="nav-cta" href="pedido.html">Falar connosco</a>' if cta else ''
    return f'''<a class="saltar" href="#conteudo">Saltar para o conteúdo</a>

<nav class="nav" id="nav" aria-label="Principal">
  <div class="w">
    <a class="logo" href="./" aria-label="Marketolder, início">
      <svg viewBox="-170 -100 340 190" aria-hidden="true">{USE}</svg>
      <span class="marca">Marketolder</span>
    </a>{c}
  </div>
</nav>
'''
RODAPE=f'''<footer>
  <div class="w">
    <a class="logo" href="./" aria-label="Voltar ao início">
      <svg viewBox="-170 -100 340 190" aria-hidden="true">{USE}</svg>
      <span class="marca">Marketolder</span>
    </a>
    <div class="dados">
      <span>Braga · Portugal</span>
      <a href="mailto:ola@marketolder.pt">ola@marketolder.pt</a>
      <a href="tel:+351913499910">+351 913 499 910</a>
      <a href="https://wa.me/351913499910?text=Ol%C3%A1!%20Vim%20pelo%20site%20da%20Marketolder." target="_blank" rel="noopener">WhatsApp</a>
      <span>© <span id="ano">2026</span> Marketolder</span>
    </div>
  </div>
</footer>
'''
def head(titulo,desc,url,extra=''):
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://marketolder.pt/{url}">
<meta name="theme-color" content="#F3EEE2">
<meta name="format-detection" content="telephone=no">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta property="og:site_name" content="Marketolder">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://marketolder.pt/{url}">
<meta property="og:image" content="https://marketolder.pt/assets/partilha.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/cormorant-garamond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/estilo.css">
{extra}</head>
'''
CTA='''<section class="verde contacto" aria-labelledby="t-cta">
  <div class="w rv">
    <p class="rot">Contacto</p>
    <h2 id="t-cta">Vamos pôr o seu negócio <em>no mapa?</em></h2>
    <p class="lead">Diga-nos o nome do negócio e a localidade. Em 24 horas respondemos com o que vimos online, sem compromisso.</p>
    <a class="btn btn-claro" href="pedido.html">Pedir proposta <span class="seta" aria-hidden="true">→</span></a>
    <p class="ou">ou escreva para <a class="email" href="mailto:ola@marketolder.pt">ola@marketolder.pt</a></p>
    <p class="ou ou-tel">ou ligue para <a class="email tel" href="tel:+351913499910">+351 913 499 910</a></p>
    <p class="ou ou-wa">ou fale connosco no <a class="email wa" href="https://wa.me/351913499910?text=Ol%C3%A1!%20Vim%20pelo%20site%20da%20Marketolder." target="_blank" rel="noopener">WhatsApp</a></p>
  </div>
</section>
'''
FIM='''<script src="assets/site.js" defer></script>
</body>
</html>
'''
