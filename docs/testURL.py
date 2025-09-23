import random
import string

def generate_random_url(length=15):
    """Generates a random string that could resemble a URL path."""
    characters = string.ascii_lowercase + string.digits
    random_path = ''.join(random.choice(characters) for i in range(length))
    subdomain = ''.join(random.choice(characters) for i in range(5))
    domain = ''.join(random.choice(characters) for i in range(8))
    tld = random.choice(['com', 'org', 'net', 'gov', 'edu'])
    return f"https://{subdomain}.{domain}.{tld}/{random_path}"

random_test_url = generate_random_url()
print(f"Generated random URL: {random_test_url}")
