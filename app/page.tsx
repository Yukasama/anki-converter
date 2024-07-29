'use client'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

export default function Home() {
  return (
    <form
      method="POST"
      action="/api/uploadfile"
      encType="multipart/form-data"
      className="flex flex-col gap-4 items-center m-20"
    >
      <h2 className="text-4xl font-thin">Anki Converter</h2>
      <Input type="file" name="file" accept=".md" className="w-96" />
      <Button>Upload</Button>
    </form>
  )
}
