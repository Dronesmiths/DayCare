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
    
    <link rel="stylesheet" href="/css/styles.css?v=2.1">
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
        .c {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    </style>
</head>

<body>

    <!-- Header -->
    <header style="padding: 20px 0; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <div class="c" style="display:flex; justify-content:space-between; align-items:center;">
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
                    <p><a href="/blog/" style="color: var(--d); font-weight: 600; text-decoration: none;">&larr; Back to Blog Index</a></p>
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
        "content_body": '''
            <h2>Safe, High-Quality Fun</h2>
            <p>Our new setup features professional-grade swings, dual slides, and a magical castle theme that inspires hours of imaginative play. We've also installed safety-first surfacing to ensure soft landings.</p>
            <h2>The Importance of Active Play</h2>
            <p>Running, climbing, and swinging help children build motor skills, coordination, and confidence. Our backyard provides the perfect controlled environment for these essential childhood experiences.</p>
            <p>Come see the new playground during our next open house!</p>
        '''
    },
    {
        "slug": "when-is-child-ready-for-preschool",
        "title": "Is Your Child Ready for Preschool? 5 Signs to Watch For",
        "category": "Parent Guides",
        "description": "How do you know when it's time for Pre-K? Discover 5 indicators that your child is ready for the exciting world of preschool.",
        "lead_text": "The transition from toddlerhood to preschool is a major milestone. While every child is different, these five signs suggest they might be ready for the next chapter.",
        "content_body": '''
            <h2>1. Growing Curiosity</h2>
            <p>If your child is constantly asking "why" and showing a keen interest in learning new things, they are likely ready for a more structured educational environment.</p>
            <h2>2. Basic Independence</h2>
            <p>Can they handle small tasks alone? Preschool requires a certain level of independence, from putting on shoes to using the restroom with minimal help.</p>
            <h2>3. Interest in Peers</h2>
            <p>Does your child actively seek out other children to play with? This social drive is a key component of the preschool experience.</p>
            <h2>4. Ability to Follow Simple Directions</h2>
            <p>Preschool involves following a routine and listening to instructions. If they can complete two-step directions at home, they are on the right track.</p>
            <h2>5. Stamina for a Full Day</h2>
            <p>Preschool can be tiring! Ensure your child has the energy and emotional resilience to handle a day filled with learning and play.</p>
        '''
    },
    {
        "slug": "transitioning-to-after-school-care",
        "title": "Smooth Sailing: Transitioning to After-School Care",
        "category": "Education",
        "description": "Make the move to after-school care easy for your child. Tips for Palmdale parents on choosing and starting an after-school program.",
        "lead_text": "The end of the school day doesn't have to be stressful. After-school care provides a safe, productive space for children while parents are at work.",
        "content_body": '''
            <h2>Creating a Consistent Routine</h2>
            <p>Children thrive on predictability. Ensure the after-school program has a clear schedule that allows for homework time, active play, and relaxation.</p>
            <h2>Communication is Key</h2>
            <p>Stay in close contact with the providers. Share updates about your child's day at school and any specific needs they might have in the afternoon.</p>
            <h2>A Safe Space to Unwind</h2>
            <p>After a full day of academics, children need a place to let off steam. Our Palmdale facility offers the perfect mix of homework support and outdoor playground fun.</p>
        '''
    },
    {
        "slug": "consistent-routine-for-toddlers",
        "title": "The Power of Patterns: Creating a Routine for Toddlers",
        "category": "Parent Guides",
        "description": "Why toddlers need routine and how to build one that works for your family. Practical tips for Palmdale parents.",
        "lead_text": "For a toddler, the world is a big, unpredictable place. A consistent routine provides the safety and structure they need to flourish.",
        "content_body": '''
            <h2>Why Routines Matter</h2>
            <p>Routines help toddlers understand what to expect next, reducing anxiety and power struggles. It also fosters a sense of security and belonging.</p>
            <h2>Building Your Daily Rhythm</h2>
            <ul>
                <li><strong>Morning Magic:</strong> Start the day with a predictable sequence of rituals.</li>
                <li><strong>Consistent Mealtimes:</strong> Eating at the same time helps regulate their energy and mood.</li>
                <li><strong>Naptime Rituals:</strong> A calm transition to rest is essential for growth.</li>
                <li><strong>Evening Wind-down:</strong> Prepare for sleep with quiet activities like reading or gentle play.</li>
            </ul>
        '''
    },
    {
        "slug": "sensory-play-for-infants",
        "title": "Sparking Discovery: Sensory Play Activities for Infants",
        "category": "Education",
        "description": "How to engage your baby's senses through safe, fun play. Discover the benefits of sensory exploration for infant development.",
        "lead_text": "From the moment they are born, infants are learning about the world through their senses. Sensory play is vital for brain development and discovery.",
        "content_body": '''
            <h2>Safe Exploration</h2>
            <p>Using different textures, sounds, and colors helps infants build neural pathways. At Fairy Tale Child Care, we use age-appropriate toys and materials to stimulate their curiosity.</p>
            <h2>Try These at Home:</h2>
            <ul>
                <li><strong>Texture Time:</strong> Let them touch soft fabrics, smooth wood, or safe crinkly paper.</li>
                <li><strong>Nature Sounds:</strong> Take them outside to hear the birds, wind, and rustling leaves.</li>
                <li><strong>High Contrast Visuals:</strong> Infants love bold black and white patterns or bright primary colors.</li>
            </ul>
        '''
    },
    {
        "slug": "daycare-center-vs-residential-care",
        "title": "Small vs. Big: Daycare Centers vs. Residential Care",
        "category": "Parent Guides",
        "description": "Which is right for your child? Comparing the pros and cons of large daycare centers versus residential childcare settings.",
        "lead_text": "Choosing a childcare setting is a personal decision. Understanding the differences can help you find the best fit for your family's needs.",
        "content_body": '''
            <h2>Residential Care: The Home-Like Feel</h2>
            <p>Residential settings offer smaller groups, a consistent caregiver, and a nurturing atmosphere that mimics a family dynamic. This is often ideal for infants and toddlers who need more personalized attention.</p>
            <h2>Daycare Centers: The Group Experience</h2>
            <p>Large centers often have more diverse resources and larger peer groups, which can be beneficial for older children preparing for public school environments.</p>
            <h2>Why We Believe in the Residential Model</h2>
            <p>At Fairy Tale Child Care, we combine the intimacy of a home with a professional curriculum and a world-class playground, giving parents the best of both worlds.</p>
        '''
    },
    {
        "slug": "west-palmdale-childcare-resources",
        "title": "Navigating Palmdale: Local Childcare Resources for Parents",
        "category": "Locality Anchor",
        "description": "A guide to local parenting resources, parks, and childcare support in West Palmdale and the Antelope Valley.",
        "lead_text": "Living in Palmdale means being part of a vibrant, family-oriented community. Here is your guide to local resources for young families.",
        "content_body": '''
            <h2>Parks & Play in Palmdale</h2>
            <p>We are lucky to have beautiful spaces like Marie Kerr Park and Pelona Vista Park nearby. These are great spots for weekend family outings!</p>
            <h2>Community Support</h2>
            <p>The Antelope Valley offers various resources for parents, from local library reading programs to community health clinics and parenting workshops.</p>
            <p><strong>Fairy Tale Child Care</strong> is proud to be a part of the West Palmdale neighborhood, providing a safe haven for our local children.</p>
        '''
    },
    {
        "slug": "why-palmdale-families-trust-us",
        "title": "Trust & Magic: Why Palmdale Families Choose Us",
        "category": "Locality Anchor",
        "description": "Discover why Fairy Tale Child Care is the most trusted residential childcare in Palmdale and the Antelope Valley.",
        "lead_text": "Trust is the foundation of everything we do. Parents in Palmdale choose us because they know their children are in a safe, loving, and magical environment.",
        "content_body": '''
            <h2>A Commitment to Excellence</h2>
            <p>We go above and beyond to provide a high-quality experience for both children and parents. From our transparent communication to our carefully curated curriculum, every detail matters.</p>
            <h2>Testimonials from Local Parents</h2>
            <p>\"Finding Fairy Tale Child Care was a game-changer for our family. Our daughter loves the playground and has learned so much in such a short time!\" - Sarah M., West Palmdale</p>
            <h2>Safety & Licensing</h2>
            <p>We are fully licensed and follow strict safety protocols. Our home-based setting is clean, secure, and designed specifically for early childhood development.</p>
        '''
    },
    {
        "slug": "childcare-in-anaverde",
        "title": "Childcare in Anaverde: Why Fairy Tale is the Local Choice",
        "category": "Locality Anchor",
        "description": "Looking for the best childcare near Anaverde? Discover why families in this beautiful Palmdale neighborhood prefer our residential setting.",
        "lead_text": "Anaverde is one of Palmdale's most scenic and family-friendly neighborhoods. We are proud to serve families in this growing community with premium childcare.",
        "content_body": '''
            <h2>A Short Drive to Magic</h2>
            <p>For parents living in Anaverde, finding a childcare provider who understands the local lifestyle is key. Our facility is conveniently located to provide a smooth commute while offering the highest standard of care.</p>
            <h2>Trusted by Your Neighbors</h2>
            <p>We already care for several children from the Anaverde area. Join our little community and see why your neighbors trust us with their children's early education.</p>
        '''
    },
    {
        "slug": "california-residential-daycare-licensing",
        "title": "Safe & Regulated: California Residential Daycare Licensing",
        "category": "PAA Capture",
        "description": "What are the rules for residential daycare in CA? Learn about the strict licensing requirements we follow to keep your child safe.",
        "lead_text": "In California, residential daycare providers are held to high standards. Understanding these regulations can give you peace of mind when choosing a provider.",
        "content_body": '''
            <h2>Strict Safety Standards</h2>
            <p>From background checks to home inspections, the California Department of Social Services ensures that licensed providers maintain a safe environment. We exceed these requirements to provide the best possible care.</p>
            <h2>Small Ratios, Higher Quality</h2>
            <p>State laws strictly limit the number of children in a residential setting. This guarantees that your child receives the individual attention they need for healthy development.</p>
        '''
    },
    {
        "slug": "infant-safety-protocols",
        "title": "Infant Safety: Our Sleep and Play Protocols",
        "category": "Service Deep Dive",
        "description": "Your baby's safety is our #1 priority. Learn about our strict infant sleep and play protocols at Fairy Tale Child Care.",
        "lead_text": "Leaving your infant in someone else's care requires absolute trust. We take that responsibility seriously with industry-leading safety standards.",
        "content_body": '''
            <h2>Safe Sleep Practices</h2>
            <p>We follow all AAP guidelines for safe sleep, ensuring every infant has a firm, flat surface and is placed on their back to rest. Our sleep areas are continuously monitored.</p>
            <h2>Active Supervision</h2>
            <p>During play, infants are always within arms-reach. We use age-appropriate, non-toxic toys and maintain a clean, sanitized environment for exploration.</p>
        '''
    },
    {
        "slug": "inside-fairy-tale-preschool",
        "title": "A Day in the Life: Inside the Fairy Tale Preschool Program",
        "category": "Project Spotlight",
        "description": "Curious what your child does all day? Take a look inside our magical preschool curriculum and daily rhythm.",
        "lead_text": "Our preschool day is a carefully balanced blend of structured learning, creative discovery, and active physical play.",
        "content_body": '''
            <h2>Morning Discovery</h2>
            <p>We start each day with storytime and "Morning Magic" circles, where we discuss the day's theme and practice basic literacy and math skills through play.</p>
            <h2>The Power of Imagination</h2>
            <p>Afternoons are for the backyard! Whether it's "Knight Training" on the playground or "Fairy Garden" planting, our activities are designed to spark wonder.</p>
        '''
    },
    {
        "slug": "palmdale-parenting-guide-2026",
        "title": "The Ultimate 2026 Palmdale Parenting Resource Guide",
        "category": "Cornerstone Pillar",
        "description": "Everything Palmdale parents need to know in 2026. From the best parks to local support groups and childcare tips.",
        "lead_text": "Raising a family in Palmdale is a rewarding experience. This guide is your gateway to the best local resources the Antelope Valley has to offer.",
        "content_body": '''
            <h2>Community Gems</h2>
            <p>From the Palmdale City Library's story hours to the family events at the Palmdale Amphitheater, there's always something happening for kids.</p>
            <h2>Top Schools & Services</h2>
            <p>We've compiled a list of the highest-rated pediatricians, youth sports leagues, and educational resources in the 93551 and 93552 area codes.</p>
        '''
    },
    {
        "slug": "handling-daycare-separation-anxiety",
        "title": "Goodbye with a Smile: Handling Daycare Separation Anxiety",
        "category": "Pro Tip",
        "description": "Drop-offs can be hard. Learn expert tips for managing separation anxiety and making the transition to daycare smooth for you and your child.",
        "lead_text": "It's natural for children (and parents!) to feel a bit of anxiety during the first few weeks of daycare. Here's how to handle it with grace.",
        "content_body": '''
            <h2>The "Quick & Happy" Goodbye</h2>
            <p>A short, positive departure routine is often more effective than a long, drawn-out goodbye. Give a firm hug, a big smile, and reassure them that you'll be back soon.</p>
            <h2>Trust the Process</h2>
            <p>Most children settle into play within minutes of their parents leaving. We provide photo updates to help you feel connected and confident throughout the day.</p>
        '''
    },
    {
        "slug": "childcare-nutrition-meal-plans",
        "title": "Nutrition & Magic: Our Storybook-Themed Meal Plans",
        "category": "Service Deep Dive",
        "description": "Healthy eating made fun! Learn about our nutritious, fresh-prepared meals and how we theme them to spark your child's appetite.",
        "lead_text": "We believe that healthy bodies fuel healthy minds. Our meal plans are designed to be both nutritious and exciting for little eaters.",
        "content_body": '''
            <h2>Fresh & Wholesome</h2>
            <p>We use fresh, seasonal ingredients to prepare balanced meals that provide the energy children need for a day of learning. No processed fillers here!</p>
            <h2>Themed for Fun</h2>
            <p>Whether it's "Dragon Breath" broccoli or "Magic Wand" fruit skewers, we turn mealtime into an extension of our storybook learning environment.</p>
        '''
    },
    {
        "slug": "after-school-programs-east-palmdale",
        "title": "Beyond Daycare: After-School Programs in East Palmdale",
        "category": "Locality Anchor",
        "description": "Searching for engaging after-school care in East Palmdale? See why our program is the perfect safe haven for school-aged kids.",
        "lead_text": "East Palmdale families need reliable, high-quality after-school support. Our program provides the perfect bridge between school and home.",
        "content_body": '''
            <h2>More Than Just Supervision</h2>
            <p>We offer homework assistance, healthy snacks, and plenty of time for physical activity on our premium playground. It's a space where kids can unwind and grow.</p>
            <h2>Safe Commutes</h2>
            <p>We are conveniently located for families in East Palmdale, offering a stress-free pickup experience and the peace of mind that your child is in a licensed home setting.</p>
        '''
    },
    {
        "slug": "playground-safety-metrics",
        "title": "Safe at Play: Our Backyard Playground Safety Metrics",
        "category": "PAA Capture",
        "description": "Is the playground safe? Learn about the professional-grade safety standards we maintain for our backyard play area in Palmdale.",
        "lead_text": "Children learn through physical play, and safety is our top priority. We've designed our playground to meet the strictest safety standards.",
        "content_body": '''
            <h2>Professional Grade Equipment</h2>
            <p>Our swings and slides are commercial-quality, designed for durability and safety. We perform daily inspections to ensure every bolt and beam is secure.</p>
            <h2>Soft Landings</h2>
            <p>We use high-impact safety surfacing under all climbing areas to reduce the risk of injury. Every "magical adventure" in our park is backed by solid safety metrics.</p>
        '''
    },
    {
        "slug": "our-storybook-reading-nook",
        "title": "Magic in Every Page: Our Storybook Reading Nook",
        "category": "Project Spotlight",
        "description": "Creating a lifelong love of reading. Take a tour of our cozy, themed reading area designed to inspire young imaginations.",
        "lead_text": "Reading is the gateway to all other learning. Our dedicated reading nook is designed to be the heart of our storybook world.",
        "content_body": '''
            <h2>A Cozy Escape</h2>
            <p>With soft cushions, magical lighting, and a carefully curated library of children's classics, our reading nook is the favorite spot for quiet time and discovery.</p>
            <h2>Early Literacy Focus</h2>
            <p>We incorporate daily read-alouds and interactive storytelling into our curriculum, helping even our youngest infants develop a deep connection to language and books.</p>
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
