import csv  # https://docs.python.org/3/library/csv.html

from polls.models import Question, Choice
from django.utils import timezone

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print(row)

        # Make a new Question and save it
        question, created = Question.objects.get_or_create(question_text=row[0], pub_date=timezone.now())
        question.save()
        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it
        for text in row[1:]:
            choice, created = Choice.objects.get_or_create(question=question, choice_text=text)
            choice.save()
            

    print("=== Load Complete")