document.getElementById("surveyForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const ciri = document.getElementById("ciri").value.trim();
  const makanan = document.getElementById("makanan").value.trim();

  if (!ciri || !makanan) return alert("Isi semua kolom dulu!");

  const response = await fetch("/api/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ciri, makanan }),
  });

  const result = await response.json();

  const hasilDiv = document.getElementById("hasil");
  hasilDiv.style.display = "block";
  hasilDiv.innerText = result.message;
});
