from django.shortcuts import render, get_object_or_404

# Data produk hardcoded (tidak perlu database)
PRODUK_LIST = [
    {
        'id': 1,
        'nama': 'Oversized Hoodie Street Vibe',
        'harga': 350000,
        'kategori': 'Fashion',
        'stok': 20,
        'deskripsi': 'Hoodie oversized dengan gaya streetwear edgy. Cocok untuk tampil santai tapi tetap standout.',
        'spesifikasi': [
            'Bahan: Cotton Fleece Premium',
            'Ukuran: M, L, XL',
            'Fit: Oversized',
            'Warna: Hitam, Abu, Cream',
            'Style: Streetwear'
        ],
        'gambar': 'https://i.pinimg.com/736x/ce/78/c8/ce78c803eb69f87e92d5d211c2771088.jpg'
    },
    {
        'id': 2,
        'nama': 'Cargo Pants Urban Tactical',
        'harga': 280000,
        'kategori': 'Fashion',
        'stok': 25,
        'deskripsi': 'Celana cargo dengan desain urban modern dan banyak kantong fungsional.',
        'spesifikasi': [
            'Bahan: Twill Stretch',
            'Ukuran: 28 - 34',
            'Fit: Regular',
            'Warna: Hitam, Army, Khaki',
            'Fitur: Multi Pocket'
        ],
        'gambar': 'https://i.pinimg.com/1200x/0c/31/24/0c3124955120abc13115e22d6d4b42ca.jpg'
    },
    {
        'id': 3,
        'nama': 'Graphic Tee Limited Drop',
        'harga': 150000,
        'kategori': 'Fashion',
        'stok': 40,
        'deskripsi': 'Kaos grafis dengan desain unik dan edisi terbatas untuk tampilan hype.',
        'spesifikasi': [
            'Bahan: Cotton Combed 24s',
            'Ukuran: S, M, L, XL',
            'Print: DTG Premium',
            'Warna: Hitam, Putih',
            'Edition: Limited'
        ],
        'gambar': 'https://i.pinimg.com/736x/5f/be/d4/5fbed4a3f5458363c38122ef08a11072.jpg'
    },
    {
        'id': 4,
        'nama': 'Sling Bag Techwear',
        'harga': 220000,
        'kategori': 'Fashion',
        'stok': 15,
        'deskripsi': 'Tas sling dengan desain techwear modern, ringkas dan stylish.',
        'spesifikasi': [
            'Bahan: Nylon Waterproof',
            'Dimensi: 30x18x8 cm',
            'Kompartemen: 3 ruang',
            'Warna: Hitam, Abu',
            'Style: Techwear'
        ],
        'gambar': 'https://i.pinimg.com/1200x/61/5a/e6/615ae6251626c5733af8e57888408025.jpg'
    },
    {
        'id': 5,
        'nama': 'Chunky Sneakers Hype Step',
        'harga': 450000,
        'kategori': 'Fashion',
        'stok': 18,
        'deskripsi': 'Sneakers chunky dengan desain bold untuk tampilan standout.',
        'spesifikasi': [
            'Material: Synthetic Leather + Mesh',
            'Ukuran: 38 - 44',
            'Sol: Anti-slip',
            'Warna: Putih, Hitam',
            'Style: Streetwear'
        ],
        'gambar': 'https://i.pinimg.com/1200x/3e/fa/7d/3efa7d0bf1ef218317bb696e5a479977.jpg'
    },
    {
        'id': 6,
        'nama': 'Denim Jacket Distressed Rebel',
        'harga': 400000,
        'kategori': 'Fashion',
        'stok': 12,
        'deskripsi': 'Jaket denim dengan efek distressed untuk gaya rebellious dan edgy.',
        'spesifikasi': [
            'Bahan: Denim Washed',
            'Ukuran: M, L, XL',
            'Fit: Regular',
            'Warna: Biru Tua, Biru Muda',
            'Style: Vintage Street'
        ],
        'gambar': 'https://i.pinimg.com/736x/11/89/13/11891379bb503f84aeaaa02680dcf23a.jpg'
    },
    {
        'id': 7,
        'nama': 'Flannel Shirt Grunge Layer',
        'harga': 230000,
        'kategori': 'Fashion',
        'stok': 22,
        'deskripsi': 'Kemeja flanel dengan nuansa grunge, cocok untuk layering outfit.',
        'spesifikasi': [
            'Bahan: Cotton Flannel',
            'Ukuran: M, L, XL',
            'Fit: Loose',
            'Motif: Tartan',
            'Style: Grunge'
        ],
        'gambar': 'https://i.pinimg.com/1200x/0f/38/3f/0f383f3b4077f11c694348600e919bd9.jpg'
    },
    {
        'id': 8,
        'nama': 'Beanie Hat Minimal Core',
        'harga': 90000,
        'kategori': 'Fashion',
        'stok': 35,
        'deskripsi': 'Beanie simpel untuk melengkapi outfit casual dan street.',
        'spesifikasi': [
            'Bahan: Acrylic Knit',
            'Size: All Size',
            'Warna: Hitam, Abu, Olive',
            'Style: Minimal',
            'Gender: Unisex'
        ],
        'gambar': 'https://i.pinimg.com/736x/f7/5a/3f/f75a3f759e125a2845de92c87268bf19.jpg'
    },
    {
        'id': 9,
        'nama': 'Leather Belt Classic Edge',
        'harga': 120000,
        'kategori': 'Fashion',
        'stok': 30,
        'deskripsi': 'Ikat pinggang dengan desain klasik tapi tetap edgy untuk daily wear.',
        'spesifikasi': [
            'Bahan: PU Leather',
            'Panjang: 110 - 130 cm',
            'Warna: Hitam, Coklat',
            'Buckle: Metal',
            'Style: Classic'
        ],
        'gambar': 'https://i.pinimg.com/1200x/06/9f/96/069f9615bb15af6eed7b9d6a314fb2d7.jpg'
    },
    {
        'id': 10,
        'nama': 'Jogger Pants Relax Fit',
        'harga': 200000,
        'kategori': 'Fashion',
        'stok': 28,
        'deskripsi': 'Celana jogger dengan fit santai dan nyaman untuk aktivitas harian.',
        'spesifikasi': [
            'Bahan: Cotton Stretch',
            'Ukuran: M, L, XL',
            'Fit: Relaxed',
            'Warna: Hitam, Abu',
            'Style: Casual Street'
        ],
        'gambar': 'https://i.pinimg.com/1200x/4d/07/da/4d07daecb91a8584041a1a4d7e5a3583.jpg'
    },
    {
        'id': 11,
        'nama': 'Varsity Jacket Retro Club',
        'harga': 420000,
        'kategori': 'Fashion',
        'stok': 14,
        'deskripsi': 'Jaket varsity dengan sentuhan retro dan gaya street modern. Cocok untuk tampilan bold dan standout.',
        'spesifikasi': [
            'Bahan: Wool Blend + Synthetic Leather',
            'Ukuran: M, L, XL',
            'Fit: Regular',
            'Warna: Hitam-Putih, Navy-Cream',
            'Style: Retro Streetwear'
        ],
        'gambar': 'https://i.pinimg.com/736x/f6/3a/d3/f63ad3388c5bb80ca5f2e91201c8b002.jpg'
    }
]


def homepage(request):
    """Halaman utama website."""
    jumlah_produk = len(PRODUK_LIST)
    return render(request, 'katalog/index.html', {
        'jumlah_produk': len(PRODUK_LIST),
        'produk_preview': PRODUK_LIST[:3],
    })


def daftar_produk(request):
    """Halaman daftar semua produk."""
    return render(request, 'katalog/produk.html', {
        'produk_list': PRODUK_LIST,
    })


def detail_produk(request, id):
    """Halaman detail satu produk berdasarkan ID."""
    produk = next((p for p in PRODUK_LIST if p['id'] == id), None)
    if produk is None:
        from django.http import Http404
        raise Http404("Produk tidak ditemukan")
    return render(request, 'katalog/detail.html', {
        'produk': produk,
    })


def kontak(request):
    """Halaman informasi kontak."""
    return render(request, 'katalog/kontak.html')