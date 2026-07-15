# -*- coding: utf-8 -*-
"""Content data for the Boundaryline site build."""

def uns(photo_id, w=1200, h=None):
    base = f"https://images.unsplash.com/photo-{photo_id}?q=80&w={w}&auto=format&fit=crop"
    if h:
        base += f"&h={h}"
    return base

# Brand copy from Boundaryline_Condensed.pdf (no em dashes)
TAGLINE = "CROSS EVERY BOUNDARY."
HERO_SUB = "Building the operating system for grassroots cricket."

VISION = (
    "To build the world's most trusted grassroots cricket ecosystem, "
    "where every aspiring cricketer gets to play, improve, get discovered, "
    "and never go unnoticed."
)

VISION_EXTRA = (
    "Picture a kid picking up his bat for the first time. He should have a clear path "
    "to the right coaching, a clear path to exposure: practice matches, tournaments, "
    "outside tours, domestic and international tours, and access to great gear that's "
    "affordable and worth it. If he goes professional, a clear path to good clubs too. "
    "Talent is universal; opportunity isn't. We're closing that gap, starting in Mumbai, "
    "scaling across India, and eventually the world."
)

MISSION = (
    "Organize every touchpoint in a cricketer's journey under one trusted platform: "
    "coaching, matches, tournaments, gear, performance tracking, community, and career progression."
)

MISSION_POINTS = [
    ("sun", "QUALITY GEAR", "Distribute quality, affordable cricket gear."),
    ("users", "COACH DEVELOPMENT", "Train coaches and build a structured coaching ecosystem."),
    ("zap", "DATA-DRIVEN JOURNEYS", "Make the journey data-driven and personal to each player."),
    ("eye", "NO TALENT OVERLOOKED", "Make sure no talent goes unnoticed. Opportunities should find players, not the other way around."),
]

WHY_POINTS = [
    ("trophy", "01", "FULL ECOSYSTEM", "Most organizers run tournaments. We build ecosystems: the full journey, not isolated events."),
    ("calendar", "02", "ALWAYS A NEXT MATCH", "Players never have to wonder where to play next. We answer that every week."),
    ("network", "03", "MATCHED FAIRLY", "We connect teams by skill, format, availability, ground preference, and competitive intensity."),
    ("globe", "04", "STARTING IN MUMBAI", "Built on real matches across the city, with a clear path to scale across India."),
]

PROBLEM = {
    "lead": "Grassroots cricket in India is fragmented, unstructured, and unorganized. Many players in the market, but no single platform, so kids and families don't know where to go.",
    "points": [
        "No centralized way to find quality matches",
        "Limited match exposure despite regular practice",
        "Heavy dependence on personal connections",
        "No structured progression, no reliable performance records",
        "Talent stays invisible for lack of exposure",
    ],
    "close": "Players don't quit for lack of talent. They quit for lack of access. Opportunity is unorganized. That's the real gap.",
}

SOLUTION = {
    "lead": "One ecosystem, solving problems for everyone at once.",
    "points": [
        ("Players", "Quality, well-matched competitive cricket."),
        ("Ground owners", "Consistent bookings."),
        ("Coaches", "Tools to manage and grow their coaching."),
        ("Every kid", "A simpler journey, optimized end to end."),
    ],
    "close": (
        "We connect teams by skill, format, availability, ground preference, and competitive intensity, "
        "so even a player with no network can walk into quality matches from day one."
    ),
}

WHAT_WE_DO = (
    "Across Mumbai: practice matches, competitive tournaments, age-group and community cricket, "
    "team matching, scheduling, and networking. Every match is another shot at getting discovered."
)

WHY_NOW = [
    "Rising grassroots participation year over year",
    "Families investing in real match experience, not just coaching",
    "Growing willingness to pay for well-organized play",
    "One of the least digitized, most underserved segments in Indian sports",
]

PROGRESS = [
    (100, "+", "COMPETITIVE PRACTICE MATCHES"),
    (6, "+", "TOURNAMENTS ACROSS AGE GROUPS"),
    (100, "+ DOZEN", "CRICKET BALLS SOLD"),
    (8, " MO", "BUILT WITHOUT PRIOR TOURNAMENT EXPERIENCE"),
]

