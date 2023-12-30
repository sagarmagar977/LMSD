
from django.db import models
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone




class BookInfo(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    catagory_choices = [
    ('textbook', 'Textbooks'),
    ('reference_materials', 'Reference Materials'),
    ('reserve_collection', 'Reserve Collection'),
    ('periodicals_journals', 'Periodicals and Journals'),
    ('fiction_literature', 'Fiction and Literature'),
    ('science_technology', 'Science and Technology'),
    ('mathematics', 'Mathematics'),
    ('social_sciences', 'Social Sciences'),
    ('humanities', 'Humanities'),
    ('business_economics', 'Business and Economics'),
    ('health_sciences', 'Health Sciences'),
    ('computer_science_it', 'Computer Science and Information Technology'),
    ('education', 'Education'),
    ('languages', 'Languages'),
    ('fine_arts', 'Fine Arts'),
    ('law_political_science', 'Law and Political Science'),
    ('environmental_sciences', 'Environmental Sciences'),
    ('architecture_design', 'Architecture and Design'),
    ('multidisciplinary_studies', 'Multidisciplinary Studies'),
    ('career_development_self_help', 'Career Development and Self-Help'),
    ('new_acquisitions_bestsellers', 'New Acquisitions and Bestsellers'),
    ('government_publications', 'Government Publications'),
    ('thesis_dissertations', 'Thesis and Dissertations'),
]

    catagory=models.CharField(max_length=100,choices=catagory_choices)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')


    def __str__(self):
        return self.title
    
    def update_status(self):
       
        if self.stock > 0:
            self.status = 'available'
        else:
            self.status = 'not_available'
        self.save()
    



class ReturnedBookInfo(models.Model):
    returner_name = models.CharField(max_length=255)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    borrowed_date = models.DateField(null=True, blank=True)
    due_date=models.DateField(null=True, blank=True)
    returned_date = models.DateField(default=timezone.now)
    due_status = models.TextField(null=True, default=None)
   
    def __str__(self):
        return self.returner_name
    
class BorrowedBookInfo(models.Model):
    
    borrower_name = models.CharField(max_length=255)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.borrower_name
    
    


# ###########################################################################################



class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('Borrow', 'Borrow'),
        ('Return', 'Return')
    ]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    transaction_date = models.DateField(default=timezone.now,null=True,blank=True)
    due_date = models.DateField(null=True, blank=True)
    user = models.CharField(max_length=255)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.user
    # def save(self):
    #     if self.transaction_type == 'Return':
    #      self.transaction_date = timezone.now().date()
        
    #      super().save()
    #     elif self.transaction_type == 'Borrow':
    #      self.transaction_date = timezone.now().date()
    #      self.due_date = self.transaction_date + timedelta(days=14)
    #      super().save()
   

    

@receiver(post_save, sender=Transaction)
def handle_transaction(sender, instance, created, **kwargs):
    if created: 

        if instance.transaction_type == 'Return':
            instance.book.stock += 1
            if instance.due_date > timezone.now().date():
               days_left=(instance.due_date-timezone.now().date()).days
               due_status = f" Returned {days_left} days before due date !"
            elif instance.due_date < timezone.now().date():
                 days_passed=(timezone.now().date()-instance.due_date).days
                 due_status = f" Returned  {days_passed} days late after the  due date !"
            ReturnedBookInfo.objects.create(
                returner_name=instance.user,
                book=instance.book,
                due_date=instance.due_date,
                returned_date=instance.transaction_date,
                borrowed_date=instance.due_date - timedelta(days=14),
                due_status=due_status
               )
            instance.book.update_status()
        elif instance.transaction_type == 'Borrow':
            instance.book.stock -= 1
            due_date=instance.transaction_date + timedelta(days=14)
            
            BorrowedBookInfo.objects.create(
                borrower_name=instance.user,
                book=instance.book,
                borrowed_date=instance.transaction_date,
                due_date=due_date,
               
                
               )
            instance.book.update_status()

   
############################ FOR USER"s Transaction ###############
            
# class TransactionForUser(models.Model):
#     TRANSACTION_CHOICES = [
#         ('Borrow', 'Borrow'),
#         ('Return', 'Return')
#     ]

#     transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
#     transaction_date = models.DateField(default=timezone.now,null=True,blank=True)
#     due_date = models.DateField(null=True, blank=True)
#     user = models.CharField(max_length=255,null=True,blank=True)
#     book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user
   

    

# @receiver(post_save, sender=TransactionForUser)
# def handle_transaction(sender, instance, created, **kwargs):
#     if created: 

#         if instance.transaction_type == 'Return':
#             instance.book.stock += 1
#             if instance.due_date > timezone.now().date():
#                days_left=(instance.due_date-timezone.now().date()).days
#                due_status = f" Returned {days_left} days before due date !"
#             elif instance.due_date < timezone.now().date():
#                  days_passed=(timezone.now().date()-instance.due_date).days
#                  due_status = f" Returned  {days_passed} days late after the  due date !"
#             ReturnedBookInfo.objects.create(
#                 returner_name=instance.user,
#                 book=instance.book,
#                 returned_date=instance.transaction_date,
#                 borrowed_date=instance.due_date - timedelta(days=14),
#                 due_status=due_status
#                )
#             instance.book.update_status()
#         elif instance.transaction_type == 'Borrow':
#             instance.book.stock -= 1
#             due_date=instance.transaction_date + timedelta(days=14)
            
#             BorrowedBookInfo.objects.create(
#                 borrower_name=instance.user,
#                 book=instance.book,
#                 borrowed_date=instance.transaction_date,
#                 due_date=due_date,
               
                
#                )
#             instance.book.update_status()

   
