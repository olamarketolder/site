# Briefing — site marketolder.pt

Este repositório é o site da **Marketolder**, uma marca de serviços de marketing para pequenos negócios. Objetivo desta fase: reconstruir o site atual (`index.html`, um rascunho) como um site **premium**, memorável, com fator "uau", rápido e que converte. O dono da marca é exigente com o design: prefere poucas coisas muito bem feitas a muitas coisas médias.

## Regras inegociáveis
- **Português de Portugal** (nunca do Brasil). Trata-se o visitante por **"você"**.
- **Sem imagens geradas por IA** e sem nada que possa receber etiqueta de IA. Usar só tipografia, formas desenhadas em código (SVG/CSS) ou fotografias reais fornecidas pelo dono.
- **Sem números, estatísticas ou testemunhos inventados.** Se faltar um dado real, deixar um marcador `<!-- TODO: número real -->` e avisar.
- **Não ativar o GitHub Pages nem ligar o domínio** sem aprovação explícita do dono. Trabalhar, fazer commits e mostrar pré-visualizações; publicar só depois de "aprovado".
- A marca é **"só empresa"**: sem fotografia nem nome do fundador em destaque.

## Marca
- **Nome:** Marketolder (escreve-se assim, sem H). No logótipo, em maiúsculas espaçadas: MARKETOLDER.
- **Assinatura:** "Marketing para pequenos negócios"
- **Promessa:** "Pomos o seu negócio onde os clientes o procuram."
- **Personalidade:** sóbria, competente, próxima, sólida. Estilo **Old Money**: elegância discreta, nada de espalhafato, nada de "growth hacking", nada de emojis.

### Símbolo: "o leque"
Cinco feixes de pontas redondas que nascem de um ponto, abertos em leque para cima. O feixe central é **camel**, os outros na cor principal. Significado público: a presença do negócio a irradiar; o feixe central é o cliente, sempre ao centro e em destaque.

Geometria (viewBox `-170 -100 340 190`): para cada ângulo em [-64, -32, 0, 32, 64] graus, uma linha de raio 50 a raio 150 a partir do ponto (0, 70), `stroke-width 26`, `stroke-linecap round`. Ficheiros prontos em `assets/` (SVG e PNG transparentes, versões verde e marfim, vertical, horizontal e símbolo).

### Cores
| Nome | HEX | Uso |
|---|---|---|
| Verde Inglês | `#1E3A2F` | principal |
| Marfim | `#F3EEE2` | fundos |
| Camel | `#B08D57` | destaque, feixe central (usar com parcimónia) |
| Tinta | `#1B1B18` | texto |
| Marinho | `#1D2A38` | secundária, pontual |
| Bordéus | `#5A2330` | uso raro |
| Pedra | `#8C877B` | neutra, texto secundário |

Proporção: marfim e verde fazem ~80% de tudo; o camel é o pormenor de requinte.

### Tipografia (Google Fonts)
- **Cormorant Garamond** (500/600/700 e itálico 500): títulos, frases de destaque, nome da marca (maiúsculas, `letter-spacing` ~0.2em).
- **Inter** (400/500/600): texto, preços, botões. Pequenos rótulos de secção em maiúsculas espaçadas, a camel.

### Tom de voz
Fala como um bom alfaiate: sabe muito, explica pouco e com precisão. Diretos, calmos, concretos, educados, confiantes sem arrogância. Exemplo bom: "Em quatro semanas, o seu restaurante passa a aparecer no Google com fotos, horário e avaliações." Exemplo a evitar: "BOMBA!! Vamos levar o teu negócio para o próximo nível!!!"

## Público
Donos de pequenos negócios locais (cafés, restaurantes, cabeleireiros, oficinas, clínicas, lojas), sobretudo na zona de Braga, com presença digital fraca ou inexistente. Visitam o site no **telemóvel**. Não são técnicos: tudo tem de ser claro em segundos.

## Argumento de credibilidade
O fundador é licenciado em Marketing e recebeu **duas bolsas de excelência como melhor aluno do curso**. Usar numa secção "Sobre" curta, sem nome nem fotografia.

## Preços (definidos pelo dono, usar exatamente estes)
**Arranque, pagamento único, 100 €:** ficha Google criada e otimizada, Instagram e Facebook, logótipo simples, primeira publicação.

