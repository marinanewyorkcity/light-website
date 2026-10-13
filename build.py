#!/usr/bin/env python3
"""Builds the marinanewyorkcity.com static site. Run: python3 build.py
Generates all HTML pages from the templates below + events.json + styles.css.
"""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

SOCIALS = [
    ("Instagram", "https://www.instagram.com/marina.newyorkcity/"),
    ("TikTok", "https://www.tiktok.com/@marina.newyorkcity"),
    ("Facebook", "https://www.facebook.com/marina.nycity"),
    ("YouTube", "https://www.youtube.com/@marina.newyorkcity"),
    ("Threads", "https://www.threads.com/@Marina.newyorkcity"),
    ("Pinterest", "https://www.pinterest.com/marinanewyorkcity/"),
]

NAV = [
    ("Home", "index.html"),
    ("NYC Events", "events.html"),
    ("Shop", "shop.html"),
    ("Guides", "guides.html"),
    ("About", "about.html"),
    ("Contact", "contact.html"),
]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://marinanewyorkcity.com/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://marinanewyorkcity.com/">
  <meta property="og:image" content="https://marinanewyorkcity.com/hero.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Garet:wght@300;400;500;600;700&family=League+Gothic&family=Noto+Serif+Display:ital,wdth,wght@0,62,400..900;1,62,400..900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="logo.png" type="image/png">
</head>
<body>
"""

def header(active):
    links = "\n".join(
        f'      <a href="{href}"{" class=\"active\"" if name == active else ""}>{name}</a>'
        for name, href in NAV
    )
    return f"""  <header class="site-header">
    <a class="wordmark" href="index.html"><img src="logo.png" alt="Marina New York City logo"> <span>Marina <em>New York City</em></span></a>
    <nav aria-label="Main navigation">
{links}
    </nav>
  </header>

  <main>
"""

def footer():
    socials = "\n".join(
        f'        <a href="{url}" target="_blank" rel="noopener">{name}</a>'
        for name, url in SOCIALS
    )
    return f"""  </main>

  <section class="follow" aria-label="Follow Marina">
    <p class="section-kicker reveal">Follow and Stay Connected</p>
    <div class="follow-links reveal">
{socials}
        <a href="https://links.marinanewyorkcity.com" target="_blank" rel="noopener">All My Links</a>
    </div>
  </section>

  <footer class="site-footer">
    <p>&copy; 2026 @marina.newyorkcity. All Rights Reserved.</p>
  </footer>

  <script src="site.js"></script>
