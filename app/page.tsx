'use client'

import { uploadFile } from '@/actions/upload-file'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useMutation } from '@tanstack/react-query'
import { useState } from 'react'
import { Form } from 'react-hook-form'

export default function Home() {
  const [file, setFile] = useState<FormData | undefined>()
  const { mutate: execute, isPending } = useMutation({
    mutationFn: uploadFile,
  })

  return (
    <Form action={uploadFile}>
      <Input type="file" name="file" />
      <Button type="submit" isLoading={isPending}>
        {isPending ? 'Converting...' : 'Convert'}
      </Button>
    </Form>
  )
}