PROGRESS_NOTE = (
    "In under eight months, without prior tournament experience: teams matched by skill and preference "
    "for stronger, more watchable fixtures. Grounds secured, and groundwork laid to launch our own "
    "coaching program. Built entirely through execution, not funding, and customers keep telling us it's working."
)

PHILOSOPHY = "Talent should determine opportunity. Not connections, geography, or privilege."

LONG_TERM = (
    "The operating system for grassroots cricket: tournament management, a practice match marketplace, "
    "player profiles, performance analytics, talent discovery, rankings, an academy and coaching network, "
    "a scouting platform, community, careers, sponsorships, and AI-powered insights. One platform "
    "connecting every stakeholder."
)

FUTURE = (
    "A kid who's never played outside his local ground discovers matches in minutes, competes against "
    "real opposition, builds a verified record, gets noticed, and earns his way up, purely on merit. "
    "Not luck. The default. We're not building another tournament company. We're building the foundation "
    "for how grassroots cricket gets organized in Mumbai, across India, and everywhere the game is played."
)

# Core team + match management (Ashish Yadav is Match Management, not Core Team)
STAFF = [
    {"name": "Shardul Bhande", "role": "Co-Founder", "id": "1507003211169-0a1dd7228f2d", "group": "core"},
    {"name": "Devavrat Kelkar", "role": "Co-Founder", "id": "1519085360753-af0119f7cbe7", "group": "core"},
    {"name": "Aditya Manjere", "role": "Match Official, Operations", "id": "1506794778202-cad84cf45f1d", "group": "core"},
    {"name": "Suneet Yadav", "role": "Operations & Match Management", "id": "1500648767791-00dcc994a43e", "group": "ops"},
    {"name": "Arpit Pandey", "role": "Match Management", "id": "1472099645785-5658abf4ff4e", "group": "ops"},
    {"name": "Ashish Yadav", "role": "Match Management", "id": "1560250097-0b93528c311a", "group": "ops"},
]

TESTIMONIAL_PORTRAIT_IDS = [
    "1472099645785-5658abf4ff4e",
    "1522872641108-bcb51e2aff69",
    "1595152128156-ed2670305e8e",
    "1595152452543-e5fc28ebc2b8",
    "1623531879509-e4944f7e34ff",
]
TESTIMONIALS = [
    {
        "quote": "Before Boundaryline, our Sundays were spent calling grounds and hoping someone showed up. Now we get proper opponents, on time, matched to our level. The cricket feels serious again.",
        "name": "Kunal Mehta",
        "role": "Captain, Andheri XI",
        "id": TESTIMONIAL_PORTRAIT_IDS[0],
    },
    {
        "quote": "My son used to only do nets. After three weekends with Boundaryline he started caring about his strike rate and fitness. That kind of match exposure is hard to find in Mumbai.",
        "name": "Neha Kulkarni",
        "role": "Parent, U-14 player",
        "id": TESTIMONIAL_PORTRAIT_IDS[1],
    },
    {
        "quote": "They don't just put on games. They put two sides on that can actually push each other. As a coach, that is the difference between a good session and a wasted morning.",
        "name": "Imran Sheikh",
        "role": "Grassroots coach, Bandra",
        "id": TESTIMONIAL_PORTRAIT_IDS[2],
    },
    {
        "quote": "Clear communication, clean scheduling, and people who are actually on the ground. We have played with a lot of organizers. Boundaryline is the one we trust week after week.",
        "name": "Siddharth Rao",
        "role": "Team manager, Thane",
        "id": TESTIMONIAL_PORTRAIT_IDS[3],
    },
    {
        "quote": "I walked in with no big network and still got competitive fixtures from day one. That should be normal. With Boundaryline, it finally is.",
        "name": "Aisha Fernandes",
        "role": "Open category batter",
        "id": TESTIMONIAL_PORTRAIT_IDS[4],
    },
    {
        "quote": "From grounds to gear to getting us the next match, everything sits in one place. It feels like someone finally built the system this city needed.",
        "name": "Vikram Patel",
        "role": "Academy coordinator",
        "id": TESTIMONIAL_PORTRAIT_IDS[0],
    },
]

