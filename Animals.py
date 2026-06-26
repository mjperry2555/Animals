import ui
import speech

# Complete alphabet data with animal emojis and names
letters_data = [
    {'upper': 'A', 'lower': 'a', 'emoji': '🐜', 'name': 'Ant'},
    {'upper': 'B', 'lower': 'b', 'emoji': '🐻', 'name': 'Bear'},
    {'upper': 'C', 'lower': 'c', 'emoji': '🐱', 'name': 'Cat'},
    {'upper': 'D', 'lower': 'd', 'emoji': '🐶', 'name': 'Dog'},
    {'upper': 'E', 'lower': 'e', 'emoji': '🐘', 'name': 'Elephant'},
    {'upper': 'F', 'lower': 'f', 'emoji': '🐸', 'name': 'Frog'},
    {'upper': 'G', 'lower': 'g', 'emoji': '🦒', 'name': 'Giraffe'},
    {'upper': 'H', 'lower': 'h', 'emoji': '🐴', 'name': 'Horse'},
    {'upper': 'I', 'lower': 'i', 'emoji': '🦎', 'name': 'Iguana'},
    {'upper': 'J', 'lower': 'j', 'emoji': '🪼', 'name': 'Jellyfish'},
    {'upper': 'K', 'lower': 'k', 'emoji': '🦘', 'name': 'Kangaroo'},
    {'upper': 'L', 'lower': 'l', 'emoji': '🦁', 'name': 'Lion'},
    {'upper': 'M', 'lower': 'm', 'emoji': '🐒', 'name': 'Monkey'},
    {'upper': 'N', 'lower': 'n', 'emoji': '🐋', 'name': 'Narwhal'},
    {'upper': 'O', 'lower': 'o', 'emoji': '🐙', 'name': 'Octopus'},
    {'upper': 'P', 'lower': 'p', 'emoji': '🐼', 'name': 'Panda'},
    {'upper': 'Q', 'lower': 'q', 'emoji': '🐦', 'name': 'Quail'},
    {'upper': 'R', 'lower': 'r', 'emoji': '🐰', 'name': 'Rabbit'},
    {'upper': 'S', 'lower': 's', 'emoji': '🐍', 'name': 'Snake'},
    {'upper': 'T', 'lower': 't', 'emoji': '🐯', 'name': 'Tiger'},
    {'upper': 'U', 'lower': 'u', 'emoji': '🦄', 'name': 'Unicorn'},
    {'upper': 'V', 'lower': 'v', 'emoji': '🦇', 'name': 'Vampire Bat'},
    {'upper': 'W', 'lower': 'w', 'emoji': '🐳', 'name': 'Whale'},
    {'upper': 'X', 'lower': 'x', 'emoji': '🐟', 'name': 'X-ray Fish'},
    {'upper': 'Y', 'lower': 'y', 'emoji': '🦬', 'name': 'Yak'},
    {'upper': 'Z', 'lower': 'z', 'emoji': '🦓', 'name': 'Zebra'},
]

current_index = 0

class AlphabetView(ui.View):
    def __init__(self):
        self.background_color = '#E0F7FA'   # Light cyan / kid-friendly
        
        # Title at top
        self.title_label = ui.Label(
            text='🐾 Alphabet Animals 🐾',
            font=('Helvetica-Bold', 36),
            alignment=ui.ALIGN_CENTER,
            text_color='#0277BD'
        )
        self.add_subview(self.title_label)
        
        # Big uppercase letter
        self.letter_label = ui.Label(
            font=('Helvetica-Bold', 220),
            alignment=ui.ALIGN_CENTER,
            text_color='#1565C0'
        )
        self.add_subview(self.letter_label)
        
        # Big animal emoji
        self.animal_label = ui.Label(
            font=('AppleColorEmoji', 180),
            alignment=ui.ALIGN_CENTER
        )
        self.add_subview(self.animal_label)
        
        # Animal name
        self.name_label = ui.Label(
            font=('Helvetica-Bold', 48),
            alignment=ui.ALIGN_CENTER,
            text_color='#2E7D32'
        )
        self.add_subview(self.name_label)
        
        # Progress indicator
        self.progress_label = ui.Label(
            font=('Helvetica', 20),
            alignment=ui.ALIGN_CENTER,
            text_color='#616161'
        )
        self.add_subview(self.progress_label)
        
        # Bottom instruction
        self.instruction_label = ui.Label(
            text='👆 Tap left side = previous   •   Tap anywhere else = next',
            font=('Helvetica', 18),
            alignment=ui.ALIGN_CENTER,
            text_color='#757575'
        )
        self.add_subview(self.instruction_label)
        
        self.update_content()
    
    def layout(self):
        """Responsive layout — works on any iPad size"""
        w, h = self.width, self.height
        
        self.title_label.frame = (0, 20, w, 50)
        self.letter_label.frame = (0, 80, w, 220)
        self.animal_label.frame = (0, 310, w, 200)
        self.name_label.frame = (0, 520, w, 60)
        self.progress_label.frame = (0, h - 100, w, 30)
        self.instruction_label.frame = (0, h - 60, w, 30)
    
    def update_content(self):
        """Update display and speak the letter"""
        global current_index
        data = letters_data[current_index]
        
        # Stop any previous speech to prevent overlapping
        speech.stop()
        
        self.letter_label.text = data['upper']
        self.animal_label.text = data['emoji']
        self.name_label.text = data['name']
        self.progress_label.text = f"{current_index + 1} / 26   •   {data['upper']}"
        
        # Speak full phrase: "v is for Vampire Bat"
        phrase = f"{data['lower']} is for {data['name']}"
        speech.say(phrase)
    
    def touch_began(self, touch):
        global current_index
        w = self.width
        
        # Left 1/3 of screen = go back
        if touch.location[0] < w / 3:
            current_index = (current_index - 1) % len(letters_data)
        else:
            # Anywhere else = go forward
            current_index = (current_index + 1) % len(letters_data)
        
        self.update_content()


# ====================== RUN THE APP ======================
view = AlphabetView()
view.present('fullscreen')