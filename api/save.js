import fs from "fs";
import path from "path";

export default function handler(req, res) {
  if (req.method === "POST") {
    const { ciri, makanan } = req.body;

    const filePath = path.join(process.cwd(), "data.txt");
    const entry = `Ciri: ${ciri} | Makanan: ${makanan} | Waktu: ${new Date().toISOString()}\n`;

    fs.appendFileSync(filePath, entry, "utf8");

    res.status(200).json({ message: "Terima kasih! Jawabanmu tersimpan di data.txt 💾" });
  } else {
    res.status(405).json({ message: "Metode tidak diizinkan" });
  }
}