**Mensalidades**
- **Presença, 75 €/mês:** 1 publicação por semana, design com a marca do cliente, agendamento nas redes.
- **Presença+, 90 €/mês (o pacote a destacar):** 1 publicação por semana, gestão da ficha Google (fotos, horários, novidades), resposta a avaliações, relatório mensal simples.
- **Crescimento, 150 €/mês:** 2 publicações por semana com vídeo, tudo do Presença+, e-mail marketing mensal, gestão de anúncios Meta e Google (o orçamento dos anúncios é pago pelo cliente diretamente às plataformas).

**Extras, à medida**
- Site de uma página: 250 €
- Site até 5 páginas: 400 €
- Loja online: desde 900 €
- Manutenção de site: desde 15 €/mês
- Kit de avaliações Google (QR): 30 €
- Menu digital com QR: 25 €
- WhatsApp Business configurado: 30 €
- Newsletter mensal: 20 €/mês

Domínio e alojamento, quando necessários, ficam em nome e a cargo do cliente. Não indicar "com/sem IVA" até o dono confirmar.

## Estrutura sugerida (página única, com âncoras)
1. **Topo:** símbolo animado + "O seu negócio, encontrado." + subtítulo + botões "Começar por 100 €" e "Ver serviços".
2. **O problema:** "Se não está no Google, não existe." Mapa e confiança: fotos, horário, avaliações.
3. **Serviços:** Arranque + 3 mensalidades (Presença+ destacado) + extras.
4. **Como funciona:** Conversa → Arranque → Acompanhamento (pode parar quando quiser).
5. **Resultados em números:** substitui a antiga lista de clientes (sem nomes de clientes). Números reais confirmados pelo dono a 7 nov 2026, a usar exatamente com esta redação:
   - Título forte: **"1 € = 505 pessoas"**. Um anúncio de 18 € alcançou 9 100 pessoas (campanha de 2 semanas, out–nov 2026).
   - **4 cêntimos por visita**: o mesmo anúncio levou 415 pessoas à página de marcações do cliente.
   - **3 setores, 3 marcas**: estética, talho, festa popular (mostra versatilidade).
   - **NÃO usar número de seguidores**: o dono considera esses valores fracos para comunicar. Comunicar eficiência (o que rende cada euro), não volume.
   Contadores animados ao entrar no ecrã, discretos.
6. **Sobre:** marketing feito por quem o estudou a sério (licenciatura + 2 bolsas de excelência).
7. **Contacto:** "Vamos pôr o seu negócio no mapa?" + ola@marketolder.pt (mailto). Promessa: resposta em 24 horas com o que vimos online, sem compromisso.
8. **Rodapé:** símbolo, Braga · Portugal, e-mail, ©.

## Fator "uau" (prioridade)
- **Animação do leque no topo:** o feixe central dourado dispara primeiro, os outros abrem-se em leque um a um com ligeiro "overshoot", e um brilho camel suave cresce por trás, como um nascer do sol. Depois, o nome surge com o espaçamento das letras a fechar.
- Revelações suaves ao fazer scroll, discretas e elegantes, nada de saltos.
- Respeitar `prefers-reduced-motion`.
- Pormenores de qualidade: tipografia grande e bem espaçada, ritmo vertical generoso, fios finos camel como separadores.

## Técnica
- Site estático (HTML, CSS e JS simples, sem frameworks pesados), alojado no **GitHub Pages** deste repositório; domínio **marketolder.pt** (DNS na Amen, tratado à parte).
- Mobile-first, rápido (Lighthouse 95+), acessível (contraste AA, navegação por teclado, `alt` nos elementos).
- SEO local: `title` e `description` em PT-PT, Open Graph com imagem de partilha (feita em SVG/PNG com a marca), dados estruturados `LocalBusiness`/`ProfessionalService` com área de serviço Braga.
- Favicon a partir do símbolo (`assets/marketolder-simbolo-verde.svg`).
- Ficheiro `CNAME` com `marketolder.pt` só quando o dono aprovar a publicação.

## Processo
1. Propor a direção visual e mostrar uma pré-visualização (capturas em desktop e telemóvel) antes de polir.
2. Iterar com o dono secção a secção.
3. Só depois do "aprovado": criar `CNAME`, ativar o GitHub Pages e indicar os registos DNS a configurar na Amen.
