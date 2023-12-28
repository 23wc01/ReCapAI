from docx import Document

def print_recap(recap):
    """Print formatted recap with titles & newlines
        Parameters:
        recap -- str, Contains summary, key points, tasks, sentiment
    """
    for key, value in recap.items():
        print("\n" + key)
        print(value)

def save_as_docx(recap, file_path="./", filename="recapai"):
    """Save formatted recap with titles & newlines as Microsoft Word docx
        Parameters:
        recap -- str, Contains summary, key points, tasks, sentiment
    """
    file_address = file_path + filename + ".docx"
    doc = Document()
    for key, value in recap.items():
        heading = key
        doc.add_heading(heading, level=1)
        doc.add_paragraph(value)
        doc.add_paragraph()
    doc.save(file_address)
    print(f"Saved {filename}.docx at {file_path}")

def save_as_txt(recap, file_path="./", filename="recapai"):
    """Save formatted recap with titles & newlines as simple text document(.txt)
        Parameters:
        recap -- str, Contains summary, key points, tasks, sentiment
    """
    file_address = file_path + filename + ".txt"
    doc = Document()
    with open(file_address, "w") as file:
        for key, value in recap.items():
            file.write("\n" + key)
            file.write(value)
    print(f"Saved {filename}.txt at {file_path}")


