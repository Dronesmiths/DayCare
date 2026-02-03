# AI Pilots: Content & Newsletter Queue

Use this checklist to track the rollout of the 50 high-authority content pieces. Mark as `[x]` only after the page is live and CloudFront cache is invalidated.

## Phase 1: The Authority Foundation (1-10)
- [x] **01: Cornerstone Guide** - The Ultimate Guide to Refrigerator Maintenance in the High Desert
- [x] **02: Locality Anchor** - Why Lancaster Residents Trust Mobile Appliance Repair
- [x] **03: Service Deep Dive** - Common Reasons Why Your Washer Isn't Spinning
- [x] **04: Project Spotlight** - Hard Water Effects on Dishwashers in Palmdale
- [x] **05: PAA Capture** - 5 Signs Your Refrigerator Needs Repair Immediately
- [x] **06: Service Deep Dive** - Dryer Not Heating? Simple Troubleshooting Steps
- [x] **07: Pro Tip** - How to Prevent Appliance Damage During Quartz Hill Power Surges
- [ ] **08: Project Spotlight** - Microwave Repair vs. Replacement: A Cost-Benefit Analysis
- [ ] **09: PAA Capture** - Why is my oven smell like gas? (Safety Warning)
- [ ] **10: Locality Anchor** - Rosamond Appliance Care: Expert Service for North Valley

## Phase 2: Strategic Expansion (11-30)
- [ ] **11: Locality Anchor** - Wind-Resistant Pool Care in Rosamond
- [ ] **12: PAA Capture** - When should I drain and refill my pool?
- [ ] **13: Service Deep Dive** - Commercial Pool Care: Keeping AV Facilities Safe
- [ ] **14: Project Spotlight** - Tile Calcium Removal Success Story
- [ ] **15: Cornerstone Pillar** - The 2026 Homeowner's Guide to Energy Efficient Pool Equipment
- [ ] **16-30:** ...

## Phase 3: Domain Dominance (31-50)
- [ ] **31:** ...
- [ ] **50:** ...

> [!IMPORTANT]
> **Deployment Rule**: Every time a checkbox is marked `[x]`, you must:
> 1. Sync the repo: `git add . && git commit -m "feat: deploy content piece #[XX]" && git push`
> 2. Sync S3: `aws s3 sync . s3://mobile-appliance-repair-av --profile mediusa`
> 3. Invalidate: `aws cloudfront create-invalidation --distribution-id [ID] --paths "/news/*" "/blog/*"`
