# Comic Book Reader (Gradio) 📚

> A comic book (CBR/CBZ) reader built with Gradio.

Upload `.cbr` or `.cbz` files and view all pages in a gallery interface.

## Features

- **Format Support** — CBR (RAR) and CBZ (ZIP) archives
- **Gallery View** — All extracted pages displayed in a grid
- **Live Processing** — Instant extraction on file upload
- **Example Files** — Sample CBR/CBZ files included

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Gradio |
| Archive | rarfile, zipfile |
| Images | Pillow (PIL) + NumPy |

## Known Limitations

- File path handling may need adjustment per deployment environment
- Large archives may cause memory pressure

## Quick Start

```bash
pip install gradio pillow rarfile numpy
python index.py
```
