from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name = 'Muriuki', email = 'tester2@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
            