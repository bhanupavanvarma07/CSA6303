# LAB 18: Malware Detection with SHA-256
# Aim: Compare a file's SHA-256 digest with known-malicious hashes.
# The small sample list below is illustrative; use a verified threat-intelligence feed.

import hashlib

known_malicious_hashes = {
    "0000000000000000000000000000000000000000000000000000000000000000",
}
file_path = input("Enter file path to check: ").strip()

sha256 = hashlib.sha256()
with open(file_path, "rb") as file:
    for chunk in iter(lambda: file.read(4096), b""):
        sha256.update(chunk)

file_hash = sha256.hexdigest()
print("SHA-256:", file_hash)
if file_hash in known_malicious_hashes:
    print("Warning: Hash matches the illustrative malicious-hash list.")
else:
    print("No match in the sample list. This does not prove the file is safe.")
