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
        {"slug": "west-palmdale-childcare-resources", "title": "Navigating Palmdale: Local Childcare Resources for Parents", "cat": "Locality Anchor", "desc": "A guide to local parenting resources, parks, and childcare support in West Palmdale..."}
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
