from django.test import TestCase
from .models import Category , Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.fashion= Category(category='fashion')

    def test_instance(self):
        self.assertTrue(isinstance(self.fashion,Category))

    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save category
        
        '''
        self.fashion.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.fashion.save_category()
        self.fashion.delete_category()
        print(self.fashion)
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

        

class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.nairobi= Location(name='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def tearDown(self):
        '''
        Method to clear the test that has been done on location
        '''
        Location.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save the location
        
        '''
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        '''
        Method to delete the location
        
        '''
        self.nairobi.save_location()
        self.nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)