</body>
</html>
"""

def page(name, title, desc, active, content, extra_scripts=""):
    html = head(title, desc) + header(active) + content + footer()
    if extra_scripts:
        html = html.replace('<script src="site.js"></script>', extra_scripts + '\n  <script src="site.js"></script>')
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)
    print("wrote", name)

# ---------------------------------------------------------------- home ---
def home_content():
    return """
    <section class="hero" aria-label="Introduction">
      <div class="hero-bg-wrap"><img class="hero-bg" src="hero.jpg" alt="New York City skyline at night with the Brooklyn Bridge" fetchpriority="high"></div>
      <div class="hero-overlay"></div>
      <div class="hero-inner">
        <p class="hero-kicker reveal">Where Magic Begins</p>
        <h1 class="reveal">New York, New York</h1>
        <p class="hero-sub reveal">Cinematic iPhone videography by <a href="https://www.instagram.com/marina.newyorkcity/" target="_blank" rel="noopener">@marina.newyorkcity</a></p>
        <div class="hero-cta reveal">
          <a class="btn btn-gold" href="contact.html">Work With Me</a>
          <a class="btn btn-ghost" href="events.html">Explore NYC Events</a>
        </div>
      </div>
      <a class="scroll-hint" href="#stats" aria-label="Scroll down"><span></span></a>
    </section>

    <section class="stats" id="stats" aria-label="By the numbers">
      <div class="stat reveal">
        <p class="stat-number"><span class="counter" data-target="30" data-suffix="M+">0</span></p>
        <p class="stat-label">Monthly Reel Views</p>
      </div>
      <div class="stat reveal">
        <p class="stat-number"><span class="counter" data-target="149" data-suffix="K+">0</span></p>
        <p class="stat-label">Instagram Followers</p>
      </div>
      <div class="stat reveal">
        <p class="stat-number"><span class="counter" data-target="100" data-suffix="%">0</span></p>
        <p class="stat-label">Shot on iPhone</p>
      </div>
    </section>

    <section class="about" id="about" aria-label="About Marina">
      <div class="about-photos reveal">
        <img src="about-marina.jpg" alt="Marina Kapler, NYC content creator and iPhone videographer" loading="lazy">
        <img src="empire.jpg" alt="Empire State Building at sunrise, New York City" loading="lazy">
      </div>
      <div class="about-text reveal">
        <p class="section-kicker">About Marina</p>
        <h2>The Creator Behind <em>@marina.newyorkcity</em></h2>
        <p>Marina Kapler is the creator behind <a href="https://www.instagram.com/marina.newyorkcity/" target="_blank" rel="noopener">@marina.newyorkcity</a>.</p>
        <p>A NYC-based content creator, marketing professional, and visual storyteller with a background in media, psychology, and design.</p>
        <p>Specializing in cinematic iPhone videography, I consistently produce short-form content that goes viral, with individual Reels reaching over 30M monthly views across my platforms.</p>
        <p><a class="text-link" href="about.html">More about me</a></p>
      </div>
    </section>

    <section class="services" id="services" aria-label="Services">
      <p class="section-kicker reveal">Cinematic Storytelling</p>
      <h2 class="reveal">What I Do</h2>
      <p class="section-lead reveal">Authentic short-form content that seamlessly integrates brands into compelling NYC stories.</p>
      <div class="service-grid">
        <article class="service-card reveal"><h3>Social Media</h3><p>Thumb-stopping short-form content built for reach, saves, and shares.</p></article>
        <article class="service-card reveal"><h3>Luxury &amp; Lifestyle</h3><p>Elevated visuals for premium products, destinations, and experiences.</p></article>
        <article class="service-card reveal"><h3>Tech &amp; Innovation</h3><p>Technology showcased naturally in aspirational, real-world settings.</p></article>
        <article class="service-card reveal"><h3>New York City</h3><p>Deep local expertise in NYC culture, events, locations, and visual storytelling.</p></article>
        <article class="service-card reveal"><h3>Extended Production</h3><p>For larger campaigns, access to professional photo and video crews, licensed drone operators, and original music and sound design.</p></article>
        <article class="service-card reveal"><h3>Content Licensing</h3><p>Licensing cinematic New York City photo and video content for editorial, commercial, tourism, hospitality, media, and digital campaigns.</p></article>
      </div>
    </section>

    <section class="gallery" id="gallery" aria-label="Photo gallery">
      <p class="section-kicker reveal">Gallery</p>
      <h2 class="reveal">New York, <em>Frame by Frame</em></h2>
      <p class="section-lead reveal">A few frames from the city I never got used to. Tap any photo to view it full screen.</p>
      <div class="gallery-grid reveal" id="gallery-grid"></div>
    </section>

    <section class="clients" id="clients" aria-label="Clients and partners">
      <p class="section-kicker reveal">Our Clients and Partners</p>
      <h2 class="reveal">Brands I've Worked With</h2>
      <div class="marquee reveal" aria-label="Client logos">
        <div class="marquee-track" id="marquee-track"></div>
      </div>
    </section>

    <section class="news" id="news" aria-label="NYC news and events">
      <p class="section-kicker reveal">NYC News &amp; Events</p>
      <h2 class="reveal">What's Happening <em>in New York</em></h2>
      <p class="section-lead reveal">The city's biggest moments, curated by a local. Updated regularly.</p>
      <div class="news-list reveal" id="news-list"></div>
      <p class="center reveal" style="margin-top:2rem"><a class="btn btn-ghost" href="events.html">All NYC Events</a></p>
    </section>

    <section class="planner" id="planner" aria-label="Trip planner">
      <p class="section-kicker reveal">Plan Your Trip</p>
      <h2 class="reveal">Visiting <em>New York?</em></h2>
      <p class="section-lead reveal">Enter your travel dates and I'll show you what's happening in the city while you're here.</p>
      <form class="planner-form reveal" id="planner-form">
        <div class="planner-field">
          <label for="arrival">Arrival</label>
          <input type="date" id="arrival" name="arrival" required>
        </div>
        <div class="planner-field">
          <label for="departure">Departure</label>
          <input type="date" id="departure" name="departure" required>
        </div>
        <button type="submit" class="btn btn-gold">Show Me What's On</button>
      </form>
      <p class="planner-error" id="planner-error" hidden>Please pick an arrival date and a departure date on or after it.</p>
      <div class="planner-results" id="planner-results" aria-live="polite"></div>
    </section>

    <section class="contact" id="contact" aria-label="Contact">
      <p class="section-kicker reveal">Contact Me</p>
      <h2 class="reveal">Let's Create <em>Together</em></h2>
      <p class="section-lead reveal">For brand collaborations, reach out below. For footage licensing inquiries, use the licensing email.</p>
      <div class="contact-buttons reveal">
        <a class="btn btn-gold" href="mailto:info@marinanewyorkcity.com?subject=Brand%20Collaboration%20Inquiry">info@marinanewyorkcity.com</a>
        <a class="btn btn-ghost" href="mailto:pr@marinanewyorkcity.com?subject=Footage%20Licensing%20Inquiry">Footage Licensing: pr@marinanewyorkcity.com</a>
      </div>
    </section>
