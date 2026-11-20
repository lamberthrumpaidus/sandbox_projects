    function isPalindrome(text) {
    text = text.toLowerCase().replace(/[^a-zA-Z]/g, ''); // Ubah ke huruf kecil dan hapus karakter non-alfabet

    for (let i = 0; i < Math.floor(text.length / 2); i++) {
        if (text[i] !== text[text.length - i - 1]) {
            return false;
        }
    }
    return true;
}

// Contoh penggunaan di lingkungan konsol
const kata = "katak"; // Ganti dengan kata yang ingin Anda periksa

if (isPalindrome(kata)) {
    console.log(`${kata} ini adalah palindrome`);
} else {
    console.log(`${kata} bukan palindrome`);
}
