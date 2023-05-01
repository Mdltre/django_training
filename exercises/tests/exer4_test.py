from exercises.models import Book, Author, Classification


# Create some classifications
c1 = Classification.objects.create(code='001', name='classif1', description='I am a description.')
c2 = Classification.objects.create(code='002', name='classif2', description='I am a description too.')

# Create some authors
a1 = Author.objects.create(full_name='Author Wan')
a2 = Author.objects.create(full_name='Author Tu')

# Create some books
Book.objects.create(title='Book 1', author=a2, classification=c1)
Book.objects.create(title='Book 2', author=a1, classification=c1)
Book.objects.create(title='Book 3', author=a1, classification=c2)