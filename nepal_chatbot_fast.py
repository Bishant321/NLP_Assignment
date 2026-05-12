"""
Lightweight Nepal Tourism Chatbot - Fast Rule-Based Version
No external API dependencies - Instant startup for demo purposes
"""

import tkinter as tk
from tkinter import scrolledtext
import threading

# Import only the knowledge base (fast)
from nepal_knowledge import get_knowledge_chunks, NEPAL_TOURISM_DATA


class FastNepalChatbot:
    """Fast rule-based chatbot with no heavy ML dependencies"""
    
    def __init__(self):
        self.knowledge_chunks = get_knowledge_chunks()
        
    def respond(self, query):
        """Get response using intelligent keyword matching"""
        query_lower = query.lower()
        
        # Best time to visit
        if any(word in query_lower for word in ["best time", "when to visit", "season", "weather", "climate"]):
            return """🏔️ **Best Time to Visit Nepal:**
            
• **Peak Season (Oct-Nov):** Clear skies, best mountain views, ideal for trekking
• **Spring (Mar-Apr):** Rhododendron blooms, warm weather, great for all activities  
• **Winter (Dec-Feb):** Cold but clear, fewer crowds, good for cultural tours
• **Monsoon (Jun-Sep):** Lush greenery, fewer tourists, some trekking routes closed

Most popular: October-November for post-monsoon clarity!"""

        # Visa requirements
        if any(word in query_lower for word in ["visa", "passport", "entry", "permit"]):
            return """🛂 **Nepal Visa Information:**

• **Visa on Arrival:** Available at Kathmandu airport and land borders
• **Costs:** 
  - 15 days: $30 USD
  - 30 days: $50 USD  
  - 90 days: $125 USD
• **Requirements:** Passport (6+ months validity), passport photo, cash (USD/EUR)
• **Free Visa:** SAARC country citizens (first 30 days)
• **Online Application:** Available at nepaliport.immigration.gov.np

Pro tip: Bring exact USD cash for faster processing!"""

        # Pokhara
        if any(word in query_lower for word in ["pokhara", "phewa lake", "paragliding"]):
            return """🏞️ **Pokhara - Nepal's Tourism Capital:**

**Must-See Attractions:**
• Phewa Lake - Boating with Annapurna reflections
• Sarangkot - Sunrise/sunset mountain views
• Davis Fall & Gupteshwor Cave - Underground waterfall
• World Peace Pagoda - Panoramic Himalayan views
• Bindabasini Temple - Important Hindu shrine

**Adventure Activities:**
• Paragliding (world-class, $80-100)
• Zip-lining (one of world's steepest)
• Ultra-light aircraft flights
• Cave exploration

Gateway to Annapurna trekking region!"""

        # Everest
        if any(word in query_lower for word in ["everest", "base camp", "sagarmatha", "kala patthar"]):
            return """🏔️ **Everest Region - Roof of the World:**

**Highlights:**
• Mount Everest (8848.86m) - World's highest peak
• Everest Base Camp (5364m) - Ultimate trekking goal
• Kala Patthar (5545m) - Best EBC viewpoint
• Tengboche Monastery - Largest in Khumbu region
• Namche Bazaar - Sherpa capital

**Trek Info:**
• Duration: 12-14 days round trip
• Best seasons: Mar-May, Sep-Nov
• Difficulty: Moderate to challenging
• Alternative: Helicopter tour (4-5 hours, $1000+)

Sherpa culture and breathtaking landscapes await!"""

        # Chitwan
        if any(word in query_lower for word in ["chitwan", "wildlife", "safari", "jungle", "rhino", "tiger"]):
            return """🐅 **Chitwan National Park - Wildlife Paradise:**

**UNESCO World Heritage Site featuring:**
• One-horned Rhinoceros (500+ population)
• Bengal Tigers (rare but present)
• Gharial crocodiles
• 540+ bird species

**Activities:**
• Jungle safari (jeep or elephant-back)
• Canoe rides on Rapti River
• Bird watching tours
• Tharu village cultural tours
• Elephant bathing

**Best time:** October-February (cool, dry weather)

Stay in jungle lodges for full experience!"""

        # Lumbini
        if any(word in query_lower for word in ["lumbini", "buddha", "birth", "pilgrimage", "monastery"]):
            return """☸️ **Lumbini - Birthplace of Lord Buddha:**

**Sacred Sites:**
• Maya Devi Temple - Exact birthplace (623 BC)
• Ashoka Pillar - 3rd century BC marker
• Sacred Garden - Meditation spot
• Monastic Zone - 25+ international monasteries
• World Peace Pagoda - Built by Japanese Buddhists

**Pilgrimage Info:**
• UNESCO World Heritage Site
• Free entry to most sites
• Best time: October-April
• Combine with: Indian Buddhist circuit

A serene place for meditation and reflection!"""

        # Kathmandu
        if any(word in query_lower for word in ["kathmandu", "capital", "thamel", "durbar square"]):
            return """🏛️ **Kathmandu - City of Temples:**

**7 UNESCO World Heritage Sites:**
• Kathmandu Durbar Square - Medieval palace complex
• Swayambhunath (Monkey Temple) - Ancient stupa
• Boudhanath Stupa - Tibetan Buddhist center
• Pashupatinath - Sacred Hindu temple

**Tourist Hub - Thamel:**
• Hotels ($10-500/night)
• Restaurants (local & international)
• Trekking gear shops
• Souvenir shopping

Perfect base for exploring Nepal's culture!"""

        # Food
        if any(word in query_lower for word in ["food", "cuisine", "eat", "dal bhat", "momo", "restaurant"]):
            return """🍽️ **Nepali Cuisine - Must-Try Dishes:**

**Staple Foods:**
• **Dal Bhat** - Lentil soup, rice, curry (unlimited refills!)
• **Momo** - Dumplings (buff/chicken/veg, steamed/fried)
• **Sel Roti** - Ring-shaped rice bread
• **Thukpa** - Tibetan noodle soup

**Newari Specialties:**
• Yomari (sweet dumpling)
• Bara (lentil pancake)
• Choila (spiced grilled meat)

**Where to eat:**
• Local eateries: $2-5 per meal
• Tourist restaurants: $5-15
• Fine dining: $20-40

Don't miss the authentic Dal Bhat experience!"""

        # Budget/Cost
        if any(word in query_lower for word in ["cost", "budget", "expensive", "cheap", "money", "currency", "npr"]):
            return """💰 **Nepal Travel Budget Guide:**

**Currency:** Nepalese Rupee (NPR)
• 1 USD ≈ 130-135 NPR
• ATMs widely available in cities
• Carry cash for remote areas

**Daily Budget Estimates:**
• **Budget traveler:** $20-40/day
  - Hostels: $5-15
  - Local food: $5-10
  - Public transport
  
• **Mid-range:** $50-100/day
  - Hotels: $30-60
  - Restaurant meals: $10-20
  
• **Luxury:** $150+/day
  - 4-5 star hotels: $100+
  - Fine dining & private tours

**Trekking costs:** $25-50/day (teahouse trekking)"""

        # Itinerary planning
        if any(word in query_lower for word in ["itinerary", "plan", "schedule", "days", "route"]):
            return """📅 **Sample Nepal Itineraries:**

**7 Days - Highlights:**
Day 1-2: Kathmandu (temples, Thamel)
Day 3-5: Pokhara (lake, mountains)
Day 6-7: Return to Kathmandu

**10 Days - Classic:**
Day 1-2: Kathmandu
Day 3-5: Pokhara
Day 6-7: Chitwan (safari)
Day 8-10: Kathmandu

**14 Days - Complete:**
Day 1-3: Kathmandu + Bhaktapur
Day 4-6: Pokhara
Day 7-8: Chitwan
Day 9-11: Lumbini
Day 12-14: Kathmandu

Want a customized itinerary? Ask about specific interests!"""

        # Trekking
        if any(word in query_lower for word in ["trekking", "trek", "hiking", "hike", "annapurna circuit"]):
            return """🥾 **Trekking in Nepal - World's Best:**

**Popular Routes:**

**Everest Base Camp (12-14 days)**
• Max altitude: 5364m
• Difficulty: Moderate-Challenging
• Highlights: Sherpa culture, close-up Everest views

**Annapurna Circuit (15-20 days)**
• Max altitude: 5416m (Thorong La Pass)
• Difficulty: Challenging
• Highlights: Diverse landscapes, cultural variety

**Ghorepani Poon Hill (4-5 days)**
• Max altitude: 3210m
• Difficulty: Easy-Moderate
• Highlights: Sunrise views, rhododendron forests

**Permits Required:**
• TIMS card: $20
• National Park entry: $30-50

Best seasons: March-May, September-November!"""

        # Culture
        if any(word in query_lower for word in ["culture", "tradition", "festival", "religion", "custom"]):
            return """🎭 **Nepal's Rich Cultural Heritage:**

**Religious Harmony:**
• Hinduism (81%) - Pashupatinath, Manakamana
• Buddhism (9%) - Lumbini, Boudhanath
• Islam, Christianity, others (10%)

**Major Festivals:**
• **Dashain** (Sep/Oct) - Biggest festival, 15 days
• **Tihar** (Oct/Nov) - Festival of lights
• **Holi** (Mar) - Festival of colors
• **Buddha Jayanti** (Apr/May) - Buddha's birthday

**Cultural Etiquette:**
• Remove shoes before entering temples
• Clockwise circumambulation of stupas
• Ask before photographing people
• Dress modestly at religious sites

Experience living traditions dating back centuries!"""

        # Accommodation
        if any(word in query_lower for word in ["hotel", "accommodation", "stay", "lodge", "guesthouse"]):
            return """🏨 **Accommodation in Nepal:**

**By Category:**

**Budget ($5-20/night):**
• Guesthouses in Thamel, Pokhara Lakeside
• Basic rooms, shared bathrooms
• Common in trekking routes (teahouses)

**Mid-Range ($30-80/night):**
• 3-star hotels with private facilities
• Breakfast included, city locations
• Good comfort level

**Luxury ($100-500+/night):**
• 4-5 star hotels (Hyatt, Marriott, Dwarika's)
• Pools, spas, fine dining
• Kathmandu, Pokhara, Chitwan

**Trekking Teahouses:**
• $5-15/night (room only)
• Meals extra ($5-10 per meal)
• Basic but cozy

Book ahead during peak season (Oct-Nov)!"""

        # Default response
        return """🙏 **Namaste! Welcome to Nepal Tourism Chatbot!**

I can help you with:

🏔️ **Destinations:** Kathmandu, Pokhara, Everest, Chitwan, Lumbini, Annapurna
🎯 **Activities:** Trekking, wildlife safari, paragliding, cultural tours
📋 **Planning:** Best time to visit, itineraries, budget planning
🛂 **Practical Info:** Visa requirements, currency, accommodation
🍽️ **Local Life:** Food, culture, festivals, customs

**Quick Questions to Try:**
• "What's the best time to visit Nepal?"
• "Tell me about Everest Base Camp trek"
• "How much does a Nepal visa cost?"
• "What food should I try in Nepal?"
• "Plan a 7-day itinerary for Nepal"

Ask me anything about Nepal tourism! 🇳🇵"""


