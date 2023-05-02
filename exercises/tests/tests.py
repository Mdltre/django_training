from exercises.models import Book, Author, Classification, Publisher


# Create some classifications
c1 = Classification.objects.create(code='001', name='name1', description='I am a description.')
c2 = Classification.objects.create(code='002', name='name2', description='I am a description too.')

# Create some authors
a1 = Author.objects.create(first_name='Author', last_name='Wan', email='awan@email.com')
a2 = Author.objects.create(first_name='Authy', last_name='Tu', email='autu@email.com')

# Create some publishers
p1 = Publisher.objects.create(name='Publisher1', address='Address1',city='City1', state_province='Province1', country='Country1', website='publisherwan.com')
p2 = Publisher.objects.create(name='Publisher2', address='Address2',city='City2', state_province='Province2', country='Country2', website='publishertu.com')

# Create some books
Book.objects.create(title='Book 1', author=a2, classification=c1, publisher=p1)
Book.objects.create(title='Book 2', author=a1, classification=c1, publisher=p2)
Book.objects.create(title='Book 3', author=a1, classification=c2, publisher=p1)