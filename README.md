# Smart-Shopping-Cart-Analyzer
Project Overview: Smart Shopping Cart Analyzer
The Smart Shopping Cart Analyzer is a Python-based automation tool designed to simulate a retail checkout experience. It demonstrates the effective use of core Python data structures—Lists, Dictionaries, and Sets—to manage inventory, process user selections, and apply complex business logic for discounts and payment restrictions.
Core Functionality
The application follows a structured workflow to ensure data integrity and a seamless user experience:
Dynamic Inventory Management: Uses a predefined dictionary to store multi-attribute product data, including names, prices, and categories.
User-Centric Input: Captures user identity and provides an intuitive numerical menu for product selection.
Data Processing:
Lists: Used to track the sequence of items added to the cart.
Dictionaries: Maps specific product names to their prices for efficient calculation.
Sets: Automatically filters and stores unique product categories to assist in rule-based logic.
Advanced Pricing Engine:
Implements a tiered discount system based on the total cart value ($ \geq 5000$ for 20% and $ \geq 2000$ for 10%).
Includes a "High-Value Card Reward" that grants an additional 5% discount for transactions exceeding 30,000.
Safety & Validation Logic: Features a conditional block to restrict Cash on Delivery (COD) for high-risk categories like Electronics, simulating real-world e-commerce fraud prevention.
Technical Highlights
Logic Gates: Utilizes if/elif/else structures to handle overlapping discount triggers and payment method validation.
Data Integrity: Ensures that categories remain unique through set theory, preventing redundant processing.
Summary Reporting: Generates a clean purchase summary detailing selected items, the applied discounts, and the final payable amount.
