"""Builds the GoEB5 multipage site from shared header/footer + per-page content.
Home page content is taken from the approved v2 home page (sections preserved)."""
import re, pathlib
ROOT = pathlib.Path(__file__).parent
v2 = (ROOT/'src'/'home-v2.html').read_text()

NAV = [('index.html','Home'),('about.html','About'),('why-usa.html','Why USA'),('eb5-program.html','EB-5 Program'),
       ('texas-solar.html','Texas Project'),('opportunities.html','Investments'),('gallery.html','Gallery'),
       ('process.html','Process'),('partners.html','Partners'),('faq.html','FAQ & Resources'),('contact.html','Contact')]

SOC = {
 'facebook':'<path fill="currentColor" d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.5V11H7v4h2.5v7h4v-7H17l.6-4h-4.1V8.7c0-.4.2-.7.5-.7z"/>',
 'instagram':'<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="currentColor"/>',
 'linkedin':'<rect x="3" y="9" width="4" height="12" fill="currentColor"/><circle cx="5" cy="5" r="2.2" fill="currentColor"/><path fill="currentColor" d="M10 9h3.8v1.7c.6-1 1.9-2 3.8-2 3.3 0 4.4 2 4.4 5.2V21h-4v-6.2c0-1.5-.3-2.8-1.9-2.8s-2.1 1.2-2.1 2.8V21h-4z"/>',
 'x':'<path fill="currentColor" d="M3.5 3h5l12 18h-5z"/><path stroke="currentColor" stroke-width="2" d="M20 3l-6.8 7.6M4 21l6.8-7.6"/>',
 'youtube':'<path fill="currentColor" fill-rule="evenodd" d="M6 5h12a4 4 0 0 1 4 4v6a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V9a4 4 0 0 1 4-4zM10 9v6l5-3z"/>',
 'whatsapp':'<path fill="none" stroke="currentColor" stroke-width="2" d="M4 20l1.3-4A8.5 8.5 0 1 1 8.6 19z"/><path fill="currentColor" d="M9 8.5c.3-.6.8-.6 1-.2l.8 1.7c.1.3 0 .6-.3.9l-.4.4c.6 1.2 1.6 2.2 2.8 2.8l.5-.5c.2-.2.6-.3.9-.2l1.6.8c.4.2.4.7-.1 1.2-.8.8-2 .9-3.5.1-1.8-.9-3.3-2.5-4-4.2-.4-1.2-.2-2.2.7-2.8z"/>',
 'telegram':'<path fill="currentColor" d="M2.5 11.2 20.6 4c.8-.3 1.6.4 1.3 1.3l-3.2 14.4c-.2.9-1.2 1.2-1.9.7l-4.6-3.5-2.4 2.3c-.3.3-.8.1-.8-.3v-3.4l8-7.4-10 6.1-4-1.3c-.8-.3-.8-1.4 0-1.7z"/>',
 'email':'<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="2"/>'}
def svg(k,size=20): return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true">{SOC[k]}</svg>'
NAMES={'facebook':'Facebook','instagram':'Instagram','linkedin':'LinkedIn','x':'X','youtube':'YouTube','whatsapp':'WhatsApp','telegram':'Telegram','email':'Email'}
def follow_icons():
    return '<div class="soc">' + ''.join(f'<a href="connect.html" data-follow="{k}" aria-label="GoEB5 on {NAMES[k]}" title="{NAMES[k]}">{svg(k)}</a>' for k in ['facebook','instagram','linkedin','x','youtube','whatsapp']) + '</div>'

