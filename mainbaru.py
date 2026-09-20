from block import Block
from pow import proof_of_work
from pos import proof_of_stake
import block


print("LOYALTY POINTS / REWARDS SYSTEM")
print("TOKEN ERC-20: Loyalty Reward Token (LRT)")


# Transaksi: Customer mendapat token poin dari Merchant 1
transaction_data = {
    "transaction_id": "TRX-001",
    "transaction_type": "REWARD_EARNED",
    "token_name": "Loyalty Reward Token",
    "token_symbol": "LRT",
    "token_standard": "ERC-20",
    "amount": 100,
    "customer": "Andi",
    "merchant": "Kopi Nusantara",
    "loyalty_platform": "Loyalty Rewards Platform",
    "payment_gateway": "Midtrans",
    "description": "Andi memperoleh 100 LRT setelah berbelanja di Kopi Nusantara."
}


print("\nPROOF OF WORK")

block = Block(
    index=1,
    data=transaction_data,
    previous_hash="0"
)

difficulty = 4

print("\nData Block :", block.data)
print("Difficulty :", difficulty)

proof_of_work(block, difficulty)

print("\nNonce :", block.nonce)
print("Hash  :", block.hash)


print("\nPROOF OF STAKE")

# Validator adalah aktor yang memvalidasi transaksi reward.
validators = {
    "Loyalty Rewards Platform": 50,
    "Midtrans Payment Gateway": 20,
    "Kopi Nusantara Merchant": 20,
    "Toko Buku Indonesia Merchant": 10
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"- {validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)


# Contoh transaksi lintas merchant:
# Andi menukarkan token LRT yang diperoleh di Kopi Nusantara
# untuk diskon di Toko Buku Indonesia.
print("\nTransaksi lintas merchant berhasil dicatat.")
print("Customer: Andi")
print("Token yang digunakan: 50 LRT")
print("Merchant tujuan: Toko Buku Indonesia")