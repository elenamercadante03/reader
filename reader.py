import sys
import csv
import os


def print_directory_files(path):

    directory = os.path.dirname(path) or "."
    print("\nFiles in directory:")
    try:
        print(os.listdir(directory))
    except Exception as e:
        print("Cannot list directory:", e)


def load_csv(path):

    with open(path, "r", newline="") as f:
        return list(csv.reader(f))


def save_csv(path, data):

    """Salva CSV"""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def print_table(data):

    for row in data:
        print(",".join(str(cell) for cell in row))



def apply_change(data, change):
    """
    change formato: X,Y,value
    X = colonna
    Y = riga
    """
    parts = change.split(",")

    if len(parts) != 3:
        print(f"Invalid change format skipped: {change}")
        return data

    try:
        col = int(parts[0])
        row = int(parts[1])
        value = parts[2]
    except ValueError:
        print(f"Invalid numbers in change skipped: {change}")
        return data

    # controllo bounds
    if row < 0 or row >= len(data):
        print(f"Row out of range skipped: {change}")
        return data

    if col < 0 or col >= len(data[0]):
        print(f"Column out of range skipped: {change}")
        return data

    # applica modifica
    data[row][col] = value
    return data


def main():
    # -----------------------------
    # 1. ARGOMENTI DA TERMINALE
    # -----------------------------
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <change1> ...")
        return

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    # -----------------------------
    # 2. CONTROLLO FILE ESISTE
    # -----------------------------
    if not os.path.isfile(src):
        print(f"Error: file '{src}' does not exist or is not a file.")
        print_directory_files(src)
        return

    # -----------------------------
    # 3. CARICA CSV
    # -----------------------------
    data = load_csv(src)

    # -----------------------------
    # 4. APPLICA MODIFICHE
    # -----------------------------
    for change in changes:
        data = apply_change(data, change)

    # -----------------------------
    # 5. STAMPA RISULTATO
    # -----------------------------
    print("\nModified CSV:")
    print_table(data)

    # -----------------------------
    # 6. SALVA FILE
    # -----------------------------
    save_csv(dst, data)
    print(f"\nSaved to {dst}")


if __name__ == "__main__":
    main()



