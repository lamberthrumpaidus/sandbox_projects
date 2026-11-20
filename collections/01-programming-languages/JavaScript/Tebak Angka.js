// Game Tebak Angka Sederhana

// Fungsi untuk menghasilkan angka acak antara 1 dan 100
function generateRandomNumber() {
    return Math.floor(Math.random() * 100) + 1;
  }
  
  // Fungsi untuk memulai permainan
  function startGame() {
    const targetNumber = generateRandomNumber();
    let numberOfTries = 0;
  
    // Fungsi untuk menerima tebakan pemain
    function makeGuess() {
      const userGuess = prompt("Tebak angka antara 1 dan 100:");
      numberOfTries++;
  
      if (userGuess === null) {
        alert("Permainan berakhir. Anda keluar dari permainan.");
        return;
      }
  
      const guess = parseInt(userGuess);
  
      if (isNaN(guess)) {
        alert("Masukkan angka yang valid.");
        makeGuess();
      } else if (guess < targetNumber) {
        alert("Tebakan terlalu rendah. Coba lagi!");
        makeGuess();
      } else if (guess > targetNumber) {
        alert("Tebakan terlalu tinggi. Coba lagi!");
        makeGuess();
      } else {
        alert(`Selamat! Anda menebak angka ${targetNumber} dengan ${numberOfTries} percobaan.`);
      }
    }
  
    makeGuess();
  }
  
  // Mulai permainan
  startGame();
  