{
    "name": "Real Estate Account Integration",
    "version": "18.0.1.0.0",
    "category": "Sales/Real Estate",
    "description": """
Real Estate Account Integration
================================
Integration module between Real Estate and Accounting.

Features:
* Automatic invoice generation when property is sold
* Commission calculation (6% of selling price)
* Administrative fees invoicing
* Integration with accounting module
    """,
    "author": "Nashta Development Team",
    "sequence": -1,
    "website": "https://www.github.com/IshworTM",
    "summary": "Real Estate and Accounting Integration",
    "depends": ["estate", "account"],
    "data": [
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
