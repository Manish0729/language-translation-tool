#!/usr/bin/env python3
"""
Language Translation Tool
CodeAlpha AI Internship - Task 1
A desktop application for translating text between different languages.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

class LanguageTranslator:
    def __init__(self, root):
        """
        Initialize the Language Translator application.
        
        Args:
            root: The main tkinter window
        """
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        # Modern color scheme
        self.bg_color = '#f4f8fb'
        self.fg_color = '#22223b'
        self.button_color = '#3a86ff'
        self.button_fg = '#fff'
        self.entry_bg = '#fff'
        self.entry_border = '#bdbdbd'
        self.label_color = '#22223b'
        self.accent_color = '#e0e7ef'
        self.root.configure(bg=self.bg_color)
        
        # Available languages for translation
        self.languages = {
            'English': 'en',
            'Hindi': 'hi', 
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Portuguese': 'pt',
            'Russian': 'ru',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Chinese': 'zh',
            'Arabic': 'ar',
            'Bengali': 'bn',
            'Turkish': 'tr',
            'Urdu': 'ur',
            'Gujarati': 'gu',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Marathi': 'mr',
            'Malayalam': 'ml',
            'Punjabi': 'pa',
            'Indonesian': 'id',
            'Dutch': 'nl',
            'Greek': 'el',
            'Hebrew': 'he',
            'Thai': 'th',
            'Vietnamese': 'vi'
        }
        
        # Create the user interface
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all the GUI widgets."""
        
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="Language Translation Tool", 
                              font=("Segoe UI", 20, "bold"), bg=self.bg_color, fg=self.fg_color)
        title_label.pack(pady=(0, 20))
        
        # Language selection frame
        lang_frame = tk.Frame(main_frame, bg=self.bg_color)
        lang_frame.pack(fill=tk.X, pady=(0, 18))
        
        # Source language selection
        source_label = tk.Label(lang_frame, text="Source Language:", 
                               font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.label_color)
        source_label.grid(row=0, column=0, padx=(0, 10), pady=5, sticky='w')
        
        self.source_var = tk.StringVar(value='English')
        self.source_combo = ttk.Combobox(lang_frame, textvariable=self.source_var, 
                                        values=list(self.languages.keys()), 
                                        state='readonly', width=18, font=("Segoe UI", 12))
        self.source_combo.grid(row=0, column=1, padx=(0, 30), pady=5)
        
        # Target language selection
        target_label = tk.Label(lang_frame, text="Target Language:", 
                               font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.label_color)
        target_label.grid(row=0, column=2, padx=(0, 10), pady=5, sticky='w')
        
        self.target_var = tk.StringVar(value='Hindi')
        self.target_combo = ttk.Combobox(lang_frame, textvariable=self.target_var, 
                                        values=list(self.languages.keys()), 
                                        state='readonly', width=18, font=("Segoe UI", 12))
        self.target_combo.grid(row=0, column=3, padx=(0, 0), pady=5)
        
        # Input area
        input_label = tk.Label(main_frame, text="Enter Text:", 
                              font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.label_color)
        input_label.pack(anchor='w', pady=(10, 5))
        
        self.input_text = tk.Text(main_frame, height=6, width=60, 
                                 font=("Segoe UI", 13), wrap=tk.WORD,
                                 bg=self.entry_bg, fg=self.fg_color, relief=tk.FLAT, bd=2, 
                                 highlightthickness=2, highlightbackground=self.entry_border,
                                 insertbackground='black', insertwidth=2)
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=(0, 18), padx=5)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=(0, 18))
        
        # --- Modern ttk styles for buttons ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=("Segoe UI", 12, "bold"), padding=10, borderwidth=0)
        style.configure('Translate.TButton', background=self.button_color, foreground=self.button_fg)
        style.map('Translate.TButton',
                  background=[('active', '#265d97'), ('disabled', '#b0b8c1')],
                  foreground=[('disabled', '#ffffff')])
        style.configure('Clear.TButton', background="#ffbe0b", foreground=self.fg_color)
        style.map('Clear.TButton',
                  background=[('active', '#e09f3e'), ('disabled', '#f3e6c6')],
                  foreground=[('disabled', '#bdbdbd')])
        style.configure('Copy.TButton', background="#43aa8b", foreground=self.button_fg)
        style.map('Copy.TButton',
                  background=[('active', '#2d6a4f'), ('disabled', '#b0b8c1')],
                  foreground=[('disabled', '#ffffff')])
        
        # Translate button
        self.translate_btn = ttk.Button(button_frame, text="Translate", 
                                        command=self.translate_language,
                                        style='Translate.TButton', cursor="hand2")
        self.translate_btn.pack(side=tk.LEFT, padx=(0, 20), ipadx=10, ipady=2)
        
        # Clear button
        self.clear_btn = ttk.Button(button_frame, text="Clear", 
                                    command=self.clear_text,
                                    style='Clear.TButton', cursor="hand2")
        self.clear_btn.pack(side=tk.LEFT, padx=(0, 20), ipadx=10, ipady=2)
        
        # Output area
        output_label = tk.Label(main_frame, text="Translated Text:", 
                               font=("Segoe UI", 12, "bold"), bg=self.bg_color, fg=self.label_color)
        output_label.pack(anchor='w', pady=(10, 5))
        
        self.output_text = tk.Text(main_frame, height=6, width=60, 
                                  font=("Segoe UI", 13), wrap=tk.WORD,
                                  bg=self.accent_color, fg=self.fg_color, 
                                  relief=tk.FLAT, bd=2, highlightthickness=2, highlightbackground=self.entry_border, state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10), padx=5)
        
        # Copy button
        self.copy_btn = ttk.Button(main_frame, text="Copy to Clipboard", 
                                   command=self.copy_text,
                                   style='Copy.TButton', cursor="hand2")
        self.copy_btn.pack(pady=(0, 10), ipadx=10, ipady=2)
        
    def translate_language(self):
        """
        Translate the text from source language to target language.
        This function is triggered by the "Translate" button.
        """
        try:
            # Get the text from input widget
            text = self.input_text.get("1.0", tk.END).strip()
            
            # Check if text is empty
            if not text:
                messagebox.showwarning("Warning", "Please enter some text to translate!")
                return
            
            # Get selected languages
            source_lang = self.languages[self.source_var.get()]
            target_lang = self.languages[self.target_var.get()]
            
            # Check if source and target languages are the same
            if source_lang == target_lang:
                messagebox.showinfo("Info", "Source and target languages are the same!")
                return
            
            # Show loading message
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", "Translating...")
            self.output_text.config(state=tk.DISABLED)
            self.root.update()
            
            # Perform translation using GoogleTranslator
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated_text = translator.translate(text)
            
            # Display the translated text
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", translated_text)
            self.output_text.config(state=tk.DISABLED)
            
        except Exception as e:
            # Handle any errors that occur during translation
            error_message = f"Translation error: {str(e)}"
            messagebox.showerror("Error", error_message)
            
            # Clear the output text
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.config(state=tk.DISABLED)
    
    def copy_text(self):
        """
        Copy the translated text from output widget to clipboard.
        This function is triggered by the "Copy to Clipboard" button.
        """
        try:
            # Get text from output widget
            translated_text = self.output_text.get("1.0", tk.END).strip()
            
            # Check if there's text to copy
            if not translated_text or translated_text == "Translating...":
                messagebox.showwarning("Warning", "No text to copy!")
                return
            
            # Copy text to clipboard
            pyperclip.copy(translated_text)
            messagebox.showinfo("Success", "Text copied to clipboard!")
            
        except Exception as e:
            # Handle any errors that occur during copying
            error_message = f"Copy error: {str(e)}"
            messagebox.showerror("Error", error_message)
    
    def clear_text(self):
        """
        Clear both input and output text areas.
        This function is triggered by the "Clear" button.
        """
        # Clear input text
        self.input_text.delete("1.0", tk.END)
        
        # Clear output text
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

def main():
    """
    Main function to create and run the Language Translator application.
    """
    # Create the main window
    root = tk.Tk()
    
    # Create the translator application
    app = LanguageTranslator(root)
    
    # Start the tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main() 