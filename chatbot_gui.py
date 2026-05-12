"""
Nepal Tourism Chatbot - Tkinter GUI Interface
Lightweight desktop application for Nepal tourism inquiries
No external API dependencies - uses local RAG system
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
from rag_system import NepalChatbot, rule_based_response


class NepalTourismChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏔️ Nepal Tourism Chatbot")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize chatbot
        self.chatbot = NepalChatbot()
        self.chatbot_initialized = False
        
        # Setup UI
        self.setup_ui()
        
        # Initialize chatbot in background
        self.init_chatbot_async()
    
    def setup_ui(self):
        """Setup the user interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🏔️ Nepal Tourism Chatbot",
            font=("Helvetica", 24, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Your guide to exploring beautiful Nepal",
            font=("Helvetica", 12),
            bg='#2c3e50',
            fg='#bdc3c7'
        )
        subtitle_label.pack()
        
        # Status bar
        self.status_var = tk.StringVar(value="Initializing chatbot...")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bg='#34495e',
            fg='white',
            anchor='w',
            padx=10,
            pady=5
        )
        status_bar.pack(fill=tk.X)
        
        # Chat display area
        chat_frame = tk.Frame(self.root, bg='white')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            padx=15,
            pady=15
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_configure("user", foreground="#2980b9", font=("Consolas", 11, "bold"))
        self.chat_display.tag_configure("bot", foreground="#27ae60", font=("Consolas", 11))
        self.chat_display.tag_configure("system", foreground="#7f8c8d", font=("Consolas", 10, "italic"))
        
        # Input area
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Consolas", 12),
            bg='white',
            fg='#2c3e50',
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground='#bdc3c7'
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        send_button = tk.Button(
            input_frame,
            text="Send 📤",
            command=self.send_message,
            bg='#27ae60',
            fg='white',
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        send_button.pack(side=tk.RIGHT)
        
        # Quick questions buttons
        quick_frame = tk.Frame(self.root, bg='#f0f0f0')
        quick_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        quick_label = tk.Label(
            quick_frame,
            text="Quick Questions:",
            bg='#f0f0f0',
            fg='#7f8c8d',
            font=("Helvetica", 10)
        )
        quick_label.pack(anchor='w')
        
        quick_buttons = [
            ("Best time to visit?", "What is the best time to visit Nepal?"),
            ("Visa info", "Tell me about visa requirements for Nepal"),
            ("Trekking", "What are the best trekking routes in Nepal?"),
            ("Everest", "Tell me about Everest Base Camp trek"),
            ("Pokhara", "What can I do in Pokhara?"),
            ("Food", "What food should I try in Nepal?")
        ]
        
        button_frame = tk.Frame(quick_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=5)
        
        for i, (text, query) in enumerate(quick_buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                command=lambda q=query: self.set_input_and_send(q),
                bg='#3498db',
                fg='white',
                font=("Helvetica", 9),
                relief=tk.FLAT,
                padx=10,
                pady=5,
                cursor="hand2"
            )
            btn.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Welcome message
        self.add_message("system", "Namaste! 🙏 Welcome to Nepal Tourism Chatbot. I'm here to help you plan your perfect Nepal adventure!")
        self.add_message("system", "Ask me about destinations, activities, visa requirements, best time to visit, food, culture, or itinerary planning.")
    
    def init_chatbot_async(self):
        """Initialize chatbot in background thread"""
        def init():
            try:
                success = self.chatbot.initialize()
                if success:
                    self.status_var.set("✓ Chatbot ready - RAG system active")
                    self.add_message("system", "✓ Full RAG system initialized with local LLM. Ready to answer your questions!")
                else:
                    self.status_var.set("⚠ Chatbot ready - Rule-based mode")
                    self.add_message("system", "⚠ Using rule-based responses. Full RAG system unavailable.")
                self.chatbot_initialized = True
            except Exception as e:
                self.status_var.set("⚠ Chatbot ready - Rule-based mode")
                self.add_message("system", f"⚠ Initialization note: {str(e)}")
                self.chatbot_initialized = True
        
        thread = threading.Thread(target=init, daemon=True)
        thread.start()
    
    def add_message(self, sender, message):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        if sender == "user":
            self.chat_display.insert(tk.END, "\nYou: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n")
        elif sender == "bot":
            self.chat_display.insert(tk.END, "\n🏔️ Nepal Bot: ", "bot")
            self.chat_display.insert(tk.END, f"{message}\n")
        elif sender == "system":
            self.chat_display.insert(tk.END, f"\n{message}\n", "system")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def set_input_and_send(self, query):
        """Set input field and send message"""
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, query)
        self.send_message()
    
    def send_message(self):
        """Send user message and get response"""
        user_input = self.input_field.get().strip()
        
        if not user_input:
            return
        
        # Clear input field
        self.input_field.delete(0, tk.END)
        
        # Add user message
        self.add_message("user", user_input)
        
        # Get response in background thread
        def get_response():
            try:
                response = self.chatbot.respond(user_input)
                self.root.after(0, lambda: self.add_message("bot", response))
            except Exception as e:
                # Fallback to rule-based
                response, _ = rule_based_response(user_input)
                if not response:
                    response = "Thank you for your question! I specialize in Nepal tourism. Please ask about destinations, trekking, visas, culture, food, or travel planning. Namaste! 🙏"
                self.root.after(0, lambda: self.add_message("bot", response))
        
        thread = threading.Thread(target=get_response, daemon=True)
        thread.start()


def main():
    """Main function to run the chatbot GUI"""
    root = tk.Tk()
    
    # Set window icon (emoji as fallback)
    try:
        root.iconbitmap(default='')
    except:
        pass
    
    app = NepalTourismChatbotGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    print("=" * 60)
    print("🏔️  Nepal Tourism Chatbot")
    print("=" * 60)
    print("Starting GUI application...")
    print("\nFeatures:")
    print("  ✓ RAG-based knowledge retrieval")
    print("  ✓ Local LLM for response generation")
    print("  ✓ No external API dependencies")
    print("  ✓ Comprehensive Nepal tourism data")
    print("  ✓ Quick question buttons")
    print("\nPress Ctrl+C in terminal to stop")
    print("=" * 60)
    
    main()
