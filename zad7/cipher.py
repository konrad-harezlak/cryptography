from substitution import create_substitution_table, substitute
from transposition import column_transposition, row_transposition

def custom_cipher(text):
    text = text.upper().replace(' ', '')  # Usuwamy spacje i zamieniamy na wielkie litery
    substitution_table = create_substitution_table()
    substituted_text = substitute(text, substitution_table)
    
    num_columns = 5  # Można zmienić liczbę kolumn
    column_transposed_text = column_transposition(substituted_text, num_columns)
    
    num_rows = len(column_transposed_text) // num_columns
    final_cipher = row_transposition(column_transposed_text, num_rows)
    
    return final_cipher

if __name__ == "__main__":
    # Przykład użycia
    with open("plaintext.txt", "r") as file:
        plaintext = file.read()
        
    ciphertext = custom_cipher(plaintext)
    
    with open("ciphertext.txt", "w") as file:
        file.write(ciphertext)
    
    print(f"Ciphertext saved to 'ciphertext.txt'")
