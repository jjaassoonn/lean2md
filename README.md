# Convert Lean file to markdown

## Usage

```bash
python lean2md.py -i <input.lean> <output.md>
```

In `input.lean` file:
- code surrounded by `--BEGIN:IGNORE` and `--END:IGNORE` will be ignored;
- comments starting with `/-MD` and ending with `MD-/` will be treated as markdown.

See `example.lean` and `example.md`.