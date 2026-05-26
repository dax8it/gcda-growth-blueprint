from pathlib import Path
import shutil
from PIL import Image

ROOT = Path('/Users/Shared/GITHUB/gcda-growth-blueprint')
GCDA_REPO = Path('/Users/Shared/GITHUB/gcda_audit/gcdadance')
SITE = ROOT / 'site'
ASSETS = SITE / 'assets'
MEDIA = SITE / 'media'
BRIEFS = SITE / 'briefs'
for d in (ASSETS, MEDIA, BRIEFS):
    d.mkdir(parents=True, exist_ok=True)

# Keep the already-rendered British-female explainer media if present. This update is strategy/control-panel focused.
source_media = ROOT / 'site' / 'media'
for name in [
    'gcda-growth-explainer.mp4',
    'gcda-growth-explainer-poster.jpg',
    'gcda-growth-explainer-narration.mp3',
]:
    src = source_media / name
    dst = MEDIA / name
    if src.exists() and src.resolve() != dst.resolve():
        shutil.copy2(src, dst)

# Curated GCDA visual proof assets from current site repo.
image_candidates = [
    GCDA_REPO / 'public/images/hero/CNO05006.jpg',
    GCDA_REPO / 'public/images/sections/classes/CNO04471.jpg',
    GCDA_REPO / 'public/images/sections/classes/CNO04507.jpg',
    GCDA_REPO / 'public/images/sections/classes/CNO04816.jpg',
    GCDA_REPO / 'public/images/sections/studio/gallery/CNO03983.jpg',
    GCDA_REPO / 'public/images/sections/studio/gallery/CNO04167.jpg',
]
for idx, src in enumerate(image_candidates, 1):
    if src.exists():
        out = ASSETS / f'gcda-proof-{idx:02d}.jpg'
        im = Image.open(src).convert('RGB')
        im.thumbnail((1800, 1200), Image.Resampling.LANCZOS)
        im.save(out, quality=82, optimize=True)

