import fs from 'node:fs/promises'
import path from 'node:path'
import { Lexicons } from '@atproto/lexicon'

const root = new URL('../schemas/lexicons/', import.meta.url).pathname
const files = (await fs.readdir(root)).filter(f => f.endsWith('.json'))
const lex = new Lexicons()

for (const f of files) {
  const p = path.join(root, f)
  const raw = JSON.parse(await fs.readFile(p, 'utf8'))
  // Enforce Lexicon v1 and NSID/filename alignment
  if (raw.lexicon !== 1) {
    throw new Error(`Lexicon version must be 1 in ${f}`)
  }
  const expected = path.basename(f, '.json')
  if (raw.id !== expected) {
    throw new Error(`Lexicon id mismatch in ${f}: id='${raw.id}' expected '${expected}'`)
  }
  lex.add(raw)
}

console.log(`Validated ${files.length} lexicon file(s)`)
