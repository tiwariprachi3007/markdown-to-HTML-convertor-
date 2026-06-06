# Markdown to HTML Converter

## Overview

Markdown to HTML Converter is a Python-based project that converts Markdown files (`.md`) into HTML files (`.html`). The project reads Markdown content from an input file, processes different Markdown elements, and generates a structured HTML webpage.

This project is developed using Python and Regular Expressions without relying on any external libraries.

---

## Features

- Convert Markdown files to HTML files
- Support for Headings (`#`, `##`, `###`)
- Support for Bold Text (`**text**`)
- Support for Italic Text (`*text*`)
- Support for Unordered Lists (`- item`)
- Support for Hyperlinks (`[text](url)`)
- Generate a complete HTML webpage
- Basic CSS styling included
- Error handling for invalid file names

---

## Technologies Used

- Python 3
- Regular Expressions (re module)
- File Handling
- HTML
- CSS

---

## Project Structure

```text
MarkdownToHTMLConverter/
│
├── converter.py
├── input.md
├── output.html
└── README.md
```

---

## How It Works

1. The user enters the Markdown file name.
2. The program reads the contents of the Markdown file.
3. Markdown syntax is identified and converted into corresponding HTML tags.
4. The converted content is wrapped inside a complete HTML document.
5. The final HTML output is saved to the specified file.

---

## How to Run

### Step 1: Create a Markdown File

Example:

```markdown
# Markdown to HTML Converter

This is **bold text**.

This is *italic text*.

## Features

- Easy to use
- Fast conversion
- No external library

[Google](https://www.google.com)
```

### Step 2: Run the Program

```bash
python converter.py
```

### Step 3: Enter File Names

Example:

```text
Enter Markdown file name: input.md
Enter HTML output file name: output.html
```

### Step 4: View Output

Open the generated `output.html` file in any web browser.

---

## Sample Output

```html
<h1>Markdown to HTML Converter</h1>

<p>This is <strong>bold text</strong>.</p>

<p>This is <em>italic text</em>.</p>

<h2>Features</h2>

<ul>
    <li>Easy to use</li>
    <li>Fast conversion</li>
    <li>No external library</li>
</ul>
```

---

## Concepts Used

- Functions
- File Handling
- String Manipulation
- Regular Expressions
- Exception Handling
- HTML Generation

---

## Future Enhancements

- Support for Ordered Lists
- Support for Images
- Support for Tables
- GUI Version using Tkinter
- Live HTML Preview
- Web-Based Version using Flask

---

## Learning Outcomes

Through this project, the following concepts were learned:

- Markdown syntax processing
- HTML document generation
- File handling in Python
- Text parsing using regular expressions
- Error handling techniques
- Basic webpage structure and styling

---

## Conclusion

This project demonstrates how Python can be used to process text files and automatically generate web content. It provides practical experience with file handling, regular expressions, and HTML generation.

---

## Author

**Prachi Tiwari**  
B.Tech Computer Science Engineering

---

## License

This project is developed for educational and learning purposes.