brief_docs = {
'goal-and-positioning.md': '''# GCDA 2–6 Market Recovery Goal

## Goal
Win back Spanish Fort families with dancers ages 2–6 by making GCDA feel like the easiest, warmest, most convenient first dance activity in town — while preserving the studio’s deeper dance-education credibility for families who later want more.

## Working target
Rebuild the preschool/tiny-dancer pipeline in 90 days by increasing qualified trial-class inquiries, parent conversations, and local family visibility before making irreversible pricing changes.

## Strategic shift
Lead with **activity, joy, confidence, convenience, and first-class experience**. Keep the college/professional dance pathway as proof in the background, not the first thing a preschool parent has to buy into.

## Core message
Your child does not need to be “serious about dance” to start here. GCDA gives Spanish Fort toddlers and young children a joyful, age-appropriate first dance experience close to home — with real teachers and room to grow if they fall in love with it.
''',
'swot-2-6-market.md': '''# SWOT — Spanish Fort Ages 2–6 Dance Market

## Strengths
- Only dance school located in Spanish Fort, reducing commute friction for local families.
- Strong dance-education credibility, real faculty, and student-development pathway.
- Existing visual assets, classes, and social proof potential.
- Contact form has been repaired; Netlify capture is now working.

## Weaknesses
- Current public framing over-indexes on “premier dance education” and long-term training outcomes.
- Preschool parents often want a fun weekly activity, confidence, socialization, and convenience — not a career pathway yet.
- Class finder/schedule still needs stable presentation.
- Social and website proof are not sharply packaged around ages 2–6.
- Pricing may be perceived as higher without a clear toddler-parent value story.

## Opportunities
- Spanish Fort’s official 2024 population is 11,118, with Census under-5 share at 9.7%; rough age 2–6 cohort estimate is about 928 children before broader Eastern Shore draw.
- High household income and commute friction make “close to home” a real buying lever.
- Competitors win emotionally: ESDA uses parent empathy and testimonials; Creative Outlet sells confidence, bodies, self-esteem, friendships, and activity value.
- Build a “Tiny Dancer / First Dance Class” funnel with trial class, 6-week starter session, parent FAQs, and short-form video proof.

## Threats
- Parents already tolerate traffic to competitors if they perceive those studios as warmer, cheaper, easier, or more preschool-friendly.
- A $15 price gap can matter if the value story is unclear.
- Small-market math means every lost preschool family hurts future pipeline.
- If schedule, tuition, and trial-class paths remain hard to understand, social traffic will not convert.
''',
'immediate-action-plan.md': '''# Immediate Action Plan — Preschool/Tiny Dancer Recovery

## Completed website foundation
1. Homepage now leads with first-dance / close-to-home positioning for Spanish Fort families.
2. Summer 2026 schedule is published locally and treated as the source of truth.
3. Stale Jackrabbit schedule/openings browsing is hidden; Jackrabbit remains registration/portal only.
4. Register, Policies/FAQ, Faculty, Classes, and Company pages now reflect the provided season documents.
5. Summer packet and company PDFs are published and linked from customer-facing pages.
6. Contact form routing was repaired before the growth sprint.

## Next 48 hours
1. Publish a dedicated `Tiny Dancers / Ages 2–6` landing page with trial-class CTA, schedule/fallback, teacher trust, parent FAQs, and “close to home” copy.
2. Add or approve a no-pressure offer path: “Book a free trial class” or “Try your first Tiny Dancer class.”
3. Create the weekly inquiry/trial/enrollment tracking sheet.
4. Ask 5–10 current preschool/kindergarten parents for short testimonial lines and phone-shot clips.
5. Add Google Business Profile services/posts for toddler dance, preschool dance, creative movement, beginner ballet/tap, and Bluey Camp.

## First 7 days
1. Launch a Spanish Fort parent campaign: “Your first dance class, close to home.”
2. Post 7 short videos/Reels: first class nerves, teacher greeting, tiny dancer warmup, what to wear, parent FAQ, why close-to-home matters, trial invitation.
3. Build referral loop: “Know a Spanish Fort family with a 2.5–5 year old?”
4. Add local partner outreach: preschools, daycares, pediatric offices, mom groups, churches, library story-time/community calendars.
5. Review inquiry data and identify whether the blocker is awareness, CTA, schedule fit, follow-up, or price.

## First 30 days
1. Run a 4–6 week Tiny Dancer Starter Session as a campaign, not a discount race.
2. Test pricing resistance with an offer before changing tuition: free trial, waived registration for preschool, sibling/friend credit, or $15 local-family intro credit.
3. Replace placeholder/stock-feeling proof with real parent quotes, preschool clips, and final faculty images/bios.
4. Restore Jackrabbit schedule links only if portal schedule parity is verified.
''',
'pricing-hypothesis.md': '''# Pricing Hypothesis — Do Not Blindly Cut First

## Current problem
A $15 higher price can hurt only if parents see GCDA as interchangeable with farther-away activity studios. If GCDA is framed as a convenient, warm, high-quality first activity in Spanish Fort, the local convenience may offset price.

## Recommendation
Do not permanently cut tuition until we have evidence. Run an offer test for ages 2–6 first.

## Tests to run
1. **Free trial class** — lowest-risk conversion lever.
2. **6-week Tiny Dancer Starter Session** — clear package for activity-seeking parents.
3. **Spanish Fort local-family credit** — test the $15 objection without resetting brand value.
4. **Waived registration for preschool enrollments by a deadline** — protects monthly tuition.
5. **Bring-a-friend credit** — turns current families into acquisition.

## Decision rule
If trial inquiries rise but enrollments fail after price is discussed, pricing is the blocker. If inquiries are low, the real blocker is presentation/discovery, not price.
''',
'website-and-social-creative-brief.md': '''# Website + Social Creative Brief — Ages 2–6

## Website hero direction
Headline: `First Dance Classes for Ages 2–6 in Spanish Fort`
Subhead: `A joyful, beginner-friendly weekly activity where little dancers build confidence, coordination, friendships, and a love of movement — close to home.`
Primary CTA: `Book a Free Trial Class`
Secondary CTA: `See Tiny Dancer Classes`

## Landing page sections
1. Is my child ready for dance?
2. What happens in a first class?
3. Tiny dancer class options by age.
4. Meet the preschool teachers.
5. What to wear / what parents need to know.
6. Parent proof and short videos.
7. Pricing/offer/test CTA.
8. FAQ and contact form.

## Social pillars
- First-class comfort: what the first day feels like.
- Parent reassurance: “You do not have to know anything about dance.”
- Tiny wins: balance, rhythm, listening, confidence, friends.
- Spanish Fort convenience: no traffic battle for a 30–45 minute class.
- Teacher warmth: faces and voices of the people teaching young children.
- Proof: parent quotes, tiny dancer smiles, recitals without pressure.

## 10 immediate content ideas
1. “Is your 3-year-old ready for dance? Here are 3 signs.”
2. “What happens in a first Tiny Dancer class at GCDA?”
3. “No dance experience needed — this is a weekly activity first.”
4. “Spanish Fort parents: skip the traffic for your child’s first dance class.”
5. “What should my toddler wear to dance?”
6. “Shy child? Here’s how we help them warm up.”
7. “Ballet/tap combo explained for ages 2–6.”
8. “Meet the teacher who greets your child at the door.”
9. “First recital does not have to be scary.”
10. “Free trial week: bring your tiny dancer.”
''',
'current-state-and-next-actions.md': '''# Current State + Next Actions — GCDA Preschool Recovery

## Published website state
As of the latest production update, the live GCDA site now has the website-side foundation for preschool market recovery in place:

- `gcdadance.com` is deployed from `dax8it/gcdadance-next` main.
- Contact form routing was repaired and published.
- Homepage now leads with first-dance / close-to-home positioning.
- Summer 2026 schedule is published as the website source of truth.
- Jackrabbit schedule/openings browsing is hidden where it could conflict with the confirmed schedule.
- Registration still uses Jackrabbit only as the secure registration/parent-portal path.
- Classes page shows 21 confirmed Summer 2026 class cards and links the Summer packet PDFs.
- Register and Policies pages include Summer 2026 dates, Bluey Camp, tuition, and mismatch guidance.
- Faculty page includes the updated Summer 2026 faculty list.
- Company Team page includes 2026–2027 commitments, fees, Destro information, recognition, and company PDFs.

## What is still missing
These are not website-code blockers, but they are the remaining recovery levers:

1. **Dedicated Tiny Dancers / Ages 2–6 landing page.** The homepage and classes page now carry the message, but a focused landing page would convert ads/social/GBP traffic better.
2. **True trial-class CTA.** Current flow routes to schedule/register/contact. A `Book a Free Trial Class` path still needs either an approved offer and form field or a simple contact-form subject route.
3. **Fresh preschool proof.** Need parent quotes, phone-shot clips, teacher greeting clips, and class photos focused on ages 2.5–5.
4. **Google Business Profile work.** Preschool/toddler/beginner dance services, GBP posts, and Q&A still need to be added manually.
5. **Tracking sheet / dashboard.** We need a weekly operating log for inquiries, trial bookings, trial attendance, enrollments, source, and price objections.
6. **Price test.** No permanent tuition change yet. Test free trial, waived registration, or local-family intro credit only after inquiry/trial data starts coming in.
7. **Local outreach.** Preschool/daycare/church/library/mom-group/community-calendar outreach has not been executed.
8. **Provider parity.** Jackrabbit schedule still needs to be corrected or verified before schedule browsing links are restored.
9. **Final assets.** Grace has a temporary placeholder image; some bios/photos may still need final source material.

## Next action items

### Next 48 hours
- Publish one dedicated Tiny Dancers / Ages 2–6 landing page.
- Add a trial-class CTA or contact-form path specifically for preschool parents.
- Create a simple tracking sheet with columns: date, parent name, child age, source, desired class, trial booked, trial attended, enrolled, objection, follow-up owner.
- Pull 5–10 parent proof requests from current preschool/kindergarten families.
- Add two GBP posts: `First Dance Classes Close to Home` and `Bluey Dance Adventure Camp`.

### Next 7 days
- Record/post 7 short-form pieces: first class walkthrough, what to wear, shy child reassurance, teacher intro, Bluey Camp reminder, close-to-home convenience, parent FAQ.
- Launch a current-family referral ask: “Know a Spanish Fort family with a 2.5–5 year old?”
- Send outreach to 10 local preschool/daycare/community partners.
- Review first inquiry data and identify whether the bottleneck is awareness, CTA, schedule fit, follow-up, or price.

### Next 30 days
- Run a Tiny Dancer Starter Session or trial week campaign.
- Test one offer without cutting base tuition: waived registration, bring-a-friend credit, or limited local-family intro credit.
- Collect/ship parent testimonials and update the landing page with real proof.
- Decide whether Jackrabbit links can be restored based on provider parity.
- Review conversion metrics weekly and update the plan based on evidence.
''',
'control-panel-metrics.md': '''# Control Panel Metrics

## North-star goal
Recover the ages 2–6 pipeline in Spanish Fort.

## Weekly dashboard
- Trial-class inquiries for ages 2–6.
- Trial classes attended.
- Trial-to-enrollment conversion rate.
- Preschool/tiny-dancer enrollments by class.
- Website clicks on `Book a Free Trial Class`.
- Contact form submissions mentioning ages 2–6.
- Social profile visits and website taps from preschool content.
- GBP calls, direction requests, and website visits.
- Review count and new reviews mentioning young children.
- Price objections logged by staff.

## Control thresholds
- If inquiries are low: fix website/social visibility and CTA clarity.
- If trials are booked but not attended: fix reminders and parent prep.
- If trials attend but do not enroll: inspect price, schedule, teacher fit, class experience.
- If social engagement rises but site actions do not: improve landing page and link path.
- If price objections exceed 30% of trial follow-ups: test registration waiver or $15 intro credit.
'''
}
for name, content in brief_docs.items():
    (BRIEFS / name).write_text(content)