"""

# ------------------------------------------------------------ events hub ---
def events_hub_content():
    return """
    <section class="page-hero" aria-label="NYC Events">
      <p class="section-kicker reveal">NYC Events</p>
      <h1 class="reveal">What's On <em>in New York</em></h1>
      <p class="section-lead reveal">My top picks this week, plus full month-by-month guides. Updated regularly.</p>
    </section>

    <section class="picks" aria-label="Top picks">
      <h2 class="reveal">Top Picks</h2>
      <div class="event-grid reveal" id="picks-grid"></div>
    </section>

    <section class="months" aria-label="Events by month">
      <h2 class="reveal">Browse by Month</h2>
      <div class="month-grid">
        <a class="month-card reveal" href="events-september.html"><span class="month-name">September</span><span class="month-cta">View events</span></a>
        <a class="month-card reveal" href="events-october.html"><span class="month-name">October</span><span class="month-cta">View events</span></a>
        <a class="month-card reveal" href="events-november.html"><span class="month-name">November</span><span class="month-cta">View events</span></a>
        <a class="month-card reveal" href="events-december.html"><span class="month-name">December</span><span class="month-cta">View events</span></a>
      </div>
    </section>

    <section class="planner" id="planner" aria-label="Trip planner">
      <p class="section-kicker reveal">Plan Your Trip</p>
      <h2 class="reveal">Visiting <em>New York?</em></h2>
      <p class="section-lead reveal">Enter your travel dates and I'll show you what's happening in the city while you're here.</p>
      <form class="planner-form reveal" id="planner-form">
        <div class="planner-field">
          <label for="arrival">Arrival</label>
          <input type="date" id="arrival" name="arrival" required>
        </div>
        <div class="planner-field">
          <label for="departure">Departure</label>
          <input type="date" id="departure" name="departure" required>
        </div>
        <button type="submit" class="btn btn-gold">Show Me What's On</button>
      </form>
      <p class="planner-error" id="planner-error" hidden>Please pick an arrival date and a departure date on or after it.</p>
      <div class="planner-results" id="planner-results" aria-live="polite"></div>
    </section>
