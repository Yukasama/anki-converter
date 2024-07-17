'use server'

import { logger } from '@/config/logger'

export const uploadFile = async (formData: FormData) => {
  try {
    const file = formData.get('file') as File
    if (!file) {
      return { error: 'No file submitted.' }
    }
    logger.debug('uploadFile (attempt): file=%o', file)

    const result = await fetch('/api/uploadfile', {
      method: 'POST',
      body: file,
    })

    if (!result.ok) {
      return { error: 'File upload failed.' }
    }

    return result
  } catch (error) {
    console.error('Error uploading file:', error)
    return { error: 'File not uploaded.' }
  }
}
