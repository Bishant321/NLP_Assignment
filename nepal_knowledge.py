"""
Nepal Tourism Knowledge Base
Comprehensive information about Nepal tourism for RAG-based chatbot
"""

NEPAL_TOURISM_DATA = {
    "destinations": {
        "Kathmandu": {
            "description": "The capital city of Nepal, known as the 'City of Temples'. Home to seven UNESCO World Heritage Sites including Kathmandu Durbar Square, Swayambhunath (Monkey Temple), and Boudhanath Stupa.",
            "highlights": ["Kathmandu Durbar Square", "Swayambhunath Stupa", "Boudhanath Stupa", "Pashupatinath Temple", "Thamel"],
            "best_time": "October to December, March to April",
            "activities": ["Temple tours", "Cultural exploration", "Shopping in Thamel", "Food tours"]
        },
        "Pokhara": {
            "description": "The tourism capital of Nepal, famous for its stunning lakes, mountain views, and adventure activities. Gateway to the Annapurna region.",
            "highlights": ["Phewa Lake", "Davis Fall", "Gupteshwor Cave", "World Peace Pagoda", "Sarangkot"],
            "best_time": "September to November, March to May",
            "activities": ["Boating", "Paragliding", "Zip-lining", "Cave exploration", "Mountain viewing"]
        },
        "Chitwan": {
            "description": "Home to Chitwan National Park, a UNESCO World Heritage Site famous for one-horned rhinoceros, Bengal tigers, and diverse wildlife.",
            "highlights": ["Chitwan National Park", "Tharu Cultural Village", "Rapti River", "Elephant Breeding Center"],
            "best_time": "October to February",
            "activities": ["Jungle safari", "Bird watching", "Canoe rides", "Elephant bathing", "Tharu cultural shows"]
        },
        "Everest Region": {
            "description": "Home to Mount Everest (8848.86m), the highest peak in the world. A paradise for trekkers and mountaineers.",
            "highlights": ["Everest Base Camp", "Kala Patthar", "Tengboche Monastery", "Namche Bazaar"],
            "best_time": "March to May, September to November",
            "activities": ["Everest Base Camp Trek", "Helicopter tours", "Monastery visits", "Sherpa cultural experiences"]
        },
        "Annapurna Region": {
            "description": "One of the most popular trekking destinations in the world, featuring diverse landscapes from subtropical forests to high-altitude deserts.",
            "highlights": ["Annapurna Base Camp", "Annapurna Circuit", "Ghorepani Poon Hill", "Mardi Himal"],
            "best_time": "March to May, September to November",
            "activities": ["Trekking", "Hot springs", "Mountain flights", "Village tours"]
        },
        "Lumbini": {
            "description": "The birthplace of Lord Buddha, a major pilgrimage site for Buddhists worldwide and a UNESCO World Heritage Site.",
            "highlights": ["Maya Devi Temple", "Ashoka Pillar", "Sacred Garden", "Monastic Zone", "World Peace Pagoda"],
            "best_time": "October to April",
            "activities": ["Pilgrimage", "Meditation", "Monastery visits", "Cultural tours"]
        },
        "Bhaktapur": {
            "description": "A medieval city preserved in time, known for its rich culture, traditional architecture, and pottery.",
            "highlights": ["Bhaktapur Durbar Square", "55 Window Palace", "Nyatapola Temple", "Pottery Square"],
            "best_time": "Year-round",
            "activities": ["Cultural tours", "Pottery workshops", "Traditional food tasting", "Photography"]
        },
        "Nagarkot": {
            "description": "A hill station famous for panoramic Himalayan views including Mount Everest on clear days.",
            "highlights": ["Sunrise viewpoint", "Himalayan panorama", "Hiking trails"],
            "best_time": "October to April",
            "activities": ["Sunrise viewing", "Hiking", "Photography", "Relaxation"]
        },
        "Langtang": {
            "description": "Known as the 'Valley of Glaciers', offering stunning mountain scenery and rich Tamang culture.",
            "highlights": ["Langtang Valley", "Kyanjin Gompa", "Langtang Ri", "Tamang villages"],
            "best_time": "March to May, September to November",
            "activities": ["Trekking", "Cultural immersion", "Cheese factory visits", "Monastery tours"]
        }
    },
    
    "activities": {
        "Trekking": {
            "description": "Nepal is a trekker's paradise with routes ranging from easy walks to challenging high-altitude expeditions.",
            "popular_routes": ["Everest Base Camp", "Annapurna Circuit", "Langtang Valley", "Manaslu Circuit", "Upper Mustang"],
            "difficulty_levels": ["Easy (Ghorepani Poon Hill)", "Moderate (Annapurna Base Camp)", "Challenging (Everest Base Camp)", "Expert (Manaslu Circuit)"],
            "permits_required": ["TIMS Card", "National Park Entry Permit", "Special Area Permits (for restricted regions)"]
        },
        "Wildlife Safari": {
            "description": "Experience thrilling jungle safaris in Nepal's national parks to spot rare wildlife.",
            "locations": ["Chitwan National Park", "Bardia National Park", "Shuklaphanta National Park"],
            "animals": ["One-horned Rhinoceros", "Bengal Tiger", "Asian Elephant", "Sloth Bear", "Various bird species"]
        },
        "Adventure Sports": {
            "description": "Nepal offers numerous adrenaline-pumping activities for adventure enthusiasts.",
            "activities": ["Paragliding (Pokhara)", "Bungee Jumping (The Last Resort)", "Zip-lining (Pokhara)", "White Water Rafting", "Mountain Biking", "Rock Climbing"]
        },
        "Cultural Tours": {
            "description": "Explore Nepal's rich cultural heritage through temples, festivals, and traditional villages.",
            "experiences": ["UNESCO World Heritage Sites", "Living Goddess Kumari", "Traditional festivals (Dashain, Tihar, Holi)", "Newari cuisine", "Tharu culture"]
        },
        "Pilgrimage": {
            "description": "Nepal is sacred to both Hindus and Buddhists with numerous pilgrimage sites.",
            "hindu_sites": ["Pashupatinath Temple", "Muktinath", "Manakamana", "Gosainkunda"],
            "buddhist_sites": ["Lumbini", "Boudhanath", "Swayambhunath", "Namobuddha"]
        }
    },
    
    "practical_info": {
        "Visa": {
            "requirements": "Tourist visa available on arrival for most nationalities",
            "duration_options": ["15 days - $30", "30 days - $50", "90 days - $125"],
            "documents_needed": ["Valid passport (6 months validity)", "Passport photos", "Completed form", "Fee in USD cash"]
        },
        "Currency": {
            "currency": "Nepalese Rupee (NPR)",
            "exchange_rate": "Approximately 1 USD = 130-135 NPR (varies)",
            "tips": "ATMs available in cities, carry cash for remote areas, USD widely accepted for visa and tours"
        },
        "Best Time to Visit": {
            "peak_season": "October to November (clear skies, best mountain views)",
            "spring_season": "March to April (rhododendron blooms, warmer weather)",
            "monsoon": "June to September (lush greenery, fewer tourists, possible disruptions)",
            "winter": "December to February (cold, clear skies, good for lower altitude treks)"
        },
        "Health & Safety": {
            "vaccinations": ["Hepatitis A", "Typhoid", "Tetanus", "Japanese Encephalitis (recommended)"],
            "altitude_sickness": "Acclimatize properly, stay hydrated, descend if symptoms worsen",
            "travel_insurance": "Highly recommended, especially for trekking and adventure activities",
            "emergency_numbers": {"police": "100", "ambulance": "102", "tourist_police": "01-4247041"}
        },
        "Transportation": {
            "international_flights": "Tribhuvan International Airport (Kathmandu)",
            "domestic_flights": "Available to Pokhara, Lukla, Chitwan, and other destinations",
            "local_transport": ["Taxis", "Rickshaws", "Local buses", "Tourist buses", "Private vehicles"]
        },
        "Accommodation": {
            "types": ["Luxury hotels", "Boutique hotels", "Budget guesthouses", "Teahouses (trekking)", "Homestays"],
            "price_range": "$10-500+ per night depending on type and location",
            "booking_tips": "Book in advance during peak season, negotiate for longer stays"
        }
    },
    
    "culture": {
        "festivals": {
            "Dashain": "Major Hindu festival celebrating victory of good over evil (September/October)",
            "Tihar": "Festival of lights honoring animals and family bonds (October/November)",
            "Holi": "Festival of colors celebrating spring (March)",
            "Buddha Jayanti": "Celebration of Buddha's birth (April/May)",
            "Indra Jatra": "Kathmandu's biggest street festival (September)"
        },
        "cuisine": {
            "dal_bhat": "Staple meal of lentil soup, rice, vegetables, and curry",
            "momo": "Nepali dumplings filled with meat or vegetables",
            "sel_roti": "Traditional ring-shaped bread",
            "thukpa": "Tibetan noodle soup",
            "newari_food": "Rich culinary tradition of the Newar people"
        },
        "etiquette": {
            "greetings": "Namaste (palms together)",
            "temples": "Remove shoes, dress modestly, ask before photographing",
            "dining": "Eat with right hand, don't waste food",
            "general": "Respect elders, avoid public displays of affection"
        }
    },
    
    "itineraries": {
        "7_days": {
            "title": "Classic Nepal Highlights",
            "days": [
                "Day 1: Arrive Kathmandu, explore Thamel",
                "Day 2: Kathmandu UNESCO sites tour",
                "Day 3: Fly to Pokhara, Phewa Lake",
                "Day 4: Pokhara adventure activities",
                "Day 5: Return to Kathmandu, Bhaktapur",
                "Day 6: Kathmandu shopping and farewell",
                "Day 7: Departure"
            ]
        },
        "10_days": {
            "title": "Nepal Adventure & Culture",
            "days": [
                "Day 1-2: Kathmandu exploration",
                "Day 3-5: Pokhara and surrounding areas",
                "Day 6-8: Chitwan jungle safari",
                "Day 9: Return to Kathmandu",
                "Day 10: Departure"
            ]
        },
        "14_days": {
            "title": "Complete Nepal Experience",
            "days": [
                "Day 1-3: Kathmandu and valley cities",
                "Day 4-7: Pokhara and Annapurna foothills",
                "Day 8-10: Chitwan National Park",
                "Day 11-12: Lumbini pilgrimage",
                "Day 13-14: Kathmandu and departure"
            ]
        }
    }
}