imgs = sorted(ASSETS.glob('gcda-proof-*.jpg'))
hero_img = imgs[0].name if imgs else ''
photo_strip = ''.join(f'<img src="/assets/{p.name}" alt="GCDA class and studio proof image">' for p in imgs[:4])

css = r'''
:root{--ink:#24152e;--muted:#67566a;--paper:#fffaf4;--soft:#f7e7ef;--rose:#ff4f85;--plum:#3b2144;--violet:#7c3aed;--green:#1f8a70;--amber:#f5a524;--red:#e11d48;--line:#ead6e2;--card:#fff;--shadow:rgba(66,38,82,.18) 0 24px 70px -28px,rgba(0,0,0,.08) 0 10px 24px -16px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:'DM Sans',system-ui,-apple-system,Segoe UI,sans-serif;color:var(--ink);background:radial-gradient(circle at top right,#f1dbe8 0,#fffaf4 36%,#fbf4eb 100%);line-height:1.45}.nav{position:sticky;top:0;z-index:50;background:rgba(255,250,244,.86);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}.nav-inner{max-width:1240px;margin:auto;display:flex;align-items:center;justify-content:space-between;padding:14px 22px}.brand{font-weight:900;letter-spacing:-.04em;color:var(--ink);text-decoration:none}.brand span{color:var(--rose)}.links a{color:var(--ink);text-decoration:none;font-size:13px;font-weight:800;margin-left:15px}.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:12px 18px;font-weight:900;text-decoration:none;border:1px solid transparent}.btn.primary{background:var(--ink);color:white;box-shadow:var(--shadow)}.btn.rose{background:var(--rose);color:white}.btn.ghost{background:#fff;color:var(--ink);border-color:var(--line)}.hero{max-width:1240px;margin:auto;padding:72px 22px 46px;display:grid;grid-template-columns:1.05fr .95fr;gap:42px;align-items:center}.eyebrow{color:var(--rose);font-weight:900;letter-spacing:.13em;text-transform:uppercase;font-size:12px}.hero h1{font-size:clamp(46px,6.5vw,88px);letter-spacing:-.075em;line-height:.92;margin:14px 0 22px}.hero p{font-size:22px;color:var(--muted);max-width:760px}.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}.dashboard,.panel,.card,.mock,.time{background:rgba(255,255,255,.78);border:1px solid var(--line);border-radius:30px;box-shadow:var(--shadow)}.dashboard{padding:18px}.dash-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.metric{padding:18px;border-radius:24px;background:#fff}.metric.wide{grid-column:1/-1}.metric small{display:block;color:var(--muted);font-weight:900;text-transform:uppercase;letter-spacing:.08em;font-size:11px}.metric b{display:block;font-size:38px;letter-spacing:-.06em}.metric span{display:block;color:var(--muted);font-size:14px}.metric.good b{color:var(--green)}.metric.danger b{color:var(--red)}.metric.rose b{color:var(--rose)}.section{max-width:1240px;margin:0 auto;padding:58px 22px}.section h2{font-size:clamp(34px,4.3vw,60px);letter-spacing:-.055em;line-height:1;margin:10px 0 22px}.section>p{font-size:20px;color:var(--muted);max-width:880px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card,.panel,.mock,.time{padding:24px}.card h3,.mock h3,.time h3{font-size:24px;margin:0 0 10px;letter-spacing:-.035em}.card p,.mock p,.time p,li{color:var(--muted)}.two{display:grid;grid-template-columns:1fr 1fr;gap:22px}.swot{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}.swot .card:nth-child(1){border-top:6px solid var(--green)}.swot .card:nth-child(2){border-top:6px solid var(--amber)}.swot .card:nth-child(3){border-top:6px solid var(--violet)}.swot .card:nth-child(4){border-top:6px solid var(--red)}.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.time:before{content:attr(data-day);display:inline-grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--plum);color:white;font-weight:900;margin-bottom:14px}.check{padding-left:0;list-style:none}.check li{margin:11px 0;padding-left:30px;position:relative}.check li:before{content:'✓';position:absolute;left:0;top:0;color:var(--green);font-weight:900}.table{width:100%;border-collapse:collapse;background:#fff;border-radius:24px;overflow:hidden;box-shadow:var(--shadow)}.table th,.table td{text-align:left;padding:16px;border-bottom:1px solid var(--line);vertical-align:top}.table th{background:var(--plum);color:white}.quote{font-size:28px;line-height:1.15;letter-spacing:-.04em;background:var(--plum);color:white;padding:30px;border-radius:30px;margin-top:20px}.photo-strip{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.photo-strip img,.mock img{width:100%;height:210px;object-fit:cover;border-radius:22px}.video-wrap{display:grid;grid-template-columns:1.25fr .75fr;gap:26px;align-items:center}.video-wrap video{width:100%;border-radius:30px;box-shadow:var(--shadow);background:#000}.brief-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.brief-grid a{text-decoration:none;color:var(--ink)}footer{padding:42px 22px;text-align:center;color:var(--muted)}@media(max-width:900px){.hero,.two,.video-wrap{grid-template-columns:1fr}.cards,.timeline,.brief-grid,.swot,.photo-strip{grid-template-columns:1fr}.links{display:none}.hero h1{font-size:48px}}
'''

index = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GCDA Preschool Market Recovery Control Panel</title><meta name="description" content="A control panel and action plan for recovering GCDA's ages 2–6 dance market share in Spanish Fort."><meta property="og:title" content="GCDA Preschool Market Recovery"><meta property="og:description" content="SWOT, immediate action plan, website strategy, social creative briefs, pricing tests, and control metrics for GCDA ages 2–6 growth."><meta property="og:image" content="/media/gcda-growth-explainer-poster.jpg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet"><link rel="stylesheet" href="/styles.css"></head><body><nav class="nav"><div class="nav-inner"><a class="brand" href="#top">GCDA<span>Control</span></a><div class="links"><a href="#diagnosis">Diagnosis</a><a href="#state">State</a><a href="#swot">SWOT</a><a href="#action">Action</a><a href="#pricing">Pricing</a><a href="#social">Social</a><a href="#metrics">Metrics</a><a href="#briefs">Briefs</a></div><a class="btn rose" href="#action">Immediate plan</a></div></nav>
<header class="hero" id="top"><div><div class="eyebrow">Spanish Fort ages 2–6 recovery / website foundation live</div><h1>Win back the tiny dancer market close to home.</h1><p>The website foundation is now live: first-dance positioning, confirmed Summer 2026 schedule, visible packet PDFs, repaired contact routing, and Jackrabbit schedule links hidden until parity. The next phase is demand capture: a dedicated Tiny Dancers path, parent proof, GBP/social execution, outreach, and weekly conversion tracking.</p><div class="hero-actions"><a class="btn primary" href="#action">See next actions</a><a class="btn ghost" href="#state">Current state</a></div></div><aside class="dashboard"><div class="dash-grid"><div class="metric rose"><small>Target cohort</small><b>2–6</b><span>preschool + kindergarten families</span></div><div class="metric"><small>Official city pop.</small><b>11.1k</b><span>Census 2024; broader local draw is still small</span></div><div class="metric good"><small>Rough cohort</small><b>~928</b><span>estimated Spanish Fort ages 2–6 from Census age shares</span></div><div class="metric danger"><small>Market issue</small><b>Leak</b><span>families drive farther despite local option</span></div><div class="metric wide"><small>Goal</small><b>Rebuild the starter pipeline.</b><span>Website foundation is live; next target is measured inquiry and trial growth.</span></div></div></aside></header>
<section class="section" id="diagnosis"><div class="eyebrow">Diagnosis</div><h2>The offer is being heard as “serious dance school” when many preschool parents want “great weekly activity.”</h2><div class="cards"><article class="card"><h3>Parent job-to-be-done</h3><p>For ages 2–6, many parents are buying confidence, movement, listening skills, socialization, cute memories, convenience, and a predictable weekly activity — not a college dance pathway yet.</p></article><article class="card"><h3>Competitive psychology</h3><p>Nearby studios win with emotional parent language: confidence, family, age-appropriate care, testimonials, friendships, and recital reassurance. GCDA has the substance but needs the preschool packaging.</p></article><article class="card"><h3>Local advantage</h3><p>Spanish Fort parents already face traffic. “Close to home” should be a conversion lever: no drive to Daphne/Fairhope for a 30–45 minute toddler class if the local option feels warm and easy.</p></article></div><div class="quote">Do not make a 3-year-old’s parent buy the dream of a dance career. Sell the first happy class. Let the long-term pathway be the proof, not the pitch.</div></section>
<section class="section" id="market"><div class="eyebrow">Market facts</div><h2>Small-market math means every preschool family matters.</h2><table class="table"><tr><th>Signal</th><th>What we know</th><th>Implication</th></tr><tr><td>Population</td><td>U.S. Census QuickFacts lists Spanish Fort at 11,118 people in 2024 and 11,203 in 2025 estimate.</td><td>This is not a big-city funnel. The campaign has to be local, repeated, and relationship-driven.</td></tr><tr><td>Young-child pool</td><td>Under 5 is 9.7%; rough ages 2–6 cohort estimate is ~928 children.</td><td>A few dozen families can materially change the preschool pipeline.</td></tr><tr><td>Income/commute</td><td>Median household income is about $99k; mean commute is 26 minutes.</td><td>Price matters, but time/convenience and trust may matter as much or more.</td></tr><tr><td>Competitors</td><td>ESDA foregrounds parent confidence/testimonials; Creative Outlet foregrounds self-esteem/friendships; BayPointe has visible tuition anchors around $72 for 45–60 minutes.</td><td>GCDA needs preschool-specific warmth and value clarity before cutting price.</td></tr></table></section>
<section class="section" id="state"><div class="eyebrow">Current state</div><h2>Website foundation is live. The remaining work is acquisition, proof, tracking, and offer testing.</h2><div class="cards"><article class="card"><h3>Live now</h3><p>Homepage positioning, confirmed Summer 2026 schedule, class cards, PDF packet links, registration guidance, policies/FAQ, faculty, company info, and contact routing are published on gcdadance.com.</p></article><article class="card"><h3>Still missing</h3><p>Dedicated Tiny Dancers landing page, true trial-class CTA, parent proof clips/quotes, GBP services/posts, tracking sheet, local outreach, price test, and Jackrabbit schedule parity.</p></article><article class="card"><h3>Decision rule</h3><p>Do not cut tuition blindly. First track inquiries, trials, attendance, enrollments, and price objections so we know whether the bottleneck is awareness, CTA, schedule, follow-up, or price.</p></article></div></section>
<section class="section" id="swot"><div class="eyebrow">SWOT</div><h2>What GCDA can use — and what can hurt if we ignore it.</h2><div class="swot"><article class="card"><h3>Strengths</h3><ul><li>Only dance school in Spanish Fort.</li><li>Real dance-education credibility and faculty depth.</li><li>Strong facility/photo proof available.</li><li>Contact form repaired and production website refreshed with source-of-truth Summer 2026 content.</li></ul></article><article class="card"><h3>Weaknesses</h3><ul><li>No dedicated Tiny Dancers landing page yet; preschool message exists but needs its own conversion page.</li><li>Jackrabbit schedule parity is still unresolved; external schedule browsing stays hidden.</li><li>Fresh parent quotes, clips, final faculty photos, and preschool proof still need to be collected.</li><li>Pricing may feel high if value is unclear.</li></ul></article><article class="card"><h3>Opportunities</h3><ul><li>Own “first dance class in Spanish Fort.”</li><li>Turn traffic avoidance into value.</li><li>Launch Tiny Dancer Starter Session.</li><li>Use current families for reviews/referrals.</li></ul></article><article class="card"><h3>Threats</h3><ul><li>Parents keep driving to warmer-feeling competitors.</li><li>Small cohort magnifies each lost family.</li><li>Discounting without diagnosis weakens positioning.</li><li>Untracked inquiries and weak follow-up data can hide the real bottleneck.</li></ul></article></div></section>
<section class="section" id="goal"><div class="eyebrow">Operating goal</div><h2>90-day goal: recover the preschool/tiny-dancer pipeline.</h2><div class="two"><article class="mock"><h3>North star</h3><p>Increase qualified ages 2–6 trial-class inquiries and enrollments from Spanish Fort families by making GCDA the obvious close-to-home first dance class.</p><ul class="check"><li>Lead with activity, joy, confidence, friends, and convenience.</li><li>Back it with teacher quality and dance education.</li><li>Measure inquiries, trials, enrollments, and price objections weekly.</li></ul></article><article class="mock"><img src="/assets/{hero_img}" alt="GCDA dancer proof"><h3>New positioning</h3><p><strong>Headline:</strong> First Dance Classes for Ages 2–6 in Spanish Fort</p><p><strong>CTA:</strong> Book a Free Trial Class</p><p><strong>Promise:</strong> A joyful, age-appropriate weekly activity close to home.</p></article></div></section>
<section class="section" id="action"><div class="eyebrow">Next action</div><h2>Move from website foundation to measured demand capture.</h2><div class="timeline"><article class="time" data-day="48h"><h3>Next 48 hours</h3><p>Publish a dedicated Tiny Dancers / Ages 2–6 landing page, add an approved trial-class CTA, create the tracking sheet, request 5–10 parent proof clips/quotes, and post GBP updates for preschool dance and Bluey Camp.</p></article><article class="time" data-day="7d"><h3>First 7 days</h3><p>Launch “Your first dance class, close to home,” post 7 short videos, start the referral ask, contact 10 local partners, and review inquiry data for the first bottleneck.</p></article><article class="time" data-day="30d"><h3>First 30 days</h3><p>Run a Tiny Dancer Starter Session or trial week, test one offer without cutting base tuition, ship parent proof to the landing page, and restore Jackrabbit schedule links only after parity.</p></article></div></section>
<section class="section" id="pricing"><div class="eyebrow">Pricing</div><h2>Do not blindly cut $15. Test the objection.</h2><div class="cards"><article class="card"><h3>If inquiries are low</h3><p>The issue is not price yet. Fix awareness, messaging, social proof, class clarity, and CTA friction first.</p></article><article class="card"><h3>If trials attend but do not enroll</h3><p>Then inspect price, schedule fit, class experience, and follow-up. Log the exact objection.</p></article><article class="card"><h3>Offer tests</h3><p>Free trial, 6-week starter session, waived registration, sibling/friend credit, or a temporary $15 Spanish Fort intro credit. Protect monthly tuition until data says otherwise.</p></article></div></section>
<section class="section" id="website"><div class="eyebrow">Website next layer</div><h2>The foundation is live; now add the focused preschool landing page.</h2><div class="two"><article class="panel"><h3>Still required: Tiny Dancers / Ages 2–6</h3><ul class="check"><li>Is my child ready for dance?</li><li>What happens in a first class?</li><li>Age/day/time options or clear placement help.</li><li>Meet the preschool teacher.</li><li>What to wear / parent prep.</li><li>Free trial CTA and contact form.</li></ul></article><article class="panel"><h3>Copy shift</h3><p>From: “Premier dance education / passion meets technique.”</p><p>To: “A joyful first dance class for Spanish Fort toddlers and young children — close to home.”</p><p>The education pathway stays on the page, but below the preschool parent’s immediate questions.</p></article></div></section>
<section class="section" id="social"><div class="eyebrow">Social strategy</div><h2>Make parents feel the class before they compare tuition.</h2><div class="cards"><article class="card"><h3>Content pillars</h3><p>First-class comfort, parent reassurance, tiny wins, Spanish Fort convenience, teacher warmth, real proof.</p></article><article class="card"><h3>Formats</h3><p>15–30 second Reels/TikToks, parent FAQ carousels, teacher intros, class clips, story polls, trial-week reminders.</p></article><article class="card"><h3>Creative hook</h3><p>“Your child’s first dance class does not have to mean a traffic battle.”</p></article></div><div class="photo-strip">{photo_strip}</div></section>
<section class="section" id="metrics"><div class="eyebrow">Control panel</div><h2>Weekly metrics decide what we fix next.</h2><table class="table"><tr><th>Metric</th><th>Why it matters</th><th>Decision trigger</th></tr><tr><td>Ages 2–6 trial inquiries</td><td>Measures whether presentation/social is creating demand.</td><td>If low: fix messaging, reach, landing page, CTA.</td></tr><tr><td>Trial attendance</td><td>Shows whether follow-up/reminders are working.</td><td>If low: add text reminders and parent prep.</td></tr><tr><td>Trial-to-enrollment rate</td><td>Shows offer/class/price fit.</td><td>If low: inspect price, schedule, experience, follow-up.</td></tr><tr><td>Price objections</td><td>Determines whether the $15 issue is real.</td><td>If >30% of trial follow-ups: run registration waiver or intro credit.</td></tr><tr><td>Social-to-site actions</td><td>Shows if content is converting, not just getting likes.</td><td>If engagement but no clicks: fix link path and landing page.</td></tr></table></section>
<section class="section" id="video"><div class="video-wrap"><video controls preload="metadata" poster="/media/gcda-growth-explainer-poster.jpg"><source src="/media/gcda-growth-explainer.mp4" type="video/mp4"></video><div><div class="eyebrow">Existing explainer</div><h2>Prior narrated strategy remains available.</h2><p>The site is now past the first implementation gate. Use the video as background context, but operate from the current-state and next-actions plan above.</p><a class="btn rose" href="/media/gcda-growth-explainer.mp4">Download MP4</a></div></div></section>
<section class="section" id="briefs"><div class="eyebrow">Briefs</div><h2>Working artifacts for action.</h2><div class="brief-grid"><a class="card" href="/briefs/goal-and-positioning.md"><h3>Goal + Positioning</h3><p>North star and message shift.</p></a><a class="card" href="/briefs/swot-2-6-market.md"><h3>SWOT</h3><p>Strengths, weaknesses, opportunities, threats.</p></a><a class="card" href="/briefs/immediate-action-plan.md"><h3>Immediate Action Plan</h3><p>72 hours, 7 days, 30 days.</p></a><a class="card" href="/briefs/pricing-hypothesis.md"><h3>Pricing Hypothesis</h3><p>How to test the $15 question.</p></a><a class="card" href="/briefs/website-and-social-creative-brief.md"><h3>Website + Social Brief</h3><p>Creative direction and content ideas.</p></a><a class="card" href="/briefs/current-state-and-next-actions.md"><h3>Current State</h3><p>What is live, what is missing, and next actions.</p></a><a class="card" href="/briefs/control-panel-metrics.md"><h3>Control Metrics</h3><p>Weekly dashboard and thresholds.</p></a></div></section>
<footer><p>GCDA Preschool Market Recovery Control Panel · updated with current live-site state, remaining gaps, and next actions.</p><p><a href="https://gcdadance.com">gcdadance.com</a> · <a href="https://gcda-growth-blueprint.netlify.app">control panel</a></p></footer></body></html>'''

(SITE / 'styles.css').write_text(css)
(SITE / 'index.html').write_text(index)
(SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
(ROOT / 'netlify.toml').write_text('[build]\n  publish = "site"\n\n[[headers]]\n  for = "/media/*.mp4"\n  [headers.values]\n    Content-Type = "video/mp4"\n    Cache-Control = "public, max-age=31536000, immutable"\n\n[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Content-Type-Options = "nosniff"\n    Referrer-Policy = "strict-origin-when-cross-origin"\n')
(ROOT / 'README.md').write_text('# GCDA Preschool Market Recovery Control Panel\n\nClient-facing control panel for recovering GCDA\'s Spanish Fort ages 2–6 dance market share. Updated with current published-site state, remaining gaps, next action items, website/social strategy, pricing test hypothesis, and weekly control metrics.\n\n## Live URLs\n\n- Production: https://gcda-growth-blueprint.netlify.app\n- GitHub: https://github.com/dax8it/gcda-growth-blueprint\n\n## Local preview\n\n```bash\npython3 -m http.server 4173 -d site\n```\n\nNetlify publish directory: `site`.\n')
(ROOT / '.gitignore').write_text('.DS_Store\n.render-frames/\nnode_modules/\n.netlify/\n__pycache__/\n*.pyc\n')
print('built', SITE / 'index.html')
