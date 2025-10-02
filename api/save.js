export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Hanya POST yang diizinkan" });
  }

  const { ciri, makanan } = req.body;

  if (!ciri || !makanan) {
    return res.status(400).json({ message: "Data tidak lengkap" });
  }

  const token = "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";
  const repo = "RooxJawa/survei";   // ganti dengan repo GitHub kamu
  const path = "data.txt";          // file tujuan di repo

  // ambil isi file sebelumnya
  const getRes = await fetch(`https://api.github.com/repos/${repo}/contents/${path}`, {
    headers: { Authorization: `token ${token}` }
  });
  const fileData = await getRes.json();

  const content = Buffer.from(fileData.content, "base64").toString("utf8");

  // tambahkan data baru
  const newEntry = `Ciri: ${ciri} | Makanan: ${makanan} | Waktu: ${new Date().toISOString()}\n`;
  const updatedContent = content + newEntry;

  // commit balik ke GitHub
  const updateRes = await fetch(`https://api.github.com/repos/${repo}/contents/${path}`, {
    method: "PUT",
    headers: {
      Authorization: `token ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: "Update data.txt via survey",
      content: Buffer.from(updatedContent).toString("base64"),
      sha: fileData.sha
    }),
  });

  if (updateRes.ok) {
    res.status(200).json({ message: "Jawaban berhasil disimpan ke GitHub ✅" });
  } else {
    res.status(500).json({ message: "Gagal menyimpan data" });
  }
}
