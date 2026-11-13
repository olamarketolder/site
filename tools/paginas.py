"""Gera servicos.html, abordagem.html e sobre.html a partir de index.html e de tools/partes.py.
Correr na raiz do repositório: python3 tools/paginas.py
Atenção: reescreve essas três páginas por inteiro (alterações feitas à mão nelas perdem-se)."""
import sys,re
sys.path.insert(0,__import__('os').path.dirname(__file__))
from partes import *
idx=open('index.html',encoding='utf-8').read()
def corta(ini,fim,incl_fim=True):
    a=idx.index(ini); b=idx.index(fim,a)+(len(fim) if incl_fim else 0); return idx[a:b]

def topo_pg(rot,h1,lead):
    return f'''<header class="pg-topo">
  <div class="w">
    <p class="migalhas"><a href="./">Início</a> <span aria-hidden="true">/</span> {rot}</p>
    <p class="rot">{rot}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</header>
'''
def pagina(nome,titulo,desc,url,atual,rot,h1,lead,corpo):
    html=(head(titulo,desc,url)+'<body class="so-pg">\n<script>document.documentElement.classList.add(\'js\')</script>\n\n'
          +SIMBOLO+'\n'+cabecalho()+'\n'+topo_pg(rot,h1,lead)+'\n'+separadores(atual)+'\n<main id="conteudo">\n\n'+corpo+'\n'+CTA+'\n</main>\n\n'+RODAPE+'\n'+FIM)
    open(nome,'w',encoding='utf-8').write(html)

# ---------- SERVIÇOS ----------
arranque=corta('<div class="arranque rv">','</div>\n    </div>')
arranque=arranque.replace('<div><p class="tag">Pagamento único</p><h3>Arranque</h3></div>',
  '<div><p class="tag">Pagamento único</p><h3>Arranque</h3><p class="para">Para quem está a começar, ou nunca tratou da presença online.</p></div>')
planos=corta('<div class="planos">','</article>\n    </div>')
for h,frase in [('<h3 id="p1">Presença</h3>','Para manter as redes vivas, todas as semanas.'),
                ('<h3 id="p2">Presença+</h3>','Para ser também encontrado e bem avaliado no Google.'),
                ('<h3 id="p3">Crescimento</h3>','Para chegar a mais gente, com vídeo, e-mail e anúncios.')]:
    assert h in planos; planos=planos.replace(h,h+f'\n        <p class="para">{frase}</p>')
nota=corta('<p class="nota rv">','</p>')
extras=corta('<div class="extras-t rv">','</ul>')
servicos=f'''<section aria-labelledby="t-planos">
  <div class="w">
    <h2 id="t-planos" class="so-leitor">Planos e preços</h2>
    {arranque}

    {planos}
    <!-- Não indicar "com/sem IVA" até o dono confirmar. -->
    {nota}

    {extras}
  </div>
</section>

<hr class="fio">

<section aria-labelledby="t-faq">
  <div class="w duas">
    <div class="cab rv">
      <p class="rot">Dúvidas frequentes</p>
      <h2 id="t-faq">Antes de <em>começar.</em></h2>
      <p class="lead">Se a sua pergunta não estiver aqui, escreva-nos. Respondemos em 24 horas.</p>
    </div>
    <div class="faq rv">
      <details><summary>Fico preso a um contrato?</summary><p>Não. Pode parar o acompanhamento mensal quando quiser.</p></details>
      <details><summary>Quem paga os anúncios?</summary><p>No plano Crescimento, nós gerimos os anúncios no Meta e no Google. O orçamento dos anúncios é pago por si, diretamente às plataformas.</p></details>
      <details><summary>O domínio e o alojamento do site ficam em nome de quem?</summary><p>Em seu nome e a seu cargo, quando forem necessários. O site é sempre seu.</p></details>
      <details><summary>Não sei que plano escolher. E agora?</summary><p>Peça uma proposta e escolha “Ainda não sei”. Vemos o que já existe online e sugerimos o que faz sentido para o seu negócio, sem compromisso.</p></details>
    </div>
  </div>
</section>
'''
pagina('servicos.html','Serviços e preços · Marketolder',
  'Arranque por 150 €, mensalidades desde 100 €/mês e extras à medida: ficha Google, redes sociais, identidade visual, sites e lojas online para pequenos negócios em Braga.',
  'servicos.html','servicos','Serviços','Comece simples. <em>Cresça quando quiser.</em>',
  'Um arranque único para pôr tudo de pé. Depois, se quiser, um acompanhamento mensal ao ritmo do seu negócio. Preços claros, sem letras pequenas.',servicos)

