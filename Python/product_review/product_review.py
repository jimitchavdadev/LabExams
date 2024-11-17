import os
import re
from collections import defaultdict

def extract_review_info(review_line):
    pattern = r'(?P<product_id>[a-z0-9]{10})\s(?P<customer_id>[a-zA-Z0-9]{6})\s(?P<review_date>\d{4}-\d{2}-\d{2})\s(?P<rating>[1-5])\s(?P<review_text>.+)'
    match = re.match(pattern, review_line)
    if match:
        return (match.group('product_id'), match.group('customer_id'), match.group('review_date'), int(match.group('rating')), match.group('review_text'))
    return None

def process_reviews(directory_path):
    valid_reviews = 0
    invalid_reviews = 0
    total_reviews = 0
    product_rating = defaultdict(list)
    
    try:
        files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
        for filename in files:
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:  # Corrected here
                for line in file:
                    total_reviews += 1
                    review = extract_review_info(line.strip())
                    if review:
                        valid_reviews += 1
                        product_id = review[0]  # Extract product_id directly
                        rating = review[3]      # Extract rating directly
                        product_rating[product_id].append(rating)
                    else:
                        invalid_reviews += 1
    except Exception as e:
        print(f"Error processing files: {e}")  # Fixed f-string

    return total_reviews, valid_reviews, invalid_reviews, product_rating  # Added return statement

def calculate_average(product_rating):
    avg_rating = {product_id: sum(ratings) / len(ratings) for product_id, ratings in product_rating.items()}  # Fixed dict comprehension
    return avg_rating

def write_summary(summary_path, total_reviews, valid_reviews, invalid_reviews, top_products):
    try:
        with open(summary_path, 'w') as file:
            file.write(f"total reviews: {total_reviews}\n")
            file.write(f"valid reviews: {valid_reviews}\n")
            file.write(f"invalid reviews: {invalid_reviews}\n")
            file.write(f"top 3 reviews: \n")
            for product_id, avg in top_products:
                file.write(f"{product_id} : {avg}\n")  # Added newline for formatting
    except Exception as e:
        print(f"Error writing summary: {e}")  # Fixed f-string

def main():
    directory_path = "/home/rebel/Desktop/lab prep/Python/product_review"
    summary_file = os.path.join(directory_path, "summary.txt")  # Fixed path creation

    total_reviews, valid_reviews, invalid_reviews, product_ratings = process_reviews(directory_path)

    avg_ratings = calculate_average(product_ratings)

    top_products = sorted(avg_ratings.items(), key=lambda x: -x[1])[:3]

    write_summary(summary_file, total_reviews, valid_reviews, invalid_reviews, top_products)

    print("Processing completed, file saved at", summary_file)

if __name__ == "__main__":
    main()