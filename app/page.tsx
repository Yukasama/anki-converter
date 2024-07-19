'use client'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

export default function Home() {
  return (
    <form method="POST" action="/api/uploadfile" encType="multipart/form-data">
      <Input type="file" name="file" accept=".md" />
      <Button>Upload</Button>
    </form>
  )
}
