function kalkulator() {
    const angka1 = parseFloat(prompt("Masukkan angka pertama:"));
    const angka2 = parseFloat(prompt("Masukkan angka kedua:"));
    const operasi = prompt("Pilih operasi (penambahan, pengurangan, perkalian, atau pembagian):");
  
    let hasil;
  
    switch (operasi) {
      case "penambahan":
        hasil = angka1 + angka2;
        break;
      case "pengurangan":
        hasil = angka1 - angka2;
        break;
      case "perkalian":
        hasil = angka1 * angka2;
        break;
      case "pembagian":
        hasil = angka1 / angka2;
        break;
      default:
        console.log("Operasi yang Anda pilih tidak valid.");
        return;
    }
  
    console.log(`Hasil ${operasi} dari ${angka1} dan ${angka2} adalah: ${hasil}`);
  }
  
  kalkulator();
  