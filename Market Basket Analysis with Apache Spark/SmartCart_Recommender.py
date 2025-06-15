import streamlit as st
import pandas as pd
import random

# Example product data with new products
df = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product_name': ['Apple', 'Banana', 'Cucumber', 'Date', 'Eggplant', 'Honey', 'Grapes', 'Carrot', 'Orange', 'Tomato'],
    'category': ['Fruit', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Food', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable'],
    'rating': [4.5, 4.3, 4.7, 4.0, 3.8, 4.8, 4.2, 4.6, 4.4, 3.9],
    'sales': [1000, 800, 1200, 700, 500, 1500, 900, 1100, 950, 800],
    'price': [2.5, 1.8, 1.2, 3.0, 2.0, 5.0, 2.2, 1.5, 2.8, 1.7],
    'stock': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
})

# Streamlit interface
st.title("Product Recommendation System")

# User category preference
selected_category = st.selectbox("Select Product Category", df['category'].unique())

# Filter data based on selected category
category_products = df[df['category'] == selected_category]

# Sort by top-selling products in the selected category
top_selling_products = category_products.sort_values(by='sales', ascending=False).head(5)

# Display the top-selling products
st.write(f"Top-Selling Products in {selected_category}")
st.write(top_selling_products[['product_name', 'rating', 'sales', 'price']])

# Add recently viewed products (dummy example here)
recently_viewed = ["Apple", "Cucumber", "Date"]  # Replace with dynamic session data if available
st.write("Recently Viewed Products")
st.write(recently_viewed)

# Similar products recommendation based on category
selected_product = st.selectbox("Select a Product to View", category_products['product_name'])

# Find similar products (same category, and maybe similar price range)
similar_products = category_products[
    (category_products['category'] == category_products[category_products['product_name'] == selected_product]['category'].values[0]) &
    (category_products['product_name'] != selected_product)
]

# Check if there are enough similar products
if similar_products.shape[0] > 0:
    # Recommend 3 similar products (if available)
    num_recommendations = min(3, similar_products.shape[0])  # If fewer than 3, sample all
    recommended_similars = similar_products.sample(num_recommendations)
    st.write(f"Similar Products to {selected_product}")
    st.write(recommended_similars[['product_name', 'rating', 'price']])
else:
    st.write(f"No similar products found for {selected_product}. Try a different product!")

# Product Bundle Recommendations (dummy logic: recommend related products in the same category)
if selected_product in ["Apple", "Banana", "Grapes", "Orange"]:  # Example logic for fruit bundles
    st.write(f"Recommended Bundles for {selected_product}")
    bundle = random.sample(list(category_products['product_name']), 3)  # Recommend random items
    st.write(bundle)
else:
    st.write(f"No recommended bundles for {selected_product}.")