TEAMS = [
    {"code": "BLS", "name": "BL Strikers", "tag": "Regular fixtures", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "MCH", "name": "Metro Chargers", "tag": "City circuit", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "CEA", "name": "Coastal Eagles", "tag": "Weekend cricket", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "NRD", "name": "North Riders", "tag": "Age-group focus", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "DGT", "name": "Desert Giants", "tag": "Competitive play", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "RWR", "name": "River Warriors", "tag": "Practice matches", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "HHW", "name": "Highland Hawks", "tag": "Community cricket", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
    {"code": "SCM", "name": "Southern Comets", "tag": "Tournament side", "record": "Skill-matched",
     "primary": "#0B0B0B", "founded": "2025", "home": "Mumbai",
     "squad": ["Squad rotating by fixture", "Open to age-group players", "Community & competitive formats"]},
]

VENUES = [
    "Mumbai grounds network",
    "Partner turfs across the city",
    "Age-group venues, Mumbai",
]

FIXTURES_UPCOMING = [
    {"day": "19", "mon": "JUL", "time": "7:00 AM", "stage": "Practice Match",
     "home": "Skill-matched XI", "away": "Skill-matched XI", "venue": VENUES[0], "status": "LIVE SOON"},
    {"day": "20", "mon": "JUL", "time": "7:30 AM", "stage": "Practice Match",
     "home": "Community side A", "away": "Community side B", "venue": VENUES[1], "status": "UPCOMING"},
    {"day": "26", "mon": "JUL", "time": "8:00 AM", "stage": "Age-Group Fixture",
     "home": "U-16 Group", "away": "U-16 Group", "venue": VENUES[2], "status": "UPCOMING"},
    {"day": "27", "mon": "JUL", "time": "7:00 AM", "stage": "Competitive Match",
     "home": "Open category", "away": "Open category", "venue": VENUES[0], "status": "UPCOMING"},
    {"day": "02", "mon": "AUG", "time": "8:00 AM", "stage": "Tournament Match",
     "home": "TBD", "away": "TBD", "venue": VENUES[1], "status": "UPCOMING"},
]
FIXTURES_RESULTS = [
    {"day": "13", "mon": "JUL", "home": "Skill-matched XI", "away": "Skill-matched XI",
     "hs": "142/7", "as_": "138/9", "venue": VENUES[0], "note": "Won by 4 runs"},
    {"day": "12", "mon": "JUL", "home": "Community side A", "away": "Community side B",
     "hs": "156/5", "as_": "151/8", "venue": VENUES[1], "note": "Won by 5 runs"},
    {"day": "06", "mon": "JUL", "home": "U-16 Group", "away": "U-16 Group",
     "hs": "121/9", "as_": "122/4", "venue": VENUES[2], "note": "Won by 6 wickets"},
    {"day": "05", "mon": "JUL", "home": "Open category", "away": "Open category",
     "hs": "168/6", "as_": "170/5", "venue": VENUES[0], "note": "Won by 5 wickets"},
]

NEWS = [
    {"tag": "UPDATE", "date": "JUL 12, 2026", "title": "100-plus practice matches and counting",
     "excerpt": "In under eight months, Boundaryline has put on 100+ competitive practice matches across Mumbai.",
     "body": "In under eight months, without prior tournament experience, the team has organized 100+ competitive practice matches and 6+ tournaments across age groups. Fixtures are matched by skill and preference so games stay competitive and worth watching. Grounds are secured week after week, and work is underway to launch a coaching program.",
     "id": "1730739463889-34c7279277a9"},
    {"tag": "PLAYERS", "date": "JUL 08, 2026", "title": "When opportunity finds the player",
     "excerpt": "The whole idea is simple. A kid with no network should still walk into a quality match.",
     "body": "We connect teams by skill, format, availability, ground preference, and competitive intensity. That means a player who doesn't have the 'right' contacts can still find real cricket from day one. Opportunities should find players, not the other way around.",
     "id": "1685541000917-fbd006a013f8"},
    {"tag": "ECOSYSTEM", "date": "JUN 28, 2026", "title": "More than another tournament company",
     "excerpt": "Most organizers run events. Boundaryline is building the operating system around them.",
     "body": "Practice matches, competitive tournaments, age-group and community cricket, team matching, scheduling, networking, and gear. Every touchpoint sits under one trusted setup so players stop wondering where to play next.",
     "id": "1652513842544-ca66b676757a"},
    {"tag": "GEAR", "date": "JUN 20, 2026", "title": "100+ dozen cricket balls into real games",
     "excerpt": "Quality gear that people can actually afford is part of the same problem we're solving.",
     "body": "Alongside fixtures, Boundaryline has moved 100+ dozen cricket balls into circulation. Good equipment shouldn't be a luxury if we're serious about grassroots play staying accessible.",
     "id": "1607734834519-d8576ae60ea6"},
    {"tag": "WHY NOW", "date": "JUN 10, 2026", "title": "Families want match experience, not just nets",
     "excerpt": "Participation is rising. So is the willingness to pay for cricket that is properly organized.",
     "body": "Grassroots cricket remains one of the least digitized parts of Indian sport. Families are investing in real match experience, not only coaching. That demand is why a trusted platform for fixtures, progression, and discovery matters now.",
     "id": "1565787154274-c8d076ad34e7"},
    {"tag": "TEAM", "date": "JUN 01, 2026", "title": "Built through execution, not funding",
     "excerpt": "The early traction came from showing up on grounds, week after week.",
     "body": "Co-founders Shardul Bhande and Devavrat Kelkar, with Aditya Manjere on match official and operations work, and the match management group including Suneet Yadav, Arpit Pandey, and Ashish Yadav, have grown Boundaryline on delivery first. Customers keep saying the cricket on the ground is working.",
     "id": "1730739628981-6537b299aea3"},
]

# Local gallery. Excludes fotos / daniel-damasio only.
PHOTO_GALLERY = [
    {"src": "assets/gallery-01.jpg", "cat": "community", "alt": "Academy team photo"},
    {"src": "assets/gallery-02.jpg", "cat": "awards", "alt": "Trophy winners"},
    {"src": "assets/alessandro-bogliari-oDs_AxeR5g4-unsplash.jpg", "cat": "action", "alt": "Cricket ball on grass"},
    {"src": "assets/gallery-03.jpg", "cat": "action", "alt": "Match day"},
    {"src": "assets/gallery-04.jpg", "cat": "action", "alt": "On the field"},
    {"src": "assets/gallery-05.jpg", "cat": "community", "alt": "Squad huddle"},
    {"src": "assets/gallery-06.jpg", "cat": "awards", "alt": "Celebration"},
    {"src": "assets/gallery-07.jpg", "cat": "action", "alt": "Practice session"},
    {"src": "assets/gallery-08.jpg", "cat": "community", "alt": "Young players"},
    {"src": "assets/gallery-09.jpg", "cat": "action", "alt": "Bowling spell"},
    {"src": "assets/gallery-10.jpg", "cat": "community", "alt": "Team moment"},
    {"src": "assets/gallery-11.jpg", "cat": "awards", "alt": "Presentation"},
    {"src": "assets/gallery-12.jpg", "cat": "action", "alt": "Batting net"},
    {"src": "assets/gallery-13.jpg", "cat": "community", "alt": "Coaching group"},
    {"src": "assets/gallery-14.jpg", "cat": "action", "alt": "Fielding drill"},
    {"src": "assets/gallery-15.jpg", "cat": "awards", "alt": "Winners' photo"},
    {"src": "assets/gallery-16.jpg", "cat": "community", "alt": "Grassroots cricket"},
    {"src": "assets/gallery-17.jpg", "cat": "action", "alt": "Game time"},
    {"src": "assets/gallery-18.jpg", "cat": "community", "alt": "After the match"},
    {"src": "assets/gallery-field.jpg", "cat": "action", "alt": "Outfield"},
    {"src": "assets/gallery-player.jpg", "cat": "action", "alt": "Player focus"},
]

# Kept for any residual references
GALLERY_ITEMS = []
HERO_IDS = []
