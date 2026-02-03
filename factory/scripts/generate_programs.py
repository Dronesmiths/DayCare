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
PRIMARY_COLOR = brand.get("primary_color", "#FCD85D")
SECONDARY_COLOR = brand.get("secondary_color", "#F28FB5")
ACCENT_BLUE = brand.get("accent_color", "#91D8E4")

service_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {business_name}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://{domain}/services/{slug}/" />
    
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
            --l: #FFFDF7;
            --s: 'Quicksand', sans-serif;
            --f-h: 'Bubblegum Sans', cursive;
        }}
        body {{ font-family: var(--s); color: var(--t); background: var(--l); }}
        .service-content h2 {{ font-family: var(--f-h); color: var(--d); margin: 30px 0 15px; font-size: 2.2rem; }}
        .service-content p {{ margin-bottom: 20px; line-height: 1.8; font-size: 1.15rem; }}
        .service-content ul {{ margin-bottom: 30px; padding-left: 20px; }}
        .service-content li {{ margin-bottom: 12px; font-size: 1.1rem; list-style: none; }}
        .service-content li::before {{ content: '⭐'; margin-right: 10px; }}
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
                    <li><a href="/blog/" style="text-decoration:none; color:var(--t); font-weight:600;">Blog</a></li>
                    <li><a href="/contact/" style="text-decoration:none; color:var(--t); font-weight:600;">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Page Hero -->
    <section style="background: linear-gradient({secondary_color}, {primary_color}); padding: 100px 0; text-align: center; color: white;">
        <div class="c">
            <h1 style="font-family: var(--f-h); font-size: clamp(2.5rem, 6vw, 4rem); text-shadow: 0 2px 10px rgba(0,0,0,0.1);">{title}</h1>
            <p style="font-size: 1.25rem; margin-top: 15px; opacity: 0.9;">Professional & Nurturing Care in Palmdale</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 80px 0;">
        <div class="c" style="max-width: 900px; margin: 0 auto; padding: 0 20px;">
            <div class="service-content">
                {content_body}

                <div style="background: white; padding: 50px; border-radius: 40px; border: 4px dashed {accent_blue}; margin-top: 60px; text-align: center;">
                    <h3 style="font-family: var(--f-h); color: var(--d); font-size: 2.2rem; margin-bottom: 20px;">Interested in our {title}?</h3>
                    <p style="margin-bottom: 30px;">We'd love to discuss your family's needs and show you how our fairy-tale environment can benefit your child.</p>
                    <div style="display:flex; gap:20px; justify-content:center; flex-wrap:wrap;">
                        <a href="tel:{phone}" class="btn" style="background:var(--d); color:white; padding: 15px 40px; border-radius: 50px; text-decoration:none; font-weight:700;">Call Us Now</a>
                        <a href="/contact/" class="btn" style="background:{secondary_color}; color:white; padding: 15px 40px; border-radius: 50px; text-decoration:none; font-weight:700;">Schedule a Tour</a>
                    </div>
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

programs = [
    {
        "slug": "infant-care",
        "title": "Infant Care Program",
        "description": "Nurturing and safe infant care for babies 0-18 months. Small ratios and personalized attention in a warm residential setting.",
        "content_body": """
            <h2>A Soft Place to Land</h2>
            <p>Our infant program is designed to provide a secure and loving foundation for your baby's first discoveries. We prioritize individual schedules, ensuring your infant eats, sleeps, and plays according to their natural rhythm.</p>
            <h2>What We Focus On:</h2>
            <ul>
                <li>Sensory exploration with safe, age-appropriate toys.</li>
                <li>Tummy time and muscle development.</li>
                <li>Language development through singing, reading, and talking.</li>
                <li>Daily updates for parents on feedings and naps.</li>
            </ul>
        """
    },
    {
        "slug": "toddler-care",
        "title": "Toddler Care Program",
        "description": "Active and engaging toddler care for children 18 months to 3 years. Focused on social skills, discovery, and physical play.",
        "content_body": """
            <h2>Growing & Discovering</h2>
            <p>Toddlers are natural explorers! Our program encourages their curiosity while providing the structure they need to feel safe and confident.</p>
            <h2>Toddler Highlights:</h2>
            <ul>
                <li>Socialization and learning to share in small groups.</li>
                <li>Potty training support and encouragement.</li>
                <li>Daily outdoor play on our premium backyard playground.</li>
                <li>Creative arts, music, and movement.</li>
            </ul>
        """
    },
    {
        "slug": "preschool",
        "title": "Preschool / Pre-K Program",
        "description": "Spark imagination and prepare for kindergarten with our storybook-themed preschool curriculum for ages 3-5.",
        "content_body": """
            <h2>Where Imagination Meets Learning</h2>
            <p>Our Pre-K program combines academic readiness with creative play. We use a storybook-themed curriculum that makes learning to read and count feel like a magical adventure.</p>
            <h2>Curriculum Focus:</h2>
            <ul>
                <li>Early literacy and phonics.</li>
                <li>Mathematical concepts and problem-solving.</li>
                <li>Character development and kindness.</li>
                <li>Preparation for a smooth transition to Kindergarten.</li>
            </ul>
        """
    },
    {
        "slug": "after-school",
        "title": "After-School Program",
        "description": "Safe and fun after-school care with homework help, healthy snacks, and plenty of outdoor playground time.",
        "content_body": """
            <h2>The Perfect End to the School Day</h2>
            <p>Our after-school program provides a comfortable space for school-aged children to unwind, get their homework done, and let off some steam on the playground.</p>
            <h2>Program Benefits:</h2>
            <ul>
                <li>Dedicated quiet time for homework with teacher assistance.</li>
                <li>Nutritious afternoon snacks prepared fresh.</li>
                <li>Structured physical activity and group games.</li>
                <li>A safe, supervised environment until pickup.</li>
            </ul>
        """
    }
]

def generate_programs():
    base_dir = "services"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for program in programs:
        p_dir = os.path.join(base_dir, program['slug'])
        if not os.path.exists(p_dir):
            os.makedirs(p_dir)
            
        html_content = service_template.format(
            title=program['title'],
            description=program['description'],
            slug=program['slug'],
            content_body=program['content_body'],
            business_name=BUSINESS_NAME,
            domain=DOMAIN,
            phone=PHONE,
            primary_color=PRIMARY_COLOR,
            secondary_color=SECONDARY_COLOR,
            accent_blue=ACCENT_BLUE
        )
        
        file_path = os.path.join(p_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_programs()