"""

# ---------------------------------------------------------- monthly page ---
MONTH_TITLES = {
    "2026-09": ("September", "events-september.html"),
    "2026-10": ("October", "events-october.html"),
    "2026-11": ("November", "events-november.html"),
    "2026-12": ("December", "events-december.html"),
}

def month_content(month):
    name, _ = MONTH_TITLES[month]
    others = "\n".join(
        f'        <a class="month-card small reveal" href="{href}"><span class="month-name">{n}</span></a>'
        for m, (n, href) in MONTH_TITLES.items() if m != month
    )
    if month == "2026-09":
        note = """<p class="section-lead reveal">September has passed. Here are the months still ahead:</p>
      <div class="month-grid">
        <a class="month-card reveal" href="events-october.html"><span class="month-name">October</span><span class="month-cta">View events</span></a>
        <a class="month-card reveal" href="events-november.html"><span class="month-name">November</span><span class="month-cta">View events</span></a>
        <a class="month-card reveal" href="events-december.html"><span class="month-name">December</span><span class="month-cta">View events</span></a>
      </div>"""
        grid = ""
    else:
        note = f'<p class="section-lead reveal">Every event worth your time in New York this {name}.</p>'
        grid = f'      <div class="event-grid reveal" id="month-grid" data-month="{month}"></div>'
    return f"""
    <section class="page-hero" aria-label="{name} events">
      <p class="section-kicker reveal"><a class="text-link" href="events.html">NYC Events</a></p>
      <h1 class="reveal">{name} <em>Events</em></h1>
      {note}
    </section>

    <section class="month-events" aria-label="{name} event list">
{grid}
    </section>

    <section class="months" aria-label="Other months">
      <h2 class="reveal">Other Months</h2>
      <div class="month-grid">
{others}
      </div>
    </section>
"""

# ------------------------------------------------------------------ shop ---
def shop_img(local, remote, alt):
    return f'<img src="{local}" onerror="this.onerror=null;this.src=\'{remote}\'" alt="{alt}" loading="lazy">'

def shop_content():
    base = "https://marinanewyorkcity.com/_assets/media/"
    return """
    <section class="page-hero" aria-label="Shop">
      <p class="section-kicker reveal">Shop</p>
      <h1 class="reveal">The <em>Shop</em></h1>
      <p class="section-lead reveal">My presets, merch, and prints. Everything I sell lives in my store.</p>
    </section>

    <section class="products" aria-label="Products">
      <div class="product-grid">
        <article class="product-card reveal">
          """ + shop_img("shop_9fe2629bd34048f71182689d85ac3101.png", base + "9fe2629bd34048f71182689d85ac3101.png", "Marina New York City Lightroom presets") + """
          <div class="product-body">
            <h2>Presets</h2>
            <p>My signature photo presets for Lightroom CC, Lightroom Classic, and Lightroom Mobile. The exact looks I use on my New York photos.</p>
            <a class="btn btn-gold" href="https://links.marinanewyorkcity.com/digitalproducts" target="_blank" rel="noopener">Shop Presets</a>
          </div>
        </article>
        <article class="product-card reveal">
          """ + shop_img("shop_1245552432c51e4794ac1de673313fca.png", base + "1245552432c51e4794ac1de673313fca.png", "Marina New York City merch") + """
          <div class="product-body">
            <h2>Merch</h2>
            <p>Hoodies, ornaments, candles, and more with my New York City designs.</p>
            <a class="btn btn-gold" href="https://links.marinanewyorkcity.com/mymerch" target="_blank" rel="noopener">Shop Merch</a>
          </div>
        </article>
        <article class="product-card reveal">
          """ + shop_img("shop_0ed1f8bfca8363b555fb7ab90963650b.png", base + "0ed1f8bfca8363b555fb7ab90963650b.png", "Marina New York City photo prints") + """
          <div class="product-body">
            <h2>Prints</h2>
            <p>Museum-quality prints of my New York City photography for your walls.</p>
            <a class="btn btn-gold" href="https://links.marinanewyorkcity.com/prints" target="_blank" rel="noopener">Shop Prints</a>
          </div>
        </article>
      </div>
    </section>
"""

# ----------------------------------------------------------------- about ---
def about_content():
    return """
    <section class="page-hero" aria-label="About Marina">
      <p class="section-kicker reveal">About Me</p>
      <h1 class="reveal">Hi, I'm <em>Marina</em></h1>
    </section>

    <section class="about-page" aria-label="Marina's story">
      <div class="about-photos reveal">
        <img src="about-marina.jpg" alt="Marina Kapler, NYC content creator and iPhone videographer" loading="lazy">
        <img src="empire.jpg" alt="Empire State Building at sunrise, New York City" loading="lazy">
      </div>
      <div class="about-text reveal">
        <p>I hold a Bachelor of Arts in Mass Media and Communication, with an additional focus in Psychology, which gives me a unique perspective on my work. My understanding of psychological principles enhances my ability to craft compelling narratives that resonate deeply with diverse audiences. This expertise has been instrumental in my years of experience in top marketing positions, including my role as a Marketing Events Director across different industries.</p>
        <p>In addition to my work as a content creator, I am an accomplished graphic designer and social media marketing expert. My background in psychology informs my approach to audience engagement, allowing me to create content that truly connects with people on an emotional level.</p>
        <p>I film New York like I never got used to it. Every Reel is shot on iPhone, edited with intention, and built to make people feel something about this city.</p>
        <p class="brand-line">"I film New York like I never got used to it."</p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- guides ---
