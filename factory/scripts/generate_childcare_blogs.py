import os
import json
import sys

def load_config():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "factory_config.json"))
    if not os.path.exists(config_path):
        print(f"ERROR: Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        return json.load(f)

config = load_config()
client = config.get("client", {})
brand = config.get("brand", {})

BUSINESS_NAME = client.get("name", "Fairy Tale Child Care")
DOMAIN = client.get("domain", "fairytalechildcare.com")
PHONE = client.get("phone", "661-XXX-XXXX")
CLEAN_PHONE = "".join(filter(str.isdigit, PHONE))
PRIMARY_COLOR = brand.get("primary_color", "#FCD85D")
SECONDARY_COLOR = brand.get("secondary_color", "#F28FB5")
ACCENT_BLUE = brand.get("accent_color", "#91D8E4")

# Using a raw string for the template and avoiding f-string to manage braces more easily
blog_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {business_name}</title>
    <meta name="description" content="{description}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://{domain}/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="/images/hero-home.webp">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bubblegum+Sans&family=Quicksand:wght@300..700&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="/css/styles.css?v=1.0">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <style>
        :root {{
            --p: {primary_color};
            --p-pink: {secondary_color};
            --p-blue: {accent_blue};
            --d: #00457C;
            --t: #2D3436;
            --s: 'Quicksand', sans-serif;
            --f-h: 'Bubblegum Sans', cursive;
        }}
        .blog-body h2 {{ font-family: var(--f-h); color: var(--d); margin: 30px 0 15px; font-size: 2rem; }}
        .blog-body p {{ margin-bottom: 20px; line-height: 1.8; }}
        .blog-body ul {{ margin-bottom: 25px; padding-left: 20px; }}
        .blog-body li {{ margin-bottom: 10px; }}
    </style>
</head>

<body>

    <!-- Header -->
    <header style="padding: 20px 0; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <div class="c" style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display:flex; justify-content:space-between; align-items:center;">
            <a href="/" class="logo" style="font-family: var(--f-h); font-size: 24px; text-decoration:none; color:var(--d);">Fairy Tale <span style="color:var(--p-pink);">Child Care</span></a>
            <nav>
                <ul style="display:flex; list-style:none; gap:25px;">
                    <li><a href="/" style="text-decoration:none; color:var(--t); font-weight:600;">Home</a></li>
                    <li><a href="/about/" style="text-decoration:none; color:var(--t); font-weight:600;">About</a></li>
                    <li><a href="/contact/" style="text-decoration:none; color:var(--t); font-weight:600;">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background: linear-gradient({secondary_color}, {primary_color}); padding: 80px 0; text-align: center; color: white;">
        <div class="c">
            <span style="font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{category}</span>
            <h1 style="font-family: var(--f-h); font-size: clamp(2rem, 5vw, 3.5rem); margin-top: 10px; text-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 0 20px;">{title}</h1>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #FFFDF7;">
        <div class="c" style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
            <div class="blog-body">
                <p class="lead" style="font-size: 1.3rem; color: var(--d); font-weight: 600; margin-bottom: 30px;">
                    {lead_text}
                </p>
                
                {content_body}

                <div style="background: white; padding: 40px; border: 3px solid {secondary_color}; margin: 50px 0; border-radius: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <h3 style="font-family: var(--f-h); color: var(--d); font-size: 2rem; margin-bottom:15px;">Come Join the Magic!</h3>
                    <p style="margin-bottom: 25px;">Schedule a tour of our Palmdale facility and see our beautiful playground in person.</p>
                    <a href="/contact/" class="btn" style="background:{secondary_color}; color:white; padding: 15px 40px; border-radius: 50px; text-decoration:none; font-weight:700; display:inline-block;">Book a Tour</a>
                </div>

                <div style="font-size: 0.9rem; color: #666; margin-top: 50px;">
                    <p><a href="/" style="color: var(--d); font-weight: 600; text-decoration: none;">&larr; Back to Home</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer style="background: #2D3436; color: white; padding: 60px 0; text-align: center;">
        <div class="c">
            <h4 style="font-family: var(--f-h); font-size: 1.5rem; margin-bottom: 10px;">{business_name}</h4>
            <p>© 2026 {business_name}. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

articles = [
    {
        "slug": "choosing-right-childcare-palmdale",
        "title": "Choosing the Right Child Care in Palmdale: A Parent's Guide",
        "category": "Parent Guides",
        "description": "Finding the perfect daycare in Palmdale can be overwhelming. Learn what to look for in a residential childcare setting for your family's peace of mind.",
        "lead_text": "Your child's first years are their most important. Choosing a childcare provider is one of the biggest decisions you'll make as a parent in the Antelope Valley.",
        "tags": "Palmdale, Daycare, Parent Tips",
        "content_body": '''
            <h2>What Makes Residential Childcare Special?</h2>
            <p>Unlike large commercial centers, residential childcare offers a warm, home-like environment that helps children transition from their own home more smoothly. At Fairy Tale Child Care, we provide that intimate setting combined with a professional curriculum.</p>
            <h2>Top 3 Things to Look For</h2>
            <ul>
                <li><strong>Safety first:</strong> Ensure the facility is licensed and has secure, monitored play areas.</li>
                <li><strong>Nurturing Atmosphere:</strong> Look for a provider who genuinely loves working with children and focuses on their individual needs.</li>
                <li><strong>Outdoor Space:</strong> A large, safe backyard for physical activity is crucial for a child's health and development.</li>
            </ul>
        '''
    },
    {
        "slug": "benefits-of-residential-daycare",
        "title": "The Magic of Small Groups: Benefits of Residential Daycare",
        "category": "Education",
        "description": "Why small ratios matter. Discover why residential daycare settings provide superior social and emotional growth for toddlers.",
        "lead_text": "In a smaller group, your child isn't just a number. They are part of a little family where their unique personality can shine.",
        "tags": "Toddler Care, Child Development, Education",
        "content_body": '''
            <h2>Personalized Attention</h2>
            <p>With a smaller child-to-teacher ratio, we can tailor activities to each child's interest and stage of development. Whether they are exploring sensory play or learning their first words, we are right there with them.</p>
            <h2>Stronger Social Bonds</h2>
            <p>Children in residential settings often form deeper friendships and learn social skills in a more natural, comfortable environment that mimics a sibling-like dynamic.</p>
            <h2>A Healthier Environment</h2>
            <p>Fewer children often means less exposure to common seasonal illnesses, helping keep your little one (and your whole family) healthier throughout the year.</p>
        '''
    },
    {
        "slug": "our-new-backyard-playground",
        "title": "Step Into the Magic: Our New Backyard Playground",
        "category": "Facility News",
        "description": "We've upgraded! Take a look at our new professional-grade backyard playground designed for safe, magical fun in Palmdale.",
        "lead_text": "We believe that outdoor play is where the real magic happens. That's why we've invested in a premium playground for our little adventurers.",
        "tags": "Playground, Outdoor Play, Palmdale",
        "content_body": '''
            <h2>Safe, High-Quality Fun</h2>
            <p>Our new setup features professional-grade swings, dual slides, and a magical castle theme that inspires hours of imaginative play. We've also installed safety-first surfacing to ensure soft landings.</p>
            <h2>The Importance of Active Play</h2>
            <p>Running, climbing, and swinging help children build motor skills, coordination, and confidence. Our backyard provides the perfect controlled environment for these essential childhood experiences.</p>
            <p>Come see the new playground during our next open house!</p>
        '''
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags'],
            business_name=BUSINESS_NAME,
            domain=DOMAIN,
            primary_color=PRIMARY_COLOR,
            secondary_color=SECONDARY_COLOR,
            accent_blue=ACCENT_BLUE
        )
        
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
