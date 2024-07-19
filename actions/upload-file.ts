'use server'

import { logger } from '@/config/logger'

export const uploadFile = async (formData: FormData) => {
  try {
    const file = formData.get('file') as File
    if (!file) {
      logger.debug('uploadFile (invalid)')
      throw new Error('No file submitted.')
    }

    const uploadData = new FormData()
    uploadData.append('file', file)

    const result = await fetch('http://localhost:8000/api/uploadfile', {
      method: 'POST',
      body: uploadData,
    })

    if (!result.ok) {
      logger.debug('uploadFile (error): error=result not ok.')
      throw new Error('File upload failed.')
    }

    logger.debug('uploadFile (done)')
    return await result.blob()
  } catch (error) {
    logger.debug('uploadFile (error): error=%s', error)
    throw new Error(`File not uploaded: ${error}`)
  }
}
