import os
import re

def update_blog_hub():
    blog_dir = "blog"
    hub_path = os.path.join(blog_dir, "index.html")
    
    if not os.path.exists(hub_path):
        print(f"ERROR: {hub_path} not found.")
        return

    with open(hub_path, 'r') as f:
        content = f.read()

    # Define the articles to add
    articles = [
        {"slug": "choosing-right-childcare-palmdale", "title": "Choosing the Right Child Care in Palmdale: A Parent's Guide", "cat": "Parent Guides", "desc": "Finding the perfect daycare in Palmdale can be overwhelming. Learn what to look for..."},
        {"slug": "why-palmdale-families-trust-us", "title": "Trust & Magic: Why Palmdale Families Choose Us", "cat": "Locality Anchor", "desc": "Discover why Fairy Tale Child Care is the most trusted residential childcare in Palmdale..."},
        {"slug": "benefits-of-residential-daycare", "title": "The Magic of Small Groups: Benefits of Residential Daycare", "cat": "Education", "desc": "Why small ratios matter. Discover why residential daycare settings provide superior social..."},
        {"slug": "our-new-backyard-playground", "title": "Step Into the Magic: Our New Backyard Playground", "cat": "Facility News", "desc": "We've upgraded! Take a look at our new professional-grade backyard playground..."},
        {"slug": "when-is-child-ready-for-preschool", "title": "Is Your Child Ready for Preschool? 5 Signs to Watch For", "cat": "Parent Guides", "desc": "How do you know when it's time for Pre-K? Discover 5 indicators that your child is ready..."},
        {"slug": "transitioning-to-after-school-care", "title": "Smooth Sailing: Transitioning to After-School Care", "cat": "Education", "desc": "Make the move to after-school care easy for your child. Tips for Palmdale parents..."},
        {"slug": "consistent-routine-for-toddlers", "title": "The Power of Patterns: Creating a Routine for Toddlers", "cat": "Parent Guides", "desc": "Why toddlers need routine and how to build one that works for your family..."},
        {"slug": "sensory-play-for-infants", "title": "Sparking Discovery: Sensory Play Activities for Infants", "cat": "Education", "desc": "How to engage your baby's senses through safe, fun play. Discover the benefits..."},
        {"slug": "daycare-center-vs-residential-care", "title": "Small vs. Big: Daycare Centers vs. Residential Care", "cat": "Parent Guides", "desc": "Which is right for your child? Comparing the pros and cons of large centers vs. residential..."},
        {"slug": "west-palmdale-childcare-resources", "title": "Navigating Palmdale: Local Childcare Resources for Parents", "cat": "Locality Anchor", "desc": "A guide to local parenting resources, parks, and childcare support in West Palmdale..."},
        {"slug": "childcare-in-anaverde", "title": "Childcare in Anaverde: Why Fairy Tale is the Local Choice", "cat": "Locality Anchor", "desc": "Looking for the best childcare near Anaverde? Discover why families in Anaverde prefer us..."},
        {"slug": "california-residential-daycare-licensing", "title": "Safe & Regulated: CA Residential Daycare Licensing", "cat": "PAA Capture", "desc": "What are the rules for residential daycare in CA? Learn about the strict licensing..."},
        {"slug": "infant-safety-protocols", "title": "Infant Safety: Our Sleep and Play Protocols", "cat": "Service Deep Dive", "desc": "Your baby's safety is our #1 priority. Learn about our strict infant sleep and play..."},
        {"slug": "inside-fairy-tale-preschool", "title": "A Day in the Life: Inside the Fairy Tale Preschool Program", "cat": "Project Spotlight", "desc": "Curious what your child does all day? Take a look inside our magical preschool curriculum..."},
        {"slug": "palmdale-parenting-guide-2026", "title": "The Ultimate 2026 Palmdale Parenting Resource Guide", "cat": "Cornerstone Pillar", "desc": "Everything Palmdale parents need to know in 2026. From the best parks to local support..."},
        {"slug": "handling-daycare-separation-anxiety", "title": "Goodbye with a Smile: Handling Daycare Separation Anxiety", "cat": "Pro Tip", "desc": "Drop-offs can be hard. Learn expert tips for managing separation anxiety..."},
        {"slug": "childcare-nutrition-meal-plans", "title": "Nutrition & Magic: Our Storybook-Themed Meal Plans", "cat": "Service Deep Dive", "desc": "Healthy eating made fun! Learn about our nutritious, fresh-prepared meals..."},
        {"slug": "after-school-programs-east-palmdale", "title": "Beyond Daycare: After-School Programs in East Palmdale", "cat": "Locality Anchor", "desc": "Searching for engaging after-school care in East Palmdale? See why our program is the..."},
        {"slug": "playground-safety-metrics", "title": "Safe at Play: Our Backyard Playground Safety Metrics", "cat": "PAA Capture", "desc": "Is the playground safe? Learn about the professional-grade safety standards we maintain..."},
        {"slug": "our-storybook-reading-nook", "title": "Magic in Every Page: Our Storybook Reading Nook", "cat": "Project Spotlight", "desc": "Creating a lifelong love of reading. Take a tour of our cozy, themed reading area..."},
        {"slug": "childcare-options-quartz-hill", "title": "Childcare Options in Quartz Hill: Finding the Best Fit", "cat": "Locality Anchor", "desc": "Exploring childcare and preschool options in the Quartz Hill community..."},
        {"slug": "average-cost-residential-daycare-palmdale", "title": "What is the Average Cost of Residential Daycare in Palmdale?", "cat": "PAA Capture", "desc": "Understanding childcare costs in the Antelope Valley. A guide to residential daycare pricing..."},
        {"slug": "socialization-at-daycare-making-friends", "title": "Socialization at Daycare: How We Help Kids Make Friends", "cat": "Service Deep Dive", "desc": "Learn how our small group setting fosters deep social bonds..."},
        {"slug": "art-magic-creative-discovery-station", "title": "Art & Magic: Our Creative Discovery Station", "cat": "Project Spotlight", "desc": "Take a look at our dedicated art and creativity area where imaginations run wild..."},
        {"slug": "2026-guide-childcare-financial-assistance-ca", "title": "The 2026 Guide to Childcare Financial Assistance in California", "cat": "Cornerstone Pillar", "desc": "A comprehensive guide to subsidies, vouchers, and financial aid programs for 2026..."},
        {"slug": "transitioning-crib-to-cot-daycare-naps", "title": "Transitioning from Crib to Cot: How We Handle Naps", "cat": "Pro Tip", "desc": "Moving to a nap cot is a big milestone! Learn how we make this transition smooth..."},
        {"slug": "safe-exploration-sensory-garden-design", "title": "Safe Exploration: Our Sensory Garden Design", "cat": "Service Deep Dive", "desc": "Discover how our outdoor sensory garden helps children learn about nature..."},
        {"slug": "weekend-fun-palmdale-families-top-picks", "title": "Weekend Fun for Palmdale Families: Our Top Picks", "cat": "Locality Anchor", "desc": "Looking for family-friendly activities in Palmdale? Our favorite local spots..."},
        {"slug": "what-to-pack-first-day-daycare", "title": "What Should I Pack for My Child's First Day of Daycare?", "cat": "PAA Capture", "desc": "A handy checklist for parents preparing for their child's exciting first day..."},
        {"slug": "music-movement-daily-dance-circle", "title": "Music & Movement: Our Daily Dance Circle", "cat": "Project Spotlight", "desc": "From nursery rhymes to rhythmic play, see how music and movement spark joy..."}
    ]

    cards_html = ""
    for a in articles:
        cards_html += f'''
            <a href="/blog/{a['slug']}/" class="blog-card">
                <div class="blog-card-content">
                    <span>{a['cat']}</span>
                    <h3>{a['title']}</h3>
                    <p>{a['desc']}</p>
                </div>
            </a>'''

    # Replace the blog-grid content
    # Look for <div class="blog-grid"> ... </div>
    pattern = re.compile(r'(<div class="blog-grid">).*?(</div>)', re.DOTALL)
    new_content = pattern.sub(r'\1' + cards_html + r'\n        \2', content)

    with open(hub_path, 'w') as f:
        f.write(new_content)
    print(f"Updated {hub_path} with 10 articles.")

if __name__ == "__main__":
    update_blog_hub()
