{
    "name": "Real Estate Management",
    "version": "18.0.1.0.0",
    "category": "Sales/Real Estate",
    "description": """
Real Estate Management Module
==============================
A comprehensive module for managing real estate properties.

Features:
* Property management with detailed information
* Property types and tags for categorization
* Property offers and bidding system
* Sales workflow with status tracking
* Integration with contacts (buyers, sellers, agents)
    """,
    "author": "Nashta Development Team",
    "website": "https://www.github.com/IshworTM",
    "summary": "Complete Real Estate Property Management System",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_inherited_model_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
