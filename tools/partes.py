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
    <div class="canais">
      <a class="canal" href="tel:+351913499910" aria-label="Ligar para +351 913 499 910" title="Ligar · +351 913 499 910"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></a>
      <a class="canal" href="https://wa.me/351913499910?text=Ol%C3%A1!%20Vim%20pelo%20site%20da%20Marketolder." target="_blank" rel="noopener" aria-label="Falar connosco no WhatsApp" title="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
    </div>
  </div>
</section>
'''
FIM='''<script src="assets/site.js" defer></script>
</body>
</html>
'''
