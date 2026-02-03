import os

pages = [
    {
        "path": "services/refrigerator-repair/index.html",
        "title": "Refrigerator Repair Service | Palmdale, Lancaster, Antelope Valley",
        "h1": "Refrigerator Repair",
        "desc": "Expert refrigerator repair specialists. We fix cooling issues, ice makers, and leaks for all major brands in the Antelope Valley. Call 661-498-4444.",
        "content": "A malfunctioning refrigerator is more than an inconvenience; it can lead to hundreds of dollars in spoiled food. Our expert technicians specialized in diagnosing and fixing cooling failures, noisy motors, leaky water dispensers, and broken ice makers. We carry common parts for Samsung, LG, Whirlpool, and GE to ensure we can often provide same-day fixes."
    },
    {
        "path": "services/washer-repair/index.html",
        "title": "Washer Repair Service | Local Expertise in Antelope Valley",
        "h1": "Washer Repair",
        "desc": "Fast washing machine repair in Palmdale and Lancaster. We fix drain issues, spinning problems, and leaks. Same-day service. Call 661-498-4444.",
        "content": "Whether your washer is leaking, not draining, or refusing to spin, we can help. Our technicians are experienced with both top-load and high-efficiency front-load washing machines. From pump replacements to control board repairs, we provide comprehensive service to get your laundry routine back on track."
    },
    {
        "path": "services/dryer-repair/index.html",
        "title": "Dryer Repair Service | Antelope Valley's Best Appliance Pros",
        "h1": "Dryer Repair",
        "desc": "Expert gas and electric dryer repair. No heat? Noisy? We fix it fast in Palmdale and Lancaster. Call 661-498-4444.",
        "content": "A dryer that won't heat up or won't tumble can slow down your entire household. We specialize in gas and electric dryer repairs, including heating element replacement, thermal fuse fixes, and belt replacements. We also check for dangerous lint buildup to ensure your appliance is safe to operate."
    },
    {
        "path": "services/oven-stove-repair/index.html",
        "title": "Oven & Stove Repair | Certified Cooking Appliance Pros",
        "h1": "Oven & Stove Repair",
        "desc": "Professional oven and stove repair in the Antelope Valley. Igniters, thermostats, and heating elements. Call 661-498-4444.",
        "content": "Don't let a broken oven stop you from cooking for your family. We provide precision repair for gas and electric ranges, ovens, and cooktops. Whether it's a broken igniter, an uneven heating element, or a faulty control panel, our techs will have you cooking again in no time."
    },
    {
        "path": "services/dishwasher-repair/index.html",
        "title": "Dishwasher Repair | Fast Fixing for Local Homes",
        "h1": "Dishwasher Repair",
        "desc": "Expert dishwasher repair in Palmdale and Lancaster. We fix leaks, drainage issues, and cleaning problems. Call 661-498-4444.",
        "content": "Is your dishwasher leaving spots or not draining at all? We fix all major dishwasher brands and models. From pump repairs to float switch replacements, we ensure your appliance runs efficiently and quietly. We service all major neighborhoods in the Antelope Valley."
    },
    {
        "path": "services/microwave-repair/index.html",
        "title": "Microwave Repair | Quick Reliable Service",
        "h1": "Microwave Repair",
        "desc": "Professional microwave repair in the Antelope Valley. Over-the-range and built-in specialists. Call 661-498-4444.",
        "content": "We handle all types of microwave repairs, from turntable malfunctions to complex magnetron issues. Our technicians are trained to safely service over-the-range and built-in units, ensuring your kitchen remains fully functional."
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://d3jg5wepg4zxcs.cloudfront.net/{path}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://d3jg5wepg4zxcs.cloudfront.net/{path}">
    <meta property="og:title" content="{h1} | Mobile Appliance Repair">
    <meta property="og:description" content="{desc}">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <style>
        :root {{ --p: #1F6AE1; --d: #004488; --t: #1a1a1a; --l: #f9fbfc; --w: #ffffff; --s: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:var(--s); color:var(--t); line-height:1.6; background:var(--w); -webkit-font-smoothing:antialiased; }}
        .c {{ max-width:1200px; margin:0 auto; padding:0 20px; }}
        header {{ background:var(--w); box-shadow:0 2px 10px rgba(0,0,0,0.05); position:sticky; top:0; z-index:1000; padding:15px 0; }}
        header .c {{ display:flex; justify-content:space-between; align-items:center; }}
        .logo {{ font-size:24px; font-weight:900; color:var(--d); text-decoration:none; }}
        .logo span {{ color:var(--p); }}
        nav ul {{ display:flex; list-style:none; gap:25px; }}
        nav a {{ font-weight:600; color:var(--t); text-decoration:none; font-size:15px; }}
        .hero-s {{ background:var(--d); color:var(--w); padding:100px 0; text-align:center; }}
        .hero-s h1 {{ font-size:3.5rem; font-weight:900; }}
        .main-c {{ padding:80px 0; max-width:800px; margin:0 auto; font-size:1.15rem; }}
        .main-c h2 {{ color:var(--d); margin:40px 0 20px; font-size:2rem; }}
        .main-c p {{ margin-bottom:25px; color:#444; }}
        .cta {{ background:var(--l); padding:60px 0; text-align:center; }}
        .b-p {{ display:inline-block; padding:15px 40px; border-radius:50px; background:var(--p); color:#fff; font-weight:700; text-decoration:none; transition:0.3s; }}
        .footer {{ background:#0a0a0a; color:var(--w); padding:60px 0 30px; text-align:center; }}
        .menu-t {{ display:none; background:none; border:none; cursor:pointer; }}
        @media (max-width:768px) {{ .hero-s h1 {{ font-size:2.5rem; }} nav {{ display:none; }} .menu-t {{ display:block; }} }}
    </style>
</head>
<body>
<header>
    <div class="c">
        <a href="/" class="logo">Mobile <span>Appliance Repair</span></a>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/services/">Services</a></li>
                <li><a href="/about/">About</a></li>
                <li><a href="/contact/">Contact</a></li>
            </ul>
        </nav>
        <button class="menu-t" aria-label="Toggle Menu">
            <svg viewBox="0 0 448 512" width="24" height="24" fill="#004488"><path d="M0 96c0-17.7 14.3-32 32-32h384c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zm0 160c0-17.7 14.3-32 32-32h384c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zm448 160c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h384c17.7 0 32 14.3 32 32z"/></svg>
        </button>
    </div>
</header>
<main>
    <section class="hero-s">
        <div class="c">
            <h1>{h1}</h1>
        </div>
    </section>
    <section class="c main-c">
        <h2>Professional Service</h2>
        <p>{content}</p>
        <p>Our technicians are background-checked and insured, giving you peace of mind while we work in your home. We use only OEM-equivalent parts to ensure long-lasting results and appliance reliability.</p>
    </section>
    <section class="cta">
        <div class="c">
            <h2>Ready to schedule your repair?</h2>
            <p style="margin:20px 0 30px;">Call us today for a same-day appointment in the Antelope Valley.</p>
            <a href="tel:6614984444" class="b-p">Call 661-498-4444</a>
        </div>
    </section>
</main>
<footer class="footer">
    <div class="c">
        <p>&copy; 2026 Mobile Appliance Repair Service. All rights reserved.</p>
    </div>
</footer>
<script>
    document.addEventListener('DOMContentLoaded', () => {{
        const t = document.querySelector('.menu-t');
        const n = document.querySelector('nav');
        if(t && n) {{
            t.addEventListener('click', () => {{
                const isV = n.style.display === 'block';
                n.style.display = isV ? 'none' : 'block';
                n.style.position = 'absolute'; n.style.top = '100%'; n.style.left = '0'; n.style.width = '100%'; n.style.background = '#fff'; n.style.padding = '20px'; n.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
            }});
        }}
    }});
</script>
</body>
</html>"""

project_root = "/Users/mediusa/NOVA/Repos/Appliance Repair Service"

for page in pages:
    file_path = os.path.join(project_root, page["path"])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(template.format(**page))
    print(f"Optimized: {page['path']}")
