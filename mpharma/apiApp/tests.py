   



# from django.test import TestCase
# from .models import icdCode


# class ModelTestCase(TestCase):
#     """This class defines the test suite for the bucketlist model."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.bucketlist_name = "Write world class code"
#         self.bucketlist = icdCode(name=self.bucketlist_name)

#     def test_model_can_create_a_bucketlist(self):
#         """Test the bucketlist model can create a bucketlist."""
#         old_count = icdCode.objects.count()
#         self.bucketlist.save()
#         new_count = icdCode.objects.count()
#         self.assertNotEqual(old_count, new_count)
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from apiApp.models import icdCode 





class ViewTestCase(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        icdCode.objects.create(
            category_code='ZY210', diagnosis_code=3, full_code='ZY2100', abbreviated_description='Salmonella pyelonephritis')
        icdCode.objects.create(
           category_code='ZY2110', diagnosis_code=4, full_code='ZY21100', abbreviated_description='Malaria pyelonephritis')

    def test_icdCode(self):
        test1 = icdCode.objects.get(full_code='ZY2100')
        test2 = icdCode.objects.get(full_code='ZY21100')
        self.assertEqual(
            test1.get_full_code(), "ZY2100")
        self.assertEqual(
            test2.get_full_code(), "ZY21100")





# class ViewTestCase(TestCase):
	"""Test suite for the api views."""

	# def setUp(self):
	# 	"""Define the test client and other test variables."""
	# 	self.client = icdCode()
	# 	self.icdcode_data = {'category_code': 'ZY210','diagnosis_code': '3','full_code': 'ZY2100','abbreviated_description': 'Salmonella pyelonephritis','full_description': 'Salmonella pyelonephritis','category_title': 'Salmonella osteomyelitis'}
	# 	self.response = self.client.post(
	# 		reverse('create'),
	# 		self.icdcode_data,
	# 		format="json")

	# def test_api_can_create_a_icdcode(self):
	# 	"""Test the api has bucket creation capability."""
	# 	self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)




	# def test_api_can_get_a_icdcode(self):
	# 	"""Test the api can get a given icdcode."""
	# 	icdcode = icdCode.objects.get()
	# 	response = self.client.get(
	# 		reverse('details',
	# 		kwargs={'pk': icdcode.full_code}), format="json")

	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)
	# 	self.assertContains(response, icdcode)

	# def test_api_can_update_icdcode(self):
	# 	"""Test the api can update a given icdcode."""
	# 	icdcode = icdCode.objects.get()
	# 	change_icdcode = {'category_code': 'ZY210','diagnosis_code': '3','full_code': 'ZY2100','abbreviated_description': 'Salmonella pyelonephritis','full_description': 'Salmonella pyelonephritis','category_title': 'Salmonella osteomyelitis'}
	# 	res = self.client.put(
	# 		reverse('details', kwargs={'pk': icdcode.full_code}),
	# 		change_bucketlist, format='json'
	# 	)
	# 	self.assertEqual(res.status_code, status.HTTP_200_OK)



	# def test_api_can_delete_bucketlist(self):
	# 	"""Test the api can delete a icdcode."""
	# 	icdcode = icdCode.objects.get()
	# 	response = self.client.delete(
	# 		reverse('details', kwargs={'pk': icdcode.full_code}),
	# 		format='json',
	# 		follow=True)

	# 	self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT

	# 	