from .models import Page
import random

def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        if page.score > 10 or page.score < 0:
            page.score = random.randint(1, 10)
            page.save()