# Flatten data for easier RAG processing
def get_knowledge_chunks():
    """Generate knowledge chunks for vector indexing"""
    chunks = []
    
    # Destinations
    for name, info in NEPAL_TOURISM_DATA["destinations"].items():
        chunk = f"""Destination: {name}
Description: {info['description']}
Highlights: {', '.join(info['highlights'])}
Best Time to Visit: {info['best_time']}
Activities: {', '.join(info['activities'])}"""
        chunks.append(chunk)
    
    # Activities
    for name, info in NEPAL_TOURISM_DATA["activities"].items():
        chunk = f"""Activity: {name}
Description: {info['description']}
Details: {str(info)}"""
        chunks.append(chunk)
    
    # Practical Info
    for category, info in NEPAL_TOURISM_DATA["practical_info"].items():
        chunk = f"""Practical Information - {category}:
{str(info)}"""
        chunks.append(chunk)
    
    # Culture
    for category, info in NEPAL_TOURISM_DATA["culture"].items():
        chunk = f"""Culture - {category}:
{str(info)}"""
        chunks.append(chunk)
    
    # Itineraries
    for duration, info in NEPAL_TOURISM_DATA["itineraries"].items():
        chunk = f"""Itinerary ({duration} days): {info['title']}
{chr(10).join(info['days'])}"""
        chunks.append(chunk)
    
    return chunks

if __name__ == "__main__":
    chunks = get_knowledge_chunks()
    print(f"Total knowledge chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- Chunk {i+1} ---")
        print(chunk)