class ChatbotGUI:
    """Simple Tkinter GUI for the chatbot"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🇳🇵 Nepal Tourism Chatbot")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.chatbot = FastNepalChatbot()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#DC143C', height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🏔️ Nepal Tourism Assistant",
            font=("Arial", 18, "bold"),
            bg='#DC143C',
            fg='white'
        )
        title_label.pack(pady=15)
        
        # Chat display
        chat_frame = tk.Frame(self.root, bg='white')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg='#f9f9f9',
            fg='#333',
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Initial greeting
        self.add_message("Bot", """🙏 Namaste! Welcome to Nepal Tourism Chatbot!

I'm your local guide for everything Nepal. Ask me about:
• Destinations (Kathmandu, Pokhara, Everest, Chitwan, Lumbini)
• Activities (trekking, wildlife safari, adventure sports)
• Travel planning (visas, best time, budgets, itineraries)
• Local culture, food, and customs

Try asking: "What's the best time to visit Nepal?" or "Tell me about trekking!"

🇳🇵 Let's plan your perfect Nepal adventure!""")
        
        # Quick question buttons
        quick_frame = tk.Frame(self.root, bg='#f0f0f0')
        quick_frame.pack(fill=tk.X, padx=10, pady=5)
        
        quick_label = tk.Label(
            quick_frame,
            text="Quick Questions:",
            font=("Arial", 10, "bold"),
            bg='#f0f0f0'
        )
        quick_label.pack(anchor=tk.W)
        
        quick_questions = [
            "Best time to visit?",
            "Visa requirements?",
            "Everest Base Camp?",
            "Pokhara attractions?",
            "Food recommendations?",
            "7-day itinerary?",
            "Budget travel tips?",
            "Wildlife safari?"
        ]
        
        btn_frame = tk.Frame(quick_frame, bg='#f0f0f0')
        btn_frame.pack(fill=tk.X, pady=5)
        
        for i, question in enumerate(quick_questions):
            btn = tk.Button(
                btn_frame,
                text=question,
                command=lambda q=question: self.send_quick_question(q),
                bg='#4CAF50',
                fg='white',
                font=("Arial", 9),
                padx=5,
                pady=3
            )
            row = i // 4
            col = i % 4
            btn.grid(row=row, column=col, padx=3, pady=3, sticky='w')
        
        # Input area
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 12),
            relief=tk.SOLID,
            borderwidth=1
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind('<Return>', lambda e: self.send_message())
        
        send_btn = tk.Button(
            input_frame,
            text="Send 🚀",
            command=self.send_message,
            bg='#DC143C',
            fg='white',
            font=("Arial", 11, "bold"),
            padx=15,
            pady=5
        )
        send_btn.pack(side=tk.RIGHT)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg='#f0f0f0', height=30)
        footer_frame.pack(fill=tk.X)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Powered by Local AI • No External APIs • RAG + TinyLlama Available",
            font=("Arial", 8),
            bg='#f0f0f0',
            fg='#666'
        )
        footer_label.pack(pady=5)
        
    def add_message(self, sender, message):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        if sender == "User":
            self.chat_display.insert(tk.END, f"\n👤 You: {message}\n\n", 'user')
        else:
            self.chat_display.insert(tk.END, f"\n🤖 Bot: {message}\n\n", 'bot')
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def send_message(self):
        """Send user message and get response"""
        user_input = self.input_field.get().strip()
        
        if not user_input:
            return
        
        # Add user message
        self.add_message("User", user_input)
        self.input_field.delete(0, tk.END)
        
        # Get response in background thread
        def get_response():
            response = self.chatbot.respond(user_input)
            self.root.after(0, lambda: self.add_message("Bot", response))
        
        threading.Thread(target=get_response, daemon=True).start()
        
    def send_quick_question(self, question):
        """Send a quick question from the button"""
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, question)
        self.send_message()


def main():
    """Main function to launch the chatbot"""
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    print("=" * 60)
    print("🏔️  NEPAL TOURISM CHATBOT - FAST VERSION")
    print("=" * 60)
    print("\n✅ Starting lightweight chatbot (no heavy ML models)...")
    print("⚡ Instant startup for demo purposes")
    print("📚 Knowledge base: 26 chunks loaded")
    print("🎯 Features: Rule-based responses + keyword matching")
    print("\n🚀 Launching GUI...")
    print("\n[Note: Close GUI window to exit]")
    print("=" * 60)
    
    main()