def guides_content():
    return """
    <section class="page-hero" aria-label="Guides">
      <p class="section-kicker reveal">Guides</p>
      <h1 class="reveal">NYC <em>Guides</em></h1>
      <p class="section-lead reveal">My in-depth New York City guides are coming soon. The Christmas guide is first.</p>
    </section>

    <section class="guides-soon" aria-label="Coming soon">
      <article class="guide-teaser reveal">
        <h2>Christmas in New York</h2>
        <p>The complete interactive guide: tree lightings, markets, shows, photo spots, day-by-day itineraries, and a tappable map. Coming soon.</p>
        <a class="btn btn-gold" href="contact.html">Get Notified</a>
      </article>
    </section>
"""

# --------------------------------------------------------------- contact ---
def contact_content():
    return """
    <section class="page-hero" aria-label="Contact">
      <p class="section-kicker reveal">Contact Me</p>
      <h1 class="reveal">Let's Create <em>Together</em></h1>
      <p class="section-lead reveal">For brand collaborations, reach out below. For footage licensing inquiries, use the licensing email.</p>
    </section>

    <section class="contact-page" aria-label="Contact details">
      <div class="contact-buttons reveal">
        <a class="btn btn-gold" href="mailto:info@marinanewyorkcity.com?subject=Brand%20Collaboration%20Inquiry">info@marinanewyorkcity.com</a>
        <a class="btn btn-ghost" href="mailto:pr@marinanewyorkcity.com?subject=Footage%20Licensing%20Inquiry">Footage Licensing: pr@marinanewyorkcity.com</a>
      </div>
      <div class="social-grid reveal">
""" + "\n".join(
        f'        <a class="social-card" href="{url}" target="_blank" rel="noopener"><span>{name}</span></a>'
        for name, url in SOCIALS
    ) + """
      </div>
    </section>
"""

# ------------------------------------------------------------------ main ---
EVENTS_SCRIPT = '  <script src="events.js"></script>'

def main():
    page("index.html", "Marina New York City | Cinematic iPhone Videography",
         "Marina Kapler (@marina.newyorkcity) films New York City like she never got used to it. Cinematic iPhone videography, NYC events, presets, and brand collaborations.",
         "Home", home_content(), EVENTS_SCRIPT)
    page("events.html", "NYC Events | Marina New York City",
         "What's happening in New York City: curated top picks and month-by-month event guides by @marina.newyorkcity.",
         "NYC Events", events_hub_content(), EVENTS_SCRIPT)
    for month, (name, fname) in MONTH_TITLES.items():
        page(fname, f"{name} Events in NYC | Marina New York City",
             f"Every event worth your time in New York City this {name}, curated by @marina.newyorkcity.",
             "NYC Events", month_content(month), EVENTS_SCRIPT)
    page("shop.html", "Shop Presets, Merch & Prints | Marina New York City",
         "Shop Marina New York City: signature Lightroom presets, merch, and photo prints.",
         "Shop", shop_content())
    page("about.html", "About Marina | Marina New York City",
         "About Marina Kapler, the creator behind @marina.newyorkcity: NYC content creator, iPhone videographer, and visual storyteller.",
         "About", about_content())
    page("guides.html", "NYC Guides | Marina New York City",
         "In-depth New York City guides by @marina.newyorkcity. Coming soon.",
         "Guides", guides_content())
    page("contact.html", "Contact | Marina New York City",
         "Contact Marina New York City for brand collaborations and footage licensing.",
         "Contact", contact_content())

if __name__ == "__main__":
    main()
