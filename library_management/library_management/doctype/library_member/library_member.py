# Copyright (c) 2024, Mohammad Faizan Sopariwala and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries


class LibraryMember(Document):
	
	# def before_save(self):
	# 	self.full_name=f'{self.first_name} {self.last_name or ""}'

	def get_full_name(self):
		"""Returns the person's full name"""
		return f'{self.first_name} {self.last_name or ""}'
	
# doc=frappe.get_doc("Library Member","LM00002")
# fullName=doc.get_full_name()
# frappe.msgprint(fullName)

	# def autoname(self):
	# 	prefix= 'LM-{}-'.format(self.first_name)
	# 	self.name=getseries(prefix,3)

	# def after_insert(self):
	# 	frappe.sendmail(recipients=[self.email],message="Thank you for registering!")

# doc=frappe.get_doc({
# 	'doctype':'Library Member',
# 	'first_name':'Ammar',
# 	'last_name':'Puthawala'
# })

# doc.insert()