import hashlib

def generate_hash(text, algorithm):
    text_bytes = text.encode('utf-8')
    
    if algorithm == 'md5':
        return hashlib.md5(text_bytes).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text_bytes).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text_bytes).hexdigest()

def compare_hashes(hash1, hash2):
    return hash1 == hash2

def main():
    print("=" * 50)
    print("   🔐 Hash Generator")
    print("=" * 50)

    text = input("\nIngresá un texto: ")

    print(f"\nMD5    (inseguro): {generate_hash(text, 'md5')}")
    print(f"SHA-1  (inseguro): {generate_hash(text, 'sha1')}")
    print(f"SHA-256 (seguro) : {generate_hash(text, 'sha256')}")

    print("\n" + "-" * 50)
    print("Verificar integridad — comparar dos textos")
    print("-" * 50)

    text1 = input("Texto original : ")
    text2 = input("Texto a verificar: ")

    hash1 = generate_hash(text1, 'sha256')
    hash2 = generate_hash(text2, 'sha256')

    if compare_hashes(hash1, hash2):
        print("\n✅ Los textos son IDÉNTICOS — integridad verificada")
    else:
        print("\n❌ Los textos son DISTINTOS — posible modificación")

    print("=" * 50)

if __name__ == "__main__":
    main()