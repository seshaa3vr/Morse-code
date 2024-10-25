
import tkinter as tk
from tkinter import messagebox

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}

# Inverse Morse Code Dictionary
INVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode_to_morse(text):
    """Encode text to Morse Code."""
    text = text.upper()
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return morse_code

def decode_from_morse(morse_code):
    """Decode Morse Code to text."""
    try:
        text = ''.join(INVERSE_MORSE_CODE_DICT[code] for code in morse_code.split(' '))
        return text
    except KeyError:
        return "Error: Invalid Morse Code"

def perform_encoding():
    """Handle encoding from text to Morse Code."""
    text = input_entry.get("1.0", tk.END).strip()
    if text:
        morse_code = encode_to_morse(text)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, morse_code)
    else:
        messagebox.showwarning("Input Error", "Please enter some text to encode.")

def perform_decoding():
    """Handle decoding from Morse Code to text."""
    morse_code = input_entry.get("1.0", tk.END).strip()
    if morse_code:
        text = decode_from_morse(morse_code)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, text)
    else:
        messagebox.showwarning("Input Error", "Please enter some Morse Code to decode.")

# GUI creation
def create_gui():
    global input_entry, output_entry

    # Main window
    root = tk.Tk()
    root.title("Morse Code Tool")
    root.geometry("500x400")

    # Title
    title_label = tk.Label(root, text="Morse Code Encoder/Decoder", font=("Arial", 14))
    title_label.pack(pady=10)

    # Input Textbox
    input_label = tk.Label(root, text="Enter your text or Morse Code:")
    input_label.pack()
    input_entry = tk.Text(root, height=4, width=50)
    input_entry.pack(pady=5)

    # Encode Button
    encode_button = tk.Button(root, text="Encode to Morse Code", command=perform_encoding)
    encode_button.pack(pady=5)

    # Decode Button
    decode_button = tk.Button(root, text="Decode Morse Code", command=perform_decoding)
    decode_button.pack(pady=5)

    # Output Textbox
    output_label = tk.Label(root, text="Output:")
    output_label.pack()
    output_entry = tk.Text(root, height=4, width=50)
    output_entry.pack(pady=5)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
