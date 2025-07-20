# Language Translation Tool

A desktop application for translating text between different languages, built with Python and tkinter for the CodeAlpha AI Internship Task 1.

## Features

- **User-friendly GUI**: Clean and intuitive interface built with tkinter
- **Multiple Languages**: Support for 12+ languages including English, Hindi, Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese, and Arabic
- **Real-time Translation**: Uses Google Translate API through the deep-translator library
- **Copy to Clipboard**: Easy copying of translated text
- **Error Handling**: Robust error handling with user-friendly messages
- **No API Key Required**: Uses the deep-translator library which doesn't require API keys

## Screenshots

The application features:
- Source and target language dropdowns
- Input text area for entering text to translate
- Translate button to perform translation
- Output area showing translated text
- Copy to clipboard functionality
- Clear button to reset both input and output areas

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone or download the project files**
   ```bash
   # If you have the files locally, navigate to the project directory
   cd "Language translation tool"
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install deep-translator==1.11.4 pyperclip==1.8.2
   ```

## Usage

### Running the Application

1. **Start the application**
   ```bash
   python language_translator.py
   ```

2. **Using the Translation Tool**
   - Select the source language from the first dropdown
   - Select the target language from the second dropdown
   - Enter the text you want to translate in the input area
   - Click the "Translate" button
   - View the translated text in the output area
   - Use "Copy to Clipboard" to copy the translated text
   - Use "Clear" to reset both input and output areas

### Supported Languages

The application supports the following languages:
- English (en)
- Hindi (hi)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Russian (ru)
- Japanese (ja)
- Korean (ko)
- Chinese (zh)
- Arabic (ar)

## Code Structure

### Main Components

1. **LanguageTranslator Class**: Main application class that handles the GUI and translation logic
2. **create_widgets()**: Creates and arranges all GUI elements
3. **translate_language()**: Handles the translation process
4. **copy_text()**: Copies translated text to clipboard
5. **clear_text()**: Clears input and output areas

### Key Features Explained

#### Translation Process
```python
# The translation uses GoogleTranslator from deep-translator
translator = GoogleTranslator(source=source_lang, target=target_lang)
translated_text = translator.translate(text)
```

#### Error Handling
- Input validation (empty text check)
- Network error handling
- Same language selection prevention
- User-friendly error messages

#### GUI Design
- Modern color scheme with professional appearance
- Responsive layout that adapts to window resizing
- Clear visual hierarchy with proper spacing
- Disabled output area to prevent user editing

## Technical Details

### Dependencies
- **tkinter**: Built-in Python GUI library
- **deep-translator**: Translation library that uses Google Translate
- **pyperclip**: Cross-platform clipboard functionality

### Architecture
- **Object-oriented design**: Clean separation of concerns
- **Event-driven**: Responds to user interactions
- **Modular**: Easy to extend with additional features

## Troubleshooting

### Common Issues

1. **Import Error for deep-translator**
   ```bash
   pip install deep-translator
   ```

2. **Import Error for pyperclip**
   ```bash
   pip install pyperclip
   ```

3. **Translation fails**
   - Check your internet connection
   - Ensure the text is not empty
   - Verify source and target languages are different

4. **Copy to clipboard doesn't work**
   - This is usually a system-specific issue
   - Try selecting and copying manually as a workaround

## Future Enhancements

Potential improvements for the project:
- Add more languages
- Implement text-to-speech functionality
- Add translation history
- Support for file upload/download
- Dark mode theme
- Keyboard shortcuts

## Project Information

- **Project**: CodeAlpha AI Internship - Task 1
- **Technology**: Python, tkinter, deep-translator
- **Type**: Desktop Application
- **Purpose**: Language translation tool

## License

This project is created for educational purposes as part of the CodeAlpha AI Internship program.

---

**Note**: This application uses the Google Translate service through the deep-translator library. While no API key is required, it relies on internet connectivity for translation services. 