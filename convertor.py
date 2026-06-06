import re

def convert_inline(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    text = re.sub(
        r"\[(.*?)\]\((.*?)\)",
        r'<a href="\2">\1</a>',
        text
    )
    return text


def markdown_to_html(markdown_text):
    lines = markdown_text.split("\n")
    html = []
    in_list = False

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("### "):
            html.append(f"<h3>{convert_inline(line[4:])}</h3>")

        elif line.startswith("## "):
            html.append(f"<h2>{convert_inline(line[3:])}</h2>")

        elif line.startswith("# "):
            html.append(f"<h1>{convert_inline(line[2:])}</h1>")

        elif line.startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True

            html.append(f"<li>{convert_inline(line[2:])}</li>")

        else:
            if in_list:
                html.append("</ul>")
                in_list = False

            html.append(f"<p>{convert_inline(line)}</p>")

    if in_list:
        html.append("</ul>")

    return "\n".join(html)


def create_html_page(content):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Markdown to HTML Converter</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }}

        .container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
        }}

        h1 {{
            color: darkblue;
        }}

        h2 {{
            color: darkgreen;
        }}

        h3 {{
            color: darkred;
        }}

        p {{
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""


def main():
    print("===== MARKDOWN TO HTML CONVERTER =====")

    input_file = input("Enter Markdown file name: ")
    output_file = input("Enter HTML output file name: ")

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            markdown_text = file.read()

        html_content = markdown_to_html(markdown_text)
        final_html = create_html_page(html_content)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(final_html)

        print("\nConversion Successful!")
        print("Output saved in:", output_file)

    except FileNotFoundError:
        print("\nError: Input file not found!")

    except Exception as e:
        print("\nUnexpected Error:", e)


if __name__ == "__main__":
    main()