# ---------- ABORDAGEM ----------
adn=corta('<figure class="adn rv">','</figure>')
princ=corta('<ul class="principios">','</ul>')
abordagem=f'''<section aria-labelledby="t-manif">
  <div class="w">
    <div class="aut-topo">
      <div class="cab rv">
        <p class="rot">Autenticidade</p>
        <h2 id="t-manif">Ser visto é fácil. <em>Ser reconhecido</em> é outra coisa.</h2>
      </div>
      <blockquote class="frase rv"><p>Uma tendência dura uma semana. <em>Uma marca autêntica fica.</em></p></blockquote>
    </div>
    <div class="texto rv" style="margin-top:clamp(40px,5vw,64px)">
      <p>Um café não é igual a outro café. Uma oficina de confiança não fala como uma loja de roupa. Antes de publicar seja o que for, procuramos perceber o que torna o seu negócio diferente.</p>
      <p>Seguimos as tendências com atenção, mas só as usamos quando servem a sua marca. O objetivo não é um momento viral: é que as pessoas o reconheçam, confiem em si e voltem.</p>
    </div>

    {adn}

    {princ}
  </div>
</section>

<section class="verde" aria-labelledby="t-adn">
  <div class="w duas">
    <div class="cab rv">
      <p class="rot">O ADN da sua marca</p>
      <h2 id="t-adn">Primeiro ouvimos. <em>Depois criamos.</em></h2>
      <p class="lead">Tudo o que descobrimos fica num guia de identidade visual, entregue no Arranque, para que cada publicação seja reconhecível como sua.</p>
    </div>
    <ul class="pontos-l rv">
      <li><h3>A história</h3><p>Como começou e porquê. É muitas vezes o que mais aproxima as pessoas.</p></li>
      <li><h3>As pessoas</h3><p>Quem atende, quem faz, quem está por trás do balcão.</p></li>
      <li><h3>A maneira de fazer</h3><p>Aquilo que faz melhor do que ninguém na sua rua.</p></li>
      <li><h3>A forma de falar</h3><p>O tom com que trata os clientes, ao vivo e online.</p></li>
    </ul>
  </div>
</section>

<section id="como" aria-labelledby="t-como">
  <div class="w">
    <div class="cab rv">
      <p class="rot">Como funciona</p>
      <h2 id="t-como">Três passos. <em>Nenhuma surpresa.</em></h2>
    </div>
    <ol class="passos-d">
      <li class="rv"><span class="num" aria-hidden="true">I</span>
        <div><h3>Conversa e diagnóstico</h3><p>Conhecemos o seu negócio e fazemos um diagnóstico do que já existe online: o que funciona e o que falta.</p></div>
        <ul class="lista plano-lista"><li>Google, redes sociais e site, se existir</li><li>Resposta em 24 horas</li><li>Sem compromisso</li></ul></li>
      <li class="rv"><span class="num" aria-hidden="true">II</span>
        <div><h3>Arranque</h3><p>Pomos tudo de pé, com a sua identidade. Pagamento único de 150 €.</p></div>
        <ul class="lista plano-lista"><li>Ficha Google criada e otimizada</li><li>Criação de redes sociais: Instagram, Facebook e TikTok</li><li>Logótipo e animação do logótipo</li><li>Guia de identidade visual</li><li>Primeira publicação</li></ul></li>
      <li class="rv"><span class="num" aria-hidden="true">III</span>
        <div><h3>Acompanhamento</h3><p>Se quiser, continuamos todos os meses, no plano que fizer sentido: Presença, Presença+ ou Crescimento.</p></div>
        <ul class="lista plano-lista"><li>Publicações todas as semanas</li><li>Relatório mensal simples, no Presença+ e no Crescimento</li><li>Pode parar quando quiser</li></ul></li>
    </ol>
    <p class="mais rv"><a href="servicos.html">Ver planos e preços <span aria-hidden="true">→</span></a></p>
  </div>
</section>
'''
pagina('abordagem.html','Abordagem · Marketolder',
  'Não há duas marcas iguais. Trabalhamos a identidade de cada negócio e promovemos a sua autenticidade, porque é isso que liga as pessoas às marcas.',
  'abordagem.html','abordagem','Abordagem','Não há duas marcas <em>iguais.</em>',
  'Cada negócio tem o seu ADN: a história, as pessoas, a maneira de fazer. O nosso trabalho é encontrá-lo e mostrá-lo, com cuidado, em tudo o que publicamos.',abordagem)

# ---------- SOBRE ----------
selos=corta('<ul class="selos rv">','</ul>')
sobre=f'''<section aria-labelledby="t-quem">
  <div class="w duas">
    <div class="cab rv">
      <p class="rot">A Marketolder</p>
      <h2 id="t-quem">O cuidado de uma grande marca, <em>à medida do seu negócio.</em></h2>
    </div>
    <div class="texto rv">
      <p>A Marketolder faz marketing para pequenos negócios locais, sobretudo na zona de Braga. Cafés, restaurantes, cabeleireiros, oficinas, clínicas e lojas que merecem ser encontrados por quem os procura.</p>
      <p>Nasceu de uma licenciatura em Marketing levada com rigor, e de uma convicção simples: o pequeno negócio merece o mesmo cuidado que uma grande marca. Cada publicação tem um porquê. Cada mês, um relatório simples e claro.</p>
    </div>
  </div>
</section>

<section class="verde" aria-labelledby="t-formacao">
  <div class="w sobre">
    <div class="rv">
      <p class="rot">Formação</p>
      <h2 id="t-formacao">Uma formação que se nota <em>no trabalho.</em></h2>
    </div>
    {selos}
  </div>
</section>

<section aria-labelledby="t-valores">
  <div class="w duas">
    <div class="cab rv">
      <p class="rot">Como trabalhamos</p>
      <h2 id="t-valores">O que pode <em>esperar de nós.</em></h2>
    </div>
    <ul class="pontos-l rv">
      <li><h3>Clareza</h3><p>Falamos sem jargão. Os relatórios leem-se num instante e dizem o que interessa.</p></li>
      <li><h3>Proximidade</h3><p>Estamos em Braga e respondemos em 24 horas.</p></li>
      <li><h3>Rigor</h3><p>Método, não improviso. Cada passo tem uma razão de ser.</p></li>
      <li><h3>Liberdade</h3><p>Sem amarras: pode parar o acompanhamento quando quiser.</p></li>
    </ul>
  </div>
</section>
'''
pagina('sobre.html','Sobre · Marketolder',
  'Marketing para pequenos negócios em Braga, feito por quem o estudou a sério: licenciatura em Marketing, prémios de mérito como melhor aluno e mais de 200 horas de formação em marketing digital.',
  'sobre.html','sobre','Sobre','Marketing feito por quem <em>o estudou a sério.</em>',
  'Sobriedade, método e proximidade, ao serviço de negócios que querem ser bem tratados.',sobre)
print('ok')
