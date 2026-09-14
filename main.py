from blockchain import Blockchain


Blockchain = Blockchain()


# Transaksi 1:
# Customer berbelanja pada Merchant dan memperoleh token poin.
Blockchain.add_block({
    "transaction_id": "TRX-001",
    "transaction_type": "REWARD_EARNED",
    "token": "LRT",
    "amount": 100,
    "customer": "Andi",
    "merchant": "Kopi Nusantara",
    "loyalty_platform": "Loyalty Rewards Platform",
    "payment_gateway": "Midtrans",
    "description": "Andi memperoleh 100 LRT setelah belanja kopi."
})


# Transaksi 2:
# Customer memakai poin pada merchant lain.
Blockchain.add_block({
    "transaction_id": "TRX-002",
    "transaction_type": "REWARD_REDEEMED",
    "token": "LRT",
    "amount": 50,
    "customer": "Andi",
    "merchant": "Toko Buku Indonesia",
    "loyalty_platform": "Loyalty Rewards Platform",
    "payment_gateway": "Midtrans",
    "description": "Andi menukarkan 50 LRT untuk diskon pembelian buku."
})


# Transaksi 3:
# Loyalty Platform menerbitkan token ERC-20 untuk program reward.
Blockchain.add_block({
    "transaction_id": "TRX-003",
    "transaction_type": "TOKEN_ISSUED",
    "token": "LRT",
    "amount": 1000,
    "customer": "Andi",
    "merchant": "Loyalty Rewards Platform",
    "loyalty_platform": "Loyalty Rewards Platform",
    "payment_gateway": "Midtrans",
    "description": "Platform menerbitkan 1000 LRT untuk program loyalty."
})


for block in Blockchain.chain:
    print("=" * 60)
    print("INDEX         :", block.index)
    print("DATA          :", block.data)
    print("PREVIOUS HASH :", block.previous_hash)
    print("HASH          :", block.hash)

print("\nBlockchain valid:", Blockchain.is_valid())