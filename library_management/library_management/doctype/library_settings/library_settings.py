# Copyright (c) 2024, Mohammad Faizan Sopariwala and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibrarySettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		loan_period: DF.Int
		max_articles: DF.Int
	# end: auto-generated types
	pass
