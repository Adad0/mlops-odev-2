import hashlib

def hash_customer_id(customer_id, buckets=50):
    """
    Adad'ın high-cardinality mantığı: Customer ID'yi hashleyip 
    belli bir bucket'a (G1-G50) atar.
    """
    if not customer_id:
        raise ValueError("Customer ID cannot be empty")
    
    hash_object = hashlib.md5(customer_id.encode())
    hex_dig = hash_object.hexdigest()
    # İlk 8 karakteri alıp integer'a çevir ve mod al
    bucket_index = int(hex_dig[:8], 16) % buckets
    return f"G{bucket_index + 1}"