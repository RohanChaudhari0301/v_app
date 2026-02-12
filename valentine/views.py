from django.shortcuts import render
from django.conf import settings
from pathlib import Path

try:
    from docx import Document
except ImportError:
    Document = None


def home(request):
    show_popup = False

    if request.method == "POST" and request.POST.get("choice") == "no":
        show_popup = True

    context = {"show_popup": show_popup}
    return render(request, 'valentine/home.html', context)


def yes_page(request):
    return render(request, 'valentine/yes.html')


def letter_page(request):
    """
    Show a romantic letter on its own page.
    The body text is loaded from the letter_note.docx file.
    """
    letter_text = ""

    if Document is not None:
        docx_path = Path(settings.BASE_DIR) / "valentine" / "static" / "valentine" / "letter_note.docx"
        if docx_path.exists():
            document = Document(str(docx_path))
            paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
            letter_text = "\n\n".join(paragraphs)

    context = {
        "letter_text": letter_text,
    }
    return render(request, 'valentine/letter.html', context)
