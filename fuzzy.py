import argparse
import ssdeep
import os

def fuzzy_hash_file(filepath):
    """Generate fuzzy hash for a file."""
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        return ssdeep.hash(data)
    except Exception as e:
        print(f"[!] Error reading {filepath}: {e}")
        return None

def compare_files(file1, file2):
    """Compare two files and return similarity score."""
    hash1 = fuzzy_hash_file(file1)
    hash2 = fuzzy_hash_file(file2)

    if hash1 and hash2:
        score = ssdeep.compare(hash1, hash2)
        print(f"\n🔹 File 1: {file1}\n   Hash: {hash1}")
        print(f"🔹 File 2: {file2}\n   Hash: {hash2}")
        print(f"\n✅ Similarity Score: {score}%\n")
    else:
        print("[!] Could not generate hashes.")

def scan_directory(directory):
    """Generate fuzzy hashes for all files in a directory."""
    print(f"\n🔍 Scanning directory: {directory}\n")
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            hash_val = fuzzy_hash_file(path)
            if hash_val:
                results[path] = hash_val
                print(f"{path} → {hash_val}")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔑 Simple Fuzzy Hashing Tool (using ssdeep)")
    parser.add_argument("-c", "--compare", nargs=2, help="Compare two files")
    parser.add_argument("-d", "--directory", help="Scan all files in a directory")

    args = parser.parse_args()

    if args.compare:
        compare_files(args.compare[0], args.compare[1])
    elif args.directory:
        scan_directory(args.directory)
    else:
        print("\nUsage:")
        print("  python fuzzyhash.py -c file1 file2   → Compare two files")
        print("  python fuzzyhash.py -d folder_path   → Scan directory for fuzzy hashes\n")