def shell(fname, title, desc, body):
    links = ''.join(f'<a href="{h}"{" aria-current=page" if h==fname else ""}>{t}</a>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — GoEB5</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="top"><span>Powered by Unite Group Inc., USA · India desk: Hyderabad</span><span style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">{follow_icons()}<a href="mailto:info@goeb5.in">info@goeb5.in</a><select class="lang" aria-label="Language"><option>English</option><option disabled>हिन्दी — soon</option><option disabled>తెలుగు — soon</option></select></span></div>
<nav><div class="wrap">
  <a class="logo" href="index.html" aria-label="GoEB5 home"><img src="img/logo-mark.png" alt="GoEB5 — U.S. Investor Visa Program"></a>
  <button class="menu" type="button" aria-expanded="false" aria-controls="links">Menu</button>
  <div class="links" id="links">{links}<a href="portal.html" class="mob">Investor login</a></div>
  <div class="navbtns"><a class="btn sm navy" href="portal.html">Investor login</a><a class="btn sm cta" href="contact.html">Book consultation</a></div>
</div></nav>
<main>
{body}
</main>
<footer class="band"><div class="wrap">
  <div class="cols">
    <div><a class="flogo" href="index.html"><img src="img/logo.png" alt="GoEB5 — Invest, create jobs, live in USA"></a><p style="opacity:.8;margin-top:14px">EB-5 investment advisory for families in India and worldwide. Powered by Unite Group Inc., USA.</p><p style="opacity:.8">India desk: Hyderabad, Telangana<br>US head office: 244 Fifth Avenue, Suite #1849, New York, NY 10001<br>info@goeb5.in</p><strong>Follow us</strong>{follow_icons()}</div>
    <div><strong>Program</strong><a href="eb5-program.html">EB-5 Program</a><a href="process.html">Process</a><a href="why-usa.html">Why USA</a><a href="faq.html">FAQ &amp; Resources</a></div>
    <div><strong>Invest</strong><a href="texas-solar.html">Texas Solar Project</a><a href="opportunities.html">Investments</a><a href="gallery.html">Gallery</a><a href="portal.html">Investor portal</a></div>
    <div><strong>Company</strong><a href="about.html">About Unite Group</a><a href="partners.html">Partners &amp; Advisors</a><a href="news.html">News &amp; Insights</a><a href="connect.html">Social &amp; Connect</a><a href="contact.html">Contact / Apply</a></div>
    <div><strong>Legal</strong><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="disclaimer.html">Investment Disclaimer</a><a href="sitemap.html">Sitemap</a></div>
  </div>
  <p class="disc">GoEB5 is not a law firm and does not give legal, tax or investment advice. Information on this site is general and not an offer to sell or a solicitation to buy securities; offers are made only through a project's private placement memorandum to qualified investors. EB-5 investments are at risk and may lose value; returns and immigration approvals are not guaranteed. Immigration outcomes are decided solely by USCIS and the US Department of State. Projects marked "under evaluation" have not been verified for EB-5 eligibility, TEA designation or regional-center sponsorship. Consult independent immigration counsel and financial advisors. © 2026 GoEB5 · goeb5.in<br><span class="credit">Photography: Unsplash (Unsplash License).</span></p>
</div></footer>
<a class="btn float" href="contact.html">Talk to an advisor</a>
<script src="assets/site.js"></script>
</body>
</html>
'''

def phead(img, crumb, h1, p):
    return f'''<header class="phead" style="background-image:linear-gradient(90deg,rgba(6,18,48,.9),rgba(6,18,48,.55)),url(img/{img}.jpg)"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / {crumb}</div><h1>{h1}</h1><p>{p}</p></div></header>'''

def ico(path):
    return f'<div class="ico"><svg viewBox="0 0 24 24">{path}</svg></div>'
I = {'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
     'lock':'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
     'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
     'user':'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
     'doc':'<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h7M9 17h7"/>',
     'chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
     'shield':'<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>',
     'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
     'bolt':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>','home':'<path d="M3 11l9-7 9 7v10H3z"/><path d="M9 21v-6h6v6"/>',
     'grad':'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>','briefcase':'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 13h18"/>'}

def cards(items, cls='cards'):
    if cls=='cards' and len(items)==4: cls='cards four'
    return f'<div class="{cls}">' + ''.join(f'<div class="card">{ico(I[i])}<h3>{h}</h3><p>{p}</p></div>' for i,h,p in items) + '</div>'

CTA = '''<section class="band cta-band"><div class="wrap"><h2>Ready to explore your path to a US green card?</h2><p class="lede">Speak with our India desk about the Texas solar opportunity, the EB-5 process and your family's eligibility.</p><div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn" href="contact.html">Book a free consultation</a><a class="btn ghost" href="texas-solar.html">Explore the Texas project</a></div></div></section>'''

pages = {}

# ---------- HOME (approved v2 content preserved; additions inserted) ----------
body = re.search(r'</nav>\n(.*?)<footer', v2, re.S).group(1)
body = body.replace('<a class="btn ghost" href="#projects">See opportunities</a>','<a class="btn ghost" href="texas-solar.html">Explore Texas project</a>')
# consultation form -> shared form handler
body = body.replace('<form id="cform" class="panel" novalidate>','<form id="cform" class="panel" novalidate data-form="Consultation request">')
body = body.replace('<input id="n" required autocomplete="name">','<input id="n" required autocomplete="name">')
body = body.replace('<select id="c"></select>','<select id="c" class="country"></select>')
body = body.replace('<input type="checkbox" id="consent"','<input type="checkbox" id="consent" required')
body = body.replace('<label style="display:flex;gap:10px;align-items:flex-start;font-weight:400;font-size:14px">','<label for="consent" style="display:flex;gap:10px;align-items:flex-start;font-weight:400;font-size:14px">')
home_add = f'''
<section class="band alt" id="featured"><div class="wrap split">
  <img class="photo" src="img/p1.jpg" alt="Solar arrays on open land in Texas" style="aspect-ratio:16/10">
  <div><span class="gold">Featured · Unite Group Inc., USA</span>
  <h2 style="margin-top:14px">Invest in America's energy future — Texas</h2>
  <p class="lede">A proposed solar development with potential battery storage on a 112-acre site in the McAllen area of Texas, promoted by Unite Group Inc., USA with local partner 112 Citrus LLC.</p>
  <div class="facts" style="margin:18px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div><b>112 acres</b><span>Proposed site</span></div><div><b>Texas</b><span>McAllen area</span></div><div><b>EB-5</b><span>Pathway under evaluation</span></div></div>
  <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn navy" href="texas-solar.html">Explore project</a><a class="btn ghost" href="contact.html">Request information</a></div>
  <p class="note" style="margin-top:12px">Concept stage. Project eligibility and offering terms are not yet verified.</p></div>
</div></section>
<section class="band"><div class="wrap">
  <h2>Everything an EB-5 investor needs, in one place</h2>
  <div class="pcards"><a class="pcard" href="portal.html"><img src="img/c-portal.jpg" alt="Investor dashboard with charts"><div><h3>Investor access portal</h3><p>Secure login, project updates, investor documents and consultation history — opening once offering documents are final.</p><span class="more">Learn more →</span></div></a><a class="pcard" href="texas-solar.html"><img src="img/p1.jpg" alt="Solar arrays on open land in Texas"><div><h3>Texas renewable-energy opportunity</h3><p>Project presentation, proposed solar development, land details, technical documentation and milestone tracking.</p><span class="more">View project →</span></div></a><a class="pcard" href="contact.html"><img src="img/c-consult.jpg" alt="Advisor reviewing documents with a client"><div><h3>EB-5 investor consultation</h3><p>Guided inquiry, investor prequalification, online appointment booking and multilingual support.</p><span class="more">Book now →</span></div></a><a class="pcard" href="eb5-program.html"><img src="img/c-learn.jpg" alt="Person studying notes at a desk"><div><h3>EB-5 education center</h3><p>Eligibility, investment thresholds, job creation, timelines and key 2027 dates, explained plainly.</p><span class="more">Start learning →</span></div></a></div>
</div></section>'''
body = body.replace('<section class="band" id="program">', home_add + '\n<section class="band" id="program">', 1)
body = body.replace('<a class="btn float" href="#contact">Talk to an advisor</a>','')
pages['index.html'] = ('U.S. Investor Visa Program','EB-5 investment and US green card advisory for Indian and global families — Texas solar and infrastructure opportunities.', body)

# ---------- ABOUT ----------
pages['about.html'] = ('About Unite Group','About Unite Group Inc., USA — the promoter behind GoEB5.', phead('g7','About','About Unite Group','GoEB5 is powered by Unite Group, Inc. — a diversified international group across renewable energy, technology, construction, fintech and consultancy, with operations in the USA, the UK and India.') + f'''
<section class="band"><div class="wrap split">
 <div><h2>A renewable energy group building across three continents</h2>
 <p class="lede">Unite Group works across solar EPC, rooftop and ground-mounted projects, OEM module manufacturing, battery energy storage and renewable energy parks. Its India operations are led from Hyderabad, serving Andhra Pradesh, Telangana and beyond.</p>
 <p class="lede">GoEB5 brings that experience to US investors: a dedicated desk that helps Indian and global families understand the EB-5 program and evaluate US renewable-energy and infrastructure opportunities — starting with a proposed solar project in Texas.</p></div>
 <img class="photo" src="img/g3.jpg" alt="Technician installing solar equipment" style="aspect-ratio:4/3">
</div></section>
<section class="band alt"><div class="wrap"><h2>What we do</h2>
{cards([('sun','Solar EPC','Design, engineering, procurement and construction for rooftop, ground-mounted and utility-scale solar.'),
        ('bolt','Storage & energy parks','Solar-plus-BESS parks and hybrid renewable projects for industrial and utility offtakers.'),
        ('briefcase','Manufacturing & supply','OEM solar module manufacturing and multi-country procurement of balance-of-system equipment.'),
        ('globe','US investment desk','GoEB5 — investor education, project presentation and consultation for EB-5 families.')])}
</div></section>
<section class="band"><div class="wrap"><h2>Leadership</h2>
<div class="cards four">
<div class="card">{ico(I['user'])}<h3>Akhil Ponnada</h3><p><b>Founder.</b> Entrepreneur and AI research leader who sets Unite Group's direction; Founder &amp; CEO of Nuro AI Labs. <a href="https://linkedin.com/in/akhil-ponnada-135837109">LinkedIn</a></p></div>
<div class="card">{ico(I['user'])}<h3>Surya Kumar Vidiyala</h3><p><b>Co-Founder.</b> Senior business leader focused on strategy, external relationships and institution-building; Managing Director &amp; CEO of the Mass Infosys group. Based in Texas. <a href="https://www.linkedin.com/in/suryavidiyala">LinkedIn</a></p></div>
<div class="card">{ico(I['user'])}<h3>Dr. Ravi Chandra Ponnada</h3><p><b>Chairman.</b> Leads the group's renewable energy, EPC and infrastructure businesses across India, the USA and the UK.</p></div>
<div class="card">{ico(I['user'])}<h3>Madhuri Kiranmai</h3><p><b>Director – Corporate Affairs.</b> A woman entrepreneur and innovator whose preparation for the Indian Administrative Service gives her a strong grounding in public policy, governance and administration. She leads Unite Group's corporate affairs, government and institutional relations, bringing a disciplined, people-first approach to building trusted partnerships.</p></div></div>
<p class="note" style="margin-top:14px">Advisory board: independent immigration counsel, securities counsel and a USCIS-designated regional center are being appointed. <a href="partners.html">See partners</a></p>
</div></section>
<section class="band alt"><div class="wrap two">
 <div><h2>Group companies</h2>
 <div class="lock"><div><b>Unite Group, Inc.</b><br><span>Parent company · Head office, New York, USA</span></div></div>
 <div class="lock"><div><b>Unite Global Developers Inc.</b><br><span>Development &amp; construction · India</span></div></div>
 <div class="lock"><div><b>Unite Greentech Limited</b><br><span>Renewable energy · United Kingdom</span></div></div>
 <div class="lock"><div><b>Nuro AI Labs Limited</b><br><span>Intelligent technology, AI and IoT · United Kingdom</span></div></div>
 <p class="note" style="margin-top:12px">Divisions: renewable energy, information technology, construction &amp; infrastructure, fintech and consultancy. <a href="https://www.unitegroupinc.com">unitegroupinc.com</a></p></div>
 <div><h2>Projects in development</h2>
 <div class="facts"><div><b>80 MW</b><span>Texas Solar Park, USA — utility-scale, grid-connected</span></div><div><b>250 MW</b><span>Donakonda Solar + BESS, Andhra Pradesh, India</span></div></div>
 <div class="lock"><div><b>Head office</b><br><span>244 Fifth Avenue, Suite #1849, New York, NY 10001, USA · info@unitegroupinc.com</span></div></div>
 <p class="lede" style="margin-top:14px">"Powering progress. Building the future." — a diversified international group across renewable energy, technology, construction, fintech and consultancy.</p></div>
</div></section></div></section>''' + CTA)

# ---------- WHY USA ----------
pages['why-usa.html'] = ('Why invest in the USA','Why the US — permanent residency benefits and the renewable-energy opportunity.', phead('countries','Why USA','Why invest in the USA?','A green card brings your family the freedom to live, study and work anywhere in the United States — and EB-5 lets you earn it by funding projects the country needs.') + f'''
<section class="band"><div class="wrap"><h2>What a green card gives your family</h2>
{cards([('home','Live anywhere','Settle in any state, with the right to travel in and out of the US.'),
        ('briefcase','Work or build a business','No employer sponsorship or H-1B lottery; change jobs or start a company freely.'),
        ('grad','Education','Children attend US schools, and green card holders often qualify for in-state tuition at public universities.'),
        ('shield','Path to citizenship','Apply for US citizenship after five years as a permanent resident, subject to eligibility.')])}
</div></section>
<section class="band alt"><div class="wrap split">
 <div><h2>Why renewable energy, why Texas</h2>
 <p class="lede">Texas runs its own power grid (ERCOT), has abundant sun and open land, and is among the fastest-growing solar and battery-storage markets in the United States. Rising demand from data centers, industry and population growth keeps the need for new generation high.</p>
 <p class="lede">Energy and infrastructure projects are capital-intensive and create construction and operating jobs — the two things EB-5 is designed to support. Qualifying infrastructure projects also have a dedicated 2% visa reserve.</p>
 <a class="btn navy" href="texas-solar.html">See the Texas project</a></div>
 <img class="photo" src="img/g1.jpg" alt="Rows of solar panels under a clear sky" style="aspect-ratio:4/3">
</div></section>
<section class="band"><div class="wrap"><h2>Why EB-5 instead of other routes</h2>
<div class="scroll"><table style="width:100%;border-collapse:collapse;font-size:15px" class="stack"><thead><tr style="text-align:left;border-bottom:2px solid var(--line)"><th style="padding:10px">Route</th><th style="padding:10px">Needs employer?</th><th style="padding:10px">Lottery?</th><th style="padding:10px">Family included</th></tr></thead><tbody>
<tr style="border-bottom:1px solid var(--line)"><td style="padding:10px"><b>EB-5 investor</b></td><td style="padding:10px">No</td><td style="padding:10px">No</td><td style="padding:10px">Spouse + children under 21</td></tr>
<tr style="border-bottom:1px solid var(--line)"><td style="padding:10px">H-1B → employment green card</td><td style="padding:10px">Yes</td><td style="padding:10px">Yes (H-1B)</td><td style="padding:10px">Yes, after long waits for Indians</td></tr>
<tr style="border-bottom:1px solid var(--line)"><td style="padding:10px">E-2 treaty investor</td><td style="padding:10px">No</td><td style="padding:10px">No</td><td style="padding:10px">Not available to Indian nationals</td></tr>
</tbody></table></div><p class="note" style="margin-top:10px">General comparison; your counsel will confirm what applies to you.</p></div></section>''' + CTA)

# ---------- EB-5 PROGRAM (education center) ----------
pages['eb5-program.html'] = ('EB-5 Visa Program','EB-5 education center: eligibility, investment thresholds, job creation and 2027 dates.', phead('liberty','EB-5 Program','The EB-5 Visa Program','Eligibility, investment thresholds, job requirements and key dates — the EB-5 education center.') + f'''
<section class="band"><div class="wrap">
<div class="stats" style="margin-top:0">
 <div><b>$800,000</b><span>TEA (rural or high-unemployment) or qualifying infrastructure project</span></div>
 <div><b>$1,050,000</b><span>Standard minimum elsewhere</span></div>
 <div><b>10 jobs</b><span>Full-time US jobs per investor</span></div>
 <div><b>1 Jan 2027</b><span>Statutory inflation adjustment of both minimums</span></div></div>
<p class="note" style="margin-top:12px">Under the EB-5 Reform and Integrity Act of 2022. The 2027 TEA minimum is projected near $937,500; USCIS has not yet published final figures. Program authorised through 30 September 2027.</p>
</div></section>
<section class="band alt"><div class="wrap two">
 <div><h2>Who is eligible</h2>
 <ul class="lede" style="padding-left:20px"><li>Any foreign national aged 18+ who invests the required capital.</li><li>Funds must come from a lawful, documented source (salary, business income, property sale, gift or loan).</li><li>Capital must be "at risk" in a new commercial enterprise.</li><li>The investment must create at least 10 full-time jobs for US workers.</li><li>Your spouse and unmarried children under 21 receive green cards too.</li></ul></div>
 <div><h2>Two ways to invest</h2>
 <div class="card" style="margin-bottom:12px"><h3>Regional center (indirect)</h3><p>Pooled investment sponsored by a USCIS-designated regional center. Indirect and induced jobs count, and you have no day-to-day management duty. Investors file Form I-526E.</p></div>
 <div class="card"><h3>Direct investment</h3><p>You invest in and help manage your own business. Only direct W-2 jobs count. Investors file Form I-526.</p></div></div>
</div></section>
<section class="band"><div class="wrap"><h2>Reserved (set-aside) visas</h2>
<p class="lede">The 2022 reform reserves 32% of EB-5 visas each year: 20% for rural projects, 10% for high-unemployment areas and 2% for infrastructure projects. These set-aside categories have recently been available for India even while the unreserved category is backlogged.</p>
<div class="stats"><div><b>20%</b><span>Rural</span></div><div><b>10%</b><span>High-unemployment</span></div><div><b>2%</b><span>Infrastructure</span></div><div><b>68%</b><span>Unreserved</span></div></div>
</div></section>
<section class="band alt"><div class="wrap"><h2>Key terms</h2>
{cards([('doc','TEA','Targeted Employment Area — a rural area or one with unemployment at least 150% of the national average; qualifies for the reduced minimum.'),
        ('doc','I-526E','The investor petition for regional-center investments, proving lawful funds and a qualifying investment.'),
        ('doc','I-829','Petition to remove conditions after about two years, showing the jobs were created and capital sustained.'),
        ('doc','PPM','Private placement memorandum — the legal offering document describing the project, risks and terms.'),
        ('doc','At risk','Capital must be exposed to gain or loss; guaranteed returns are not permitted.'),
        ('doc','Visa Bulletin','Monthly State Department chart showing when each category and country can take the final step.')])}
</div></section>''' + CTA)

# ---------- TEXAS PROJECT ----------
ms = [('done','Site identified','112-acre property in the McAllen area, Texas.'),
      ('now','Local partnership','Arrangement with 112 Citrus LLC for land rights and local development.'),
      ('','Technical feasibility','Solar resource, layout, battery storage sizing and grid interconnection studies.'),
      ('','EB-5 structuring','TEA / infrastructure qualification review, job-creation model and regional-center sponsorship.'),
      ('','Offering documents','PPM, subscription agreement, business plan and economic report prepared by counsel.'),
      ('','Investor subscriptions','Escrow-protected subscriptions and I-526E filings — only after the offering is live.'),
      ('','Construction & operation','EPC by Unite Solar USA, commissioning and job verification for I-829.')]
ms_html = ''.join(f'<li class="{c}"><b>{t}<span class="st {"ok" if c=="done" else "now" if c=="now" else ""}">{"Complete" if c=="done" else "In progress" if c=="now" else "Planned"}</span></b><span>{d}</span></li>' for c,t,d in ms)
pages['texas-solar.html'] = ('Texas Solar Project','Proposed 112-acre solar and battery storage project in the McAllen area, Texas — Unite Group Inc., USA.', phead('hero','Texas Solar Project','Texas Solar Project — McAllen Area','A proposed solar development with potential battery energy storage on a 112-acre site in South Texas.') + f'''
<section class="band"><div class="wrap">
<div class="facts">
 <div><b>Unite Group Inc., USA</b><span>Parent / promoter</span></div>
 <div><b>112 Citrus LLC</b><span>Local project partner</span></div>
 <div><b>McAllen area, TX</b><span>Project location</span></div>
 <div><b>112 acres</b><span>Proposed land</span></div>
 <div><b>Solar + BESS</b><span>Solar with potential storage</span></div>
 <div><b>Under evaluation</b><span>EB-5 feasibility &amp; structuring</span></div></div>
</div></section>
<section class="band alt"><div class="wrap split">
 <div><h2>Project concept</h2>
 <p class="lede">The concept is a ground-mounted solar plant on single-axis trackers, with battery energy storage evaluated to shift power into evening peak hours on the ERCOT grid. Unite Solar USA would deliver engineering, procurement and construction, drawing on Unite Group's multi-country supply chain.</p>
 <p class="lede">Final capacity, storage size and interconnection point will be fixed by the feasibility and grid studies now being planned.</p></div>
 <img class="photo" src="img/g2.jpg" alt="Close view of solar modules on grassland" style="aspect-ratio:4/3">
</div></section>
<section class="band"><div class="wrap two">
 <div><h2>Project milestones</h2><ol class="ms">{ms_html}</ol></div>
 <div><h2>Important to know</h2>
 <div class="warn"><p>The 112-acre property does not automatically qualify for the reduced $800,000 amount or a rural / TEA designation. Eligibility, the job-creation model, regional-center sponsorship, land rights and the offering structure must be independently verified before any offering is made.</p><p style="margin:0">No investment is being accepted for this project today. Investment capital is at risk, and returns and immigration approvals are not guaranteed. Securities are offered only through lawful channels and formal offering documents.</p></div>
 <h3 style="margin-top:24px">Get project updates</h3>
 <form class="panel" data-form="Project update request" novalidate><label for="tn">Full name</label><input id="tn" required autocomplete="name"><label for="te">Email</label><input id="te" type="email" required autocomplete="email"><label for="tc">Country</label><select id="tc" class="country"></select><button class="btn" style="width:100%;margin-top:14px">Notify me</button><div class="ok"></div></form></div>
</div></section>''' + CTA)

# ---------- OPPORTUNITIES ----------
pages['opportunities.html'] = ('Investment Opportunities','EB-5 investment opportunities in solar and infrastructure, with suitability and risk information.', phead('p5','Investments','Investment opportunities','Solar and infrastructure projects — with the suitability questions and risks every investor should weigh.') + f'''
<section class="band alt"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter projects"><button data-f="all" aria-pressed="true">All projects</button><button data-f="solar" aria-pressed="false">Solar</button><button data-f="infra" aria-pressed="false">Infrastructure</button><button data-f="open" aria-pressed="false">Open now</button></div>
  <div class="grid" id="pgrid"></div>
  <p class="note" style="margin-top:16px">Except the featured Unite project, cards are an illustrative pipeline for layout. Verified offering terms will appear here only when a project's PPM is final.</p>
</div></section>
<section class="band"><div class="wrap two">
 <div><h2>Is EB-5 suitable for you?</h2><p class="lede">EB-5 suits families who want permanent residency, can commit capital for roughly five or more years, and can document where their money came from.</p>
 <div class="panel"><h3>Quick eligibility check</h3><div id="quiz"></div><div class="res" id="qres">Answer the five questions to see where you stand.</div></div></div>
 <div><h2>Key risks</h2>
 {''.join(f'<div class="lock"><div><b>{a}</b><br><span>{b}</span></div></div>' for a,b in [('Capital at risk','Projects can underperform or fail; repayment is not guaranteed.'),('Immigration risk','USCIS may deny a petition, for example if job creation or source of funds falls short.'),('Visa availability','Backlogs or retrogression can delay the final green card.'),('Liquidity','Capital is typically locked in for five or more years.'),('Program changes','Congress and USCIS can change rules, amounts and authorisation.'),('Currency','INR–USD movements affect the rupee value of your return.')])}
 </div>
</div></section>''' + CTA)

# ---------- GALLERY ----------
G = [('hero','Solar rooftop at sunset'),('p1','Utility-scale solar field'),('g1','Solar arrays under clear skies'),('g2','Bifacial modules on grassland'),('p3','Tracker rows, wide view'),('p2','Community solar with campus'),('g3','Installation crew at work'),('g4','Rooftop module installation'),('g5','Wind and solar at dusk'),('g6','Hybrid renewable landscape'),('p4','Freight rail infrastructure'),('p5','Port and logistics hub'),('p6','EV fast charging'),('g8','Logistics warehouse'),('g7','American infrastructure')]
pages['gallery.html'] = ('Project Gallery','Photo gallery of solar, storage and infrastructure project types.', phead('g1','Gallery','Project gallery','Solar, storage and infrastructure — the kinds of projects EB-5 capital helps build.') + '''
<section class="band"><div class="wrap"><div class="gal">''' + ''.join(f'<button type="button"><img src="img/{f}.jpg" alt="{t}"><span>{t}</span></button>' for f,t in G) + '''</div>
<p class="note" style="margin-top:14px">Representative stock photography. Aerial images, layouts and 3D visualisations of the Texas site will be added after surveys and design.</p></div></section>
<div class="lb" id="lb" role="dialog" aria-label="Photo viewer"><button class="btn x" type="button">Close</button><img src="" alt=""><p></p></div>''' + CTA)

# ---------- PROCESS ----------
steps = [('Week 1','Discovery call','Your goals, family, timeline and source of funds reviewed with our India desk.'),
         ('Weeks 2–4','Project selection','Compare offerings, PPMs and due-diligence reports side by side with your counsel.'),
         ('Weeks 3–8','Source-of-funds file','Bank statements, tax returns, property or business sale records and gift deeds assembled and translated.'),
         ('Weeks 4–10','Investment & I-526E','LRS remittance to escrow; your attorney files Form I-526E with USCIS.'),
         ('12–24 months','Petition approval','USCIS adjudicates I-526E. Filers inside the US may hold work and travel permits meanwhile.'),
         ('After approval','Conditional green card','Consular interview in Mumbai (or I-485 adjustment in the US); 2-year conditional residency.'),
         ('Year 2–3','I-829 & permanent card','Show jobs created and capital sustained; conditions removed and 10-year card issued.'),
         ('Year 5+','Exit & citizenship','Capital returned per offering terms; eligible for US citizenship after five years of residency.')]
pages['process.html'] = ('EB-5 Process','Step-by-step EB-5 application and investment journey.', phead('plane','Process','The EB-5 journey, step by step','From your first call to a permanent green card — what happens, when, and who does it.') + f'''
<section class="band"><div class="wrap two">
 <div><h2>Your journey</h2><ol class="ms">{''.join(f'<li><b>{t} <span class="st">{w}</span></b><span>{d}</span></li>' for w,t,d in steps)}</ol></div>
 <div><h2>Documents you'll need</h2>
 {''.join(f'<div class="lock"><div><b>{a}</b><br><span>{b}</span></div></div>' for a,b in [('Identity','Passports for all family members, birth and marriage certificates.'),('Source of funds','Bank statements, ITRs, Form 16, sale deeds, business financials, gift deeds.'),('Path of funds','Remittance records under LRS showing money moving from India to escrow.'),('Background','Police clearance certificates and medical exams (at visa stage).')])}
 <div class="panel" style="margin-top:20px"><h3>Plan your cost</h3>
 <label for="amt">Investment type</label><select id="amt"><option value="800000">TEA / infrastructure — $800,000</option><option value="1050000">Standard — $1,050,000</option><option value="937500">Projected 2027 TEA — about $937,500</option></select>
 <div class="row2"><div><label for="adm">Admin fee (USD)</label><input id="adm" type="number" value="60000" min="0"></div><div><label for="leg">Legal &amp; filing (USD)</label><input id="leg" type="number" value="35000" min="0"></div></div>
 <div class="row2"><div><label for="fx">USD to INR</label><input id="fx" type="number" step="0.01" value="88.50"></div><div><label for="fam">Family members</label><select id="fam"><option>1</option><option>2</option><option selected>3</option><option>4</option></select></div></div>
 <div class="total"><span>Total commitment</span><b id="tINR">₹0</b><span id="tUSD">$0</span></div><p class="note" id="lrs" style="margin-top:10px"></p></div></div>
</div></section>''' + CTA)

# ---------- PARTNERS ----------
pages['partners.html'] = ('Partners & Advisors','Regional center, legal, financial and EPC partners for GoEB5 projects.', phead('g7','Partners','Partners & advisors','The independent professionals who make an EB-5 project trustworthy.') + f'''
<section class="band"><div class="wrap">
<div class="cards">
 <div class="card">{ico(I['sun'])}<h3>Unite Group Inc., USA</h3><p>Parent and promoter of the Texas project. <span class="st ok">Confirmed</span></p></div>
 <div class="card">{ico(I['home'])}<h3>112 Citrus LLC</h3><p>Local project partner, McAllen area, Texas. <span class="st now">In progress</span></p></div>
 <div class="card">{ico(I['bolt'])}<h3>Unite Solar USA</h3><p>Proposed EPC and O&amp;M contractor. <span class="st ok">Group company</span></p></div>
 <div class="card">{ico(I['shield'])}<h3>USCIS-designated regional center</h3><p>Sponsors the offering and files the I-956F project application. <span class="st">To be appointed</span></p></div>
 <div class="card">{ico(I['doc'])}<h3>Securities &amp; immigration counsel</h3><p>Prepares the PPM and offering documents; investors also retain their own counsel. <span class="st">To be appointed</span></p></div>
 <div class="card">{ico(I['chart'])}<h3>Economist &amp; fund administrator</h3><p>Job-creation economic report, escrow agent and independent fund administration. <span class="st">To be appointed</span></p></div>
</div>
<p class="note" style="margin-top:16px">Partner names will be published here as engagements are signed.</p>
<h2 style="margin-top:40px">Become a partner</h2><p class="lede">We welcome regional centers, immigration attorneys, chartered accountants and migration agents across India and worldwide.</p><a class="btn navy" href="contact.html">Contact our partnerships team</a>
</div></section>''')

# ---------- FAQ & RESOURCES ----------
faq = re.search(r'(<details open>.*?</details>\s*(?:<details>.*?</details>\s*)*)\s*</div>\s*<div id="contact">', v2, re.S).group(1)
pages['faq.html'] = ('FAQ & Resources','EB-5 questions, brochures and official USCIS resources.', phead('liberty','FAQ & Resources','FAQ & resources','Straight answers, plus links to official US government sources.') + f'''
<section class="band"><div class="wrap two">
 <div><h2>Common questions</h2>{faq}
 <details><summary>Is the Texas project open for investment?</summary><p>Not yet. It is at concept and feasibility stage; EB-5 eligibility, structuring and offering documents are still being prepared.</p></details>
 <details><summary>Which languages do you support?</summary><p>English today, with Hindi and Telugu consultations available on request and website translations planned.</p></details></div>
 <div><h2>Official resources</h2><div class="res-links">
 <a href="https://www.uscis.gov/working-in-the-united-states/permanent-workers/eb-5-immigrant-investor-program">EB-5 Immigrant Investor Program<span>uscis.gov</span></a>
 <a href="https://www.uscis.gov/i-526e">Form I-526E<span>uscis.gov</span></a>
 <a href="https://www.uscis.gov/i-829">Form I-829<span>uscis.gov</span></a>
 <a href="https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html">Monthly Visa Bulletin<span>travel.state.gov</span></a>
 <a href="https://egov.uscis.gov/processing-times/">USCIS processing times<span>uscis.gov</span></a>
 <a href="https://www.sec.gov/resources-for-investors/investor-alerts-bulletins/investor-alerts-ia_immigrant">SEC investor alert on EB-5<span>sec.gov</span></a></div>
 <h3 style="margin-top:24px">Request the GoEB5 brochure</h3>
 <form class="panel" data-form="Brochure request" novalidate><label for="fn">Full name</label><input id="fn" required><label for="fe">Email</label><input id="fe" type="email" required><button class="btn" style="width:100%;margin-top:14px">Send me the brochure</button><div class="ok"></div></form></div>
</div></section>''' + CTA)

# ---------- PORTAL ----------
pages['portal.html'] = ('Investor Portal','Secure investor portal and data room — opening after offering documents are finalised.', phead('flag','Investor portal','Investor portal','Secure access to documents, project updates and your case progress.') + f'''
<section class="band"><div class="wrap two">
 <div class="panel"><h2 style="font-size:28px">Sign in</h2>
 <div class="warn" style="margin-bottom:12px">The portal opens once the legal structure and offering documents are final. Registered investors will receive an invitation by email.</div>
 <label for="pe">Email</label><input id="pe" type="email" disabled placeholder="Available at launch"><label for="pp">Password</label><input id="pp" type="password" disabled>
 <button class="btn" disabled style="width:100%;margin-top:14px;opacity:.5">Sign in</button>
 <h3 style="margin-top:28px">Register for early access</h3>
 <form data-form="Portal registration" novalidate><label for="rn">Full name</label><input id="rn" required><label for="re">Email</label><input id="re" type="email" required><label for="rc">Country</label><select id="rc" class="country"></select><button class="btn navy" style="width:100%;margin-top:14px">Register interest</button><div class="ok"></div></form></div>
 <div><h2>What's inside</h2>
 {''.join(f'<div class="lock"><div><b>{a}</b><br><span>{b}</span></div><span class="st">Locked</span></div>' for a,b in [('Private placement memorandum','Offering terms, risks and subscription documents.'),('Financial model','Project budget, revenue assumptions and exit plan.'),('Due diligence','Land title, permits, interconnection and EPC contracts.'),('Economic report','Job-creation analysis for I-526E and I-829.'),('Progress dashboard','Verified milestones, construction photos and jobs created.'),('My case','Petition status, documents uploaded and consultation history.')])}
 </div>
</div></section>''')

# ---------- CONTACT / APPLY ----------
pages['contact.html'] = ('Contact / Apply','Book an EB-5 consultation and prequalify as an investor.', phead('flag','Contact','Book a consultation','Prequalify in two minutes, choose a time, and speak with our India desk.') + f'''
<section class="band"><div class="wrap two">
 <form id="cform" class="panel" data-form="Consultation booking" novalidate>
  <h2 style="font-size:28px">Investor prequalification</h2>
  <div class="row2"><div><label for="n">Full name</label><input id="n" required autocomplete="name"></div><div><label for="p">Phone / WhatsApp</label><input id="p" type="tel" required autocomplete="tel"></div></div>
  <label for="e">Email</label><input id="e" type="email" required autocomplete="email">
  <div class="row2"><div><label for="c">Country of residence</label><select id="c" class="country"></select></div><div><label for="i">Interested in</label><select id="i"><option>Texas solar project</option><option>Solar projects</option><option>Infrastructure projects</option><option>Not sure yet</option></select></div></div>
  <div class="row2"><div><label for="rd">Investment readiness</label><select id="rd"><option>Funds available now</option><option>Within 6 months</option><option>6–12 months</option><option>Just exploring</option></select></div><div><label for="tl">Intended timeline</label><select id="tl"><option>File before 1 Jan 2027</option><option>During 2027</option><option>Flexible</option></select></div></div>
  <div class="row2"><div><label for="fm">Family applying</label><select id="fm"><option>Investor only</option><option>Investor + spouse</option><option>Investor + spouse + children</option></select></div><div><label for="us">Currently in the US?</label><select id="us"><option>No</option><option>Yes — H-1B</option><option>Yes — F-1 / OPT</option><option>Yes — other status</option></select></div></div>
  <label for="lg">Preferred language</label><select id="lg"><option>English</option><option>Hindi</option><option>Telugu</option></select>
  <h3 style="margin-top:22px">Choose a time</h3>
  <label for="bdate">Date</label><input id="bdate" type="date"><input id="btime" type="hidden"><div class="slots" id="slots"></div>
  <label for="m">Message</label><textarea id="m" rows="3"></textarea>
  <label for="consent" style="display:flex;gap:10px;align-items:flex-start;font-weight:400;font-size:14px"><input type="checkbox" id="consent" required style="width:20px;min-height:20px;margin-top:2px"> I agree to be contacted by call, WhatsApp or email.</label>
  <button class="btn" type="submit" style="width:100%;margin-top:12px">Confirm consultation</button><div class="ok"></div>
 </form>
 <div><h2>Other ways to reach us</h2>
  <div class="lock"><div><b>Email</b><br><span>info@goeb5.in</span></div></div>
  <div class="lock"><div><b>India desk</b><br><span>Hyderabad, Telangana · Mon–Sat, 10am–7pm IST</span></div></div>
  <div class="lock"><div><b>US head office</b><br><span>Unite Group, Inc., 244 Fifth Avenue, Suite #1849, New York, NY 10001</span></div></div>
  <img class="photo" src="img/liberty.jpg" alt="Statue of Liberty" style="aspect-ratio:4/3;margin-top:20px">
 </div>
</div></section>''')


# ---------- NEWS ----------
N=[('2026-11-16','Minimums rise on 1 January 2027','The EB-5 Reform and Integrity Act requires the $800,000 and $1,050,000 minimums to be adjusted for inflation from 1 January 2027. Industry projections put the new TEA minimum near $937,500; USCIS has not yet published final figures. Petitions filed before the adjustment are expected to keep today\'s amounts.'),
   ('2026-10-20','Set-aside visas remain the faster lane for India','While the unreserved EB-5 category stays backlogged for India-born investors, the rural, high-unemployment and infrastructure set-aside categories have continued to show as current in recent Visa Bulletins.'),
   ('2026-09-30','Grandfathering window closed on 30 September 2026','Petitions filed by 30 September 2026 received statutory grandfathering protection. The regional-center program itself remains authorised through 30 September 2027.'),
   ('2026-09-15','Unite Group advances its Texas Solar Park','Unite Group\'s 80 MW Texas Solar Park — a utility-scale, grid-connected project — is in development, alongside a proposed 112-acre solar and storage site in the McAllen area.')]
pages['news.html']=('News & Insights','EB-5 news and Unite Group project updates.', phead('countries','News','News &amp; insights','Key EB-5 dates, visa availability and Unite Group project updates.') + '<section class="band"><div class="wrap"><div class="news">' + ''.join(f'<article><time datetime="{d}">{d[8:]}/{d[5:7]}/{d[:4]}</time><h3 style="margin-top:6px">{t}</h3><p style="margin:0;color:var(--mute)">{b}</p></article>' for d,t,b in N) + '</div><p class="note" style="margin-top:14px">Summaries for general information; check uscis.gov and the Visa Bulletin for current rules.</p></div></section>' + CTA)

# ---------- CONNECT (social) ----------
pages['connect.html']=('Social & Connect','Follow GoEB5 and share it with your family.', phead('flag','Connect','Social &amp; connect','Follow GoEB5 for EB-5 updates, and share the opportunity with family and friends.') + f"""
<section class="band"><div class="wrap two">
 <div><h2>Follow GoEB5</h2><p class="lede">Our official channels are launching soon. Each button opens the profile once it is live.</p>
 <div class="share">{''.join(f'<a href="connect.html" data-follow="{k}">{svg(k,26)}<span>{NAMES[k]}<br><small class="note" style="font-weight:400">Official page launching soon</small></span></a>' for k in ['facebook','instagram','linkedin','x','youtube','whatsapp'])}</div></div>
 <div><h2>Share GoEB5</h2><p class="lede">Send goeb5.in to someone considering a US green card.</p>
 <div class="share">{''.join(f'<a href="#" data-share="{k}">{svg(k,26)}<span>Share on {NAMES[k]}</span></a>' for k in ['whatsapp','facebook','linkedin','x','telegram','email'])}</div>
 <h3 style="margin-top:28px">Unite Group leadership on LinkedIn</h3>
 <div class="res-links"><a href="https://linkedin.com/in/akhil-ponnada-135837109">Akhil Ponnada — Founder<span>LinkedIn</span></a><a href="https://www.linkedin.com/in/suryavidiyala">Surya Kumar Vidiyala — Co-Founder<span>LinkedIn</span></a><a href="https://www.unitegroupinc.com">Unite Group, Inc.<span>unitegroupinc.com</span></a></div></div>
</div></section>""")

# ---------- LEGAL ----------
def legal(f,title,img,intro,secs):
    pages[f]=(title,title+' — GoEB5', phead(img,title,title,intro) + '<section class="band"><div class="wrap prose">' + ''.join(f'<h2>{h}</h2>'+''.join(f'<p>{x}</p>' for x in ps) for h,ps in secs) + '<p class="note" style="margin-top:28px">Last updated 16 November 2026. Draft for review by counsel before launch.</p></div></section>')
legal('privacy.html','Privacy Policy','g7','How GoEB5 collects, uses and protects your information.',[
 ('Information we collect',['Details you submit in our forms: name, email, phone or WhatsApp number, country, investment readiness, timeline, family details and messages.','Basic technical data such as browser type and pages visited, used to keep the site working and secure.']),
 ('How we use it',['To respond to enquiries, schedule consultations, send requested brochures and project updates, and assess general suitability for the EB-5 program.','We do not sell your personal information.']),
 ('Sharing',['With your consent, we may share your details with independent immigration counsel, regional centers or project sponsors you choose to engage, and with service providers who host our systems under confidentiality obligations.']),
 ('Your choices',['You can ask us to access, correct or delete your information, or stop contacting you, by writing to info@goeb5.in.','We follow applicable data protection law, including India\'s Digital Personal Data Protection Act, 2023.']),
 ('Security and retention',['We use reasonable safeguards and keep data only as long as needed for the purposes above or as required by law.'])])
legal('terms.html','Terms of Use','g7','The terms that apply when you use goeb5.in.',[
 ('Use of the site',['GoEB5 provides general information about the US EB-5 program and investment opportunities. By using the site you agree to these terms.']),
 ('No advice',['Content is not legal, immigration, tax or investment advice. Always consult qualified, independent professionals before making decisions.']),
 ('No offer',['Nothing on this site is an offer to sell or a solicitation to buy securities. Any offering is made only through official offering documents to eligible investors, in compliance with applicable law.']),
 ('Intellectual property',['The GoEB5 name, logo and site content belong to their owners. Photography is used under the Unsplash License.']),
 ('Liability',['Information may change without notice. To the extent permitted by law, GoEB5 and Unite Group are not liable for decisions made on the basis of this site.']),
 ('Governing law',['These terms are governed by the laws of India, with courts at Hyderabad, Telangana having jurisdiction, unless otherwise required by law.'])])
legal('disclaimer.html','Investment Disclaimer','hero','Important information about EB-5 investment risk.',[
 ('Capital at risk',['EB-5 investments must be "at risk". You may lose some or all of your investment. Past performance of any project or sponsor does not predict future results.']),
 ('No guaranteed immigration outcome',['USCIS and the US Department of State alone decide petitions and visas. Investment does not guarantee a green card.']),
 ('Projects under evaluation',['Projects described as "under evaluation", including the proposed Texas solar site, have not been verified for EB-5 eligibility, TEA designation, job creation or regional-center sponsorship, and are not open for investment.']),
 ('Illustrative content',['Some project cards are illustrative examples for layout. Final terms appear only in a private placement memorandum.']),
 ('Securities law',['Offerings are made only through lawful channels and formal documentation. Read the SEC investor alert on EB-5 offerings before investing.'])])

# ---------- SITEMAP ----------
allp=[('index.html','Home')]+NAV[1:]+[('portal.html','Investor Portal'),('news.html','News & Insights'),('connect.html','Social & Connect'),('privacy.html','Privacy Policy'),('terms.html','Terms of Use'),('disclaimer.html','Investment Disclaimer')]
pages['sitemap.html']=('Sitemap','All pages on goeb5.in.', phead('countries','Sitemap','Sitemap','Every page on goeb5.in.') + '<section class="band"><div class="wrap"><div class="res-links">' + ''.join(f'<a href="{h}">{t}<span>{h}</span></a>' for h,t in allp) + '</div></div></section>')

for f,(t,d,b) in pages.items():
    (ROOT/f).write_text(shell(f,t,d,b))
print('built', len(pages), 'pages')

# ---------- single-file preview (hash routes) for the claude.ai artifact ----------
import html as _h
route = lambda f: 'home' if f=='index.html' else f[:-5]
def spa_links(x):
    return re.sub(r'href="([a-z0-9-]+)\.html"', lambda m: f'href="#{route(m.group(1)+".html")}"', x)
home_t,home_d,home_b = pages['index.html']
doc = shell('index.html', home_t, home_d, home_b)
tpls = ''.join(f'<template id="tpl-{route(f)}" data-title="{_h.escape(t)} — GoEB5">{spa_links(b)}</template>\n' for f,(t,d,b) in pages.items())
router = """<script>
window.GO_SPA=1;
</script>"""
router_end = """<script>
{const main=document.querySelector('main'),R=[...document.querySelectorAll('template[id^=tpl-]')].map(t=>t.id.slice(4));
 let cur='';
 const go=()=>{let h=(location.hash||'#home').slice(1);let anchor='';
  if(!R.includes(h)){anchor=h;h=document.getElementById(h)&&cur?cur:'home'}
  if(h!==cur){const t=document.getElementById('tpl-'+h);main.innerHTML='';main.appendChild(t.content.cloneNode(true));cur=h;document.title=t.dataset.title;
   document.querySelectorAll('.links a').forEach(a=>a.getAttribute('href')=='#'+h?a.setAttribute('aria-current','page'):a.removeAttribute('aria-current'));
   const l=document.getElementById('links');if(l&&l.classList.contains('open')){l.classList.remove('open');const m=document.querySelector('.menu');m.setAttribute('aria-expanded',false);m.textContent='Menu'}
   goInit();goSocial();}
  const el=anchor&&document.getElementById(anchor);if(el)el.scrollIntoView();else window.scrollTo(0,0)};
 addEventListener('hashchange',go);go()}
</script>"""
doc = spa_links(doc)
doc = re.sub(r'<main>.*?</main>', lambda m: '<main></main>\n'+tpls, doc, flags=re.S)
doc = doc.replace('<script src="assets/site.js"></script>', router + '\n<script src="assets/site.js"></script>\n' + router_end)
spa_dir = ROOT/'spa'; spa_dir.mkdir(exist_ok=True)
(spa_dir/'index.html').write_text(doc)
print('spa built', len(doc)//1024, 'KB')
